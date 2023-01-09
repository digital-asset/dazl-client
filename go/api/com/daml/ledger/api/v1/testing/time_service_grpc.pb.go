// Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v3.19.5
// source: com/daml/ledger/api/v1/testing/time_service.proto

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

// TimeServiceClient is the client API for TimeService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type TimeServiceClient interface {
	// Returns a stream of time updates.
	// Always returns at least one response, where the first one is the current time.
	// Subsequent responses are emitted whenever the ledger server's time is updated.
	GetTime(ctx context.Context, in *GetTimeRequest, opts ...grpc.CallOption) (TimeService_GetTimeClient, error)
	// Allows clients to change the ledger's clock in an atomic get-and-set operation.
	SetTime(ctx context.Context, in *SetTimeRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
}

type timeServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewTimeServiceClient(cc grpc.ClientConnInterface) TimeServiceClient {
	return &timeServiceClient{cc}
}

func (c *timeServiceClient) GetTime(ctx context.Context, in *GetTimeRequest, opts ...grpc.CallOption) (TimeService_GetTimeClient, error) {
	stream, err := c.cc.NewStream(ctx, &TimeService_ServiceDesc.Streams[0], "/com.daml.ledger.api.v1.testing.TimeService/GetTime", opts...)
	if err != nil {
		return nil, err
	}
	x := &timeServiceGetTimeClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type TimeService_GetTimeClient interface {
	Recv() (*GetTimeResponse, error)
	grpc.ClientStream
}

type timeServiceGetTimeClient struct {
	grpc.ClientStream
}

func (x *timeServiceGetTimeClient) Recv() (*GetTimeResponse, error) {
	m := new(GetTimeResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *timeServiceClient) SetTime(ctx context.Context, in *SetTimeRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.testing.TimeService/SetTime", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// TimeServiceServer is the server API for TimeService service.
// All implementations must embed UnimplementedTimeServiceServer
// for forward compatibility
type TimeServiceServer interface {
	// Returns a stream of time updates.
	// Always returns at least one response, where the first one is the current time.
	// Subsequent responses are emitted whenever the ledger server's time is updated.
	GetTime(*GetTimeRequest, TimeService_GetTimeServer) error
	// Allows clients to change the ledger's clock in an atomic get-and-set operation.
	SetTime(context.Context, *SetTimeRequest) (*emptypb.Empty, error)
	mustEmbedUnimplementedTimeServiceServer()
}

// UnimplementedTimeServiceServer must be embedded to have forward compatible implementations.
type UnimplementedTimeServiceServer struct {
}

func (UnimplementedTimeServiceServer) GetTime(*GetTimeRequest, TimeService_GetTimeServer) error {
	return status.Errorf(codes.Unimplemented, "method GetTime not implemented")
}
func (UnimplementedTimeServiceServer) SetTime(context.Context, *SetTimeRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SetTime not implemented")
}
func (UnimplementedTimeServiceServer) mustEmbedUnimplementedTimeServiceServer() {}

// UnsafeTimeServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to TimeServiceServer will
// result in compilation errors.
type UnsafeTimeServiceServer interface {
	mustEmbedUnimplementedTimeServiceServer()
}

func RegisterTimeServiceServer(s grpc.ServiceRegistrar, srv TimeServiceServer) {
	s.RegisterService(&TimeService_ServiceDesc, srv)
}

func _TimeService_GetTime_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(GetTimeRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(TimeServiceServer).GetTime(m, &timeServiceGetTimeServer{stream})
}

type TimeService_GetTimeServer interface {
	Send(*GetTimeResponse) error
	grpc.ServerStream
}

type timeServiceGetTimeServer struct {
	grpc.ServerStream
}

func (x *timeServiceGetTimeServer) Send(m *GetTimeResponse) error {
	return x.ServerStream.SendMsg(m)
}

func _TimeService_SetTime_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SetTimeRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TimeServiceServer).SetTime(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.testing.TimeService/SetTime",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TimeServiceServer).SetTime(ctx, req.(*SetTimeRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// TimeService_ServiceDesc is the grpc.ServiceDesc for TimeService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var TimeService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.daml.ledger.api.v1.testing.TimeService",
	HandlerType: (*TimeServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "SetTime",
			Handler:    _TimeService_SetTime_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "GetTime",
			Handler:       _TimeService_GetTime_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "com/daml/ledger/api/v1/testing/time_service.proto",
}
