// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v5.27.2
// source: com/digitalasset/canton/domain/admin/v0/sequencer_initialization_service.proto

package sequencerinitializationservice

import (
	context "context"
	v1 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/admin/v1"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.64.0 or later.
const _ = grpc.SupportPackageIsVersion9

const (
	SequencerInitializationService_Init_FullMethodName   = "/com.digitalasset.canton.domain.admin.v0.SequencerInitializationService/Init"
	SequencerInitializationService_InitV1_FullMethodName = "/com.digitalasset.canton.domain.admin.v0.SequencerInitializationService/InitV1"
)

// SequencerInitializationServiceClient is the client API for SequencerInitializationService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type SequencerInitializationServiceClient interface {
	Init(ctx context.Context, in *InitRequest, opts ...grpc.CallOption) (*InitResponse, error)
	InitV1(ctx context.Context, in *v1.InitRequest, opts ...grpc.CallOption) (*InitResponse, error)
}

type sequencerInitializationServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewSequencerInitializationServiceClient(cc grpc.ClientConnInterface) SequencerInitializationServiceClient {
	return &sequencerInitializationServiceClient{cc}
}

func (c *sequencerInitializationServiceClient) Init(ctx context.Context, in *InitRequest, opts ...grpc.CallOption) (*InitResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(InitResponse)
	err := c.cc.Invoke(ctx, SequencerInitializationService_Init_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sequencerInitializationServiceClient) InitV1(ctx context.Context, in *v1.InitRequest, opts ...grpc.CallOption) (*InitResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(InitResponse)
	err := c.cc.Invoke(ctx, SequencerInitializationService_InitV1_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// SequencerInitializationServiceServer is the server API for SequencerInitializationService service.
// All implementations must embed UnimplementedSequencerInitializationServiceServer
// for forward compatibility.
type SequencerInitializationServiceServer interface {
	Init(context.Context, *InitRequest) (*InitResponse, error)
	InitV1(context.Context, *v1.InitRequest) (*InitResponse, error)
	mustEmbedUnimplementedSequencerInitializationServiceServer()
}

// UnimplementedSequencerInitializationServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedSequencerInitializationServiceServer struct{}

func (UnimplementedSequencerInitializationServiceServer) Init(context.Context, *InitRequest) (*InitResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Init not implemented")
}
func (UnimplementedSequencerInitializationServiceServer) InitV1(context.Context, *v1.InitRequest) (*InitResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method InitV1 not implemented")
}
func (UnimplementedSequencerInitializationServiceServer) mustEmbedUnimplementedSequencerInitializationServiceServer() {
}
func (UnimplementedSequencerInitializationServiceServer) testEmbeddedByValue() {}

// UnsafeSequencerInitializationServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to SequencerInitializationServiceServer will
// result in compilation errors.
type UnsafeSequencerInitializationServiceServer interface {
	mustEmbedUnimplementedSequencerInitializationServiceServer()
}

func RegisterSequencerInitializationServiceServer(s grpc.ServiceRegistrar, srv SequencerInitializationServiceServer) {
	// If the following call pancis, it indicates UnimplementedSequencerInitializationServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&SequencerInitializationService_ServiceDesc, srv)
}

func _SequencerInitializationService_Init_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(InitRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerInitializationServiceServer).Init(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SequencerInitializationService_Init_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerInitializationServiceServer).Init(ctx, req.(*InitRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SequencerInitializationService_InitV1_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.InitRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerInitializationServiceServer).InitV1(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SequencerInitializationService_InitV1_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerInitializationServiceServer).InitV1(ctx, req.(*v1.InitRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// SequencerInitializationService_ServiceDesc is the grpc.ServiceDesc for SequencerInitializationService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var SequencerInitializationService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.domain.admin.v0.SequencerInitializationService",
	HandlerType: (*SequencerInitializationServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Init",
			Handler:    _SequencerInitializationService_Init_Handler,
		},
		{
			MethodName: "InitV1",
			Handler:    _SequencerInitializationService_InitV1_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/digitalasset/canton/domain/admin/v0/sequencer_initialization_service.proto",
}

const (
	TopologyBootstrapService_Bootstrap_FullMethodName = "/com.digitalasset.canton.domain.admin.v0.TopologyBootstrapService/Bootstrap"
)

// TopologyBootstrapServiceClient is the client API for TopologyBootstrapService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type TopologyBootstrapServiceClient interface {
	Bootstrap(ctx context.Context, in *TopologyBootstrapRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
}

type topologyBootstrapServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewTopologyBootstrapServiceClient(cc grpc.ClientConnInterface) TopologyBootstrapServiceClient {
	return &topologyBootstrapServiceClient{cc}
}

func (c *topologyBootstrapServiceClient) Bootstrap(ctx context.Context, in *TopologyBootstrapRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, TopologyBootstrapService_Bootstrap_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// TopologyBootstrapServiceServer is the server API for TopologyBootstrapService service.
// All implementations must embed UnimplementedTopologyBootstrapServiceServer
// for forward compatibility.
type TopologyBootstrapServiceServer interface {
	Bootstrap(context.Context, *TopologyBootstrapRequest) (*emptypb.Empty, error)
	mustEmbedUnimplementedTopologyBootstrapServiceServer()
}

// UnimplementedTopologyBootstrapServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedTopologyBootstrapServiceServer struct{}

func (UnimplementedTopologyBootstrapServiceServer) Bootstrap(context.Context, *TopologyBootstrapRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Bootstrap not implemented")
}
func (UnimplementedTopologyBootstrapServiceServer) mustEmbedUnimplementedTopologyBootstrapServiceServer() {
}
func (UnimplementedTopologyBootstrapServiceServer) testEmbeddedByValue() {}

// UnsafeTopologyBootstrapServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to TopologyBootstrapServiceServer will
// result in compilation errors.
type UnsafeTopologyBootstrapServiceServer interface {
	mustEmbedUnimplementedTopologyBootstrapServiceServer()
}

func RegisterTopologyBootstrapServiceServer(s grpc.ServiceRegistrar, srv TopologyBootstrapServiceServer) {
	// If the following call pancis, it indicates UnimplementedTopologyBootstrapServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&TopologyBootstrapService_ServiceDesc, srv)
}

func _TopologyBootstrapService_Bootstrap_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(TopologyBootstrapRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyBootstrapServiceServer).Bootstrap(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: TopologyBootstrapService_Bootstrap_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyBootstrapServiceServer).Bootstrap(ctx, req.(*TopologyBootstrapRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// TopologyBootstrapService_ServiceDesc is the grpc.ServiceDesc for TopologyBootstrapService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var TopologyBootstrapService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.domain.admin.v0.TopologyBootstrapService",
	HandlerType: (*TopologyBootstrapServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Bootstrap",
			Handler:    _TopologyBootstrapService_Bootstrap_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/digitalasset/canton/domain/admin/v0/sequencer_initialization_service.proto",
}
