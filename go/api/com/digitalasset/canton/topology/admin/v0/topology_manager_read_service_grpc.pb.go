// Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v4.24.3
// source: com/digitalasset/canton/topology/admin/v0/topology_manager_read_service.proto

package v0

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// TopologyManagerReadServiceClient is the client API for TopologyManagerReadService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type TopologyManagerReadServiceClient interface {
	ListAvailableStores(ctx context.Context, in *ListAvailableStoresRequest, opts ...grpc.CallOption) (*ListAvailableStoresResult, error)
	ListPartyToParticipant(ctx context.Context, in *ListPartyToParticipantRequest, opts ...grpc.CallOption) (*ListPartyToParticipantResult, error)
	ListOwnerToKeyMapping(ctx context.Context, in *ListOwnerToKeyMappingRequest, opts ...grpc.CallOption) (*ListOwnerToKeyMappingResult, error)
	ListNamespaceDelegation(ctx context.Context, in *ListNamespaceDelegationRequest, opts ...grpc.CallOption) (*ListNamespaceDelegationResult, error)
	ListIdentifierDelegation(ctx context.Context, in *ListIdentifierDelegationRequest, opts ...grpc.CallOption) (*ListIdentifierDelegationResult, error)
	ListSignedLegalIdentityClaim(ctx context.Context, in *ListSignedLegalIdentityClaimRequest, opts ...grpc.CallOption) (*ListSignedLegalIdentityClaimResult, error)
	ListParticipantDomainState(ctx context.Context, in *ListParticipantDomainStateRequest, opts ...grpc.CallOption) (*ListParticipantDomainStateResult, error)
	ListMediatorDomainState(ctx context.Context, in *ListMediatorDomainStateRequest, opts ...grpc.CallOption) (*ListMediatorDomainStateResult, error)
	ListVettedPackages(ctx context.Context, in *ListVettedPackagesRequest, opts ...grpc.CallOption) (*ListVettedPackagesResult, error)
	ListDomainParametersChanges(ctx context.Context, in *ListDomainParametersChangesRequest, opts ...grpc.CallOption) (*ListDomainParametersChangesResult, error)
	ListAll(ctx context.Context, in *ListAllRequest, opts ...grpc.CallOption) (*ListAllResponse, error)
}

type topologyManagerReadServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewTopologyManagerReadServiceClient(cc grpc.ClientConnInterface) TopologyManagerReadServiceClient {
	return &topologyManagerReadServiceClient{cc}
}

func (c *topologyManagerReadServiceClient) ListAvailableStores(ctx context.Context, in *ListAvailableStoresRequest, opts ...grpc.CallOption) (*ListAvailableStoresResult, error) {
	out := new(ListAvailableStoresResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListAvailableStores", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceClient) ListPartyToParticipant(ctx context.Context, in *ListPartyToParticipantRequest, opts ...grpc.CallOption) (*ListPartyToParticipantResult, error) {
	out := new(ListPartyToParticipantResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListPartyToParticipant", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceClient) ListOwnerToKeyMapping(ctx context.Context, in *ListOwnerToKeyMappingRequest, opts ...grpc.CallOption) (*ListOwnerToKeyMappingResult, error) {
	out := new(ListOwnerToKeyMappingResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListOwnerToKeyMapping", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceClient) ListNamespaceDelegation(ctx context.Context, in *ListNamespaceDelegationRequest, opts ...grpc.CallOption) (*ListNamespaceDelegationResult, error) {
	out := new(ListNamespaceDelegationResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListNamespaceDelegation", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceClient) ListIdentifierDelegation(ctx context.Context, in *ListIdentifierDelegationRequest, opts ...grpc.CallOption) (*ListIdentifierDelegationResult, error) {
	out := new(ListIdentifierDelegationResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListIdentifierDelegation", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceClient) ListSignedLegalIdentityClaim(ctx context.Context, in *ListSignedLegalIdentityClaimRequest, opts ...grpc.CallOption) (*ListSignedLegalIdentityClaimResult, error) {
	out := new(ListSignedLegalIdentityClaimResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListSignedLegalIdentityClaim", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceClient) ListParticipantDomainState(ctx context.Context, in *ListParticipantDomainStateRequest, opts ...grpc.CallOption) (*ListParticipantDomainStateResult, error) {
	out := new(ListParticipantDomainStateResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListParticipantDomainState", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceClient) ListMediatorDomainState(ctx context.Context, in *ListMediatorDomainStateRequest, opts ...grpc.CallOption) (*ListMediatorDomainStateResult, error) {
	out := new(ListMediatorDomainStateResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListMediatorDomainState", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceClient) ListVettedPackages(ctx context.Context, in *ListVettedPackagesRequest, opts ...grpc.CallOption) (*ListVettedPackagesResult, error) {
	out := new(ListVettedPackagesResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListVettedPackages", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceClient) ListDomainParametersChanges(ctx context.Context, in *ListDomainParametersChangesRequest, opts ...grpc.CallOption) (*ListDomainParametersChangesResult, error) {
	out := new(ListDomainParametersChangesResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListDomainParametersChanges", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceClient) ListAll(ctx context.Context, in *ListAllRequest, opts ...grpc.CallOption) (*ListAllResponse, error) {
	out := new(ListAllResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListAll", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// TopologyManagerReadServiceServer is the server API for TopologyManagerReadService service.
// All implementations must embed UnimplementedTopologyManagerReadServiceServer
// for forward compatibility
type TopologyManagerReadServiceServer interface {
	ListAvailableStores(context.Context, *ListAvailableStoresRequest) (*ListAvailableStoresResult, error)
	ListPartyToParticipant(context.Context, *ListPartyToParticipantRequest) (*ListPartyToParticipantResult, error)
	ListOwnerToKeyMapping(context.Context, *ListOwnerToKeyMappingRequest) (*ListOwnerToKeyMappingResult, error)
	ListNamespaceDelegation(context.Context, *ListNamespaceDelegationRequest) (*ListNamespaceDelegationResult, error)
	ListIdentifierDelegation(context.Context, *ListIdentifierDelegationRequest) (*ListIdentifierDelegationResult, error)
	ListSignedLegalIdentityClaim(context.Context, *ListSignedLegalIdentityClaimRequest) (*ListSignedLegalIdentityClaimResult, error)
	ListParticipantDomainState(context.Context, *ListParticipantDomainStateRequest) (*ListParticipantDomainStateResult, error)
	ListMediatorDomainState(context.Context, *ListMediatorDomainStateRequest) (*ListMediatorDomainStateResult, error)
	ListVettedPackages(context.Context, *ListVettedPackagesRequest) (*ListVettedPackagesResult, error)
	ListDomainParametersChanges(context.Context, *ListDomainParametersChangesRequest) (*ListDomainParametersChangesResult, error)
	ListAll(context.Context, *ListAllRequest) (*ListAllResponse, error)
	mustEmbedUnimplementedTopologyManagerReadServiceServer()
}

// UnimplementedTopologyManagerReadServiceServer must be embedded to have forward compatible implementations.
type UnimplementedTopologyManagerReadServiceServer struct {
}

func (UnimplementedTopologyManagerReadServiceServer) ListAvailableStores(context.Context, *ListAvailableStoresRequest) (*ListAvailableStoresResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListAvailableStores not implemented")
}
func (UnimplementedTopologyManagerReadServiceServer) ListPartyToParticipant(context.Context, *ListPartyToParticipantRequest) (*ListPartyToParticipantResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListPartyToParticipant not implemented")
}
func (UnimplementedTopologyManagerReadServiceServer) ListOwnerToKeyMapping(context.Context, *ListOwnerToKeyMappingRequest) (*ListOwnerToKeyMappingResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListOwnerToKeyMapping not implemented")
}
func (UnimplementedTopologyManagerReadServiceServer) ListNamespaceDelegation(context.Context, *ListNamespaceDelegationRequest) (*ListNamespaceDelegationResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListNamespaceDelegation not implemented")
}
func (UnimplementedTopologyManagerReadServiceServer) ListIdentifierDelegation(context.Context, *ListIdentifierDelegationRequest) (*ListIdentifierDelegationResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListIdentifierDelegation not implemented")
}
func (UnimplementedTopologyManagerReadServiceServer) ListSignedLegalIdentityClaim(context.Context, *ListSignedLegalIdentityClaimRequest) (*ListSignedLegalIdentityClaimResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListSignedLegalIdentityClaim not implemented")
}
func (UnimplementedTopologyManagerReadServiceServer) ListParticipantDomainState(context.Context, *ListParticipantDomainStateRequest) (*ListParticipantDomainStateResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListParticipantDomainState not implemented")
}
func (UnimplementedTopologyManagerReadServiceServer) ListMediatorDomainState(context.Context, *ListMediatorDomainStateRequest) (*ListMediatorDomainStateResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListMediatorDomainState not implemented")
}
func (UnimplementedTopologyManagerReadServiceServer) ListVettedPackages(context.Context, *ListVettedPackagesRequest) (*ListVettedPackagesResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListVettedPackages not implemented")
}
func (UnimplementedTopologyManagerReadServiceServer) ListDomainParametersChanges(context.Context, *ListDomainParametersChangesRequest) (*ListDomainParametersChangesResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListDomainParametersChanges not implemented")
}
func (UnimplementedTopologyManagerReadServiceServer) ListAll(context.Context, *ListAllRequest) (*ListAllResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListAll not implemented")
}
func (UnimplementedTopologyManagerReadServiceServer) mustEmbedUnimplementedTopologyManagerReadServiceServer() {
}

// UnsafeTopologyManagerReadServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to TopologyManagerReadServiceServer will
// result in compilation errors.
type UnsafeTopologyManagerReadServiceServer interface {
	mustEmbedUnimplementedTopologyManagerReadServiceServer()
}

func RegisterTopologyManagerReadServiceServer(s grpc.ServiceRegistrar, srv TopologyManagerReadServiceServer) {
	s.RegisterService(&TopologyManagerReadService_ServiceDesc, srv)
}

func _TopologyManagerReadService_ListAvailableStores_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListAvailableStoresRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceServer).ListAvailableStores(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListAvailableStores",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceServer).ListAvailableStores(ctx, req.(*ListAvailableStoresRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadService_ListPartyToParticipant_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListPartyToParticipantRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceServer).ListPartyToParticipant(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListPartyToParticipant",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceServer).ListPartyToParticipant(ctx, req.(*ListPartyToParticipantRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadService_ListOwnerToKeyMapping_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListOwnerToKeyMappingRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceServer).ListOwnerToKeyMapping(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListOwnerToKeyMapping",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceServer).ListOwnerToKeyMapping(ctx, req.(*ListOwnerToKeyMappingRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadService_ListNamespaceDelegation_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListNamespaceDelegationRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceServer).ListNamespaceDelegation(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListNamespaceDelegation",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceServer).ListNamespaceDelegation(ctx, req.(*ListNamespaceDelegationRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadService_ListIdentifierDelegation_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListIdentifierDelegationRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceServer).ListIdentifierDelegation(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListIdentifierDelegation",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceServer).ListIdentifierDelegation(ctx, req.(*ListIdentifierDelegationRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadService_ListSignedLegalIdentityClaim_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListSignedLegalIdentityClaimRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceServer).ListSignedLegalIdentityClaim(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListSignedLegalIdentityClaim",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceServer).ListSignedLegalIdentityClaim(ctx, req.(*ListSignedLegalIdentityClaimRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadService_ListParticipantDomainState_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListParticipantDomainStateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceServer).ListParticipantDomainState(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListParticipantDomainState",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceServer).ListParticipantDomainState(ctx, req.(*ListParticipantDomainStateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadService_ListMediatorDomainState_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListMediatorDomainStateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceServer).ListMediatorDomainState(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListMediatorDomainState",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceServer).ListMediatorDomainState(ctx, req.(*ListMediatorDomainStateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadService_ListVettedPackages_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListVettedPackagesRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceServer).ListVettedPackages(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListVettedPackages",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceServer).ListVettedPackages(ctx, req.(*ListVettedPackagesRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadService_ListDomainParametersChanges_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListDomainParametersChangesRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceServer).ListDomainParametersChanges(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListDomainParametersChanges",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceServer).ListDomainParametersChanges(ctx, req.(*ListDomainParametersChangesRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadService_ListAll_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListAllRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceServer).ListAll(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService/ListAll",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceServer).ListAll(ctx, req.(*ListAllRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// TopologyManagerReadService_ServiceDesc is the grpc.ServiceDesc for TopologyManagerReadService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var TopologyManagerReadService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.topology.admin.v0.TopologyManagerReadService",
	HandlerType: (*TopologyManagerReadServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "ListAvailableStores",
			Handler:    _TopologyManagerReadService_ListAvailableStores_Handler,
		},
		{
			MethodName: "ListPartyToParticipant",
			Handler:    _TopologyManagerReadService_ListPartyToParticipant_Handler,
		},
		{
			MethodName: "ListOwnerToKeyMapping",
			Handler:    _TopologyManagerReadService_ListOwnerToKeyMapping_Handler,
		},
		{
			MethodName: "ListNamespaceDelegation",
			Handler:    _TopologyManagerReadService_ListNamespaceDelegation_Handler,
		},
		{
			MethodName: "ListIdentifierDelegation",
			Handler:    _TopologyManagerReadService_ListIdentifierDelegation_Handler,
		},
		{
			MethodName: "ListSignedLegalIdentityClaim",
			Handler:    _TopologyManagerReadService_ListSignedLegalIdentityClaim_Handler,
		},
		{
			MethodName: "ListParticipantDomainState",
			Handler:    _TopologyManagerReadService_ListParticipantDomainState_Handler,
		},
		{
			MethodName: "ListMediatorDomainState",
			Handler:    _TopologyManagerReadService_ListMediatorDomainState_Handler,
		},
		{
			MethodName: "ListVettedPackages",
			Handler:    _TopologyManagerReadService_ListVettedPackages_Handler,
		},
		{
			MethodName: "ListDomainParametersChanges",
			Handler:    _TopologyManagerReadService_ListDomainParametersChanges_Handler,
		},
		{
			MethodName: "ListAll",
			Handler:    _TopologyManagerReadService_ListAll_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/digitalasset/canton/topology/admin/v0/topology_manager_read_service.proto",
}
