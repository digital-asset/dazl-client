// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v6.30.0
// source: com/daml/ledger/api/v2/command_service.proto

package v2

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
	CommandService_SubmitAndWait_FullMethodName                   = "/com.daml.ledger.api.v2.CommandService/SubmitAndWait"
	CommandService_SubmitAndWaitForTransaction_FullMethodName     = "/com.daml.ledger.api.v2.CommandService/SubmitAndWaitForTransaction"
	CommandService_SubmitAndWaitForTransactionTree_FullMethodName = "/com.daml.ledger.api.v2.CommandService/SubmitAndWaitForTransactionTree"
	CommandService_SubmitAndWaitForReassignment_FullMethodName    = "/com.daml.ledger.api.v2.CommandService/SubmitAndWaitForReassignment"
)

// CommandServiceClient is the client API for CommandService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type CommandServiceClient interface {
	SubmitAndWait(ctx context.Context, in *SubmitAndWaitRequest, opts ...grpc.CallOption) (*SubmitAndWaitResponse, error)
	SubmitAndWaitForTransaction(ctx context.Context, in *SubmitAndWaitForTransactionRequest, opts ...grpc.CallOption) (*SubmitAndWaitForTransactionResponse, error)
	SubmitAndWaitForTransactionTree(ctx context.Context, in *SubmitAndWaitRequest, opts ...grpc.CallOption) (*SubmitAndWaitForTransactionTreeResponse, error)
	SubmitAndWaitForReassignment(ctx context.Context, in *SubmitAndWaitForReassignmentRequest, opts ...grpc.CallOption) (*SubmitAndWaitForReassignmentResponse, error)
}

type commandServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewCommandServiceClient(cc grpc.ClientConnInterface) CommandServiceClient {
	return &commandServiceClient{cc}
}

func (c *commandServiceClient) SubmitAndWait(ctx context.Context, in *SubmitAndWaitRequest, opts ...grpc.CallOption) (*SubmitAndWaitResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(SubmitAndWaitResponse)
	err := c.cc.Invoke(ctx, CommandService_SubmitAndWait_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *commandServiceClient) SubmitAndWaitForTransaction(ctx context.Context, in *SubmitAndWaitForTransactionRequest, opts ...grpc.CallOption) (*SubmitAndWaitForTransactionResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(SubmitAndWaitForTransactionResponse)
	err := c.cc.Invoke(ctx, CommandService_SubmitAndWaitForTransaction_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *commandServiceClient) SubmitAndWaitForTransactionTree(ctx context.Context, in *SubmitAndWaitRequest, opts ...grpc.CallOption) (*SubmitAndWaitForTransactionTreeResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(SubmitAndWaitForTransactionTreeResponse)
	err := c.cc.Invoke(ctx, CommandService_SubmitAndWaitForTransactionTree_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *commandServiceClient) SubmitAndWaitForReassignment(ctx context.Context, in *SubmitAndWaitForReassignmentRequest, opts ...grpc.CallOption) (*SubmitAndWaitForReassignmentResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(SubmitAndWaitForReassignmentResponse)
	err := c.cc.Invoke(ctx, CommandService_SubmitAndWaitForReassignment_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// CommandServiceServer is the server API for CommandService service.
// All implementations must embed UnimplementedCommandServiceServer
// for forward compatibility.
type CommandServiceServer interface {
	SubmitAndWait(context.Context, *SubmitAndWaitRequest) (*SubmitAndWaitResponse, error)
	SubmitAndWaitForTransaction(context.Context, *SubmitAndWaitForTransactionRequest) (*SubmitAndWaitForTransactionResponse, error)
	SubmitAndWaitForTransactionTree(context.Context, *SubmitAndWaitRequest) (*SubmitAndWaitForTransactionTreeResponse, error)
	SubmitAndWaitForReassignment(context.Context, *SubmitAndWaitForReassignmentRequest) (*SubmitAndWaitForReassignmentResponse, error)
	mustEmbedUnimplementedCommandServiceServer()
}

// UnimplementedCommandServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedCommandServiceServer struct{}

func (UnimplementedCommandServiceServer) SubmitAndWait(context.Context, *SubmitAndWaitRequest) (*SubmitAndWaitResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SubmitAndWait not implemented")
}
func (UnimplementedCommandServiceServer) SubmitAndWaitForTransaction(context.Context, *SubmitAndWaitForTransactionRequest) (*SubmitAndWaitForTransactionResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SubmitAndWaitForTransaction not implemented")
}
func (UnimplementedCommandServiceServer) SubmitAndWaitForTransactionTree(context.Context, *SubmitAndWaitRequest) (*SubmitAndWaitForTransactionTreeResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SubmitAndWaitForTransactionTree not implemented")
}
func (UnimplementedCommandServiceServer) SubmitAndWaitForReassignment(context.Context, *SubmitAndWaitForReassignmentRequest) (*SubmitAndWaitForReassignmentResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SubmitAndWaitForReassignment not implemented")
}
func (UnimplementedCommandServiceServer) mustEmbedUnimplementedCommandServiceServer() {}
func (UnimplementedCommandServiceServer) testEmbeddedByValue()                        {}

// UnsafeCommandServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to CommandServiceServer will
// result in compilation errors.
type UnsafeCommandServiceServer interface {
	mustEmbedUnimplementedCommandServiceServer()
}

func RegisterCommandServiceServer(s grpc.ServiceRegistrar, srv CommandServiceServer) {
	// If the following call pancis, it indicates UnimplementedCommandServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&CommandService_ServiceDesc, srv)
}

func _CommandService_SubmitAndWait_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SubmitAndWaitRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(CommandServiceServer).SubmitAndWait(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: CommandService_SubmitAndWait_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(CommandServiceServer).SubmitAndWait(ctx, req.(*SubmitAndWaitRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _CommandService_SubmitAndWaitForTransaction_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SubmitAndWaitForTransactionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(CommandServiceServer).SubmitAndWaitForTransaction(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: CommandService_SubmitAndWaitForTransaction_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(CommandServiceServer).SubmitAndWaitForTransaction(ctx, req.(*SubmitAndWaitForTransactionRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _CommandService_SubmitAndWaitForTransactionTree_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SubmitAndWaitRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(CommandServiceServer).SubmitAndWaitForTransactionTree(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: CommandService_SubmitAndWaitForTransactionTree_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(CommandServiceServer).SubmitAndWaitForTransactionTree(ctx, req.(*SubmitAndWaitRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _CommandService_SubmitAndWaitForReassignment_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SubmitAndWaitForReassignmentRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(CommandServiceServer).SubmitAndWaitForReassignment(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: CommandService_SubmitAndWaitForReassignment_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(CommandServiceServer).SubmitAndWaitForReassignment(ctx, req.(*SubmitAndWaitForReassignmentRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// CommandService_ServiceDesc is the grpc.ServiceDesc for CommandService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var CommandService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.daml.ledger.api.v2.CommandService",
	HandlerType: (*CommandServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "SubmitAndWait",
			Handler:    _CommandService_SubmitAndWait_Handler,
		},
		{
			MethodName: "SubmitAndWaitForTransaction",
			Handler:    _CommandService_SubmitAndWaitForTransaction_Handler,
		},
		{
			MethodName: "SubmitAndWaitForTransactionTree",
			Handler:    _CommandService_SubmitAndWaitForTransactionTree_Handler,
		},
		{
			MethodName: "SubmitAndWaitForReassignment",
			Handler:    _CommandService_SubmitAndWaitForReassignment_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/daml/ledger/api/v2/command_service.proto",
}
