# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/broadcast/v1/broadcast.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%bilibili/broadcast/v1/broadcast.proto\x12\x15\x62ilibili.broadcast.v1\x1a\x19\x62ilibili/rpc/status.proto\x1a\x19google/protobuf/any.proto\x1a\x1bgoogle/protobuf/empty.proto\"=\n\x07\x41uthReq\x12\x0c\n\x04guid\x18\x01 \x01(\t\x12\x0f\n\x07\x63onn_id\x18\x02 \x01(\t\x12\x13\n\x0blast_msg_id\x18\x03 \x01(\x03\"\n\n\x08\x41uthResp\"~\n\x0e\x42roadcastFrame\x12\x33\n\x07options\x18\x01 \x01(\x0b\x32\".bilibili.broadcast.v1.FrameOption\x12\x13\n\x0btarget_path\x18\x02 \x01(\t\x12\"\n\x04\x62ody\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"\x90\x01\n\x0b\x46rameOption\x12\x12\n\nmessage_id\x18\x01 \x01(\x03\x12\x10\n\x08sequence\x18\x02 \x01(\x03\x12\x0e\n\x06is_ack\x18\x03 \x01(\x08\x12$\n\x06status\x18\x04 \x01(\x0b\x32\x14.bilibili.rpc.Status\x12\x12\n\nack_origin\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\x03\"\x0e\n\x0cHeartbeatReq\"\x0f\n\rHeartbeatResp\"H\n\rMessageAckReq\x12\x0e\n\x06\x61\x63k_id\x18\x01 \x01(\x03\x12\x12\n\nack_origin\x18\x02 \x01(\t\x12\x13\n\x0btarget_path\x18\x03 \x01(\t\"\"\n\nTargetPath\x12\x14\n\x0ctarget_paths\x18\x01 \x03(\t*-\n\x06\x41\x63tion\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06UPDATE\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\x32\x8a\x03\n\tBroadcast\x12G\n\x04\x41uth\x12\x1e.bilibili.broadcast.v1.AuthReq\x1a\x1f.bilibili.broadcast.v1.AuthResp\x12V\n\tHeartbeat\x12#.bilibili.broadcast.v1.HeartbeatReq\x1a$.bilibili.broadcast.v1.HeartbeatResp\x12\x46\n\tSubscribe\x12!.bilibili.broadcast.v1.TargetPath\x1a\x16.google.protobuf.Empty\x12H\n\x0bUnsubscribe\x12!.bilibili.broadcast.v1.TargetPath\x1a\x16.google.protobuf.Empty\x12J\n\nMessageAck\x12$.bilibili.broadcast.v1.MessageAckReq\x1a\x16.google.protobuf.Empty2s\n\x0f\x42roadcastTunnel\x12`\n\x0c\x43reateTunnel\x12%.bilibili.broadcast.v1.BroadcastFrame\x1a%.bilibili.broadcast.v1.BroadcastFrame(\x01\x30\x01\x62\x06proto3')

_ACTION = DESCRIPTOR.enum_types_by_name['Action']
Action = enum_type_wrapper.EnumTypeWrapper(_ACTION)
UNKNOWN = 0
UPDATE = 1
DELETE = 2


_AUTHREQ = DESCRIPTOR.message_types_by_name['AuthReq']
_AUTHRESP = DESCRIPTOR.message_types_by_name['AuthResp']
_BROADCASTFRAME = DESCRIPTOR.message_types_by_name['BroadcastFrame']
_FRAMEOPTION = DESCRIPTOR.message_types_by_name['FrameOption']
_HEARTBEATREQ = DESCRIPTOR.message_types_by_name['HeartbeatReq']
_HEARTBEATRESP = DESCRIPTOR.message_types_by_name['HeartbeatResp']
_MESSAGEACKREQ = DESCRIPTOR.message_types_by_name['MessageAckReq']
_TARGETPATH = DESCRIPTOR.message_types_by_name['TargetPath']
AuthReq = _reflection.GeneratedProtocolMessageType('AuthReq', (_message.Message,), {
  'DESCRIPTOR' : _AUTHREQ,
  '__module__' : 'bilibili.broadcast.v1.broadcast_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.broadcast.v1.AuthReq)
  })
_sym_db.RegisterMessage(AuthReq)

AuthResp = _reflection.GeneratedProtocolMessageType('AuthResp', (_message.Message,), {
  'DESCRIPTOR' : _AUTHRESP,
  '__module__' : 'bilibili.broadcast.v1.broadcast_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.broadcast.v1.AuthResp)
  })
_sym_db.RegisterMessage(AuthResp)

BroadcastFrame = _reflection.GeneratedProtocolMessageType('BroadcastFrame', (_message.Message,), {
  'DESCRIPTOR' : _BROADCASTFRAME,
  '__module__' : 'bilibili.broadcast.v1.broadcast_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.broadcast.v1.BroadcastFrame)
  })
_sym_db.RegisterMessage(BroadcastFrame)

FrameOption = _reflection.GeneratedProtocolMessageType('FrameOption', (_message.Message,), {
  'DESCRIPTOR' : _FRAMEOPTION,
  '__module__' : 'bilibili.broadcast.v1.broadcast_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.broadcast.v1.FrameOption)
  })
_sym_db.RegisterMessage(FrameOption)

HeartbeatReq = _reflection.GeneratedProtocolMessageType('HeartbeatReq', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATREQ,
  '__module__' : 'bilibili.broadcast.v1.broadcast_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.broadcast.v1.HeartbeatReq)
  })
_sym_db.RegisterMessage(HeartbeatReq)

HeartbeatResp = _reflection.GeneratedProtocolMessageType('HeartbeatResp', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATRESP,
  '__module__' : 'bilibili.broadcast.v1.broadcast_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.broadcast.v1.HeartbeatResp)
  })
_sym_db.RegisterMessage(HeartbeatResp)

MessageAckReq = _reflection.GeneratedProtocolMessageType('MessageAckReq', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEACKREQ,
  '__module__' : 'bilibili.broadcast.v1.broadcast_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.broadcast.v1.MessageAckReq)
  })
_sym_db.RegisterMessage(MessageAckReq)

TargetPath = _reflection.GeneratedProtocolMessageType('TargetPath', (_message.Message,), {
  'DESCRIPTOR' : _TARGETPATH,
  '__module__' : 'bilibili.broadcast.v1.broadcast_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.broadcast.v1.TargetPath)
  })
_sym_db.RegisterMessage(TargetPath)

_BROADCAST = DESCRIPTOR.services_by_name['Broadcast']
_BROADCASTTUNNEL = DESCRIPTOR.services_by_name['BroadcastTunnel']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ACTION._serialized_start=640
  _ACTION._serialized_end=685
  _AUTHREQ._serialized_start=147
  _AUTHREQ._serialized_end=208
  _AUTHRESP._serialized_start=210
  _AUTHRESP._serialized_end=220
  _BROADCASTFRAME._serialized_start=222
  _BROADCASTFRAME._serialized_end=348
  _FRAMEOPTION._serialized_start=351
  _FRAMEOPTION._serialized_end=495
  _HEARTBEATREQ._serialized_start=497
  _HEARTBEATREQ._serialized_end=511
  _HEARTBEATRESP._serialized_start=513
  _HEARTBEATRESP._serialized_end=528
  _MESSAGEACKREQ._serialized_start=530
  _MESSAGEACKREQ._serialized_end=602
  _TARGETPATH._serialized_start=604
  _TARGETPATH._serialized_end=638
  _BROADCAST._serialized_start=688
  _BROADCAST._serialized_end=1082
  _BROADCASTTUNNEL._serialized_start=1084
  _BROADCASTTUNNEL._serialized_end=1199
# @@protoc_insertion_point(module_scope)
