// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v5.27.2
// source: com/daml/ledger/api/v1/admin/identity_provider_config_service.proto

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
	IdentityProviderConfigService_CreateIdentityProviderConfig_FullMethodName = "/com.daml.ledger.api.v1.admin.IdentityProviderConfigService/CreateIdentityProviderConfig"
	IdentityProviderConfigService_GetIdentityProviderConfig_FullMethodName    = "/com.daml.ledger.api.v1.admin.IdentityProviderConfigService/GetIdentityProviderConfig"
	IdentityProviderConfigService_UpdateIdentityProviderConfig_FullMethodName = "/com.daml.ledger.api.v1.admin.IdentityProviderConfigService/UpdateIdentityProviderConfig"
	IdentityProviderConfigService_ListIdentityProviderConfigs_FullMethodName  = "/com.daml.ledger.api.v1.admin.IdentityProviderConfigService/ListIdentityProviderConfigs"
	IdentityProviderConfigService_DeleteIdentityProviderConfig_FullMethodName = "/com.daml.ledger.api.v1.admin.IdentityProviderConfigService/DeleteIdentityProviderConfig"
)

// IdentityProviderConfigServiceClient is the client API for IdentityProviderConfigService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type IdentityProviderConfigServiceClient interface {
	CreateIdentityProviderConfig(ctx context.Context, in *CreateIdentityProviderConfigRequest, opts ...grpc.CallOption) (*CreateIdentityProviderConfigResponse, error)
	GetIdentityProviderConfig(ctx context.Context, in *GetIdentityProviderConfigRequest, opts ...grpc.CallOption) (*GetIdentityProviderConfigResponse, error)
	UpdateIdentityProviderConfig(ctx context.Context, in *UpdateIdentityProviderConfigRequest, opts ...grpc.CallOption) (*UpdateIdentityProviderConfigResponse, error)
	ListIdentityProviderConfigs(ctx context.Context, in *ListIdentityProviderConfigsRequest, opts ...grpc.CallOption) (*ListIdentityProviderConfigsResponse, error)
	DeleteIdentityProviderConfig(ctx context.Context, in *DeleteIdentityProviderConfigRequest, opts ...grpc.CallOption) (*DeleteIdentityProviderConfigResponse, error)
}

type identityProviderConfigServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewIdentityProviderConfigServiceClient(cc grpc.ClientConnInterface) IdentityProviderConfigServiceClient {
	return &identityProviderConfigServiceClient{cc}
}

func (c *identityProviderConfigServiceClient) CreateIdentityProviderConfig(ctx context.Context, in *CreateIdentityProviderConfigRequest, opts ...grpc.CallOption) (*CreateIdentityProviderConfigResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(CreateIdentityProviderConfigResponse)
	err := c.cc.Invoke(ctx, IdentityProviderConfigService_CreateIdentityProviderConfig_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *identityProviderConfigServiceClient) GetIdentityProviderConfig(ctx context.Context, in *GetIdentityProviderConfigRequest, opts ...grpc.CallOption) (*GetIdentityProviderConfigResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GetIdentityProviderConfigResponse)
	err := c.cc.Invoke(ctx, IdentityProviderConfigService_GetIdentityProviderConfig_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *identityProviderConfigServiceClient) UpdateIdentityProviderConfig(ctx context.Context, in *UpdateIdentityProviderConfigRequest, opts ...grpc.CallOption) (*UpdateIdentityProviderConfigResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(UpdateIdentityProviderConfigResponse)
	err := c.cc.Invoke(ctx, IdentityProviderConfigService_UpdateIdentityProviderConfig_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *identityProviderConfigServiceClient) ListIdentityProviderConfigs(ctx context.Context, in *ListIdentityProviderConfigsRequest, opts ...grpc.CallOption) (*ListIdentityProviderConfigsResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(ListIdentityProviderConfigsResponse)
	err := c.cc.Invoke(ctx, IdentityProviderConfigService_ListIdentityProviderConfigs_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *identityProviderConfigServiceClient) DeleteIdentityProviderConfig(ctx context.Context, in *DeleteIdentityProviderConfigRequest, opts ...grpc.CallOption) (*DeleteIdentityProviderConfigResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(DeleteIdentityProviderConfigResponse)
	err := c.cc.Invoke(ctx, IdentityProviderConfigService_DeleteIdentityProviderConfig_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// IdentityProviderConfigServiceServer is the server API for IdentityProviderConfigService service.
// All implementations must embed UnimplementedIdentityProviderConfigServiceServer
// for forward compatibility.
type IdentityProviderConfigServiceServer interface {
	CreateIdentityProviderConfig(context.Context, *CreateIdentityProviderConfigRequest) (*CreateIdentityProviderConfigResponse, error)
	GetIdentityProviderConfig(context.Context, *GetIdentityProviderConfigRequest) (*GetIdentityProviderConfigResponse, error)
	UpdateIdentityProviderConfig(context.Context, *UpdateIdentityProviderConfigRequest) (*UpdateIdentityProviderConfigResponse, error)
	ListIdentityProviderConfigs(context.Context, *ListIdentityProviderConfigsRequest) (*ListIdentityProviderConfigsResponse, error)
	DeleteIdentityProviderConfig(context.Context, *DeleteIdentityProviderConfigRequest) (*DeleteIdentityProviderConfigResponse, error)
	mustEmbedUnimplementedIdentityProviderConfigServiceServer()
}

// UnimplementedIdentityProviderConfigServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedIdentityProviderConfigServiceServer struct{}

func (UnimplementedIdentityProviderConfigServiceServer) CreateIdentityProviderConfig(context.Context, *CreateIdentityProviderConfigRequest) (*CreateIdentityProviderConfigResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateIdentityProviderConfig not implemented")
}
func (UnimplementedIdentityProviderConfigServiceServer) GetIdentityProviderConfig(context.Context, *GetIdentityProviderConfigRequest) (*GetIdentityProviderConfigResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetIdentityProviderConfig not implemented")
}
func (UnimplementedIdentityProviderConfigServiceServer) UpdateIdentityProviderConfig(context.Context, *UpdateIdentityProviderConfigRequest) (*UpdateIdentityProviderConfigResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateIdentityProviderConfig not implemented")
}
func (UnimplementedIdentityProviderConfigServiceServer) ListIdentityProviderConfigs(context.Context, *ListIdentityProviderConfigsRequest) (*ListIdentityProviderConfigsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListIdentityProviderConfigs not implemented")
}
func (UnimplementedIdentityProviderConfigServiceServer) DeleteIdentityProviderConfig(context.Context, *DeleteIdentityProviderConfigRequest) (*DeleteIdentityProviderConfigResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteIdentityProviderConfig not implemented")
}
func (UnimplementedIdentityProviderConfigServiceServer) mustEmbedUnimplementedIdentityProviderConfigServiceServer() {
}
func (UnimplementedIdentityProviderConfigServiceServer) testEmbeddedByValue() {}

// UnsafeIdentityProviderConfigServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to IdentityProviderConfigServiceServer will
// result in compilation errors.
type UnsafeIdentityProviderConfigServiceServer interface {
	mustEmbedUnimplementedIdentityProviderConfigServiceServer()
}

func RegisterIdentityProviderConfigServiceServer(s grpc.ServiceRegistrar, srv IdentityProviderConfigServiceServer) {
	// If the following call pancis, it indicates UnimplementedIdentityProviderConfigServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&IdentityProviderConfigService_ServiceDesc, srv)
}

func _IdentityProviderConfigService_CreateIdentityProviderConfig_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateIdentityProviderConfigRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(IdentityProviderConfigServiceServer).CreateIdentityProviderConfig(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: IdentityProviderConfigService_CreateIdentityProviderConfig_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(IdentityProviderConfigServiceServer).CreateIdentityProviderConfig(ctx, req.(*CreateIdentityProviderConfigRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _IdentityProviderConfigService_GetIdentityProviderConfig_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetIdentityProviderConfigRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(IdentityProviderConfigServiceServer).GetIdentityProviderConfig(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: IdentityProviderConfigService_GetIdentityProviderConfig_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(IdentityProviderConfigServiceServer).GetIdentityProviderConfig(ctx, req.(*GetIdentityProviderConfigRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _IdentityProviderConfigService_UpdateIdentityProviderConfig_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateIdentityProviderConfigRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(IdentityProviderConfigServiceServer).UpdateIdentityProviderConfig(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: IdentityProviderConfigService_UpdateIdentityProviderConfig_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(IdentityProviderConfigServiceServer).UpdateIdentityProviderConfig(ctx, req.(*UpdateIdentityProviderConfigRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _IdentityProviderConfigService_ListIdentityProviderConfigs_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListIdentityProviderConfigsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(IdentityProviderConfigServiceServer).ListIdentityProviderConfigs(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: IdentityProviderConfigService_ListIdentityProviderConfigs_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(IdentityProviderConfigServiceServer).ListIdentityProviderConfigs(ctx, req.(*ListIdentityProviderConfigsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _IdentityProviderConfigService_DeleteIdentityProviderConfig_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DeleteIdentityProviderConfigRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(IdentityProviderConfigServiceServer).DeleteIdentityProviderConfig(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: IdentityProviderConfigService_DeleteIdentityProviderConfig_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(IdentityProviderConfigServiceServer).DeleteIdentityProviderConfig(ctx, req.(*DeleteIdentityProviderConfigRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// IdentityProviderConfigService_ServiceDesc is the grpc.ServiceDesc for IdentityProviderConfigService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var IdentityProviderConfigService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.daml.ledger.api.v1.admin.IdentityProviderConfigService",
	HandlerType: (*IdentityProviderConfigServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "CreateIdentityProviderConfig",
			Handler:    _IdentityProviderConfigService_CreateIdentityProviderConfig_Handler,
		},
		{
			MethodName: "GetIdentityProviderConfig",
			Handler:    _IdentityProviderConfigService_GetIdentityProviderConfig_Handler,
		},
		{
			MethodName: "UpdateIdentityProviderConfig",
			Handler:    _IdentityProviderConfigService_UpdateIdentityProviderConfig_Handler,
		},
		{
			MethodName: "ListIdentityProviderConfigs",
			Handler:    _IdentityProviderConfigService_ListIdentityProviderConfigs_Handler,
		},
		{
			MethodName: "DeleteIdentityProviderConfig",
			Handler:    _IdentityProviderConfigService_DeleteIdentityProviderConfig_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/daml/ledger/api/v1/admin/identity_provider_config_service.proto",
}
