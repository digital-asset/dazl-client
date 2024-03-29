# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import enterprise_participant_replication_service_pb2 as com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_enterprise__participant__replication__service__pb2


class EnterpriseParticipantReplicationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetPassive = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.EnterpriseParticipantReplicationService/SetPassive',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_enterprise__participant__replication__service__pb2.SetPassive.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_enterprise__participant__replication__service__pb2.SetPassive.Response.FromString,
                )


class EnterpriseParticipantReplicationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetPassive(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EnterpriseParticipantReplicationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetPassive': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPassive,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_enterprise__participant__replication__service__pb2.SetPassive.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_enterprise__participant__replication__service__pb2.SetPassive.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.digitalasset.canton.participant.admin.v0.EnterpriseParticipantReplicationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EnterpriseParticipantReplicationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetPassive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.EnterpriseParticipantReplicationService/SetPassive',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_enterprise__participant__replication__service__pb2.SetPassive.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_enterprise__participant__replication__service__pb2.SetPassive.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
