// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v6.30.0
// source: com/digitalasset/canton/domain/api/v0/sequencer_authentication_service.proto

package v0

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
	SequencerAuthenticationService_Challenge_FullMethodName    = "/com.digitalasset.canton.domain.api.v0.SequencerAuthenticationService/Challenge"
	SequencerAuthenticationService_Authenticate_FullMethodName = "/com.digitalasset.canton.domain.api.v0.SequencerAuthenticationService/Authenticate"
)

// SequencerAuthenticationServiceClient is the client API for SequencerAuthenticationService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type SequencerAuthenticationServiceClient interface {
	Challenge(ctx context.Context, in *Challenge_Request, opts ...grpc.CallOption) (*Challenge_Response, error)
	Authenticate(ctx context.Context, in *Authentication_Request, opts ...grpc.CallOption) (*Authentication_Response, error)
}

type sequencerAuthenticationServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewSequencerAuthenticationServiceClient(cc grpc.ClientConnInterface) SequencerAuthenticationServiceClient {
	return &sequencerAuthenticationServiceClient{cc}
}

func (c *sequencerAuthenticationServiceClient) Challenge(ctx context.Context, in *Challenge_Request, opts ...grpc.CallOption) (*Challenge_Response, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(Challenge_Response)
	err := c.cc.Invoke(ctx, SequencerAuthenticationService_Challenge_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sequencerAuthenticationServiceClient) Authenticate(ctx context.Context, in *Authentication_Request, opts ...grpc.CallOption) (*Authentication_Response, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(Authentication_Response)
	err := c.cc.Invoke(ctx, SequencerAuthenticationService_Authenticate_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// SequencerAuthenticationServiceServer is the server API for SequencerAuthenticationService service.
// All implementations must embed UnimplementedSequencerAuthenticationServiceServer
// for forward compatibility.
type SequencerAuthenticationServiceServer interface {
	Challenge(context.Context, *Challenge_Request) (*Challenge_Response, error)
	Authenticate(context.Context, *Authentication_Request) (*Authentication_Response, error)
	mustEmbedUnimplementedSequencerAuthenticationServiceServer()
}

// UnimplementedSequencerAuthenticationServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedSequencerAuthenticationServiceServer struct{}

func (UnimplementedSequencerAuthenticationServiceServer) Challenge(context.Context, *Challenge_Request) (*Challenge_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Challenge not implemented")
}
func (UnimplementedSequencerAuthenticationServiceServer) Authenticate(context.Context, *Authentication_Request) (*Authentication_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Authenticate not implemented")
}
func (UnimplementedSequencerAuthenticationServiceServer) mustEmbedUnimplementedSequencerAuthenticationServiceServer() {
}
func (UnimplementedSequencerAuthenticationServiceServer) testEmbeddedByValue() {}

// UnsafeSequencerAuthenticationServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to SequencerAuthenticationServiceServer will
// result in compilation errors.
type UnsafeSequencerAuthenticationServiceServer interface {
	mustEmbedUnimplementedSequencerAuthenticationServiceServer()
}

func RegisterSequencerAuthenticationServiceServer(s grpc.ServiceRegistrar, srv SequencerAuthenticationServiceServer) {
	// If the following call pancis, it indicates UnimplementedSequencerAuthenticationServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&SequencerAuthenticationService_ServiceDesc, srv)
}

func _SequencerAuthenticationService_Challenge_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Challenge_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerAuthenticationServiceServer).Challenge(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SequencerAuthenticationService_Challenge_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerAuthenticationServiceServer).Challenge(ctx, req.(*Challenge_Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _SequencerAuthenticationService_Authenticate_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Authentication_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerAuthenticationServiceServer).Authenticate(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SequencerAuthenticationService_Authenticate_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerAuthenticationServiceServer).Authenticate(ctx, req.(*Authentication_Request))
	}
	return interceptor(ctx, in, info, handler)
}

// SequencerAuthenticationService_ServiceDesc is the grpc.ServiceDesc for SequencerAuthenticationService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var SequencerAuthenticationService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.domain.api.v0.SequencerAuthenticationService",
	HandlerType: (*SequencerAuthenticationServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Challenge",
			Handler:    _SequencerAuthenticationService_Challenge_Handler,
		},
		{
			MethodName: "Authenticate",
			Handler:    _SequencerAuthenticationService_Authenticate_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/digitalasset/canton/domain/api/v0/sequencer_authentication_service.proto",
}
