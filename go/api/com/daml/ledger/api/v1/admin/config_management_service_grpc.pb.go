// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v5.27.2
// source: com/daml/ledger/api/v1/admin/config_management_service.proto

package admin

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
	ConfigManagementService_GetTimeModel_FullMethodName = "/com.daml.ledger.api.v1.admin.ConfigManagementService/GetTimeModel"
	ConfigManagementService_SetTimeModel_FullMethodName = "/com.daml.ledger.api.v1.admin.ConfigManagementService/SetTimeModel"
)

// ConfigManagementServiceClient is the client API for ConfigManagementService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ConfigManagementServiceClient interface {
	GetTimeModel(ctx context.Context, in *GetTimeModelRequest, opts ...grpc.CallOption) (*GetTimeModelResponse, error)
	SetTimeModel(ctx context.Context, in *SetTimeModelRequest, opts ...grpc.CallOption) (*SetTimeModelResponse, error)
}

type configManagementServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewConfigManagementServiceClient(cc grpc.ClientConnInterface) ConfigManagementServiceClient {
	return &configManagementServiceClient{cc}
}

func (c *configManagementServiceClient) GetTimeModel(ctx context.Context, in *GetTimeModelRequest, opts ...grpc.CallOption) (*GetTimeModelResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GetTimeModelResponse)
	err := c.cc.Invoke(ctx, ConfigManagementService_GetTimeModel_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *configManagementServiceClient) SetTimeModel(ctx context.Context, in *SetTimeModelRequest, opts ...grpc.CallOption) (*SetTimeModelResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(SetTimeModelResponse)
	err := c.cc.Invoke(ctx, ConfigManagementService_SetTimeModel_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ConfigManagementServiceServer is the server API for ConfigManagementService service.
// All implementations must embed UnimplementedConfigManagementServiceServer
// for forward compatibility.
type ConfigManagementServiceServer interface {
	GetTimeModel(context.Context, *GetTimeModelRequest) (*GetTimeModelResponse, error)
	SetTimeModel(context.Context, *SetTimeModelRequest) (*SetTimeModelResponse, error)
	mustEmbedUnimplementedConfigManagementServiceServer()
}

// UnimplementedConfigManagementServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedConfigManagementServiceServer struct{}

func (UnimplementedConfigManagementServiceServer) GetTimeModel(context.Context, *GetTimeModelRequest) (*GetTimeModelResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetTimeModel not implemented")
}
func (UnimplementedConfigManagementServiceServer) SetTimeModel(context.Context, *SetTimeModelRequest) (*SetTimeModelResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SetTimeModel not implemented")
}
func (UnimplementedConfigManagementServiceServer) mustEmbedUnimplementedConfigManagementServiceServer() {
}
func (UnimplementedConfigManagementServiceServer) testEmbeddedByValue() {}

// UnsafeConfigManagementServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ConfigManagementServiceServer will
// result in compilation errors.
type UnsafeConfigManagementServiceServer interface {
	mustEmbedUnimplementedConfigManagementServiceServer()
}

func RegisterConfigManagementServiceServer(s grpc.ServiceRegistrar, srv ConfigManagementServiceServer) {
	// If the following call pancis, it indicates UnimplementedConfigManagementServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&ConfigManagementService_ServiceDesc, srv)
}

func _ConfigManagementService_GetTimeModel_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetTimeModelRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ConfigManagementServiceServer).GetTimeModel(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ConfigManagementService_GetTimeModel_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ConfigManagementServiceServer).GetTimeModel(ctx, req.(*GetTimeModelRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ConfigManagementService_SetTimeModel_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SetTimeModelRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ConfigManagementServiceServer).SetTimeModel(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ConfigManagementService_SetTimeModel_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ConfigManagementServiceServer).SetTimeModel(ctx, req.(*SetTimeModelRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// ConfigManagementService_ServiceDesc is the grpc.ServiceDesc for ConfigManagementService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var ConfigManagementService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.daml.ledger.api.v1.admin.ConfigManagementService",
	HandlerType: (*ConfigManagementServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetTimeModel",
			Handler:    _ConfigManagementService_GetTimeModel_Handler,
		},
		{
			MethodName: "SetTimeModel",
			Handler:    _ConfigManagementService_SetTimeModel_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/daml/ledger/api/v1/admin/config_management_service.proto",
}
