// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v6.30.0
// source: com/digitalasset/canton/domain/admin/v0/enterprise_sequencer_connection_service.proto

package v0

import (
	context "context"
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
	EnterpriseSequencerConnectionService_GetConnection_FullMethodName = "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerConnectionService/GetConnection"
	EnterpriseSequencerConnectionService_SetConnection_FullMethodName = "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerConnectionService/SetConnection"
)

// EnterpriseSequencerConnectionServiceClient is the client API for EnterpriseSequencerConnectionService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type EnterpriseSequencerConnectionServiceClient interface {
	GetConnection(ctx context.Context, in *GetConnectionRequest, opts ...grpc.CallOption) (*GetConnectionResponse, error)
	SetConnection(ctx context.Context, in *SetConnectionRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
}

type enterpriseSequencerConnectionServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewEnterpriseSequencerConnectionServiceClient(cc grpc.ClientConnInterface) EnterpriseSequencerConnectionServiceClient {
	return &enterpriseSequencerConnectionServiceClient{cc}
}

func (c *enterpriseSequencerConnectionServiceClient) GetConnection(ctx context.Context, in *GetConnectionRequest, opts ...grpc.CallOption) (*GetConnectionResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GetConnectionResponse)
	err := c.cc.Invoke(ctx, EnterpriseSequencerConnectionService_GetConnection_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerConnectionServiceClient) SetConnection(ctx context.Context, in *SetConnectionRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, EnterpriseSequencerConnectionService_SetConnection_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// EnterpriseSequencerConnectionServiceServer is the server API for EnterpriseSequencerConnectionService service.
// All implementations must embed UnimplementedEnterpriseSequencerConnectionServiceServer
// for forward compatibility.
type EnterpriseSequencerConnectionServiceServer interface {
	GetConnection(context.Context, *GetConnectionRequest) (*GetConnectionResponse, error)
	SetConnection(context.Context, *SetConnectionRequest) (*emptypb.Empty, error)
	mustEmbedUnimplementedEnterpriseSequencerConnectionServiceServer()
}

// UnimplementedEnterpriseSequencerConnectionServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedEnterpriseSequencerConnectionServiceServer struct{}

func (UnimplementedEnterpriseSequencerConnectionServiceServer) GetConnection(context.Context, *GetConnectionRequest) (*GetConnectionResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetConnection not implemented")
}
func (UnimplementedEnterpriseSequencerConnectionServiceServer) SetConnection(context.Context, *SetConnectionRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SetConnection not implemented")
}
func (UnimplementedEnterpriseSequencerConnectionServiceServer) mustEmbedUnimplementedEnterpriseSequencerConnectionServiceServer() {
}
func (UnimplementedEnterpriseSequencerConnectionServiceServer) testEmbeddedByValue() {}

// UnsafeEnterpriseSequencerConnectionServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to EnterpriseSequencerConnectionServiceServer will
// result in compilation errors.
type UnsafeEnterpriseSequencerConnectionServiceServer interface {
	mustEmbedUnimplementedEnterpriseSequencerConnectionServiceServer()
}

func RegisterEnterpriseSequencerConnectionServiceServer(s grpc.ServiceRegistrar, srv EnterpriseSequencerConnectionServiceServer) {
	// If the following call pancis, it indicates UnimplementedEnterpriseSequencerConnectionServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&EnterpriseSequencerConnectionService_ServiceDesc, srv)
}

func _EnterpriseSequencerConnectionService_GetConnection_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetConnectionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnterpriseSequencerConnectionServiceServer).GetConnection(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EnterpriseSequencerConnectionService_GetConnection_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnterpriseSequencerConnectionServiceServer).GetConnection(ctx, req.(*GetConnectionRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _EnterpriseSequencerConnectionService_SetConnection_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SetConnectionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnterpriseSequencerConnectionServiceServer).SetConnection(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EnterpriseSequencerConnectionService_SetConnection_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnterpriseSequencerConnectionServiceServer).SetConnection(ctx, req.(*SetConnectionRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// EnterpriseSequencerConnectionService_ServiceDesc is the grpc.ServiceDesc for EnterpriseSequencerConnectionService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var EnterpriseSequencerConnectionService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerConnectionService",
	HandlerType: (*EnterpriseSequencerConnectionServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetConnection",
			Handler:    _EnterpriseSequencerConnectionService_GetConnection_Handler,
		},
		{
			MethodName: "SetConnection",
			Handler:    _EnterpriseSequencerConnectionService_SetConnection_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/digitalasset/canton/domain/admin/v0/enterprise_sequencer_connection_service.proto",
}
