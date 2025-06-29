// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v6.30.0
// source: com/digitalasset/canton/domain/api/v0/domain_time_service.proto

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
	DomainTimeService_FetchTime_FullMethodName = "/com.digitalasset.canton.domain.api.v0.DomainTimeService/FetchTime"
	DomainTimeService_AwaitTime_FullMethodName = "/com.digitalasset.canton.domain.api.v0.DomainTimeService/AwaitTime"
)

// DomainTimeServiceClient is the client API for DomainTimeService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type DomainTimeServiceClient interface {
	FetchTime(ctx context.Context, in *FetchTimeRequest, opts ...grpc.CallOption) (*FetchTimeResponse, error)
	AwaitTime(ctx context.Context, in *AwaitTimeRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
}

type domainTimeServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewDomainTimeServiceClient(cc grpc.ClientConnInterface) DomainTimeServiceClient {
	return &domainTimeServiceClient{cc}
}

func (c *domainTimeServiceClient) FetchTime(ctx context.Context, in *FetchTimeRequest, opts ...grpc.CallOption) (*FetchTimeResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(FetchTimeResponse)
	err := c.cc.Invoke(ctx, DomainTimeService_FetchTime_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *domainTimeServiceClient) AwaitTime(ctx context.Context, in *AwaitTimeRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, DomainTimeService_AwaitTime_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// DomainTimeServiceServer is the server API for DomainTimeService service.
// All implementations must embed UnimplementedDomainTimeServiceServer
// for forward compatibility.
type DomainTimeServiceServer interface {
	FetchTime(context.Context, *FetchTimeRequest) (*FetchTimeResponse, error)
	AwaitTime(context.Context, *AwaitTimeRequest) (*emptypb.Empty, error)
	mustEmbedUnimplementedDomainTimeServiceServer()
}

// UnimplementedDomainTimeServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedDomainTimeServiceServer struct{}

func (UnimplementedDomainTimeServiceServer) FetchTime(context.Context, *FetchTimeRequest) (*FetchTimeResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method FetchTime not implemented")
}
func (UnimplementedDomainTimeServiceServer) AwaitTime(context.Context, *AwaitTimeRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AwaitTime not implemented")
}
func (UnimplementedDomainTimeServiceServer) mustEmbedUnimplementedDomainTimeServiceServer() {}
func (UnimplementedDomainTimeServiceServer) testEmbeddedByValue()                           {}

// UnsafeDomainTimeServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to DomainTimeServiceServer will
// result in compilation errors.
type UnsafeDomainTimeServiceServer interface {
	mustEmbedUnimplementedDomainTimeServiceServer()
}

func RegisterDomainTimeServiceServer(s grpc.ServiceRegistrar, srv DomainTimeServiceServer) {
	// If the following call pancis, it indicates UnimplementedDomainTimeServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&DomainTimeService_ServiceDesc, srv)
}

func _DomainTimeService_FetchTime_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(FetchTimeRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DomainTimeServiceServer).FetchTime(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: DomainTimeService_FetchTime_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DomainTimeServiceServer).FetchTime(ctx, req.(*FetchTimeRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DomainTimeService_AwaitTime_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AwaitTimeRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DomainTimeServiceServer).AwaitTime(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: DomainTimeService_AwaitTime_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DomainTimeServiceServer).AwaitTime(ctx, req.(*AwaitTimeRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// DomainTimeService_ServiceDesc is the grpc.ServiceDesc for DomainTimeService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var DomainTimeService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.domain.api.v0.DomainTimeService",
	HandlerType: (*DomainTimeServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "FetchTime",
			Handler:    _DomainTimeService_FetchTime_Handler,
		},
		{
			MethodName: "AwaitTime",
			Handler:    _DomainTimeService_AwaitTime_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/digitalasset/canton/domain/api/v0/domain_time_service.proto",
}
