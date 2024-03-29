// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v4.24.3
// source: com/digitalasset/canton/topology/admin/v1/topology_manager_read_service.proto

package v1

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

// TopologyManagerReadServiceXClient is the client API for TopologyManagerReadServiceX service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type TopologyManagerReadServiceXClient interface {
	ListNamespaceDelegation(ctx context.Context, in *ListNamespaceDelegationRequest, opts ...grpc.CallOption) (*ListNamespaceDelegationResult, error)
	ListUnionspaceDefinition(ctx context.Context, in *ListUnionspaceDefinitionRequest, opts ...grpc.CallOption) (*ListUnionspaceDefinitionResult, error)
	ListIdentifierDelegation(ctx context.Context, in *ListIdentifierDelegationRequest, opts ...grpc.CallOption) (*ListIdentifierDelegationResult, error)
	ListOwnerToKeyMapping(ctx context.Context, in *ListOwnerToKeyMappingRequest, opts ...grpc.CallOption) (*ListOwnerToKeyMappingResult, error)
	ListDomainTrustCertificate(ctx context.Context, in *ListDomainTrustCertificateRequest, opts ...grpc.CallOption) (*ListDomainTrustCertificateResult, error)
	ListParticipantDomainPermission(ctx context.Context, in *ListParticipantDomainPermissionRequest, opts ...grpc.CallOption) (*ListParticipantDomainPermissionResult, error)
	ListPartyHostingLimits(ctx context.Context, in *ListPartyHostingLimitsRequest, opts ...grpc.CallOption) (*ListPartyHostingLimitsResult, error)
	ListVettedPackages(ctx context.Context, in *ListVettedPackagesRequest, opts ...grpc.CallOption) (*ListVettedPackagesResult, error)
	ListPartyToParticipant(ctx context.Context, in *ListPartyToParticipantRequest, opts ...grpc.CallOption) (*ListPartyToParticipantResult, error)
	ListAuthorityOf(ctx context.Context, in *ListAuthorityOfRequest, opts ...grpc.CallOption) (*ListAuthorityOfResult, error)
	ListDomainParametersState(ctx context.Context, in *ListDomainParametersStateRequest, opts ...grpc.CallOption) (*ListDomainParametersStateResult, error)
	ListMediatorDomainState(ctx context.Context, in *ListMediatorDomainStateRequest, opts ...grpc.CallOption) (*ListMediatorDomainStateResult, error)
	ListSequencerDomainState(ctx context.Context, in *ListSequencerDomainStateRequest, opts ...grpc.CallOption) (*ListSequencerDomainStateResult, error)
	ListPurgeTopologyTransactionX(ctx context.Context, in *ListPurgeTopologyTransactionXRequest, opts ...grpc.CallOption) (*ListPurgeTopologyTransactionXResult, error)
	ListAvailableStores(ctx context.Context, in *ListAvailableStoresRequest, opts ...grpc.CallOption) (*ListAvailableStoresResult, error)
	ListAll(ctx context.Context, in *ListAllRequest, opts ...grpc.CallOption) (*ListAllResponse, error)
	ListTrafficState(ctx context.Context, in *ListTrafficStateRequest, opts ...grpc.CallOption) (*ListTrafficStateResult, error)
}

type topologyManagerReadServiceXClient struct {
	cc grpc.ClientConnInterface
}

func NewTopologyManagerReadServiceXClient(cc grpc.ClientConnInterface) TopologyManagerReadServiceXClient {
	return &topologyManagerReadServiceXClient{cc}
}

func (c *topologyManagerReadServiceXClient) ListNamespaceDelegation(ctx context.Context, in *ListNamespaceDelegationRequest, opts ...grpc.CallOption) (*ListNamespaceDelegationResult, error) {
	out := new(ListNamespaceDelegationResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListNamespaceDelegation", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceXClient) ListUnionspaceDefinition(ctx context.Context, in *ListUnionspaceDefinitionRequest, opts ...grpc.CallOption) (*ListUnionspaceDefinitionResult, error) {
	out := new(ListUnionspaceDefinitionResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListUnionspaceDefinition", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceXClient) ListIdentifierDelegation(ctx context.Context, in *ListIdentifierDelegationRequest, opts ...grpc.CallOption) (*ListIdentifierDelegationResult, error) {
	out := new(ListIdentifierDelegationResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListIdentifierDelegation", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceXClient) ListOwnerToKeyMapping(ctx context.Context, in *ListOwnerToKeyMappingRequest, opts ...grpc.CallOption) (*ListOwnerToKeyMappingResult, error) {
	out := new(ListOwnerToKeyMappingResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListOwnerToKeyMapping", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceXClient) ListDomainTrustCertificate(ctx context.Context, in *ListDomainTrustCertificateRequest, opts ...grpc.CallOption) (*ListDomainTrustCertificateResult, error) {
	out := new(ListDomainTrustCertificateResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListDomainTrustCertificate", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceXClient) ListParticipantDomainPermission(ctx context.Context, in *ListParticipantDomainPermissionRequest, opts ...grpc.CallOption) (*ListParticipantDomainPermissionResult, error) {
	out := new(ListParticipantDomainPermissionResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListParticipantDomainPermission", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceXClient) ListPartyHostingLimits(ctx context.Context, in *ListPartyHostingLimitsRequest, opts ...grpc.CallOption) (*ListPartyHostingLimitsResult, error) {
	out := new(ListPartyHostingLimitsResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListPartyHostingLimits", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceXClient) ListVettedPackages(ctx context.Context, in *ListVettedPackagesRequest, opts ...grpc.CallOption) (*ListVettedPackagesResult, error) {
	out := new(ListVettedPackagesResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListVettedPackages", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceXClient) ListPartyToParticipant(ctx context.Context, in *ListPartyToParticipantRequest, opts ...grpc.CallOption) (*ListPartyToParticipantResult, error) {
	out := new(ListPartyToParticipantResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListPartyToParticipant", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceXClient) ListAuthorityOf(ctx context.Context, in *ListAuthorityOfRequest, opts ...grpc.CallOption) (*ListAuthorityOfResult, error) {
	out := new(ListAuthorityOfResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListAuthorityOf", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceXClient) ListDomainParametersState(ctx context.Context, in *ListDomainParametersStateRequest, opts ...grpc.CallOption) (*ListDomainParametersStateResult, error) {
	out := new(ListDomainParametersStateResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListDomainParametersState", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceXClient) ListMediatorDomainState(ctx context.Context, in *ListMediatorDomainStateRequest, opts ...grpc.CallOption) (*ListMediatorDomainStateResult, error) {
	out := new(ListMediatorDomainStateResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListMediatorDomainState", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceXClient) ListSequencerDomainState(ctx context.Context, in *ListSequencerDomainStateRequest, opts ...grpc.CallOption) (*ListSequencerDomainStateResult, error) {
	out := new(ListSequencerDomainStateResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListSequencerDomainState", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceXClient) ListPurgeTopologyTransactionX(ctx context.Context, in *ListPurgeTopologyTransactionXRequest, opts ...grpc.CallOption) (*ListPurgeTopologyTransactionXResult, error) {
	out := new(ListPurgeTopologyTransactionXResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListPurgeTopologyTransactionX", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceXClient) ListAvailableStores(ctx context.Context, in *ListAvailableStoresRequest, opts ...grpc.CallOption) (*ListAvailableStoresResult, error) {
	out := new(ListAvailableStoresResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListAvailableStores", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceXClient) ListAll(ctx context.Context, in *ListAllRequest, opts ...grpc.CallOption) (*ListAllResponse, error) {
	out := new(ListAllResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListAll", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerReadServiceXClient) ListTrafficState(ctx context.Context, in *ListTrafficStateRequest, opts ...grpc.CallOption) (*ListTrafficStateResult, error) {
	out := new(ListTrafficStateResult)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListTrafficState", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// TopologyManagerReadServiceXServer is the server API for TopologyManagerReadServiceX service.
// All implementations must embed UnimplementedTopologyManagerReadServiceXServer
// for forward compatibility
type TopologyManagerReadServiceXServer interface {
	ListNamespaceDelegation(context.Context, *ListNamespaceDelegationRequest) (*ListNamespaceDelegationResult, error)
	ListUnionspaceDefinition(context.Context, *ListUnionspaceDefinitionRequest) (*ListUnionspaceDefinitionResult, error)
	ListIdentifierDelegation(context.Context, *ListIdentifierDelegationRequest) (*ListIdentifierDelegationResult, error)
	ListOwnerToKeyMapping(context.Context, *ListOwnerToKeyMappingRequest) (*ListOwnerToKeyMappingResult, error)
	ListDomainTrustCertificate(context.Context, *ListDomainTrustCertificateRequest) (*ListDomainTrustCertificateResult, error)
	ListParticipantDomainPermission(context.Context, *ListParticipantDomainPermissionRequest) (*ListParticipantDomainPermissionResult, error)
	ListPartyHostingLimits(context.Context, *ListPartyHostingLimitsRequest) (*ListPartyHostingLimitsResult, error)
	ListVettedPackages(context.Context, *ListVettedPackagesRequest) (*ListVettedPackagesResult, error)
	ListPartyToParticipant(context.Context, *ListPartyToParticipantRequest) (*ListPartyToParticipantResult, error)
	ListAuthorityOf(context.Context, *ListAuthorityOfRequest) (*ListAuthorityOfResult, error)
	ListDomainParametersState(context.Context, *ListDomainParametersStateRequest) (*ListDomainParametersStateResult, error)
	ListMediatorDomainState(context.Context, *ListMediatorDomainStateRequest) (*ListMediatorDomainStateResult, error)
	ListSequencerDomainState(context.Context, *ListSequencerDomainStateRequest) (*ListSequencerDomainStateResult, error)
	ListPurgeTopologyTransactionX(context.Context, *ListPurgeTopologyTransactionXRequest) (*ListPurgeTopologyTransactionXResult, error)
	ListAvailableStores(context.Context, *ListAvailableStoresRequest) (*ListAvailableStoresResult, error)
	ListAll(context.Context, *ListAllRequest) (*ListAllResponse, error)
	ListTrafficState(context.Context, *ListTrafficStateRequest) (*ListTrafficStateResult, error)
	mustEmbedUnimplementedTopologyManagerReadServiceXServer()
}

// UnimplementedTopologyManagerReadServiceXServer must be embedded to have forward compatible implementations.
type UnimplementedTopologyManagerReadServiceXServer struct {
}

func (UnimplementedTopologyManagerReadServiceXServer) ListNamespaceDelegation(context.Context, *ListNamespaceDelegationRequest) (*ListNamespaceDelegationResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListNamespaceDelegation not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) ListUnionspaceDefinition(context.Context, *ListUnionspaceDefinitionRequest) (*ListUnionspaceDefinitionResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListUnionspaceDefinition not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) ListIdentifierDelegation(context.Context, *ListIdentifierDelegationRequest) (*ListIdentifierDelegationResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListIdentifierDelegation not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) ListOwnerToKeyMapping(context.Context, *ListOwnerToKeyMappingRequest) (*ListOwnerToKeyMappingResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListOwnerToKeyMapping not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) ListDomainTrustCertificate(context.Context, *ListDomainTrustCertificateRequest) (*ListDomainTrustCertificateResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListDomainTrustCertificate not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) ListParticipantDomainPermission(context.Context, *ListParticipantDomainPermissionRequest) (*ListParticipantDomainPermissionResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListParticipantDomainPermission not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) ListPartyHostingLimits(context.Context, *ListPartyHostingLimitsRequest) (*ListPartyHostingLimitsResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListPartyHostingLimits not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) ListVettedPackages(context.Context, *ListVettedPackagesRequest) (*ListVettedPackagesResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListVettedPackages not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) ListPartyToParticipant(context.Context, *ListPartyToParticipantRequest) (*ListPartyToParticipantResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListPartyToParticipant not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) ListAuthorityOf(context.Context, *ListAuthorityOfRequest) (*ListAuthorityOfResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListAuthorityOf not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) ListDomainParametersState(context.Context, *ListDomainParametersStateRequest) (*ListDomainParametersStateResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListDomainParametersState not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) ListMediatorDomainState(context.Context, *ListMediatorDomainStateRequest) (*ListMediatorDomainStateResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListMediatorDomainState not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) ListSequencerDomainState(context.Context, *ListSequencerDomainStateRequest) (*ListSequencerDomainStateResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListSequencerDomainState not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) ListPurgeTopologyTransactionX(context.Context, *ListPurgeTopologyTransactionXRequest) (*ListPurgeTopologyTransactionXResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListPurgeTopologyTransactionX not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) ListAvailableStores(context.Context, *ListAvailableStoresRequest) (*ListAvailableStoresResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListAvailableStores not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) ListAll(context.Context, *ListAllRequest) (*ListAllResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListAll not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) ListTrafficState(context.Context, *ListTrafficStateRequest) (*ListTrafficStateResult, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListTrafficState not implemented")
}
func (UnimplementedTopologyManagerReadServiceXServer) mustEmbedUnimplementedTopologyManagerReadServiceXServer() {
}

// UnsafeTopologyManagerReadServiceXServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to TopologyManagerReadServiceXServer will
// result in compilation errors.
type UnsafeTopologyManagerReadServiceXServer interface {
	mustEmbedUnimplementedTopologyManagerReadServiceXServer()
}

func RegisterTopologyManagerReadServiceXServer(s grpc.ServiceRegistrar, srv TopologyManagerReadServiceXServer) {
	s.RegisterService(&TopologyManagerReadServiceX_ServiceDesc, srv)
}

func _TopologyManagerReadServiceX_ListNamespaceDelegation_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListNamespaceDelegationRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListNamespaceDelegation(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListNamespaceDelegation",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListNamespaceDelegation(ctx, req.(*ListNamespaceDelegationRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadServiceX_ListUnionspaceDefinition_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListUnionspaceDefinitionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListUnionspaceDefinition(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListUnionspaceDefinition",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListUnionspaceDefinition(ctx, req.(*ListUnionspaceDefinitionRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadServiceX_ListIdentifierDelegation_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListIdentifierDelegationRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListIdentifierDelegation(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListIdentifierDelegation",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListIdentifierDelegation(ctx, req.(*ListIdentifierDelegationRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadServiceX_ListOwnerToKeyMapping_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListOwnerToKeyMappingRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListOwnerToKeyMapping(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListOwnerToKeyMapping",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListOwnerToKeyMapping(ctx, req.(*ListOwnerToKeyMappingRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadServiceX_ListDomainTrustCertificate_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListDomainTrustCertificateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListDomainTrustCertificate(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListDomainTrustCertificate",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListDomainTrustCertificate(ctx, req.(*ListDomainTrustCertificateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadServiceX_ListParticipantDomainPermission_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListParticipantDomainPermissionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListParticipantDomainPermission(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListParticipantDomainPermission",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListParticipantDomainPermission(ctx, req.(*ListParticipantDomainPermissionRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadServiceX_ListPartyHostingLimits_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListPartyHostingLimitsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListPartyHostingLimits(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListPartyHostingLimits",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListPartyHostingLimits(ctx, req.(*ListPartyHostingLimitsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadServiceX_ListVettedPackages_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListVettedPackagesRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListVettedPackages(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListVettedPackages",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListVettedPackages(ctx, req.(*ListVettedPackagesRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadServiceX_ListPartyToParticipant_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListPartyToParticipantRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListPartyToParticipant(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListPartyToParticipant",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListPartyToParticipant(ctx, req.(*ListPartyToParticipantRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadServiceX_ListAuthorityOf_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListAuthorityOfRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListAuthorityOf(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListAuthorityOf",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListAuthorityOf(ctx, req.(*ListAuthorityOfRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadServiceX_ListDomainParametersState_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListDomainParametersStateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListDomainParametersState(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListDomainParametersState",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListDomainParametersState(ctx, req.(*ListDomainParametersStateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadServiceX_ListMediatorDomainState_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListMediatorDomainStateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListMediatorDomainState(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListMediatorDomainState",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListMediatorDomainState(ctx, req.(*ListMediatorDomainStateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadServiceX_ListSequencerDomainState_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListSequencerDomainStateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListSequencerDomainState(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListSequencerDomainState",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListSequencerDomainState(ctx, req.(*ListSequencerDomainStateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadServiceX_ListPurgeTopologyTransactionX_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListPurgeTopologyTransactionXRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListPurgeTopologyTransactionX(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListPurgeTopologyTransactionX",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListPurgeTopologyTransactionX(ctx, req.(*ListPurgeTopologyTransactionXRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadServiceX_ListAvailableStores_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListAvailableStoresRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListAvailableStores(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListAvailableStores",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListAvailableStores(ctx, req.(*ListAvailableStoresRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadServiceX_ListAll_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListAllRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListAll(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListAll",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListAll(ctx, req.(*ListAllRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerReadServiceX_ListTrafficState_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListTrafficStateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerReadServiceXServer).ListTrafficState(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX/ListTrafficState",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerReadServiceXServer).ListTrafficState(ctx, req.(*ListTrafficStateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// TopologyManagerReadServiceX_ServiceDesc is the grpc.ServiceDesc for TopologyManagerReadServiceX service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var TopologyManagerReadServiceX_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.topology.admin.v1.TopologyManagerReadServiceX",
	HandlerType: (*TopologyManagerReadServiceXServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "ListNamespaceDelegation",
			Handler:    _TopologyManagerReadServiceX_ListNamespaceDelegation_Handler,
		},
		{
			MethodName: "ListUnionspaceDefinition",
			Handler:    _TopologyManagerReadServiceX_ListUnionspaceDefinition_Handler,
		},
		{
			MethodName: "ListIdentifierDelegation",
			Handler:    _TopologyManagerReadServiceX_ListIdentifierDelegation_Handler,
		},
		{
			MethodName: "ListOwnerToKeyMapping",
			Handler:    _TopologyManagerReadServiceX_ListOwnerToKeyMapping_Handler,
		},
		{
			MethodName: "ListDomainTrustCertificate",
			Handler:    _TopologyManagerReadServiceX_ListDomainTrustCertificate_Handler,
		},
		{
			MethodName: "ListParticipantDomainPermission",
			Handler:    _TopologyManagerReadServiceX_ListParticipantDomainPermission_Handler,
		},
		{
			MethodName: "ListPartyHostingLimits",
			Handler:    _TopologyManagerReadServiceX_ListPartyHostingLimits_Handler,
		},
		{
			MethodName: "ListVettedPackages",
			Handler:    _TopologyManagerReadServiceX_ListVettedPackages_Handler,
		},
		{
			MethodName: "ListPartyToParticipant",
			Handler:    _TopologyManagerReadServiceX_ListPartyToParticipant_Handler,
		},
		{
			MethodName: "ListAuthorityOf",
			Handler:    _TopologyManagerReadServiceX_ListAuthorityOf_Handler,
		},
		{
			MethodName: "ListDomainParametersState",
			Handler:    _TopologyManagerReadServiceX_ListDomainParametersState_Handler,
		},
		{
			MethodName: "ListMediatorDomainState",
			Handler:    _TopologyManagerReadServiceX_ListMediatorDomainState_Handler,
		},
		{
			MethodName: "ListSequencerDomainState",
			Handler:    _TopologyManagerReadServiceX_ListSequencerDomainState_Handler,
		},
		{
			MethodName: "ListPurgeTopologyTransactionX",
			Handler:    _TopologyManagerReadServiceX_ListPurgeTopologyTransactionX_Handler,
		},
		{
			MethodName: "ListAvailableStores",
			Handler:    _TopologyManagerReadServiceX_ListAvailableStores_Handler,
		},
		{
			MethodName: "ListAll",
			Handler:    _TopologyManagerReadServiceX_ListAll_Handler,
		},
		{
			MethodName: "ListTrafficState",
			Handler:    _TopologyManagerReadServiceX_ListTrafficState_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/digitalasset/canton/topology/admin/v1/topology_manager_read_service.proto",
}
