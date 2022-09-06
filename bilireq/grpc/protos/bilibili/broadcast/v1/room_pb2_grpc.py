# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bilireq.grpc.protos.bilibili.broadcast.v1 import room_pb2 as bilibili_dot_broadcast_dot_v1_dot_room__pb2


class BroadcastRoomStub(object):
    """
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Enter = channel.stream_stream(
                '/bilibili.broadcast.v1.BroadcastRoom/Enter',
                request_serializer=bilibili_dot_broadcast_dot_v1_dot_room__pb2.RoomReq.SerializeToString,
                response_deserializer=bilibili_dot_broadcast_dot_v1_dot_room__pb2.RoomResp.FromString,
                )


class BroadcastRoomServicer(object):
    """
    """

    def Enter(self, request_iterator, context):
        """
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BroadcastRoomServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Enter': grpc.stream_stream_rpc_method_handler(
                    servicer.Enter,
                    request_deserializer=bilibili_dot_broadcast_dot_v1_dot_room__pb2.RoomReq.FromString,
                    response_serializer=bilibili_dot_broadcast_dot_v1_dot_room__pb2.RoomResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bilibili.broadcast.v1.BroadcastRoom', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BroadcastRoom(object):
    """
    """

    @staticmethod
    def Enter(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/bilibili.broadcast.v1.BroadcastRoom/Enter',
            bilibili_dot_broadcast_dot_v1_dot_room__pb2.RoomReq.SerializeToString,
            bilibili_dot_broadcast_dot_v1_dot_room__pb2.RoomResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
