// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v4.24.3
// source: com/digitalasset/canton/participant/admin/v0/traffic_control_service.proto

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

// TrafficControlServiceClient is the client API for TrafficControlService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type TrafficControlServiceClient interface {
	TrafficControlState(ctx context.Context, in *TrafficControlStateRequest, opts ...grpc.CallOption) (*TrafficControlStateResponse, error)
}

type trafficControlServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewTrafficControlServiceClient(cc grpc.ClientConnInterface) TrafficControlServiceClient {
	return &trafficControlServiceClient{cc}
}

func (c *trafficControlServiceClient) TrafficControlState(ctx context.Context, in *TrafficControlStateRequest, opts ...grpc.CallOption) (*TrafficControlStateResponse, error) {
	out := new(TrafficControlStateResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.participant.admin.v0.TrafficControlService/TrafficControlState", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// TrafficControlServiceServer is the server API for TrafficControlService service.
// All implementations must embed UnimplementedTrafficControlServiceServer
// for forward compatibility
type TrafficControlServiceServer interface {
	TrafficControlState(context.Context, *TrafficControlStateRequest) (*TrafficControlStateResponse, error)
	mustEmbedUnimplementedTrafficControlServiceServer()
}

// UnimplementedTrafficControlServiceServer must be embedded to have forward compatible implementations.
type UnimplementedTrafficControlServiceServer struct {
}

func (UnimplementedTrafficControlServiceServer) TrafficControlState(context.Context, *TrafficControlStateRequest) (*TrafficControlStateResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method TrafficControlState not implemented")
}
func (UnimplementedTrafficControlServiceServer) mustEmbedUnimplementedTrafficControlServiceServer() {}

// UnsafeTrafficControlServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to TrafficControlServiceServer will
// result in compilation errors.
type UnsafeTrafficControlServiceServer interface {
	mustEmbedUnimplementedTrafficControlServiceServer()
}

func RegisterTrafficControlServiceServer(s grpc.ServiceRegistrar, srv TrafficControlServiceServer) {
	s.RegisterService(&TrafficControlService_ServiceDesc, srv)
}

func _TrafficControlService_TrafficControlState_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(TrafficControlStateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TrafficControlServiceServer).TrafficControlState(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.participant.admin.v0.TrafficControlService/TrafficControlState",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TrafficControlServiceServer).TrafficControlState(ctx, req.(*TrafficControlStateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// TrafficControlService_ServiceDesc is the grpc.ServiceDesc for TrafficControlService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var TrafficControlService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.participant.admin.v0.TrafficControlService",
	HandlerType: (*TrafficControlServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "TrafficControlState",
			Handler:    _TrafficControlService_TrafficControlState_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/digitalasset/canton/participant/admin/v0/traffic_control_service.proto",
}
