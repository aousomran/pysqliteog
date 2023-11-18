from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ConnectionId(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ConnectionRequest(_message.Message):
    __slots__ = ["db_name", "functions", "aggregators"]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATORS_FIELD_NUMBER: _ClassVar[int]
    db_name: str
    functions: _containers.RepeatedScalarFieldContainer[str]
    aggregators: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, db_name: _Optional[str] = ..., functions: _Optional[_Iterable[str]] = ..., aggregators: _Optional[_Iterable[str]] = ...) -> None: ...

class InvocationResult(_message.Message):
    __slots__ = ["initial", "result"]
    INITIAL_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    initial: bool
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, initial: bool = ..., result: _Optional[_Iterable[str]] = ...) -> None: ...

class Invoke(_message.Message):
    __slots__ = ["functionName", "args"]
    FUNCTIONNAME_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    functionName: str
    args: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, functionName: _Optional[str] = ..., args: _Optional[_Iterable[str]] = ...) -> None: ...

class ExecuteOrQueryResult(_message.Message):
    __slots__ = ["query_result", "execute_result"]
    QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_RESULT_FIELD_NUMBER: _ClassVar[int]
    query_result: QueryResult
    execute_result: ExecuteResult
    def __init__(self, query_result: _Optional[_Union[QueryResult, _Mapping]] = ..., execute_result: _Optional[_Union[ExecuteResult, _Mapping]] = ...) -> None: ...

class Statement(_message.Message):
    __slots__ = ["sql", "params", "cnx_id"]
    SQL_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    CNX_ID_FIELD_NUMBER: _ClassVar[int]
    sql: str
    params: _containers.RepeatedScalarFieldContainer[str]
    cnx_id: str
    def __init__(self, sql: _Optional[str] = ..., params: _Optional[_Iterable[str]] = ..., cnx_id: _Optional[str] = ...) -> None: ...

class Row(_message.Message):
    __slots__ = ["fields"]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, fields: _Optional[_Iterable[str]] = ...) -> None: ...

class QueryResult(_message.Message):
    __slots__ = ["columns", "columnTypes", "rows"]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    COLUMNTYPES_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedScalarFieldContainer[str]
    columnTypes: _containers.RepeatedScalarFieldContainer[str]
    rows: _containers.RepeatedCompositeFieldContainer[Row]
    def __init__(self, columns: _Optional[_Iterable[str]] = ..., columnTypes: _Optional[_Iterable[str]] = ..., rows: _Optional[_Iterable[_Union[Row, _Mapping]]] = ...) -> None: ...

class ExecuteResult(_message.Message):
    __slots__ = ["lastInsertId", "affectedRows"]
    LASTINSERTID_FIELD_NUMBER: _ClassVar[int]
    AFFECTEDROWS_FIELD_NUMBER: _ClassVar[int]
    lastInsertId: int
    affectedRows: int
    def __init__(self, lastInsertId: _Optional[int] = ..., affectedRows: _Optional[int] = ...) -> None: ...
