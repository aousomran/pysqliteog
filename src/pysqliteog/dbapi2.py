import datetime
from ast import literal_eval
from queue import Queue
from threading import Thread

import grpc

from .gen.sqliteog_pb2_grpc import SqliteOGStub
from .gen.sqliteog_pb2 import *
from .errors import *

# Globals
paramstyle = "qmark"
threadsafety = 1
apilevel = "2.0"
PARSE_COLNAMES = 2
PARSE_DECLTYPES = 1
sqlite_version = '3.31.1'
version = '0.0.4'
version_info = tuple([int(x) for x in version.split(".")])
sqlite_version_info = tuple([int(x) for x in sqlite_version.split(".")])

Date = datetime.date
Time = datetime.time
Timestamp = datetime.datetime


# Connection
def connect(host, port, dbname):
    return Connection(host, port, dbname)


class Connection:
    channel = None
    grpc_stub = None
    _function_register = dict()
    initialized = False
    _cnx_id = ""
    _db_name = ""

    @property
    def cnx_id(self):
        return self._cnx_id

    @property
    def function_register(self):
        return self._function_register

    def __init__(self, host, port, dbname):
        self._db_name = dbname
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.grpc_stub = SqliteOGStub(self.channel)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        # fire a call to close our remote db connection, before closing the grpc channel
        self.grpc_stub.Close(ConnectionId(id=self.cnx_id))
        self.channel.close()

    def initialize_remote_connection(self):
        resp: ConnectionId = self.grpc_stub.Connection(
            ConnectionRequest(db_name=self._db_name, functions=self._function_register.keys())
        )
        self._cnx_id = resp.id
        self.initialized = True

    def commit(self):
        pass

    def rollback(self):
        pass

    def cursor(self, factory=None):
        # let's initialize our connection before the first cursor call
        # we're waiting this long to make sure that all custom functions
        # have been registered
        if not self.initialized:
            self.initialize_remote_connection()
        if factory:
            return factory(self)
        return Cursor(self)

    def execute(self, sql, params=None):
        """
        for some reason the sqlite dbapi supports execute directly on the connection
        django also uses this when registering functions
        """
        cursor = self.cursor()
        cursor.execute(sql, params)
        return cursor

    def create_function(self, *args, **kwargs):
        name = args[0]
        num_args = args[1]
        func = args[2]
        self._function_register[name] = func

    def create_aggregate(self, *args, **kwargs):
        pass


class Cursor:
    grpc_stub = None
    connection = None
    description = [None for i in range(7)]
    rowcount = 0
    arraysize = 0

    # the following _vars represent a "buffer" of sorts
    # values would be set to the results from the latest .execute() call
    # this is because callers may not fetch all results at once, so we'd
    # need to keep results until "buffer" is emptied...
    _statement = None
    _rows = []
    _columns = []
    _last_insert_id = -1
    _affected_rows = -1

    _callback_queue = None
    _callback_thread = None
    _callback_invocations = None
    _sentinel = object()

    @property
    def lastrowid(self):
        return self._last_insert_id

    def __init__(self, connection):
        self.connection = connection
        self.grpc_stub = self.connection.grpc_stub
        self._init_callback()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def _process_invocations(self):
        try:
            # blocks until we get an invocation from the generator
            for invoke in self._callback_invocations:
                function = self.connection.function_register.get(invoke.functionName)
                if not function:
                    raise Error(f"function {invoke.functionName} not registered")
                result = function(*invoke.args)
                self._callback_queue.put(result)
        except grpc.RpcError as e:
            # we're cancelling the rpc on cursor.close()
            if e.code() != grpc.StatusCode.CANCELLED:
                raise e

    def _invocation_results_iterator(self):
        # block until we get a result from queue, the sentinel value should end the iterator
        for i in iter(self._callback_queue.get, self._sentinel):
            if i != self._sentinel:
                yield InvocationResult(result=[f"{i}"])

    def _init_callback(self):
        self._callback_queue = Queue(maxsize=0)
        # add the connection id to the request metadata
        metadata = [('cnx_id', self.connection.cnx_id)]
        self._callback_invocations = self.grpc_stub.Callback(self._invocation_results_iterator(), metadata=metadata)
        self._callback_thread = Thread(target=self._process_invocations)
        self._callback_thread.start()

    def close(self, *args, **kwargs):
        """ Closes the cursor. """
        self._callback_invocations.cancel()
        self._callback_thread.join(0)

    def _prepare_params(self, params):
        if params and len(params) > 0:
            # at this time using string types for all request & result params
            return (str(x) for x in params)
        return None

    def _cast_row_fields(self, fields):
        result = []
        for f in fields:
            try:
                f = literal_eval(f)
            except:
                pass
            result.append(f)
        return tuple(result)

    def _results_to_buffer(self, results: ExecuteOrQueryResult):
        self._columns = results.query_result.columns
        self._last_insert_id = results.execute_result.lastInsertId
        self._affected_rows = results.execute_result.affectedRows
        self._rows = [self._cast_row_fields(row.fields) for row in results.query_result.rows]

    def reset_buffer(self):
        self._rows = []
        self._columns = []
        self._last_insert_id = -1
        self._affected_rows = -1

    def execute(self, sql, params=None):
        """
        Executes remote query & put the result in the buffer
        """
        # reset buffer before we start executing, so that if there's a failure
        # we won't have any stale data
        self.reset_buffer()
        # we require all string params for now
        params = self._prepare_params(params)
        self._statement = Statement(sql=sql, params=params, cnx_id=self.connection.cnx_id)
        results: ExecuteOrQueryResult = self.grpc_stub.ExecuteOrQuery(self._statement)
        self._results_to_buffer(results)
        return self

    def executemany(self, *args, **kwargs):
        """ Repeatedly executes a SQL statement. """
        pass

    def executescript(self, *args, **kwargs):
        """ Executes a multiple SQL statements at once. Non-standard. """
        pass

    def fetchall(self):
        """ Fetches all (remaining) rows from the buffer """
        self._rows, fetched = [], self._rows
        return fetched

    def fetchmany(self, size):
        """ Fetches n=size rows and removes them from the buffer """
        fetched = []
        if size < len(self._rows):
            self._rows, fetched = self._rows[size:], self._rows[:size]
        else:
            self._rows, fetched = [], self._rows
        return fetched

    def fetchone(self, *args, **kwargs):
        """ Fetches one row from the buffer """
        rows = self.fetchmany(1)
        # avoid index out of range
        if len(rows) < 1:
            result = rows
            return result
        result = rows[0]
        return result

    def setinputsizes(self, *args, **kwargs):
        """ Required by DB-API """
        pass

    def setoutputsize(self, *args, **kwargs):
        """ Required by DB-API """
        pass
