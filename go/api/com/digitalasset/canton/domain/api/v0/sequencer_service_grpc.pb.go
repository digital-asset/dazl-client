// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v5.27.2
// source: com/digitalasset/canton/domain/api/v0/sequencer_service.proto

package v0

import (
	context "context"
	v0 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v0"
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
	SequencerService_SendAsync_FullMethodName                         = "/com.digitalasset.canton.domain.api.v0.SequencerService/SendAsync"
	SequencerService_SendAsyncSigned_FullMethodName                   = "/com.digitalasset.canton.domain.api.v0.SequencerService/SendAsyncSigned"
	SequencerService_SendAsyncUnauthenticated_FullMethodName          = "/com.digitalasset.canton.domain.api.v0.SequencerService/SendAsyncUnauthenticated"
	SequencerService_SendAsyncVersioned_FullMethodName                = "/com.digitalasset.canton.domain.api.v0.SequencerService/SendAsyncVersioned"
	SequencerService_SendAsyncUnauthenticatedVersioned_FullMethodName = "/com.digitalasset.canton.domain.api.v0.SequencerService/SendAsyncUnauthenticatedVersioned"
	SequencerService_Subscribe_FullMethodName                         = "/com.digitalasset.canton.domain.api.v0.SequencerService/Subscribe"
	SequencerService_SubscribeVersioned_FullMethodName                = "/com.digitalasset.canton.domain.api.v0.SequencerService/SubscribeVersioned"
	SequencerService_SubscribeUnauthenticated_FullMethodName          = "/com.digitalasset.canton.domain.api.v0.SequencerService/SubscribeUnauthenticated"
	SequencerService_SubscribeUnauthenticatedVersioned_FullMethodName = "/com.digitalasset.canton.domain.api.v0.SequencerService/SubscribeUnauthenticatedVersioned"
	SequencerService_Acknowledge_FullMethodName                       = "/com.digitalasset.canton.domain.api.v0.SequencerService/Acknowledge"
	SequencerService_AcknowledgeSigned_FullMethodName                 = "/com.digitalasset.canton.domain.api.v0.SequencerService/AcknowledgeSigned"
)

// SequencerServiceClient is the client API for SequencerService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type SequencerServiceClient interface {
	SendAsync(ctx context.Context, in *v0.SubmissionRequest, opts ...grpc.CallOption) (*SendAsyncResponse, error)
	SendAsyncSigned(ctx context.Context, in *v0.SignedContent, opts ...grpc.CallOption) (*SendAsyncSignedResponse, error)
	SendAsyncUnauthenticated(ctx context.Context, in *v0.SubmissionRequest, opts ...grpc.CallOption) (*SendAsyncResponse, error)
	SendAsyncVersioned(ctx context.Context, in *SendAsyncVersionedRequest, opts ...grpc.CallOption) (*SendAsyncSignedResponse, error)
	SendAsyncUnauthenticatedVersioned(ctx context.Context, in *SendAsyncUnauthenticatedVersionedRequest, opts ...grpc.CallOption) (*SendAsyncResponse, error)
	Subscribe(ctx context.Context, in *SubscriptionRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[SubscriptionResponse], error)
	SubscribeVersioned(ctx context.Context, in *SubscriptionRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[VersionedSubscriptionResponse], error)
	SubscribeUnauthenticated(ctx context.Context, in *SubscriptionRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[SubscriptionResponse], error)
	SubscribeUnauthenticatedVersioned(ctx context.Context, in *SubscriptionRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[VersionedSubscriptionResponse], error)
	Acknowledge(ctx context.Context, in *AcknowledgeRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	AcknowledgeSigned(ctx context.Context, in *v0.SignedContent, opts ...grpc.CallOption) (*emptypb.Empty, error)
}

type sequencerServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewSequencerServiceClient(cc grpc.ClientConnInterface) SequencerServiceClient {
	return &sequencerServiceClient{cc}
}

func (c *sequencerServiceClient) SendAsync(ctx context.Context, in *v0.SubmissionRequest, opts ...grpc.CallOption) (*SendAsyncResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(SendAsyncResponse)
	err := c.cc.Invoke(ctx, SequencerService_SendAsync_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sequencerServiceClient) SendAsyncSigned(ctx context.Context, in *v0.SignedContent, opts ...grpc.CallOption) (*SendAsyncSignedResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(SendAsyncSignedResponse)
	err := c.cc.Invoke(ctx, SequencerService_SendAsyncSigned_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sequencerServiceClient) SendAsyncUnauthenticated(ctx context.Context, in *v0.SubmissionRequest, opts ...grpc.CallOption) (*SendAsyncResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(SendAsyncResponse)
	err := c.cc.Invoke(ctx, SequencerService_SendAsyncUnauthenticated_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sequencerServiceClient) SendAsyncVersioned(ctx context.Context, in *SendAsyncVersionedRequest, opts ...grpc.CallOption) (*SendAsyncSignedResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(SendAsyncSignedResponse)
	err := c.cc.Invoke(ctx, SequencerService_SendAsyncVersioned_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sequencerServiceClient) SendAsyncUnauthenticatedVersioned(ctx context.Context, in *SendAsyncUnauthenticatedVersionedRequest, opts ...grpc.CallOption) (*SendAsyncResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(SendAsyncResponse)
	err := c.cc.Invoke(ctx, SequencerService_SendAsyncUnauthenticatedVersioned_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sequencerServiceClient) Subscribe(ctx context.Context, in *SubscriptionRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[SubscriptionResponse], error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	stream, err := c.cc.NewStream(ctx, &SequencerService_ServiceDesc.Streams[0], SequencerService_Subscribe_FullMethodName, cOpts...)
	if err != nil {
		return nil, err
	}
	x := &grpc.GenericClientStream[SubscriptionRequest, SubscriptionResponse]{ClientStream: stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type SequencerService_SubscribeClient = grpc.ServerStreamingClient[SubscriptionResponse]

func (c *sequencerServiceClient) SubscribeVersioned(ctx context.Context, in *SubscriptionRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[VersionedSubscriptionResponse], error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	stream, err := c.cc.NewStream(ctx, &SequencerService_ServiceDesc.Streams[1], SequencerService_SubscribeVersioned_FullMethodName, cOpts...)
	if err != nil {
		return nil, err
	}
	x := &grpc.GenericClientStream[SubscriptionRequest, VersionedSubscriptionResponse]{ClientStream: stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type SequencerService_SubscribeVersionedClient = grpc.ServerStreamingClient[VersionedSubscriptionResponse]

func (c *sequencerServiceClient) SubscribeUnauthenticated(ctx context.Context, in *SubscriptionRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[SubscriptionResponse], error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	stream, err := c.cc.NewStream(ctx, &SequencerService_ServiceDesc.Streams[2], SequencerService_SubscribeUnauthenticated_FullMethodName, cOpts...)
	if err != nil {
		return nil, err
	}
	x := &grpc.GenericClientStream[SubscriptionRequest, SubscriptionResponse]{ClientStream: stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type SequencerService_SubscribeUnauthenticatedClient = grpc.ServerStreamingClient[SubscriptionResponse]

func (c *sequencerServiceClient) SubscribeUnauthenticatedVersioned(ctx context.Context, in *SubscriptionRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[VersionedSubscriptionResponse], error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	stream, err := c.cc.NewStream(ctx, &SequencerService_ServiceDesc.Streams[3], SequencerService_SubscribeUnauthenticatedVersioned_FullMethodName, cOpts...)
	if err != nil {
		return nil, err
	}
	x := &grpc.GenericClientStream[SubscriptionRequest, VersionedSubscriptionResponse]{ClientStream: stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type SequencerService_SubscribeUnauthenticatedVersionedClient = grpc.ServerStreamingClient[VersionedSubscriptionResponse]

func (c *sequencerServiceClient) Acknowledge(ctx context.Context, in *AcknowledgeRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, SequencerService_Acknowledge_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sequencerServiceClient) AcknowledgeSigned(ctx context.Context, in *v0.SignedContent, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, SequencerService_AcknowledgeSigned_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// SequencerServiceServer is the server API for SequencerService service.
// All implementations must embed UnimplementedSequencerServiceServer
// for forward compatibility.
type SequencerServiceServer interface {
	SendAsync(context.Context, *v0.SubmissionRequest) (*SendAsyncResponse, error)
	SendAsyncSigned(context.Context, *v0.SignedContent) (*SendAsyncSignedResponse, error)
	SendAsyncUnauthenticated(context.Context, *v0.SubmissionRequest) (*SendAsyncResponse, error)
	SendAsyncVersioned(context.Context, *SendAsyncVersionedRequest) (*SendAsyncSignedResponse, error)
	SendAsyncUnauthenticatedVersioned(context.Context, *SendAsyncUnauthenticatedVersionedRequest) (*SendAsyncResponse, error)
	Subscribe(*SubscriptionRequest, grpc.ServerStreamingServer[SubscriptionResponse]) error
	SubscribeVersioned(*SubscriptionRequest, grpc.ServerStreamingServer[VersionedSubscriptionResponse]) error
	SubscribeUnauthenticated(*SubscriptionRequest, grpc.ServerStreamingServer[SubscriptionResponse]) error
	SubscribeUnauthenticatedVersioned(*SubscriptionRequest, grpc.ServerStreamingServer[VersionedSubscriptionResponse]) error
	Acknowledge(context.Context, *AcknowledgeRequest) (*emptypb.Empty, error)
	AcknowledgeSigned(context.Context, *v0.SignedContent) (*emptypb.Empty, error)
	mustEmbedUnimplementedSequencerServiceServer()
}

// UnimplementedSequencerServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedSequencerServiceServer struct{}

func (UnimplementedSequencerServiceServer) SendAsync(context.Context, *v0.SubmissionRequest) (*SendAsyncResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SendAsync not implemented")
}
func (UnimplementedSequencerServiceServer) SendAsyncSigned(context.Context, *v0.SignedContent) (*SendAsyncSignedResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SendAsyncSigned not implemented")
}
func (UnimplementedSequencerServiceServer) SendAsyncUnauthenticated(context.Context, *v0.SubmissionRequest) (*SendAsyncResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SendAsyncUnauthenticated not implemented")
}
func (UnimplementedSequencerServiceServer) SendAsyncVersioned(context.Context, *SendAsyncVersionedRequest) (*SendAsyncSignedResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SendAsyncVersioned not implemented")
}
func (UnimplementedSequencerServiceServer) SendAsyncUnauthenticatedVersioned(context.Context, *SendAsyncUnauthenticatedVersionedRequest) (*SendAsyncResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SendAsyncUnauthenticatedVersioned not implemented")
}
func (UnimplementedSequencerServiceServer) Subscribe(*SubscriptionRequest, grpc.ServerStreamingServer[SubscriptionResponse]) error {
	return status.Errorf(codes.Unimplemented, "method Subscribe not implemented")
}
func (UnimplementedSequencerServiceServer) SubscribeVersioned(*SubscriptionRequest, grpc.ServerStreamingServer[VersionedSubscriptionResponse]) error {
	return status.Errorf(codes.Unimplemented, "method SubscribeVersioned not implemented")
}
func (UnimplementedSequencerServiceServer) SubscribeUnauthenticated(*SubscriptionRequest, grpc.ServerStreamingServer[SubscriptionResponse]) error {
	return status.Errorf(codes.Unimplemented, "method SubscribeUnauthenticated not implemented")
}
func (UnimplementedSequencerServiceServer) SubscribeUnauthenticatedVersioned(*SubscriptionRequest, grpc.ServerStreamingServer[VersionedSubscriptionResponse]) error {
	return status.Errorf(codes.Unimplemented, "method SubscribeUnauthenticatedVersioned not implemented")
}
func (UnimplementedSequencerServiceServer) Acknowledge(context.Context, *AcknowledgeRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Acknowledge not implemented")
}
func (UnimplementedSequencerServiceServer) AcknowledgeSigned(context.Context, *v0.SignedContent) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AcknowledgeSigned not implemented")
}
func (UnimplementedSequencerServiceServer) mustEmbedUnimplementedSequencerServiceServer() {}
func (UnimplementedSequencerServiceServer) testEmbeddedByValue()                          {}

// UnsafeSequencerServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to SequencerServiceServer will
// result in compilation errors.
type UnsafeSequencerServiceServer interface {
	mustEmbedUnimplementedSequencerServiceServer()
}

func RegisterSequencerServiceServer(s grpc.ServiceRegistrar, srv SequencerServiceServer) {
	// If the following call pancis, it indicates UnimplementedSequencerServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&SequencerService_ServiceDesc, srv)
}

func _SequencerService_SendAsync_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v0.SubmissionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerServiceServer).SendAsync(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SequencerService_SendAsync_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerServiceServer).SendAsync(ctx, req.(*v0.SubmissionRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SequencerService_SendAsyncSigned_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v0.SignedContent)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerServiceServer).SendAsyncSigned(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SequencerService_SendAsyncSigned_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerServiceServer).SendAsyncSigned(ctx, req.(*v0.SignedContent))
	}
	return interceptor(ctx, in, info, handler)
}

func _SequencerService_SendAsyncUnauthenticated_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v0.SubmissionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerServiceServer).SendAsyncUnauthenticated(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SequencerService_SendAsyncUnauthenticated_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerServiceServer).SendAsyncUnauthenticated(ctx, req.(*v0.SubmissionRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SequencerService_SendAsyncVersioned_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SendAsyncVersionedRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerServiceServer).SendAsyncVersioned(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SequencerService_SendAsyncVersioned_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerServiceServer).SendAsyncVersioned(ctx, req.(*SendAsyncVersionedRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SequencerService_SendAsyncUnauthenticatedVersioned_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SendAsyncUnauthenticatedVersionedRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerServiceServer).SendAsyncUnauthenticatedVersioned(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SequencerService_SendAsyncUnauthenticatedVersioned_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerServiceServer).SendAsyncUnauthenticatedVersioned(ctx, req.(*SendAsyncUnauthenticatedVersionedRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SequencerService_Subscribe_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(SubscriptionRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(SequencerServiceServer).Subscribe(m, &grpc.GenericServerStream[SubscriptionRequest, SubscriptionResponse]{ServerStream: stream})
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type SequencerService_SubscribeServer = grpc.ServerStreamingServer[SubscriptionResponse]

func _SequencerService_SubscribeVersioned_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(SubscriptionRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(SequencerServiceServer).SubscribeVersioned(m, &grpc.GenericServerStream[SubscriptionRequest, VersionedSubscriptionResponse]{ServerStream: stream})
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type SequencerService_SubscribeVersionedServer = grpc.ServerStreamingServer[VersionedSubscriptionResponse]

func _SequencerService_SubscribeUnauthenticated_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(SubscriptionRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(SequencerServiceServer).SubscribeUnauthenticated(m, &grpc.GenericServerStream[SubscriptionRequest, SubscriptionResponse]{ServerStream: stream})
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type SequencerService_SubscribeUnauthenticatedServer = grpc.ServerStreamingServer[SubscriptionResponse]

func _SequencerService_SubscribeUnauthenticatedVersioned_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(SubscriptionRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(SequencerServiceServer).SubscribeUnauthenticatedVersioned(m, &grpc.GenericServerStream[SubscriptionRequest, VersionedSubscriptionResponse]{ServerStream: stream})
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type SequencerService_SubscribeUnauthenticatedVersionedServer = grpc.ServerStreamingServer[VersionedSubscriptionResponse]

func _SequencerService_Acknowledge_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AcknowledgeRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerServiceServer).Acknowledge(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SequencerService_Acknowledge_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerServiceServer).Acknowledge(ctx, req.(*AcknowledgeRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SequencerService_AcknowledgeSigned_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v0.SignedContent)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerServiceServer).AcknowledgeSigned(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SequencerService_AcknowledgeSigned_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerServiceServer).AcknowledgeSigned(ctx, req.(*v0.SignedContent))
	}
	return interceptor(ctx, in, info, handler)
}

// SequencerService_ServiceDesc is the grpc.ServiceDesc for SequencerService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var SequencerService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.domain.api.v0.SequencerService",
	HandlerType: (*SequencerServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "SendAsync",
			Handler:    _SequencerService_SendAsync_Handler,
		},
		{
			MethodName: "SendAsyncSigned",
			Handler:    _SequencerService_SendAsyncSigned_Handler,
		},
		{
			MethodName: "SendAsyncUnauthenticated",
			Handler:    _SequencerService_SendAsyncUnauthenticated_Handler,
		},
		{
			MethodName: "SendAsyncVersioned",
			Handler:    _SequencerService_SendAsyncVersioned_Handler,
		},
		{
			MethodName: "SendAsyncUnauthenticatedVersioned",
			Handler:    _SequencerService_SendAsyncUnauthenticatedVersioned_Handler,
		},
		{
			MethodName: "Acknowledge",
			Handler:    _SequencerService_Acknowledge_Handler,
		},
		{
			MethodName: "AcknowledgeSigned",
			Handler:    _SequencerService_AcknowledgeSigned_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "Subscribe",
			Handler:       _SequencerService_Subscribe_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "SubscribeVersioned",
			Handler:       _SequencerService_SubscribeVersioned_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "SubscribeUnauthenticated",
			Handler:       _SequencerService_SubscribeUnauthenticated_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "SubscribeUnauthenticatedVersioned",
			Handler:       _SequencerService_SubscribeUnauthenticatedVersioned_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "com/digitalasset/canton/domain/api/v0/sequencer_service.proto",
}
