# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import ledger_configuration_service_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__configuration__service__pb2


class LedgerConfigurationServiceStub(object):
  """LedgerConfigurationService allows clients to subscribe to changes of the ledger configuration.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetLedgerConfiguration = channel.unary_stream(
        '/com.daml.ledger.api.v1.LedgerConfigurationService/GetLedgerConfiguration',
        request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__configuration__service__pb2.GetLedgerConfigurationRequest.SerializeToString,
        response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__configuration__service__pb2.GetLedgerConfigurationResponse.FromString,
        )


class LedgerConfigurationServiceServicer(object):
  """LedgerConfigurationService allows clients to subscribe to changes of the ledger configuration.
  """

  def GetLedgerConfiguration(self, request, context):
    """Returns the latest configuration as the first response, and publishes configuration updates in the same stream.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LedgerConfigurationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetLedgerConfiguration': grpc.unary_stream_rpc_method_handler(
          servicer.GetLedgerConfiguration,
          request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__configuration__service__pb2.GetLedgerConfigurationRequest.FromString,
          response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__configuration__service__pb2.GetLedgerConfigurationResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.daml.ledger.api.v1.LedgerConfigurationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
