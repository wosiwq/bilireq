# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pgc/gaetway/vega/v1/vega.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bilireq.grpc.protos.bilibili.rpc import status_pb2 as bilibili_dot_rpc_dot_status__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1epgc/gaetway/vega/v1/vega.proto\x12\x13pgc.gateway.vega.v1\x1a\x19\x62ilibili/rpc/status.proto\x1a\x19google/protobuf/any.proto\x1a\x1bgoogle/protobuf/empty.proto\"\t\n\x07\x41uthReq\"\n\n\x08\x41uthResp\"\x97\x01\n\x0b\x46rameOption\x12\x0f\n\x07vega_id\x18\x01 \x01(\x03\x12\x0e\n\x06req_id\x18\x02 \x01(\t\x12\x10\n\x08sequence\x18\x03 \x01(\x03\x12\x0e\n\x06is_ack\x18\x04 \x01(\x08\x12$\n\x06status\x18\x05 \x01(\x0b\x32\x14.bilibili.rpc.Status\x12\x12\n\nack_origin\x18\x06 \x01(\t\x12\x0b\n\x03mid\x18\x07 \x01(\x03\"\x0e\n\x0cHeartbeatReq\"\x0f\n\rHeartbeatResp\"U\n\rMessageAckReq\x12\x0f\n\x07vega_id\x18\x01 \x01(\t\x12\x0e\n\x06req_id\x18\x02 \x01(\t\x12\x0e\n\x06origin\x18\x03 \x01(\t\x12\x13\n\x0btarget_path\x18\x04 \x01(\t\"E\n\x0cSubscribeReq\x12\x35\n\x0ctarget_paths\x18\x01 \x03(\x0b\x32\x1f.pgc.gateway.vega.v1.TargetPath\"=\n\nTargetPath\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x04subs\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"\x9d\x01\n\tVegaFrame\x12\x31\n\x07options\x18\x01 \x01(\x0b\x32 .pgc.gateway.vega.v1.FrameOption\x12\x12\n\nroute_path\x18\x02 \x01(\t\x12\"\n\x04\x62ody\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12%\n\x07sub_biz\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any2V\n\x04Vega\x12N\n\x0c\x43reateTunnel\x12\x1e.pgc.gateway.vega.v1.VegaFrame\x1a\x1e.pgc.gateway.vega.v1.VegaFrame2\xb9\x02\n\x0cVegaFrameDoc\x12\x43\n\x04\x41uth\x12\x1c.pgc.gateway.vega.v1.AuthReq\x1a\x1d.pgc.gateway.vega.v1.AuthResp\x12R\n\tHeartbeat\x12!.pgc.gateway.vega.v1.HeartbeatReq\x1a\".pgc.gateway.vega.v1.HeartbeatResp\x12H\n\nMessageAck\x12\".pgc.gateway.vega.v1.MessageAckReq\x1a\x16.google.protobuf.Empty\x12\x46\n\tSubscribe\x12!.pgc.gateway.vega.v1.SubscribeReq\x1a\x16.google.protobuf.Emptyb\x06proto3')



_AUTHREQ = DESCRIPTOR.message_types_by_name['AuthReq']
_AUTHRESP = DESCRIPTOR.message_types_by_name['AuthResp']
_FRAMEOPTION = DESCRIPTOR.message_types_by_name['FrameOption']
_HEARTBEATREQ = DESCRIPTOR.message_types_by_name['HeartbeatReq']
_HEARTBEATRESP = DESCRIPTOR.message_types_by_name['HeartbeatResp']
_MESSAGEACKREQ = DESCRIPTOR.message_types_by_name['MessageAckReq']
_SUBSCRIBEREQ = DESCRIPTOR.message_types_by_name['SubscribeReq']
_TARGETPATH = DESCRIPTOR.message_types_by_name['TargetPath']
_VEGAFRAME = DESCRIPTOR.message_types_by_name['VegaFrame']
AuthReq = _reflection.GeneratedProtocolMessageType('AuthReq', (_message.Message,), {
  'DESCRIPTOR' : _AUTHREQ,
  '__module__' : 'pgc.gaetway.vega.v1.vega_pb2'
  # @@protoc_insertion_point(class_scope:pgc.gateway.vega.v1.AuthReq)
  })
_sym_db.RegisterMessage(AuthReq)

AuthResp = _reflection.GeneratedProtocolMessageType('AuthResp', (_message.Message,), {
  'DESCRIPTOR' : _AUTHRESP,
  '__module__' : 'pgc.gaetway.vega.v1.vega_pb2'
  # @@protoc_insertion_point(class_scope:pgc.gateway.vega.v1.AuthResp)
  })
_sym_db.RegisterMessage(AuthResp)

FrameOption = _reflection.GeneratedProtocolMessageType('FrameOption', (_message.Message,), {
  'DESCRIPTOR' : _FRAMEOPTION,
  '__module__' : 'pgc.gaetway.vega.v1.vega_pb2'
  # @@protoc_insertion_point(class_scope:pgc.gateway.vega.v1.FrameOption)
  })
_sym_db.RegisterMessage(FrameOption)

HeartbeatReq = _reflection.GeneratedProtocolMessageType('HeartbeatReq', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATREQ,
  '__module__' : 'pgc.gaetway.vega.v1.vega_pb2'
  # @@protoc_insertion_point(class_scope:pgc.gateway.vega.v1.HeartbeatReq)
  })
_sym_db.RegisterMessage(HeartbeatReq)

HeartbeatResp = _reflection.GeneratedProtocolMessageType('HeartbeatResp', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATRESP,
  '__module__' : 'pgc.gaetway.vega.v1.vega_pb2'
  # @@protoc_insertion_point(class_scope:pgc.gateway.vega.v1.HeartbeatResp)
  })
_sym_db.RegisterMessage(HeartbeatResp)

MessageAckReq = _reflection.GeneratedProtocolMessageType('MessageAckReq', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEACKREQ,
  '__module__' : 'pgc.gaetway.vega.v1.vega_pb2'
  # @@protoc_insertion_point(class_scope:pgc.gateway.vega.v1.MessageAckReq)
  })
_sym_db.RegisterMessage(MessageAckReq)

SubscribeReq = _reflection.GeneratedProtocolMessageType('SubscribeReq', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEREQ,
  '__module__' : 'pgc.gaetway.vega.v1.vega_pb2'
  # @@protoc_insertion_point(class_scope:pgc.gateway.vega.v1.SubscribeReq)
  })
_sym_db.RegisterMessage(SubscribeReq)

TargetPath = _reflection.GeneratedProtocolMessageType('TargetPath', (_message.Message,), {
  'DESCRIPTOR' : _TARGETPATH,
  '__module__' : 'pgc.gaetway.vega.v1.vega_pb2'
  # @@protoc_insertion_point(class_scope:pgc.gateway.vega.v1.TargetPath)
  })
_sym_db.RegisterMessage(TargetPath)

VegaFrame = _reflection.GeneratedProtocolMessageType('VegaFrame', (_message.Message,), {
  'DESCRIPTOR' : _VEGAFRAME,
  '__module__' : 'pgc.gaetway.vega.v1.vega_pb2'
  # @@protoc_insertion_point(class_scope:pgc.gateway.vega.v1.VegaFrame)
  })
_sym_db.RegisterMessage(VegaFrame)

_VEGA = DESCRIPTOR.services_by_name['Vega']
_VEGAFRAMEDOC = DESCRIPTOR.services_by_name['VegaFrameDoc']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AUTHREQ._serialized_start=138
  _AUTHREQ._serialized_end=147
  _AUTHRESP._serialized_start=149
  _AUTHRESP._serialized_end=159
  _FRAMEOPTION._serialized_start=162
  _FRAMEOPTION._serialized_end=313
  _HEARTBEATREQ._serialized_start=315
  _HEARTBEATREQ._serialized_end=329
  _HEARTBEATRESP._serialized_start=331
  _HEARTBEATRESP._serialized_end=346
  _MESSAGEACKREQ._serialized_start=348
  _MESSAGEACKREQ._serialized_end=433
  _SUBSCRIBEREQ._serialized_start=435
  _SUBSCRIBEREQ._serialized_end=504
  _TARGETPATH._serialized_start=506
  _TARGETPATH._serialized_end=567
  _VEGAFRAME._serialized_start=570
  _VEGAFRAME._serialized_end=727
  _VEGA._serialized_start=729
  _VEGA._serialized_end=815
  _VEGAFRAMEDOC._serialized_start=818
  _VEGAFRAMEDOC._serialized_end=1131
# @@protoc_insertion_point(module_scope)
