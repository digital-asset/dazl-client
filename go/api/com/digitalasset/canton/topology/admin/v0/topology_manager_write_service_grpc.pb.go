// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v5.27.2
// source: com/digitalasset/canton/topology/admin/v0/topology_manager_write_service.proto

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

// TopologyManagerWriteServiceClient is the client API for TopologyManagerWriteService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type TopologyManagerWriteServiceClient interface {
	AuthorizePartyToParticipant(ctx context.Context, in *PartyToParticipantAuthorization, opts ...grpc.CallOption) (*AuthorizationSuccess, error)
	AuthorizeOwnerToKeyMapping(ctx context.Context, in *OwnerToKeyMappingAuthorization, opts ...grpc.CallOption) (*AuthorizationSuccess, error)
	AuthorizeNamespaceDelegation(ctx context.Context, in *NamespaceDelegationAuthorization, opts ...grpc.CallOption) (*AuthorizationSuccess, error)
	AuthorizeIdentifierDelegation(ctx context.Context, in *IdentifierDelegationAuthorization, opts ...grpc.CallOption) (*AuthorizationSuccess, error)
	AuthorizeVettedPackages(ctx context.Context, in *VettedPackagesAuthorization, opts ...grpc.CallOption) (*AuthorizationSuccess, error)
	AuthorizeDomainParametersChange(ctx context.Context, in *DomainParametersChangeAuthorization, opts ...grpc.CallOption) (*AuthorizationSuccess, error)
	AuthorizeParticipantDomainState(ctx context.Context, in *ParticipantDomainStateAuthorization, opts ...grpc.CallOption) (*AuthorizationSuccess, error)
	AuthorizeMediatorDomainState(ctx context.Context, in *MediatorDomainStateAuthorization, opts ...grpc.CallOption) (*AuthorizationSuccess, error)
	AddSignedTopologyTransaction(ctx context.Context, in *SignedTopologyTransactionAddition, opts ...grpc.CallOption) (*AdditionSuccess, error)
}

type topologyManagerWriteServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewTopologyManagerWriteServiceClient(cc grpc.ClientConnInterface) TopologyManagerWriteServiceClient {
	return &topologyManagerWriteServiceClient{cc}
}

func (c *topologyManagerWriteServiceClient) AuthorizePartyToParticipant(ctx context.Context, in *PartyToParticipantAuthorization, opts ...grpc.CallOption) (*AuthorizationSuccess, error) {
	out := new(AuthorizationSuccess)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AuthorizePartyToParticipant", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerWriteServiceClient) AuthorizeOwnerToKeyMapping(ctx context.Context, in *OwnerToKeyMappingAuthorization, opts ...grpc.CallOption) (*AuthorizationSuccess, error) {
	out := new(AuthorizationSuccess)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AuthorizeOwnerToKeyMapping", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerWriteServiceClient) AuthorizeNamespaceDelegation(ctx context.Context, in *NamespaceDelegationAuthorization, opts ...grpc.CallOption) (*AuthorizationSuccess, error) {
	out := new(AuthorizationSuccess)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AuthorizeNamespaceDelegation", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerWriteServiceClient) AuthorizeIdentifierDelegation(ctx context.Context, in *IdentifierDelegationAuthorization, opts ...grpc.CallOption) (*AuthorizationSuccess, error) {
	out := new(AuthorizationSuccess)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AuthorizeIdentifierDelegation", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerWriteServiceClient) AuthorizeVettedPackages(ctx context.Context, in *VettedPackagesAuthorization, opts ...grpc.CallOption) (*AuthorizationSuccess, error) {
	out := new(AuthorizationSuccess)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AuthorizeVettedPackages", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerWriteServiceClient) AuthorizeDomainParametersChange(ctx context.Context, in *DomainParametersChangeAuthorization, opts ...grpc.CallOption) (*AuthorizationSuccess, error) {
	out := new(AuthorizationSuccess)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AuthorizeDomainParametersChange", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerWriteServiceClient) AuthorizeParticipantDomainState(ctx context.Context, in *ParticipantDomainStateAuthorization, opts ...grpc.CallOption) (*AuthorizationSuccess, error) {
	out := new(AuthorizationSuccess)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AuthorizeParticipantDomainState", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerWriteServiceClient) AuthorizeMediatorDomainState(ctx context.Context, in *MediatorDomainStateAuthorization, opts ...grpc.CallOption) (*AuthorizationSuccess, error) {
	out := new(AuthorizationSuccess)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AuthorizeMediatorDomainState", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerWriteServiceClient) AddSignedTopologyTransaction(ctx context.Context, in *SignedTopologyTransactionAddition, opts ...grpc.CallOption) (*AdditionSuccess, error) {
	out := new(AdditionSuccess)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AddSignedTopologyTransaction", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// TopologyManagerWriteServiceServer is the server API for TopologyManagerWriteService service.
// All implementations must embed UnimplementedTopologyManagerWriteServiceServer
// for forward compatibility
type TopologyManagerWriteServiceServer interface {
	AuthorizePartyToParticipant(context.Context, *PartyToParticipantAuthorization) (*AuthorizationSuccess, error)
	AuthorizeOwnerToKeyMapping(context.Context, *OwnerToKeyMappingAuthorization) (*AuthorizationSuccess, error)
	AuthorizeNamespaceDelegation(context.Context, *NamespaceDelegationAuthorization) (*AuthorizationSuccess, error)
	AuthorizeIdentifierDelegation(context.Context, *IdentifierDelegationAuthorization) (*AuthorizationSuccess, error)
	AuthorizeVettedPackages(context.Context, *VettedPackagesAuthorization) (*AuthorizationSuccess, error)
	AuthorizeDomainParametersChange(context.Context, *DomainParametersChangeAuthorization) (*AuthorizationSuccess, error)
	AuthorizeParticipantDomainState(context.Context, *ParticipantDomainStateAuthorization) (*AuthorizationSuccess, error)
	AuthorizeMediatorDomainState(context.Context, *MediatorDomainStateAuthorization) (*AuthorizationSuccess, error)
	AddSignedTopologyTransaction(context.Context, *SignedTopologyTransactionAddition) (*AdditionSuccess, error)
	mustEmbedUnimplementedTopologyManagerWriteServiceServer()
}

// UnimplementedTopologyManagerWriteServiceServer must be embedded to have forward compatible implementations.
type UnimplementedTopologyManagerWriteServiceServer struct {
}

func (UnimplementedTopologyManagerWriteServiceServer) AuthorizePartyToParticipant(context.Context, *PartyToParticipantAuthorization) (*AuthorizationSuccess, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AuthorizePartyToParticipant not implemented")
}
func (UnimplementedTopologyManagerWriteServiceServer) AuthorizeOwnerToKeyMapping(context.Context, *OwnerToKeyMappingAuthorization) (*AuthorizationSuccess, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AuthorizeOwnerToKeyMapping not implemented")
}
func (UnimplementedTopologyManagerWriteServiceServer) AuthorizeNamespaceDelegation(context.Context, *NamespaceDelegationAuthorization) (*AuthorizationSuccess, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AuthorizeNamespaceDelegation not implemented")
}
func (UnimplementedTopologyManagerWriteServiceServer) AuthorizeIdentifierDelegation(context.Context, *IdentifierDelegationAuthorization) (*AuthorizationSuccess, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AuthorizeIdentifierDelegation not implemented")
}
func (UnimplementedTopologyManagerWriteServiceServer) AuthorizeVettedPackages(context.Context, *VettedPackagesAuthorization) (*AuthorizationSuccess, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AuthorizeVettedPackages not implemented")
}
func (UnimplementedTopologyManagerWriteServiceServer) AuthorizeDomainParametersChange(context.Context, *DomainParametersChangeAuthorization) (*AuthorizationSuccess, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AuthorizeDomainParametersChange not implemented")
}
func (UnimplementedTopologyManagerWriteServiceServer) AuthorizeParticipantDomainState(context.Context, *ParticipantDomainStateAuthorization) (*AuthorizationSuccess, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AuthorizeParticipantDomainState not implemented")
}
func (UnimplementedTopologyManagerWriteServiceServer) AuthorizeMediatorDomainState(context.Context, *MediatorDomainStateAuthorization) (*AuthorizationSuccess, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AuthorizeMediatorDomainState not implemented")
}
func (UnimplementedTopologyManagerWriteServiceServer) AddSignedTopologyTransaction(context.Context, *SignedTopologyTransactionAddition) (*AdditionSuccess, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AddSignedTopologyTransaction not implemented")
}
func (UnimplementedTopologyManagerWriteServiceServer) mustEmbedUnimplementedTopologyManagerWriteServiceServer() {
}

// UnsafeTopologyManagerWriteServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to TopologyManagerWriteServiceServer will
// result in compilation errors.
type UnsafeTopologyManagerWriteServiceServer interface {
	mustEmbedUnimplementedTopologyManagerWriteServiceServer()
}

func RegisterTopologyManagerWriteServiceServer(s grpc.ServiceRegistrar, srv TopologyManagerWriteServiceServer) {
	s.RegisterService(&TopologyManagerWriteService_ServiceDesc, srv)
}

func _TopologyManagerWriteService_AuthorizePartyToParticipant_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PartyToParticipantAuthorization)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceServer).AuthorizePartyToParticipant(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AuthorizePartyToParticipant",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceServer).AuthorizePartyToParticipant(ctx, req.(*PartyToParticipantAuthorization))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerWriteService_AuthorizeOwnerToKeyMapping_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(OwnerToKeyMappingAuthorization)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceServer).AuthorizeOwnerToKeyMapping(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AuthorizeOwnerToKeyMapping",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceServer).AuthorizeOwnerToKeyMapping(ctx, req.(*OwnerToKeyMappingAuthorization))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerWriteService_AuthorizeNamespaceDelegation_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(NamespaceDelegationAuthorization)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceServer).AuthorizeNamespaceDelegation(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AuthorizeNamespaceDelegation",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceServer).AuthorizeNamespaceDelegation(ctx, req.(*NamespaceDelegationAuthorization))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerWriteService_AuthorizeIdentifierDelegation_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(IdentifierDelegationAuthorization)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceServer).AuthorizeIdentifierDelegation(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AuthorizeIdentifierDelegation",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceServer).AuthorizeIdentifierDelegation(ctx, req.(*IdentifierDelegationAuthorization))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerWriteService_AuthorizeVettedPackages_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(VettedPackagesAuthorization)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceServer).AuthorizeVettedPackages(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AuthorizeVettedPackages",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceServer).AuthorizeVettedPackages(ctx, req.(*VettedPackagesAuthorization))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerWriteService_AuthorizeDomainParametersChange_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DomainParametersChangeAuthorization)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceServer).AuthorizeDomainParametersChange(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AuthorizeDomainParametersChange",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceServer).AuthorizeDomainParametersChange(ctx, req.(*DomainParametersChangeAuthorization))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerWriteService_AuthorizeParticipantDomainState_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ParticipantDomainStateAuthorization)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceServer).AuthorizeParticipantDomainState(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AuthorizeParticipantDomainState",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceServer).AuthorizeParticipantDomainState(ctx, req.(*ParticipantDomainStateAuthorization))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerWriteService_AuthorizeMediatorDomainState_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(MediatorDomainStateAuthorization)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceServer).AuthorizeMediatorDomainState(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AuthorizeMediatorDomainState",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceServer).AuthorizeMediatorDomainState(ctx, req.(*MediatorDomainStateAuthorization))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerWriteService_AddSignedTopologyTransaction_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SignedTopologyTransactionAddition)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceServer).AddSignedTopologyTransaction(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService/AddSignedTopologyTransaction",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceServer).AddSignedTopologyTransaction(ctx, req.(*SignedTopologyTransactionAddition))
	}
	return interceptor(ctx, in, info, handler)
}

// TopologyManagerWriteService_ServiceDesc is the grpc.ServiceDesc for TopologyManagerWriteService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var TopologyManagerWriteService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.topology.admin.v0.TopologyManagerWriteService",
	HandlerType: (*TopologyManagerWriteServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "AuthorizePartyToParticipant",
			Handler:    _TopologyManagerWriteService_AuthorizePartyToParticipant_Handler,
		},
		{
			MethodName: "AuthorizeOwnerToKeyMapping",
			Handler:    _TopologyManagerWriteService_AuthorizeOwnerToKeyMapping_Handler,
		},
		{
			MethodName: "AuthorizeNamespaceDelegation",
			Handler:    _TopologyManagerWriteService_AuthorizeNamespaceDelegation_Handler,
		},
		{
			MethodName: "AuthorizeIdentifierDelegation",
			Handler:    _TopologyManagerWriteService_AuthorizeIdentifierDelegation_Handler,
		},
		{
			MethodName: "AuthorizeVettedPackages",
			Handler:    _TopologyManagerWriteService_AuthorizeVettedPackages_Handler,
		},
		{
			MethodName: "AuthorizeDomainParametersChange",
			Handler:    _TopologyManagerWriteService_AuthorizeDomainParametersChange_Handler,
		},
		{
			MethodName: "AuthorizeParticipantDomainState",
			Handler:    _TopologyManagerWriteService_AuthorizeParticipantDomainState_Handler,
		},
		{
			MethodName: "AuthorizeMediatorDomainState",
			Handler:    _TopologyManagerWriteService_AuthorizeMediatorDomainState_Handler,
		},
		{
			MethodName: "AddSignedTopologyTransaction",
			Handler:    _TopologyManagerWriteService_AddSignedTopologyTransaction_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/digitalasset/canton/topology/admin/v0/topology_manager_write_service.proto",
}
