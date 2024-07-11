// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v3.19.5
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
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// ConfigManagementServiceClient is the client API for ConfigManagementService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ConfigManagementServiceClient interface {
	// Return the currently active time model and the current configuration generation.
	GetTimeModel(ctx context.Context, in *GetTimeModelRequest, opts ...grpc.CallOption) (*GetTimeModelResponse, error)
	// Set the ledger time model.
	SetTimeModel(ctx context.Context, in *SetTimeModelRequest, opts ...grpc.CallOption) (*SetTimeModelResponse, error)
}

type configManagementServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewConfigManagementServiceClient(cc grpc.ClientConnInterface) ConfigManagementServiceClient {
	return &configManagementServiceClient{cc}
}

func (c *configManagementServiceClient) GetTimeModel(ctx context.Context, in *GetTimeModelRequest, opts ...grpc.CallOption) (*GetTimeModelResponse, error) {
	out := new(GetTimeModelResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.admin.ConfigManagementService/GetTimeModel", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *configManagementServiceClient) SetTimeModel(ctx context.Context, in *SetTimeModelRequest, opts ...grpc.CallOption) (*SetTimeModelResponse, error) {
	out := new(SetTimeModelResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.admin.ConfigManagementService/SetTimeModel", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ConfigManagementServiceServer is the server API for ConfigManagementService service.
// All implementations must embed UnimplementedConfigManagementServiceServer
// for forward compatibility
type ConfigManagementServiceServer interface {
	// Return the currently active time model and the current configuration generation.
	GetTimeModel(context.Context, *GetTimeModelRequest) (*GetTimeModelResponse, error)
	// Set the ledger time model.
	SetTimeModel(context.Context, *SetTimeModelRequest) (*SetTimeModelResponse, error)
	mustEmbedUnimplementedConfigManagementServiceServer()
}

// UnimplementedConfigManagementServiceServer must be embedded to have forward compatible implementations.
type UnimplementedConfigManagementServiceServer struct {
}

func (UnimplementedConfigManagementServiceServer) GetTimeModel(context.Context, *GetTimeModelRequest) (*GetTimeModelResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetTimeModel not implemented")
}
func (UnimplementedConfigManagementServiceServer) SetTimeModel(context.Context, *SetTimeModelRequest) (*SetTimeModelResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SetTimeModel not implemented")
}
func (UnimplementedConfigManagementServiceServer) mustEmbedUnimplementedConfigManagementServiceServer() {
}

// UnsafeConfigManagementServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ConfigManagementServiceServer will
// result in compilation errors.
type UnsafeConfigManagementServiceServer interface {
	mustEmbedUnimplementedConfigManagementServiceServer()
}

func RegisterConfigManagementServiceServer(s grpc.ServiceRegistrar, srv ConfigManagementServiceServer) {
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
		FullMethod: "/com.daml.ledger.api.v1.admin.ConfigManagementService/GetTimeModel",
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
		FullMethod: "/com.daml.ledger.api.v1.admin.ConfigManagementService/SetTimeModel",
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
