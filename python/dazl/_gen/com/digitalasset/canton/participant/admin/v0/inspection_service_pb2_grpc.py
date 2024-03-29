# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import inspection_service_pb2 as com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2


class InspectionServiceStub(object):
    """*
    Inspection Service

    Supports inspecting the Participant for details about its ledger.
    This contains only a subset of the ParticipantInspection commands that can run over the admin-api instead of requiring
    direct access to the participant node instance.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LookupContractDomain = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupContractDomain',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupContractDomain.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupContractDomain.Response.FromString,
                )
        self.LookupTransactionDomain = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupTransactionDomain',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupTransactionDomain.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupTransactionDomain.Response.FromString,
                )
        self.LookupOffsetByTime = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupOffsetByTime',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByTime.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByTime.Response.FromString,
                )
        self.LookupOffsetByIndex = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupOffsetByIndex',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByIndex.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByIndex.Response.FromString,
                )


class InspectionServiceServicer(object):
    """*
    Inspection Service

    Supports inspecting the Participant for details about its ledger.
    This contains only a subset of the ParticipantInspection commands that can run over the admin-api instead of requiring
    direct access to the participant node instance.
    """

    def LookupContractDomain(self, request, context):
        """Lookup the domain where a contract is currently active.
        Supports querying many contracts at once.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupTransactionDomain(self, request, context):
        """Lookup the domain that the transaction was committed over. Can fail with NOT_FOUND if no domain was found.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupOffsetByTime(self, request, context):
        """Look up the ledger offset corresponding to the timestamp, specifically the largest offset such that no later
        offset corresponds to a later timestamp than the specified one.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupOffsetByIndex(self, request, context):
        """Look up the ledger offset by an index, e.g. 1 returns the first offset, 2 the second, etc.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InspectionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LookupContractDomain': grpc.unary_unary_rpc_method_handler(
                    servicer.LookupContractDomain,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupContractDomain.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupContractDomain.Response.SerializeToString,
            ),
            'LookupTransactionDomain': grpc.unary_unary_rpc_method_handler(
                    servicer.LookupTransactionDomain,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupTransactionDomain.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupTransactionDomain.Response.SerializeToString,
            ),
            'LookupOffsetByTime': grpc.unary_unary_rpc_method_handler(
                    servicer.LookupOffsetByTime,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByTime.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByTime.Response.SerializeToString,
            ),
            'LookupOffsetByIndex': grpc.unary_unary_rpc_method_handler(
                    servicer.LookupOffsetByIndex,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByIndex.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByIndex.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.digitalasset.canton.participant.admin.v0.InspectionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InspectionService(object):
    """*
    Inspection Service

    Supports inspecting the Participant for details about its ledger.
    This contains only a subset of the ParticipantInspection commands that can run over the admin-api instead of requiring
    direct access to the participant node instance.
    """

    @staticmethod
    def LookupContractDomain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupContractDomain',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupContractDomain.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupContractDomain.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LookupTransactionDomain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupTransactionDomain',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupTransactionDomain.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupTransactionDomain.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LookupOffsetByTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupOffsetByTime',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByTime.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByTime.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LookupOffsetByIndex(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupOffsetByIndex',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByIndex.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByIndex.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
