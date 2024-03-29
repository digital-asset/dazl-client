// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v4.24.3
// source: com/digitalasset/canton/topology/admin/v1/topology_manager_write_service.proto

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

// TopologyManagerWriteServiceXClient is the client API for TopologyManagerWriteServiceX service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type TopologyManagerWriteServiceXClient interface {
	Authorize(ctx context.Context, in *AuthorizeRequest, opts ...grpc.CallOption) (*AuthorizeResponse, error)
	AddTransactions(ctx context.Context, in *AddTransactionsRequest, opts ...grpc.CallOption) (*AddTransactionsResponse, error)
}

type topologyManagerWriteServiceXClient struct {
	cc grpc.ClientConnInterface
}

func NewTopologyManagerWriteServiceXClient(cc grpc.ClientConnInterface) TopologyManagerWriteServiceXClient {
	return &topologyManagerWriteServiceXClient{cc}
}

func (c *topologyManagerWriteServiceXClient) Authorize(ctx context.Context, in *AuthorizeRequest, opts ...grpc.CallOption) (*AuthorizeResponse, error) {
	out := new(AuthorizeResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerWriteServiceX/Authorize", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *topologyManagerWriteServiceXClient) AddTransactions(ctx context.Context, in *AddTransactionsRequest, opts ...grpc.CallOption) (*AddTransactionsResponse, error) {
	out := new(AddTransactionsResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.topology.admin.v1.TopologyManagerWriteServiceX/AddTransactions", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// TopologyManagerWriteServiceXServer is the server API for TopologyManagerWriteServiceX service.
// All implementations must embed UnimplementedTopologyManagerWriteServiceXServer
// for forward compatibility
type TopologyManagerWriteServiceXServer interface {
	Authorize(context.Context, *AuthorizeRequest) (*AuthorizeResponse, error)
	AddTransactions(context.Context, *AddTransactionsRequest) (*AddTransactionsResponse, error)
	mustEmbedUnimplementedTopologyManagerWriteServiceXServer()
}

// UnimplementedTopologyManagerWriteServiceXServer must be embedded to have forward compatible implementations.
type UnimplementedTopologyManagerWriteServiceXServer struct {
}

func (UnimplementedTopologyManagerWriteServiceXServer) Authorize(context.Context, *AuthorizeRequest) (*AuthorizeResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Authorize not implemented")
}
func (UnimplementedTopologyManagerWriteServiceXServer) AddTransactions(context.Context, *AddTransactionsRequest) (*AddTransactionsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AddTransactions not implemented")
}
func (UnimplementedTopologyManagerWriteServiceXServer) mustEmbedUnimplementedTopologyManagerWriteServiceXServer() {
}

// UnsafeTopologyManagerWriteServiceXServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to TopologyManagerWriteServiceXServer will
// result in compilation errors.
type UnsafeTopologyManagerWriteServiceXServer interface {
	mustEmbedUnimplementedTopologyManagerWriteServiceXServer()
}

func RegisterTopologyManagerWriteServiceXServer(s grpc.ServiceRegistrar, srv TopologyManagerWriteServiceXServer) {
	s.RegisterService(&TopologyManagerWriteServiceX_ServiceDesc, srv)
}

func _TopologyManagerWriteServiceX_Authorize_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AuthorizeRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceXServer).Authorize(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerWriteServiceX/Authorize",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceXServer).Authorize(ctx, req.(*AuthorizeRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TopologyManagerWriteServiceX_AddTransactions_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AddTransactionsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TopologyManagerWriteServiceXServer).AddTransactions(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.topology.admin.v1.TopologyManagerWriteServiceX/AddTransactions",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TopologyManagerWriteServiceXServer).AddTransactions(ctx, req.(*AddTransactionsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// TopologyManagerWriteServiceX_ServiceDesc is the grpc.ServiceDesc for TopologyManagerWriteServiceX service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var TopologyManagerWriteServiceX_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.topology.admin.v1.TopologyManagerWriteServiceX",
	HandlerType: (*TopologyManagerWriteServiceXServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Authorize",
			Handler:    _TopologyManagerWriteServiceX_Authorize_Handler,
		},
		{
			MethodName: "AddTransactions",
			Handler:    _TopologyManagerWriteServiceX_AddTransactions_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/digitalasset/canton/topology/admin/v1/topology_manager_write_service.proto",
}
