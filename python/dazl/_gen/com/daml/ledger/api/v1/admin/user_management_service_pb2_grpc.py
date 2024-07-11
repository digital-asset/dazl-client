# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import user_management_service_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2


class UserManagementServiceStub(object):
    """Service to manage users and their rights for interacting with the Ledger API
    served by a participant node.

    The authorization rules for its RPCs are specified on the ``<RpcName>Request``
    messages as boolean expressions over these facts:
    (1) ``HasRight(r)`` denoting whether the authenticated user has right ``r`` and
    (2) ``IsAuthenticatedUser(uid)`` denoting whether ``uid`` is the empty string or equal to the id of the authenticated user.
    (3) ``IsAuthenticatedIdentityProviderAdmin(idp)`` denoting whether ``idp`` is equal to the ``identity_provider_id``
    of the authenticated user and the user has an IdentityProviderAdmin right.
    If `user_id` is set to the empty string (the default), then the data for the authenticated user will be retrieved.
    If `identity_provider_id` is set to an empty string, then it's effectively set to the value of access token's 'iss' field if that is provided.
    If `identity_provider_id` remains an empty string, the default identity provider will be assumed.

    The fields of request messages (and sub-messages) are marked either as ``Optional`` or ``Required``:
    (1) ``Optional`` denoting the client may leave the field unset when sending a request.
    (2) ``Required`` denoting the client must set the field to a non-default value when sending a request.

    A user resource consists of:
    (1) a set of properties represented by the ``User`` message,
    (2) a set of user rights, where each right is represented by the ``Right`` message.

    A user resource, once it has been created, can be modified.
    In order to update the properties represented by the ``User`` message use the ``UpdateUser`` RPC. The only fields that can be modified are those marked as ``Modifiable``.
    In order to grant or revoke user rights use ``GrantRights' and ``RevokeRights`` RPCs.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/com.daml.ledger.api.v1.admin.UserManagementService/CreateUser',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.CreateUserResponse.FromString,
                )
        self.GetUser = channel.unary_unary(
                '/com.daml.ledger.api.v1.admin.UserManagementService/GetUser',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.GetUserRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.GetUserResponse.FromString,
                )
        self.UpdateUser = channel.unary_unary(
                '/com.daml.ledger.api.v1.admin.UserManagementService/UpdateUser',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.UpdateUserResponse.FromString,
                )
        self.DeleteUser = channel.unary_unary(
                '/com.daml.ledger.api.v1.admin.UserManagementService/DeleteUser',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.DeleteUserResponse.FromString,
                )
        self.ListUsers = channel.unary_unary(
                '/com.daml.ledger.api.v1.admin.UserManagementService/ListUsers',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.ListUsersRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.ListUsersResponse.FromString,
                )
        self.GrantUserRights = channel.unary_unary(
                '/com.daml.ledger.api.v1.admin.UserManagementService/GrantUserRights',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.GrantUserRightsRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.GrantUserRightsResponse.FromString,
                )
        self.RevokeUserRights = channel.unary_unary(
                '/com.daml.ledger.api.v1.admin.UserManagementService/RevokeUserRights',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.RevokeUserRightsRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.RevokeUserRightsResponse.FromString,
                )
        self.ListUserRights = channel.unary_unary(
                '/com.daml.ledger.api.v1.admin.UserManagementService/ListUserRights',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.ListUserRightsRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.ListUserRightsResponse.FromString,
                )
        self.UpdateUserIdentityProviderId = channel.unary_unary(
                '/com.daml.ledger.api.v1.admin.UserManagementService/UpdateUserIdentityProviderId',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.UpdateUserIdentityProviderRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.UpdateUserIdentityProviderResponse.FromString,
                )


class UserManagementServiceServicer(object):
    """Service to manage users and their rights for interacting with the Ledger API
    served by a participant node.

    The authorization rules for its RPCs are specified on the ``<RpcName>Request``
    messages as boolean expressions over these facts:
    (1) ``HasRight(r)`` denoting whether the authenticated user has right ``r`` and
    (2) ``IsAuthenticatedUser(uid)`` denoting whether ``uid`` is the empty string or equal to the id of the authenticated user.
    (3) ``IsAuthenticatedIdentityProviderAdmin(idp)`` denoting whether ``idp`` is equal to the ``identity_provider_id``
    of the authenticated user and the user has an IdentityProviderAdmin right.
    If `user_id` is set to the empty string (the default), then the data for the authenticated user will be retrieved.
    If `identity_provider_id` is set to an empty string, then it's effectively set to the value of access token's 'iss' field if that is provided.
    If `identity_provider_id` remains an empty string, the default identity provider will be assumed.

    The fields of request messages (and sub-messages) are marked either as ``Optional`` or ``Required``:
    (1) ``Optional`` denoting the client may leave the field unset when sending a request.
    (2) ``Required`` denoting the client must set the field to a non-default value when sending a request.

    A user resource consists of:
    (1) a set of properties represented by the ``User`` message,
    (2) a set of user rights, where each right is represented by the ``Right`` message.

    A user resource, once it has been created, can be modified.
    In order to update the properties represented by the ``User`` message use the ``UpdateUser`` RPC. The only fields that can be modified are those marked as ``Modifiable``.
    In order to grant or revoke user rights use ``GrantRights' and ``RevokeRights`` RPCs.
    """

    def CreateUser(self, request, context):
        """Create a new user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUser(self, request, context):
        """Get the user data of a specific user or the authenticated user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Update selected modifiable attribute of a user resource described by the ``User`` message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Delete an existing user and all its rights.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUsers(self, request, context):
        """List all existing users.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GrantUserRights(self, request, context):
        """Grant rights to a user.
        Granting rights does not affect the resource version of the corresponding user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevokeUserRights(self, request, context):
        """Revoke rights from a user.
        Revoking rights does not affect the resource version of the corresponding user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUserRights(self, request, context):
        """List the set of all rights granted to a user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUserIdentityProviderId(self, request, context):
        """Update the assignment of a user from one IDP to another.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserManagementServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.CreateUserRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.CreateUserResponse.SerializeToString,
            ),
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.GetUserRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.GetUserResponse.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.UpdateUserRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.UpdateUserResponse.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.DeleteUserRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.DeleteUserResponse.SerializeToString,
            ),
            'ListUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUsers,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.ListUsersRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.ListUsersResponse.SerializeToString,
            ),
            'GrantUserRights': grpc.unary_unary_rpc_method_handler(
                    servicer.GrantUserRights,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.GrantUserRightsRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.GrantUserRightsResponse.SerializeToString,
            ),
            'RevokeUserRights': grpc.unary_unary_rpc_method_handler(
                    servicer.RevokeUserRights,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.RevokeUserRightsRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.RevokeUserRightsResponse.SerializeToString,
            ),
            'ListUserRights': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUserRights,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.ListUserRightsRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.ListUserRightsResponse.SerializeToString,
            ),
            'UpdateUserIdentityProviderId': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUserIdentityProviderId,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.UpdateUserIdentityProviderRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.UpdateUserIdentityProviderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.daml.ledger.api.v1.admin.UserManagementService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserManagementService(object):
    """Service to manage users and their rights for interacting with the Ledger API
    served by a participant node.

    The authorization rules for its RPCs are specified on the ``<RpcName>Request``
    messages as boolean expressions over these facts:
    (1) ``HasRight(r)`` denoting whether the authenticated user has right ``r`` and
    (2) ``IsAuthenticatedUser(uid)`` denoting whether ``uid`` is the empty string or equal to the id of the authenticated user.
    (3) ``IsAuthenticatedIdentityProviderAdmin(idp)`` denoting whether ``idp`` is equal to the ``identity_provider_id``
    of the authenticated user and the user has an IdentityProviderAdmin right.
    If `user_id` is set to the empty string (the default), then the data for the authenticated user will be retrieved.
    If `identity_provider_id` is set to an empty string, then it's effectively set to the value of access token's 'iss' field if that is provided.
    If `identity_provider_id` remains an empty string, the default identity provider will be assumed.

    The fields of request messages (and sub-messages) are marked either as ``Optional`` or ``Required``:
    (1) ``Optional`` denoting the client may leave the field unset when sending a request.
    (2) ``Required`` denoting the client must set the field to a non-default value when sending a request.

    A user resource consists of:
    (1) a set of properties represented by the ``User`` message,
    (2) a set of user rights, where each right is represented by the ``Right`` message.

    A user resource, once it has been created, can be modified.
    In order to update the properties represented by the ``User`` message use the ``UpdateUser`` RPC. The only fields that can be modified are those marked as ``Modifiable``.
    In order to grant or revoke user rights use ``GrantRights' and ``RevokeRights`` RPCs.
    """

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.admin.UserManagementService/CreateUser',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.CreateUserRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.CreateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.admin.UserManagementService/GetUser',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.GetUserRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.GetUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.admin.UserManagementService/UpdateUser',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.UpdateUserRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.UpdateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.admin.UserManagementService/DeleteUser',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.DeleteUserRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.DeleteUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.admin.UserManagementService/ListUsers',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.ListUsersRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.ListUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GrantUserRights(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.admin.UserManagementService/GrantUserRights',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.GrantUserRightsRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.GrantUserRightsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RevokeUserRights(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.admin.UserManagementService/RevokeUserRights',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.RevokeUserRightsRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.RevokeUserRightsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUserRights(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.admin.UserManagementService/ListUserRights',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.ListUserRightsRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.ListUserRightsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUserIdentityProviderId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.admin.UserManagementService/UpdateUserIdentityProviderId',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.UpdateUserIdentityProviderRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_user__management__service__pb2.UpdateUserIdentityProviderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
