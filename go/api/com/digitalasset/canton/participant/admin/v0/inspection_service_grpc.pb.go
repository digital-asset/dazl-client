// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v5.26.1
// source: com/digitalasset/canton/participant/admin/v0/inspection_service.proto

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

// InspectionServiceClient is the client API for InspectionService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type InspectionServiceClient interface {
	LookupContractDomain(ctx context.Context, in *LookupContractDomain_Request, opts ...grpc.CallOption) (*LookupContractDomain_Response, error)
	LookupTransactionDomain(ctx context.Context, in *LookupTransactionDomain_Request, opts ...grpc.CallOption) (*LookupTransactionDomain_Response, error)
	LookupOffsetByTime(ctx context.Context, in *LookupOffsetByTime_Request, opts ...grpc.CallOption) (*LookupOffsetByTime_Response, error)
	LookupOffsetByIndex(ctx context.Context, in *LookupOffsetByIndex_Request, opts ...grpc.CallOption) (*LookupOffsetByIndex_Response, error)
}

type inspectionServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewInspectionServiceClient(cc grpc.ClientConnInterface) InspectionServiceClient {
	return &inspectionServiceClient{cc}
}

func (c *inspectionServiceClient) LookupContractDomain(ctx context.Context, in *LookupContractDomain_Request, opts ...grpc.CallOption) (*LookupContractDomain_Response, error) {
	out := new(LookupContractDomain_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupContractDomain", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *inspectionServiceClient) LookupTransactionDomain(ctx context.Context, in *LookupTransactionDomain_Request, opts ...grpc.CallOption) (*LookupTransactionDomain_Response, error) {
	out := new(LookupTransactionDomain_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupTransactionDomain", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *inspectionServiceClient) LookupOffsetByTime(ctx context.Context, in *LookupOffsetByTime_Request, opts ...grpc.CallOption) (*LookupOffsetByTime_Response, error) {
	out := new(LookupOffsetByTime_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupOffsetByTime", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *inspectionServiceClient) LookupOffsetByIndex(ctx context.Context, in *LookupOffsetByIndex_Request, opts ...grpc.CallOption) (*LookupOffsetByIndex_Response, error) {
	out := new(LookupOffsetByIndex_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupOffsetByIndex", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// InspectionServiceServer is the server API for InspectionService service.
// All implementations must embed UnimplementedInspectionServiceServer
// for forward compatibility
type InspectionServiceServer interface {
	LookupContractDomain(context.Context, *LookupContractDomain_Request) (*LookupContractDomain_Response, error)
	LookupTransactionDomain(context.Context, *LookupTransactionDomain_Request) (*LookupTransactionDomain_Response, error)
	LookupOffsetByTime(context.Context, *LookupOffsetByTime_Request) (*LookupOffsetByTime_Response, error)
	LookupOffsetByIndex(context.Context, *LookupOffsetByIndex_Request) (*LookupOffsetByIndex_Response, error)
	mustEmbedUnimplementedInspectionServiceServer()
}

// UnimplementedInspectionServiceServer must be embedded to have forward compatible implementations.
type UnimplementedInspectionServiceServer struct {
}

func (UnimplementedInspectionServiceServer) LookupContractDomain(context.Context, *LookupContractDomain_Request) (*LookupContractDomain_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method LookupContractDomain not implemented")
}
func (UnimplementedInspectionServiceServer) LookupTransactionDomain(context.Context, *LookupTransactionDomain_Request) (*LookupTransactionDomain_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method LookupTransactionDomain not implemented")
}
func (UnimplementedInspectionServiceServer) LookupOffsetByTime(context.Context, *LookupOffsetByTime_Request) (*LookupOffsetByTime_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method LookupOffsetByTime not implemented")
}
func (UnimplementedInspectionServiceServer) LookupOffsetByIndex(context.Context, *LookupOffsetByIndex_Request) (*LookupOffsetByIndex_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method LookupOffsetByIndex not implemented")
}
func (UnimplementedInspectionServiceServer) mustEmbedUnimplementedInspectionServiceServer() {}

// UnsafeInspectionServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to InspectionServiceServer will
// result in compilation errors.
type UnsafeInspectionServiceServer interface {
	mustEmbedUnimplementedInspectionServiceServer()
}

func RegisterInspectionServiceServer(s grpc.ServiceRegistrar, srv InspectionServiceServer) {
	s.RegisterService(&InspectionService_ServiceDesc, srv)
}

func _InspectionService_LookupContractDomain_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(LookupContractDomain_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InspectionServiceServer).LookupContractDomain(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupContractDomain",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InspectionServiceServer).LookupContractDomain(ctx, req.(*LookupContractDomain_Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _InspectionService_LookupTransactionDomain_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(LookupTransactionDomain_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InspectionServiceServer).LookupTransactionDomain(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupTransactionDomain",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InspectionServiceServer).LookupTransactionDomain(ctx, req.(*LookupTransactionDomain_Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _InspectionService_LookupOffsetByTime_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(LookupOffsetByTime_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InspectionServiceServer).LookupOffsetByTime(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupOffsetByTime",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InspectionServiceServer).LookupOffsetByTime(ctx, req.(*LookupOffsetByTime_Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _InspectionService_LookupOffsetByIndex_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(LookupOffsetByIndex_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InspectionServiceServer).LookupOffsetByIndex(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupOffsetByIndex",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InspectionServiceServer).LookupOffsetByIndex(ctx, req.(*LookupOffsetByIndex_Request))
	}
	return interceptor(ctx, in, info, handler)
}

// InspectionService_ServiceDesc is the grpc.ServiceDesc for InspectionService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var InspectionService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.participant.admin.v0.InspectionService",
	HandlerType: (*InspectionServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "LookupContractDomain",
			Handler:    _InspectionService_LookupContractDomain_Handler,
		},
		{
			MethodName: "LookupTransactionDomain",
			Handler:    _InspectionService_LookupTransactionDomain_Handler,
		},
		{
			MethodName: "LookupOffsetByTime",
			Handler:    _InspectionService_LookupOffsetByTime_Handler,
		},
		{
			MethodName: "LookupOffsetByIndex",
			Handler:    _InspectionService_LookupOffsetByIndex_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/digitalasset/canton/participant/admin/v0/inspection_service.proto",
}
