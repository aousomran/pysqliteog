# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sqliteog.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0esqliteog.proto\"\x07\n\x05\x45mpty\"\x1a\n\x0c\x43onnectionId\x12\n\n\x02id\x18\x01 \x01(\t\"L\n\x11\x43onnectionRequest\x12\x0f\n\x07\x64\x62_name\x18\x01 \x01(\t\x12\x11\n\tfunctions\x18\x02 \x03(\t\x12\x13\n\x0b\x61ggregators\x18\x03 \x03(\t\"3\n\x10InvocationResult\x12\x0f\n\x07initial\x18\x01 \x01(\x08\x12\x0e\n\x06result\x18\x02 \x03(\t\",\n\x06Invoke\x12\x14\n\x0c\x66unctionName\x18\x01 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x02 \x03(\t\"b\n\x14\x45xecuteOrQueryResult\x12\"\n\x0cquery_result\x18\x01 \x01(\x0b\x32\x0c.QueryResult\x12&\n\x0e\x65xecute_result\x18\x02 \x01(\x0b\x32\x0e.ExecuteResult\"8\n\tStatement\x12\x0b\n\x03sql\x18\x01 \x01(\t\x12\x0e\n\x06params\x18\x02 \x03(\t\x12\x0e\n\x06\x63nx_id\x18\x03 \x01(\t\"\x15\n\x03Row\x12\x0e\n\x06\x66ields\x18\x01 \x03(\t\"G\n\x0bQueryResult\x12\x0f\n\x07\x63olumns\x18\x01 \x03(\t\x12\x13\n\x0b\x63olumnTypes\x18\x02 \x03(\t\x12\x12\n\x04rows\x18\x03 \x03(\x0b\x32\x04.Row\";\n\rExecuteResult\x12\x14\n\x0clastInsertId\x18\x01 \x01(\x03\x12\x14\n\x0c\x61\x66\x66\x65\x63tedRows\x18\x02 \x01(\x03\x32\x80\x03\n\x08SqliteOG\x12#\n\x05Query\x12\n.Statement\x1a\x0c.QueryResult\"\x00\x12\'\n\x07\x45xecute\x12\n.Statement\x1a\x0e.ExecuteResult\"\x00\x12\x35\n\x0e\x45xecuteOrQuery\x12\n.Statement\x1a\x15.ExecuteOrQueryResult\"\x00\x12,\n\x08\x43\x61llback\x12\x11.InvocationResult\x1a\x07.Invoke\"\x00(\x01\x30\x01\x12\x31\n\nConnection\x12\x12.ConnectionRequest\x1a\r.ConnectionId\"\x00\x12 \n\x05\x43lose\x12\r.ConnectionId\x1a\x06.Empty\"\x00\x12\"\n\x07IsValid\x12\r.ConnectionId\x1a\x06.Empty\"\x00\x12\x18\n\x04Ping\x12\x06.Empty\x1a\x06.Empty\"\x00\x12.\n\x0cResetSession\x12\r.ConnectionId\x1a\r.ConnectionId\"\x00\x42 Z\x1egithub.com/aousomran/sqlite-ogb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sqliteog_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\036github.com/aousomran/sqlite-og'
  _globals['_EMPTY']._serialized_start=18
  _globals['_EMPTY']._serialized_end=25
  _globals['_CONNECTIONID']._serialized_start=27
  _globals['_CONNECTIONID']._serialized_end=53
  _globals['_CONNECTIONREQUEST']._serialized_start=55
  _globals['_CONNECTIONREQUEST']._serialized_end=131
  _globals['_INVOCATIONRESULT']._serialized_start=133
  _globals['_INVOCATIONRESULT']._serialized_end=184
  _globals['_INVOKE']._serialized_start=186
  _globals['_INVOKE']._serialized_end=230
  _globals['_EXECUTEORQUERYRESULT']._serialized_start=232
  _globals['_EXECUTEORQUERYRESULT']._serialized_end=330
  _globals['_STATEMENT']._serialized_start=332
  _globals['_STATEMENT']._serialized_end=388
  _globals['_ROW']._serialized_start=390
  _globals['_ROW']._serialized_end=411
  _globals['_QUERYRESULT']._serialized_start=413
  _globals['_QUERYRESULT']._serialized_end=484
  _globals['_EXECUTERESULT']._serialized_start=486
  _globals['_EXECUTERESULT']._serialized_end=545
  _globals['_SQLITEOG']._serialized_start=548
  _globals['_SQLITEOG']._serialized_end=932
# @@protoc_insertion_point(module_scope)
