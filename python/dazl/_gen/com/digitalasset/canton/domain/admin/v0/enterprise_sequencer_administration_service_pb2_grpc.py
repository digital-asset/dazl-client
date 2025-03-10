# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import enterprise_sequencer_administration_service_pb2 as com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2
from ....pruning.admin.v0 import pruning_pb2 as com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in com/digitalasset/canton/domain/admin/v0/enterprise_sequencer_administration_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class EnterpriseSequencerAdministrationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Prune = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/Prune',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.Pruning.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.Pruning.Response.FromString,
                _registered_method=True)
        self.Snapshot = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/Snapshot',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.Snapshot.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.Snapshot.Response.FromString,
                _registered_method=True)
        self.DisableMember = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/DisableMember',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.DisableMemberRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.AuthorizeLedgerIdentity = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/AuthorizeLedgerIdentity',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.LedgerIdentity.AuthorizeRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.LedgerIdentity.AuthorizeResponse.FromString,
                _registered_method=True)
        self.SetSchedule = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetSchedule',
                request_serializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetSchedule.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetSchedule.Response.FromString,
                _registered_method=True)
        self.SetCron = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetCron',
                request_serializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetCron.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetCron.Response.FromString,
                _registered_method=True)
        self.SetMaxDuration = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetMaxDuration',
                request_serializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetMaxDuration.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetMaxDuration.Response.FromString,
                _registered_method=True)
        self.SetRetention = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetRetention',
                request_serializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetRetention.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetRetention.Response.FromString,
                _registered_method=True)
        self.ClearSchedule = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/ClearSchedule',
                request_serializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.ClearSchedule.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.ClearSchedule.Response.FromString,
                _registered_method=True)
        self.GetSchedule = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/GetSchedule',
                request_serializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.GetSchedule.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.GetSchedule.Response.FromString,
                _registered_method=True)
        self.LocatePruningTimestamp = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/LocatePruningTimestamp',
                request_serializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.LocatePruningTimestamp.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.LocatePruningTimestamp.Response.FromString,
                _registered_method=True)


class EnterpriseSequencerAdministrationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Prune(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Snapshot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableMember(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuthorizeLedgerIdentity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSchedule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCron(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetMaxDuration(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetRetention(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearSchedule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSchedule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LocatePruningTimestamp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EnterpriseSequencerAdministrationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Prune': grpc.unary_unary_rpc_method_handler(
                    servicer.Prune,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.Pruning.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.Pruning.Response.SerializeToString,
            ),
            'Snapshot': grpc.unary_unary_rpc_method_handler(
                    servicer.Snapshot,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.Snapshot.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.Snapshot.Response.SerializeToString,
            ),
            'DisableMember': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableMember,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.DisableMemberRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'AuthorizeLedgerIdentity': grpc.unary_unary_rpc_method_handler(
                    servicer.AuthorizeLedgerIdentity,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.LedgerIdentity.AuthorizeRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.LedgerIdentity.AuthorizeResponse.SerializeToString,
            ),
            'SetSchedule': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSchedule,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetSchedule.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetSchedule.Response.SerializeToString,
            ),
            'SetCron': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCron,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetCron.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetCron.Response.SerializeToString,
            ),
            'SetMaxDuration': grpc.unary_unary_rpc_method_handler(
                    servicer.SetMaxDuration,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetMaxDuration.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetMaxDuration.Response.SerializeToString,
            ),
            'SetRetention': grpc.unary_unary_rpc_method_handler(
                    servicer.SetRetention,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetRetention.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetRetention.Response.SerializeToString,
            ),
            'ClearSchedule': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearSchedule,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.ClearSchedule.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.ClearSchedule.Response.SerializeToString,
            ),
            'GetSchedule': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSchedule,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.GetSchedule.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.GetSchedule.Response.SerializeToString,
            ),
            'LocatePruningTimestamp': grpc.unary_unary_rpc_method_handler(
                    servicer.LocatePruningTimestamp,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.LocatePruningTimestamp.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.LocatePruningTimestamp.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class EnterpriseSequencerAdministrationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Prune(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/Prune',
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.Pruning.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.Pruning.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Snapshot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/Snapshot',
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.Snapshot.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.Snapshot.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DisableMember(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/DisableMember',
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.DisableMemberRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AuthorizeLedgerIdentity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/AuthorizeLedgerIdentity',
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.LedgerIdentity.AuthorizeRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_enterprise__sequencer__administration__service__pb2.LedgerIdentity.AuthorizeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetSchedule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetSchedule',
            com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetSchedule.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetSchedule.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetCron(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetCron',
            com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetCron.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetCron.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetMaxDuration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetMaxDuration',
            com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetMaxDuration.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetMaxDuration.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetRetention(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetRetention',
            com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetRetention.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.SetRetention.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ClearSchedule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/ClearSchedule',
            com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.ClearSchedule.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.ClearSchedule.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetSchedule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/GetSchedule',
            com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.GetSchedule.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.GetSchedule.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def LocatePruningTimestamp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/LocatePruningTimestamp',
            com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.LocatePruningTimestamp.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2.LocatePruningTimestamp.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
