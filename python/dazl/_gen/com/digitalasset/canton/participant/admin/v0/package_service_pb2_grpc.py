# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import package_service_pb2 as com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class PackageServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListPackages = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.PackageService/ListPackages',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListPackagesRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListPackagesResponse.FromString,
                )
        self.ListPackageContents = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.PackageService/ListPackageContents',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListPackageContentsRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListPackageContentsResponse.FromString,
                )
        self.ListDars = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.PackageService/ListDars',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListDarsRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListDarsResponse.FromString,
                )
        self.ListDarContents = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.PackageService/ListDarContents',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListDarContentsRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListDarContentsResponse.FromString,
                )
        self.UploadDar = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.PackageService/UploadDar',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.UploadDarRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.UploadDarResponse.FromString,
                )
        self.RemovePackage = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.PackageService/RemovePackage',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.RemovePackageRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.RemovePackageResponse.FromString,
                )
        self.RemoveDar = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.PackageService/RemoveDar',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.RemoveDarRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.RemoveDarResponse.FromString,
                )
        self.GetDar = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.PackageService/GetDar',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.GetDarRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.GetDarResponse.FromString,
                )
        self.Share = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.PackageService/Share',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ShareRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ListShareRequests = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.PackageService/ListShareRequests',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListShareRequestsResponse.FromString,
                )
        self.ListShareOffers = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.PackageService/ListShareOffers',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListShareOffersResponse.FromString,
                )
        self.AcceptShareOffer = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.PackageService/AcceptShareOffer',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.AcceptShareOfferRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.RejectShareOffer = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.PackageService/RejectShareOffer',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.RejectShareOfferRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.WhitelistAdd = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.PackageService/WhitelistAdd',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.WhitelistChangeRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.WhitelistRemove = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.PackageService/WhitelistRemove',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.WhitelistChangeRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.WhitelistList = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.PackageService/WhitelistList',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.WhitelistListResponse.FromString,
                )


class PackageServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListPackages(self, request, context):
        """List all Daml-LF archives on the participant node - return their hashes
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPackageContents(self, request, context):
        """Lists all the modules in package on the participant node
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDars(self, request, context):
        """List all DARs on the participant node - return their hashes and filenames
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDarContents(self, request, context):
        """List content of a Dar
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadDar(self, request, context):
        """Upload a DAR file and all packages inside to the participant node
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemovePackage(self, request, context):
        """Remove a package that is not vetted
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveDar(self, request, context):
        """Remove a DAR that is not needed
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDar(self, request, context):
        """Obtain a DAR file by hash -- for inspection & download
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Share(self, request, context):
        """Share a DAR with another participant
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListShareRequests(self, request, context):
        """List requests this participant has made to share DARs with another participant
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListShareOffers(self, request, context):
        """List offers to share a DAR that this participant has received
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AcceptShareOffer(self, request, context):
        """Accept a DAR sharing offer (this will install the DAR into the participant)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RejectShareOffer(self, request, context):
        """Reject a DAR sharing offer
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WhitelistAdd(self, request, context):
        """Add party to our DAR distribution whitelist
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WhitelistRemove(self, request, context):
        """Remove party from our DAR distribution whitelist
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WhitelistList(self, request, context):
        """List all parties currently on the whitelist
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PackageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListPackages': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPackages,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListPackagesRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListPackagesResponse.SerializeToString,
            ),
            'ListPackageContents': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPackageContents,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListPackageContentsRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListPackageContentsResponse.SerializeToString,
            ),
            'ListDars': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDars,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListDarsRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListDarsResponse.SerializeToString,
            ),
            'ListDarContents': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDarContents,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListDarContentsRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListDarContentsResponse.SerializeToString,
            ),
            'UploadDar': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadDar,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.UploadDarRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.UploadDarResponse.SerializeToString,
            ),
            'RemovePackage': grpc.unary_unary_rpc_method_handler(
                    servicer.RemovePackage,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.RemovePackageRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.RemovePackageResponse.SerializeToString,
            ),
            'RemoveDar': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveDar,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.RemoveDarRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.RemoveDarResponse.SerializeToString,
            ),
            'GetDar': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDar,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.GetDarRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.GetDarResponse.SerializeToString,
            ),
            'Share': grpc.unary_unary_rpc_method_handler(
                    servicer.Share,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ShareRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ListShareRequests': grpc.unary_unary_rpc_method_handler(
                    servicer.ListShareRequests,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListShareRequestsResponse.SerializeToString,
            ),
            'ListShareOffers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListShareOffers,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListShareOffersResponse.SerializeToString,
            ),
            'AcceptShareOffer': grpc.unary_unary_rpc_method_handler(
                    servicer.AcceptShareOffer,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.AcceptShareOfferRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'RejectShareOffer': grpc.unary_unary_rpc_method_handler(
                    servicer.RejectShareOffer,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.RejectShareOfferRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'WhitelistAdd': grpc.unary_unary_rpc_method_handler(
                    servicer.WhitelistAdd,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.WhitelistChangeRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'WhitelistRemove': grpc.unary_unary_rpc_method_handler(
                    servicer.WhitelistRemove,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.WhitelistChangeRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'WhitelistList': grpc.unary_unary_rpc_method_handler(
                    servicer.WhitelistList,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.WhitelistListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.digitalasset.canton.participant.admin.v0.PackageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PackageService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListPackages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.PackageService/ListPackages',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListPackagesRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListPackagesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPackageContents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.PackageService/ListPackageContents',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListPackageContentsRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListPackageContentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDars(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.PackageService/ListDars',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListDarsRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListDarsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDarContents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.PackageService/ListDarContents',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListDarContentsRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListDarContentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadDar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.PackageService/UploadDar',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.UploadDarRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.UploadDarResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemovePackage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.PackageService/RemovePackage',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.RemovePackageRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.RemovePackageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveDar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.PackageService/RemoveDar',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.RemoveDarRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.RemoveDarResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.PackageService/GetDar',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.GetDarRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.GetDarResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Share(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.PackageService/Share',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ShareRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListShareRequests(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.PackageService/ListShareRequests',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListShareRequestsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListShareOffers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.PackageService/ListShareOffers',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.ListShareOffersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AcceptShareOffer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.PackageService/AcceptShareOffer',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.AcceptShareOfferRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RejectShareOffer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.PackageService/RejectShareOffer',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.RejectShareOfferRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WhitelistAdd(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.PackageService/WhitelistAdd',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.WhitelistChangeRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WhitelistRemove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.PackageService/WhitelistRemove',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.WhitelistChangeRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WhitelistList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.participant.admin.v0.PackageService/WhitelistList',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_package__service__pb2.WhitelistListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
