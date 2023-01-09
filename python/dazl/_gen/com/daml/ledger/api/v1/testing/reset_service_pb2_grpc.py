# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import reset_service_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_testing_dot_reset__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ResetServiceStub(object):
    """Service to reset the ledger state. The goal here is to be able to reset the state in a way
    that's much faster compared to restarting the whole ledger application (be it a sandbox
    or the real ledger server).

    Note that *all* state present in the ledger implementation will be reset, most importantly
    including the ledger ID. This means that clients will have to re-fetch the ledger ID
    from the identity service after hitting this endpoint.

    The semantics are as follows:

    * When the reset service returns the reset is initiated, but not completed;
    * While the reset is performed, the ledger will not accept new requests. In fact we guarantee
    that ledger stops accepting new requests by the time the response to Reset is delivered;
    * In-flight requests might be aborted, we make no guarantees on when or how quickly this
    happens;
    * The ledger might be unavailable for a period of time before the reset is complete.

    Given the above, the recommended mode of operation for clients of the reset endpoint is to
    call it, then call the ledger identity endpoint in a retry loop that will tolerate a brief
    window when the ledger is down, and resume operation as soon as the new ledger ID is delivered.

    Note that this service will be available on the sandbox and might be available in some other testing
    environments, but will *never* be available in production.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Reset = channel.unary_unary(
                '/com.daml.ledger.api.v1.testing.ResetService/Reset',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_testing_dot_reset__service__pb2.ResetRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class ResetServiceServicer(object):
    """Service to reset the ledger state. The goal here is to be able to reset the state in a way
    that's much faster compared to restarting the whole ledger application (be it a sandbox
    or the real ledger server).

    Note that *all* state present in the ledger implementation will be reset, most importantly
    including the ledger ID. This means that clients will have to re-fetch the ledger ID
    from the identity service after hitting this endpoint.

    The semantics are as follows:

    * When the reset service returns the reset is initiated, but not completed;
    * While the reset is performed, the ledger will not accept new requests. In fact we guarantee
    that ledger stops accepting new requests by the time the response to Reset is delivered;
    * In-flight requests might be aborted, we make no guarantees on when or how quickly this
    happens;
    * The ledger might be unavailable for a period of time before the reset is complete.

    Given the above, the recommended mode of operation for clients of the reset endpoint is to
    call it, then call the ledger identity endpoint in a retry loop that will tolerate a brief
    window when the ledger is down, and resume operation as soon as the new ledger ID is delivered.

    Note that this service will be available on the sandbox and might be available in some other testing
    environments, but will *never* be available in production.
    """

    def Reset(self, request, context):
        """Resets the ledger state. Note that loaded DARs won't be removed -- this only rolls back the
        ledger to genesis.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ResetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Reset': grpc.unary_unary_rpc_method_handler(
                    servicer.Reset,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_testing_dot_reset__service__pb2.ResetRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.daml.ledger.api.v1.testing.ResetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ResetService(object):
    """Service to reset the ledger state. The goal here is to be able to reset the state in a way
    that's much faster compared to restarting the whole ledger application (be it a sandbox
    or the real ledger server).

    Note that *all* state present in the ledger implementation will be reset, most importantly
    including the ledger ID. This means that clients will have to re-fetch the ledger ID
    from the identity service after hitting this endpoint.

    The semantics are as follows:

    * When the reset service returns the reset is initiated, but not completed;
    * While the reset is performed, the ledger will not accept new requests. In fact we guarantee
    that ledger stops accepting new requests by the time the response to Reset is delivered;
    * In-flight requests might be aborted, we make no guarantees on when or how quickly this
    happens;
    * The ledger might be unavailable for a period of time before the reset is complete.

    Given the above, the recommended mode of operation for clients of the reset endpoint is to
    call it, then call the ledger identity endpoint in a retry loop that will tolerate a brief
    window when the ledger is down, and resume operation as soon as the new ledger ID is delivered.

    Note that this service will be available on the sandbox and might be available in some other testing
    environments, but will *never* be available in production.
    """

    @staticmethod
    def Reset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.testing.ResetService/Reset',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_testing_dot_reset__service__pb2.ResetRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
