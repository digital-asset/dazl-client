// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v5.27.2
// source: com/digitalasset/canton/sequencer/admin/v30/sequencer_bft_administration_service.proto

package v30

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.64.0 or later.
const _ = grpc.SupportPackageIsVersion9

const (
	SequencerBftAdministrationService_AddPeerEndpoint_FullMethodName      = "/com.digitalasset.canton.sequencer.admin.v30.SequencerBftAdministrationService/AddPeerEndpoint"
	SequencerBftAdministrationService_RemovePeerEndpoint_FullMethodName   = "/com.digitalasset.canton.sequencer.admin.v30.SequencerBftAdministrationService/RemovePeerEndpoint"
	SequencerBftAdministrationService_GetPeerNetworkStatus_FullMethodName = "/com.digitalasset.canton.sequencer.admin.v30.SequencerBftAdministrationService/GetPeerNetworkStatus"
	SequencerBftAdministrationService_GetOrderingTopology_FullMethodName  = "/com.digitalasset.canton.sequencer.admin.v30.SequencerBftAdministrationService/GetOrderingTopology"
)

// SequencerBftAdministrationServiceClient is the client API for SequencerBftAdministrationService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type SequencerBftAdministrationServiceClient interface {
	AddPeerEndpoint(ctx context.Context, in *AddPeerEndpointRequest, opts ...grpc.CallOption) (*AddPeerEndpointResponse, error)
	RemovePeerEndpoint(ctx context.Context, in *RemovePeerEndpointRequest, opts ...grpc.CallOption) (*RemovePeerEndpointResponse, error)
	GetPeerNetworkStatus(ctx context.Context, in *GetPeerNetworkStatusRequest, opts ...grpc.CallOption) (*GetPeerNetworkStatusResponse, error)
	GetOrderingTopology(ctx context.Context, in *GetOrderingTopologyRequest, opts ...grpc.CallOption) (*GetOrderingTopologyResponse, error)
}

type sequencerBftAdministrationServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewSequencerBftAdministrationServiceClient(cc grpc.ClientConnInterface) SequencerBftAdministrationServiceClient {
	return &sequencerBftAdministrationServiceClient{cc}
}

func (c *sequencerBftAdministrationServiceClient) AddPeerEndpoint(ctx context.Context, in *AddPeerEndpointRequest, opts ...grpc.CallOption) (*AddPeerEndpointResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(AddPeerEndpointResponse)
	err := c.cc.Invoke(ctx, SequencerBftAdministrationService_AddPeerEndpoint_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sequencerBftAdministrationServiceClient) RemovePeerEndpoint(ctx context.Context, in *RemovePeerEndpointRequest, opts ...grpc.CallOption) (*RemovePeerEndpointResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(RemovePeerEndpointResponse)
	err := c.cc.Invoke(ctx, SequencerBftAdministrationService_RemovePeerEndpoint_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sequencerBftAdministrationServiceClient) GetPeerNetworkStatus(ctx context.Context, in *GetPeerNetworkStatusRequest, opts ...grpc.CallOption) (*GetPeerNetworkStatusResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GetPeerNetworkStatusResponse)
	err := c.cc.Invoke(ctx, SequencerBftAdministrationService_GetPeerNetworkStatus_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sequencerBftAdministrationServiceClient) GetOrderingTopology(ctx context.Context, in *GetOrderingTopologyRequest, opts ...grpc.CallOption) (*GetOrderingTopologyResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GetOrderingTopologyResponse)
	err := c.cc.Invoke(ctx, SequencerBftAdministrationService_GetOrderingTopology_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// SequencerBftAdministrationServiceServer is the server API for SequencerBftAdministrationService service.
// All implementations must embed UnimplementedSequencerBftAdministrationServiceServer
// for forward compatibility.
type SequencerBftAdministrationServiceServer interface {
	AddPeerEndpoint(context.Context, *AddPeerEndpointRequest) (*AddPeerEndpointResponse, error)
	RemovePeerEndpoint(context.Context, *RemovePeerEndpointRequest) (*RemovePeerEndpointResponse, error)
	GetPeerNetworkStatus(context.Context, *GetPeerNetworkStatusRequest) (*GetPeerNetworkStatusResponse, error)
	GetOrderingTopology(context.Context, *GetOrderingTopologyRequest) (*GetOrderingTopologyResponse, error)
	mustEmbedUnimplementedSequencerBftAdministrationServiceServer()
}

// UnimplementedSequencerBftAdministrationServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedSequencerBftAdministrationServiceServer struct{}

func (UnimplementedSequencerBftAdministrationServiceServer) AddPeerEndpoint(context.Context, *AddPeerEndpointRequest) (*AddPeerEndpointResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AddPeerEndpoint not implemented")
}
func (UnimplementedSequencerBftAdministrationServiceServer) RemovePeerEndpoint(context.Context, *RemovePeerEndpointRequest) (*RemovePeerEndpointResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RemovePeerEndpoint not implemented")
}
func (UnimplementedSequencerBftAdministrationServiceServer) GetPeerNetworkStatus(context.Context, *GetPeerNetworkStatusRequest) (*GetPeerNetworkStatusResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetPeerNetworkStatus not implemented")
}
func (UnimplementedSequencerBftAdministrationServiceServer) GetOrderingTopology(context.Context, *GetOrderingTopologyRequest) (*GetOrderingTopologyResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetOrderingTopology not implemented")
}
func (UnimplementedSequencerBftAdministrationServiceServer) mustEmbedUnimplementedSequencerBftAdministrationServiceServer() {
}
func (UnimplementedSequencerBftAdministrationServiceServer) testEmbeddedByValue() {}

// UnsafeSequencerBftAdministrationServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to SequencerBftAdministrationServiceServer will
// result in compilation errors.
type UnsafeSequencerBftAdministrationServiceServer interface {
	mustEmbedUnimplementedSequencerBftAdministrationServiceServer()
}

func RegisterSequencerBftAdministrationServiceServer(s grpc.ServiceRegistrar, srv SequencerBftAdministrationServiceServer) {
	// If the following call pancis, it indicates UnimplementedSequencerBftAdministrationServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&SequencerBftAdministrationService_ServiceDesc, srv)
}

func _SequencerBftAdministrationService_AddPeerEndpoint_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AddPeerEndpointRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerBftAdministrationServiceServer).AddPeerEndpoint(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SequencerBftAdministrationService_AddPeerEndpoint_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerBftAdministrationServiceServer).AddPeerEndpoint(ctx, req.(*AddPeerEndpointRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SequencerBftAdministrationService_RemovePeerEndpoint_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(RemovePeerEndpointRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerBftAdministrationServiceServer).RemovePeerEndpoint(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SequencerBftAdministrationService_RemovePeerEndpoint_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerBftAdministrationServiceServer).RemovePeerEndpoint(ctx, req.(*RemovePeerEndpointRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SequencerBftAdministrationService_GetPeerNetworkStatus_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetPeerNetworkStatusRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerBftAdministrationServiceServer).GetPeerNetworkStatus(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SequencerBftAdministrationService_GetPeerNetworkStatus_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerBftAdministrationServiceServer).GetPeerNetworkStatus(ctx, req.(*GetPeerNetworkStatusRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SequencerBftAdministrationService_GetOrderingTopology_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetOrderingTopologyRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerBftAdministrationServiceServer).GetOrderingTopology(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SequencerBftAdministrationService_GetOrderingTopology_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerBftAdministrationServiceServer).GetOrderingTopology(ctx, req.(*GetOrderingTopologyRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// SequencerBftAdministrationService_ServiceDesc is the grpc.ServiceDesc for SequencerBftAdministrationService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var SequencerBftAdministrationService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.sequencer.admin.v30.SequencerBftAdministrationService",
	HandlerType: (*SequencerBftAdministrationServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "AddPeerEndpoint",
			Handler:    _SequencerBftAdministrationService_AddPeerEndpoint_Handler,
		},
		{
			MethodName: "RemovePeerEndpoint",
			Handler:    _SequencerBftAdministrationService_RemovePeerEndpoint_Handler,
		},
		{
			MethodName: "GetPeerNetworkStatus",
			Handler:    _SequencerBftAdministrationService_GetPeerNetworkStatus_Handler,
		},
		{
			MethodName: "GetOrderingTopology",
			Handler:    _SequencerBftAdministrationService_GetOrderingTopology_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/digitalasset/canton/sequencer/admin/v30/sequencer_bft_administration_service.proto",
}
