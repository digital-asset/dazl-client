// Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package testing

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// ResetServiceClient is the client API for ResetService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ResetServiceClient interface {
	// Resets the ledger state. Note that loaded DARs won't be removed -- this only rolls back the
	// ledger to genesis.
	Reset(ctx context.Context, in *ResetRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
}

type resetServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewResetServiceClient(cc grpc.ClientConnInterface) ResetServiceClient {
	return &resetServiceClient{cc}
}

func (c *resetServiceClient) Reset(ctx context.Context, in *ResetRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.testing.ResetService/Reset", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ResetServiceServer is the server API for ResetService service.
// All implementations must embed UnimplementedResetServiceServer
// for forward compatibility
type ResetServiceServer interface {
	// Resets the ledger state. Note that loaded DARs won't be removed -- this only rolls back the
	// ledger to genesis.
	Reset(context.Context, *ResetRequest) (*emptypb.Empty, error)
	mustEmbedUnimplementedResetServiceServer()
}

// UnimplementedResetServiceServer must be embedded to have forward compatible implementations.
type UnimplementedResetServiceServer struct {
}

func (UnimplementedResetServiceServer) Reset(context.Context, *ResetRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Reset not implemented")
}
func (UnimplementedResetServiceServer) mustEmbedUnimplementedResetServiceServer() {}

// UnsafeResetServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ResetServiceServer will
// result in compilation errors.
type UnsafeResetServiceServer interface {
	mustEmbedUnimplementedResetServiceServer()
}

func RegisterResetServiceServer(s grpc.ServiceRegistrar, srv ResetServiceServer) {
	s.RegisterService(&ResetService_ServiceDesc, srv)
}

func _ResetService_Reset_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ResetRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ResetServiceServer).Reset(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.testing.ResetService/Reset",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ResetServiceServer).Reset(ctx, req.(*ResetRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// ResetService_ServiceDesc is the grpc.ServiceDesc for ResetService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var ResetService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.daml.ledger.api.v1.testing.ResetService",
	HandlerType: (*ResetServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Reset",
			Handler:    _ResetService_Reset_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/daml/ledger/api/v1/testing/reset_service.proto",
}
