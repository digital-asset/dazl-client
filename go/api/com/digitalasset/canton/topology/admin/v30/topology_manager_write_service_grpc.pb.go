// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v6.30.0
// source: com/digitalasset/canton/topology/admin/v30/topology_manager_write_service.proto

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
	TopologyManagerWriteService_Authorize_FullMethodName                    = "/com.digitalasset.canton.topology.admin.v30.TopologyManagerWriteService/Authorize"
	TopologyManagerWriteService_AddTransactions_FullMethodName              = "/com.digitalasset.canton.topology.admin.v30.TopologyManagerWriteService/AddTransactions"
	TopologyManagerWriteService_ImportTopologySnapshot_FullMethodName       = "/com.digitalasset.canton.topology.admin.v30.TopologyManagerWriteService/ImportTopologySnapshot"
	TopologyManagerWriteService_SignTransactions_FullMethodName             = "/com.digitalasset.canton.topology.admin.v30.TopologyManagerWriteService/SignTransactions"
	TopologyManagerWriteService_GenerateTransactions_FullMethodName         = "/com.digitalasset.canton.topology.admin.v30.TopologyManagerWriteService/GenerateTransactions"
	TopologyManagerWriteService_CreateTemporaryTopologyStore_FullMethodName = "/com.digitalasset.canton.topology.admin.v30.TopologyManagerWriteService/CreateTemporaryTopologyStore"
	TopologyManagerWriteService_DropTemporaryTopologyStore_FullMethodName   = "/com.digitalasset.canton.topology.admin.v30.TopologyManagerWriteService/DropTemporaryTopologyStore"
)

// TopologyManagerWriteServiceClient is the client API for TopologyManagerWriteService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type TopologyManagerWriteServiceClient interface {
	Authorize(ctx context.Context, in *AuthorizeRequest, opts ...grpc.CallOption) (*AuthorizeResponse, error)
	AddTransactions(ctx context.Context, in *AddTransactionsRequest, opts ...grpc.CallOption) (*AddTransactionsResponse, error)
	ImportTopologySnapshot(ctx context.Context, opts ...grpc.CallOption) (grpc.ClientStreamingClient[ImportTopologySnapshotRequest, ImportTopologySnapshotResponse], error)
	SignTransactions(ctx context.Context, in *SignTransactionsRequest, opts ...grpc.CallOption) (*SignTransactionsResponse, error)
	GenerateTransactions(ctx context.Context, in *GenerateTransactionsRequest, opts ...grpc.CallOption) (*GenerateTransactionsResponse, error)
	CreateTemporaryTopologyStore(ctx context.Context, in *CreateTemporaryTopologyStoreRequest, opts ...grpc.CallOption) (*CreateTemporaryTopologyStoreResponse, error)
	DropTemporaryTopologyStore(ctx context.Context, in *DropTemporaryTopologyStoreRequest, opts ...grpc.CallOption) (*DropTemporaryTopologyStoreResponse, error)
}

type topologyManagerWriteServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewTopologyManagerWriteServiceClient(cc grpc.ClientConnInterface) TopologyManagerWriteServiceClient {
	return &topologyManagerWriteServiceClient{cc}
}

func (c *topologyManagerWriteServiceClient) Authorize(ctx context.Context, in *AuthorizeRequest, opts ...grpc.CallOption) (*AuthorizeResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(AuthorizeResponse)
	err := c.cc.Invoke(ctx, TopologyManagerWriteService_Authorize_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerWriteServiceClient) AddTransactions(ctx context.Context, in *AddTransactionsRequest, opts ...grpc.CallOption) (*AddTransactionsResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(AddTransactionsResponse)
	err := c.cc.Invoke(ctx, TopologyManagerWriteService_AddTransactions_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerWriteServiceClient) ImportTopologySnapshot(ctx context.Context, opts ...grpc.CallOption) (grpc.ClientStreamingClient[ImportTopologySnapshotRequest, ImportTopologySnapshotResponse], error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	stream, err := c.cc.NewStream(ctx, &TopologyManagerWriteService_ServiceDesc.Streams[0], TopologyManagerWriteService_ImportTopologySnapshot_FullMethodName, cOpts...)
	if err != nil {
		return nil, err
	}
	x := &grpc.GenericClientStream[ImportTopologySnapshotRequest, ImportTopologySnapshotResponse]{ClientStream: stream}
	return x, nil
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type TopologyManagerWriteService_ImportTopologySnapshotClient = grpc.ClientStreamingClient[ImportTopologySnapshotRequest, ImportTopologySnapshotResponse]

func (c *topologyManagerWriteServiceClient) SignTransactions(ctx context.Context, in *SignTransactionsRequest, opts ...grpc.CallOption) (*SignTransactionsResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(SignTransactionsResponse)
	err := c.cc.Invoke(ctx, TopologyManagerWriteService_SignTransactions_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerWriteServiceClient) GenerateTransactions(ctx context.Context, in *GenerateTransactionsRequest, opts ...grpc.CallOption) (*GenerateTransactionsResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GenerateTransactionsResponse)
	err := c.cc.Invoke(ctx, TopologyManagerWriteService_GenerateTransactions_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerWriteServiceClient) CreateTemporaryTopologyStore(ctx context.Context, in *CreateTemporaryTopologyStoreRequest, opts ...grpc.CallOption) (*CreateTemporaryTopologyStoreResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(CreateTemporaryTopologyStoreResponse)
	err := c.cc.Invoke(ctx, TopologyManagerWriteService_CreateTemporaryTopologyStore_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerWriteServiceClient) DropTemporaryTopologyStore(ctx context.Context, in *DropTemporaryTopologyStoreRequest, opts ...grpc.CallOption) (*DropTemporaryTopologyStoreResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(DropTemporaryTopologyStoreResponse)
	err := c.cc.Invoke(ctx, TopologyManagerWriteService_DropTemporaryTopologyStore_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// TopologyManagerWriteServiceServer is the server API for TopologyManagerWriteService service.
// All implementations must embed UnimplementedTopologyManagerWriteServiceServer
// for forward compatibility.
type TopologyManagerWriteServiceServer interface {
	Authorize(context.Context, *AuthorizeRequest) (*AuthorizeResponse, error)
	AddTransactions(context.Context, *AddTransactionsRequest) (*AddTransactionsResponse, error)
	ImportTopologySnapshot(grpc.ClientStreamingServer[ImportTopologySnapshotRequest, ImportTopologySnapshotResponse]) error
	SignTransactions(context.Context, *SignTransactionsRequest) (*SignTransactionsResponse, error)
	GenerateTransactions(context.Context, *GenerateTransactionsRequest) (*GenerateTransactionsResponse, error)
	CreateTemporaryTopologyStore(context.Context, *CreateTemporaryTopologyStoreRequest) (*CreateTemporaryTopologyStoreResponse, error)
	DropTemporaryTopologyStore(context.Context, *DropTemporaryTopologyStoreRequest) (*DropTemporaryTopologyStoreResponse, error)
	mustEmbedUnimplementedTopologyManagerWriteServiceServer()
}

// UnimplementedTopologyManagerWriteServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedTopologyManagerWriteServiceServer struct{}

func (UnimplementedTopologyManagerWriteServiceServer) Authorize(context.Context, *AuthorizeRequest) (*AuthorizeResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Authorize not implemented")
}
func (UnimplementedTopologyManagerWriteServiceServer) AddTransactions(context.Context, *AddTransactionsRequest) (*AddTransactionsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AddTransactions not implemented")
}
func (UnimplementedTopologyManagerWriteServiceServer) ImportTopologySnapshot(grpc.ClientStreamingServer[ImportTopologySnapshotRequest, ImportTopologySnapshotResponse]) error {
	return status.Errorf(codes.Unimplemented, "method ImportTopologySnapshot not implemented")
}
func (UnimplementedTopologyManagerWriteServiceServer) SignTransactions(context.Context, *SignTransactionsRequest) (*SignTransactionsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SignTransactions not implemented")
}
func (UnimplementedTopologyManagerWriteServiceServer) GenerateTransactions(context.Context, *GenerateTransactionsRequest) (*GenerateTransactionsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GenerateTransactions not implemented")
}
func (UnimplementedTopologyManagerWriteServiceServer) CreateTemporaryTopologyStore(context.Context, *CreateTemporaryTopologyStoreRequest) (*CreateTemporaryTopologyStoreResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateTemporaryTopologyStore not implemented")
}
func (UnimplementedTopologyManagerWriteServiceServer) DropTemporaryTopologyStore(context.Context, *DropTemporaryTopologyStoreRequest) (*DropTemporaryTopologyStoreResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DropTemporaryTopologyStore not implemented")
}
func (UnimplementedTopologyManagerWriteServiceServer) mustEmbedUnimplementedTopologyManagerWriteServiceServer() {
}
func (UnimplementedTopologyManagerWriteServiceServer) testEmbeddedByValue() {}

// UnsafeTopologyManagerWriteServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to TopologyManagerWriteServiceServer will
// result in compilation errors.
type UnsafeTopologyManagerWriteServiceServer interface {
	mustEmbedUnimplementedTopologyManagerWriteServiceServer()
}

func RegisterTopologyManagerWriteServiceServer(s grpc.ServiceRegistrar, srv TopologyManagerWriteServiceServer) {
	// If the following call pancis, it indicates UnimplementedTopologyManagerWriteServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&TopologyManagerWriteService_ServiceDesc, srv)
}

func _TopologyManagerWriteService_Authorize_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AuthorizeRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceServer).Authorize(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: TopologyManagerWriteService_Authorize_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceServer).Authorize(ctx, req.(*AuthorizeRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerWriteService_AddTransactions_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AddTransactionsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceServer).AddTransactions(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: TopologyManagerWriteService_AddTransactions_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceServer).AddTransactions(ctx, req.(*AddTransactionsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerWriteService_ImportTopologySnapshot_Handler(srv interface{}, stream grpc.ServerStream) error {
	return srv.(TopologyManagerWriteServiceServer).ImportTopologySnapshot(&grpc.GenericServerStream[ImportTopologySnapshotRequest, ImportTopologySnapshotResponse]{ServerStream: stream})
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type TopologyManagerWriteService_ImportTopologySnapshotServer = grpc.ClientStreamingServer[ImportTopologySnapshotRequest, ImportTopologySnapshotResponse]

func _TopologyManagerWriteService_SignTransactions_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SignTransactionsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceServer).SignTransactions(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: TopologyManagerWriteService_SignTransactions_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceServer).SignTransactions(ctx, req.(*SignTransactionsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerWriteService_GenerateTransactions_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GenerateTransactionsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceServer).GenerateTransactions(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: TopologyManagerWriteService_GenerateTransactions_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceServer).GenerateTransactions(ctx, req.(*GenerateTransactionsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerWriteService_CreateTemporaryTopologyStore_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateTemporaryTopologyStoreRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceServer).CreateTemporaryTopologyStore(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: TopologyManagerWriteService_CreateTemporaryTopologyStore_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceServer).CreateTemporaryTopologyStore(ctx, req.(*CreateTemporaryTopologyStoreRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerWriteService_DropTemporaryTopologyStore_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DropTemporaryTopologyStoreRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceServer).DropTemporaryTopologyStore(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: TopologyManagerWriteService_DropTemporaryTopologyStore_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceServer).DropTemporaryTopologyStore(ctx, req.(*DropTemporaryTopologyStoreRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// TopologyManagerWriteService_ServiceDesc is the grpc.ServiceDesc for TopologyManagerWriteService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var TopologyManagerWriteService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.topology.admin.v30.TopologyManagerWriteService",
	HandlerType: (*TopologyManagerWriteServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Authorize",
			Handler:    _TopologyManagerWriteService_Authorize_Handler,
		},
		{
			MethodName: "AddTransactions",
			Handler:    _TopologyManagerWriteService_AddTransactions_Handler,
		},
		{
			MethodName: "SignTransactions",
			Handler:    _TopologyManagerWriteService_SignTransactions_Handler,
		},
		{
			MethodName: "GenerateTransactions",
			Handler:    _TopologyManagerWriteService_GenerateTransactions_Handler,
		},
		{
			MethodName: "CreateTemporaryTopologyStore",
			Handler:    _TopologyManagerWriteService_CreateTemporaryTopologyStore_Handler,
		},
		{
			MethodName: "DropTemporaryTopologyStore",
			Handler:    _TopologyManagerWriteService_DropTemporaryTopologyStore_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "ImportTopologySnapshot",
			Handler:       _TopologyManagerWriteService_ImportTopologySnapshot_Handler,
			ClientStreams: true,
		},
	},
	Metadata: "com/digitalasset/canton/topology/admin/v30/topology_manager_write_service.proto",
}
