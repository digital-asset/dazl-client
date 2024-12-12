// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v5.27.2
// source: com/daml/ledger/api/v1/admin/user_management_service.proto

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
	UserManagementService_CreateUser_FullMethodName                   = "/com.daml.ledger.api.v1.admin.UserManagementService/CreateUser"
	UserManagementService_GetUser_FullMethodName                      = "/com.daml.ledger.api.v1.admin.UserManagementService/GetUser"
	UserManagementService_UpdateUser_FullMethodName                   = "/com.daml.ledger.api.v1.admin.UserManagementService/UpdateUser"
	UserManagementService_DeleteUser_FullMethodName                   = "/com.daml.ledger.api.v1.admin.UserManagementService/DeleteUser"
	UserManagementService_ListUsers_FullMethodName                    = "/com.daml.ledger.api.v1.admin.UserManagementService/ListUsers"
	UserManagementService_GrantUserRights_FullMethodName              = "/com.daml.ledger.api.v1.admin.UserManagementService/GrantUserRights"
	UserManagementService_RevokeUserRights_FullMethodName             = "/com.daml.ledger.api.v1.admin.UserManagementService/RevokeUserRights"
	UserManagementService_ListUserRights_FullMethodName               = "/com.daml.ledger.api.v1.admin.UserManagementService/ListUserRights"
	UserManagementService_UpdateUserIdentityProviderId_FullMethodName = "/com.daml.ledger.api.v1.admin.UserManagementService/UpdateUserIdentityProviderId"
)

// UserManagementServiceClient is the client API for UserManagementService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type UserManagementServiceClient interface {
	CreateUser(ctx context.Context, in *CreateUserRequest, opts ...grpc.CallOption) (*CreateUserResponse, error)
	GetUser(ctx context.Context, in *GetUserRequest, opts ...grpc.CallOption) (*GetUserResponse, error)
	UpdateUser(ctx context.Context, in *UpdateUserRequest, opts ...grpc.CallOption) (*UpdateUserResponse, error)
	DeleteUser(ctx context.Context, in *DeleteUserRequest, opts ...grpc.CallOption) (*DeleteUserResponse, error)
	ListUsers(ctx context.Context, in *ListUsersRequest, opts ...grpc.CallOption) (*ListUsersResponse, error)
	GrantUserRights(ctx context.Context, in *GrantUserRightsRequest, opts ...grpc.CallOption) (*GrantUserRightsResponse, error)
	RevokeUserRights(ctx context.Context, in *RevokeUserRightsRequest, opts ...grpc.CallOption) (*RevokeUserRightsResponse, error)
	ListUserRights(ctx context.Context, in *ListUserRightsRequest, opts ...grpc.CallOption) (*ListUserRightsResponse, error)
	UpdateUserIdentityProviderId(ctx context.Context, in *UpdateUserIdentityProviderRequest, opts ...grpc.CallOption) (*UpdateUserIdentityProviderResponse, error)
}

type userManagementServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewUserManagementServiceClient(cc grpc.ClientConnInterface) UserManagementServiceClient {
	return &userManagementServiceClient{cc}
}

func (c *userManagementServiceClient) CreateUser(ctx context.Context, in *CreateUserRequest, opts ...grpc.CallOption) (*CreateUserResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(CreateUserResponse)
	err := c.cc.Invoke(ctx, UserManagementService_CreateUser_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *userManagementServiceClient) GetUser(ctx context.Context, in *GetUserRequest, opts ...grpc.CallOption) (*GetUserResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GetUserResponse)
	err := c.cc.Invoke(ctx, UserManagementService_GetUser_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *userManagementServiceClient) UpdateUser(ctx context.Context, in *UpdateUserRequest, opts ...grpc.CallOption) (*UpdateUserResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(UpdateUserResponse)
	err := c.cc.Invoke(ctx, UserManagementService_UpdateUser_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *userManagementServiceClient) DeleteUser(ctx context.Context, in *DeleteUserRequest, opts ...grpc.CallOption) (*DeleteUserResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(DeleteUserResponse)
	err := c.cc.Invoke(ctx, UserManagementService_DeleteUser_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *userManagementServiceClient) ListUsers(ctx context.Context, in *ListUsersRequest, opts ...grpc.CallOption) (*ListUsersResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(ListUsersResponse)
	err := c.cc.Invoke(ctx, UserManagementService_ListUsers_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *userManagementServiceClient) GrantUserRights(ctx context.Context, in *GrantUserRightsRequest, opts ...grpc.CallOption) (*GrantUserRightsResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GrantUserRightsResponse)
	err := c.cc.Invoke(ctx, UserManagementService_GrantUserRights_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *userManagementServiceClient) RevokeUserRights(ctx context.Context, in *RevokeUserRightsRequest, opts ...grpc.CallOption) (*RevokeUserRightsResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(RevokeUserRightsResponse)
	err := c.cc.Invoke(ctx, UserManagementService_RevokeUserRights_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *userManagementServiceClient) ListUserRights(ctx context.Context, in *ListUserRightsRequest, opts ...grpc.CallOption) (*ListUserRightsResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(ListUserRightsResponse)
	err := c.cc.Invoke(ctx, UserManagementService_ListUserRights_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *userManagementServiceClient) UpdateUserIdentityProviderId(ctx context.Context, in *UpdateUserIdentityProviderRequest, opts ...grpc.CallOption) (*UpdateUserIdentityProviderResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(UpdateUserIdentityProviderResponse)
	err := c.cc.Invoke(ctx, UserManagementService_UpdateUserIdentityProviderId_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// UserManagementServiceServer is the server API for UserManagementService service.
// All implementations must embed UnimplementedUserManagementServiceServer
// for forward compatibility.
type UserManagementServiceServer interface {
	CreateUser(context.Context, *CreateUserRequest) (*CreateUserResponse, error)
	GetUser(context.Context, *GetUserRequest) (*GetUserResponse, error)
	UpdateUser(context.Context, *UpdateUserRequest) (*UpdateUserResponse, error)
	DeleteUser(context.Context, *DeleteUserRequest) (*DeleteUserResponse, error)
	ListUsers(context.Context, *ListUsersRequest) (*ListUsersResponse, error)
	GrantUserRights(context.Context, *GrantUserRightsRequest) (*GrantUserRightsResponse, error)
	RevokeUserRights(context.Context, *RevokeUserRightsRequest) (*RevokeUserRightsResponse, error)
	ListUserRights(context.Context, *ListUserRightsRequest) (*ListUserRightsResponse, error)
	UpdateUserIdentityProviderId(context.Context, *UpdateUserIdentityProviderRequest) (*UpdateUserIdentityProviderResponse, error)
	mustEmbedUnimplementedUserManagementServiceServer()
}

// UnimplementedUserManagementServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedUserManagementServiceServer struct{}

func (UnimplementedUserManagementServiceServer) CreateUser(context.Context, *CreateUserRequest) (*CreateUserResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateUser not implemented")
}
func (UnimplementedUserManagementServiceServer) GetUser(context.Context, *GetUserRequest) (*GetUserResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetUser not implemented")
}
func (UnimplementedUserManagementServiceServer) UpdateUser(context.Context, *UpdateUserRequest) (*UpdateUserResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateUser not implemented")
}
func (UnimplementedUserManagementServiceServer) DeleteUser(context.Context, *DeleteUserRequest) (*DeleteUserResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteUser not implemented")
}
func (UnimplementedUserManagementServiceServer) ListUsers(context.Context, *ListUsersRequest) (*ListUsersResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListUsers not implemented")
}
func (UnimplementedUserManagementServiceServer) GrantUserRights(context.Context, *GrantUserRightsRequest) (*GrantUserRightsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GrantUserRights not implemented")
}
func (UnimplementedUserManagementServiceServer) RevokeUserRights(context.Context, *RevokeUserRightsRequest) (*RevokeUserRightsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RevokeUserRights not implemented")
}
func (UnimplementedUserManagementServiceServer) ListUserRights(context.Context, *ListUserRightsRequest) (*ListUserRightsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListUserRights not implemented")
}
func (UnimplementedUserManagementServiceServer) UpdateUserIdentityProviderId(context.Context, *UpdateUserIdentityProviderRequest) (*UpdateUserIdentityProviderResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateUserIdentityProviderId not implemented")
}
func (UnimplementedUserManagementServiceServer) mustEmbedUnimplementedUserManagementServiceServer() {}
func (UnimplementedUserManagementServiceServer) testEmbeddedByValue()                               {}

// UnsafeUserManagementServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to UserManagementServiceServer will
// result in compilation errors.
type UnsafeUserManagementServiceServer interface {
	mustEmbedUnimplementedUserManagementServiceServer()
}

func RegisterUserManagementServiceServer(s grpc.ServiceRegistrar, srv UserManagementServiceServer) {
	// If the following call pancis, it indicates UnimplementedUserManagementServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&UserManagementService_ServiceDesc, srv)
}

func _UserManagementService_CreateUser_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateUserRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(UserManagementServiceServer).CreateUser(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: UserManagementService_CreateUser_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(UserManagementServiceServer).CreateUser(ctx, req.(*CreateUserRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _UserManagementService_GetUser_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetUserRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(UserManagementServiceServer).GetUser(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: UserManagementService_GetUser_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(UserManagementServiceServer).GetUser(ctx, req.(*GetUserRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _UserManagementService_UpdateUser_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateUserRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(UserManagementServiceServer).UpdateUser(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: UserManagementService_UpdateUser_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(UserManagementServiceServer).UpdateUser(ctx, req.(*UpdateUserRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _UserManagementService_DeleteUser_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DeleteUserRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(UserManagementServiceServer).DeleteUser(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: UserManagementService_DeleteUser_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(UserManagementServiceServer).DeleteUser(ctx, req.(*DeleteUserRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _UserManagementService_ListUsers_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListUsersRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(UserManagementServiceServer).ListUsers(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: UserManagementService_ListUsers_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(UserManagementServiceServer).ListUsers(ctx, req.(*ListUsersRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _UserManagementService_GrantUserRights_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GrantUserRightsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(UserManagementServiceServer).GrantUserRights(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: UserManagementService_GrantUserRights_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(UserManagementServiceServer).GrantUserRights(ctx, req.(*GrantUserRightsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _UserManagementService_RevokeUserRights_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(RevokeUserRightsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(UserManagementServiceServer).RevokeUserRights(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: UserManagementService_RevokeUserRights_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(UserManagementServiceServer).RevokeUserRights(ctx, req.(*RevokeUserRightsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _UserManagementService_ListUserRights_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListUserRightsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(UserManagementServiceServer).ListUserRights(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: UserManagementService_ListUserRights_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(UserManagementServiceServer).ListUserRights(ctx, req.(*ListUserRightsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _UserManagementService_UpdateUserIdentityProviderId_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateUserIdentityProviderRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(UserManagementServiceServer).UpdateUserIdentityProviderId(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: UserManagementService_UpdateUserIdentityProviderId_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(UserManagementServiceServer).UpdateUserIdentityProviderId(ctx, req.(*UpdateUserIdentityProviderRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// UserManagementService_ServiceDesc is the grpc.ServiceDesc for UserManagementService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var UserManagementService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.daml.ledger.api.v1.admin.UserManagementService",
	HandlerType: (*UserManagementServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "CreateUser",
			Handler:    _UserManagementService_CreateUser_Handler,
		},
		{
			MethodName: "GetUser",
			Handler:    _UserManagementService_GetUser_Handler,
		},
		{
			MethodName: "UpdateUser",
			Handler:    _UserManagementService_UpdateUser_Handler,
		},
		{
			MethodName: "DeleteUser",
			Handler:    _UserManagementService_DeleteUser_Handler,
		},
		{
			MethodName: "ListUsers",
			Handler:    _UserManagementService_ListUsers_Handler,
		},
		{
			MethodName: "GrantUserRights",
			Handler:    _UserManagementService_GrantUserRights_Handler,
		},
		{
			MethodName: "RevokeUserRights",
			Handler:    _UserManagementService_RevokeUserRights_Handler,
		},
		{
			MethodName: "ListUserRights",
			Handler:    _UserManagementService_ListUserRights_Handler,
		},
		{
			MethodName: "UpdateUserIdentityProviderId",
			Handler:    _UserManagementService_UpdateUserIdentityProviderId_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/daml/ledger/api/v1/admin/user_management_service.proto",
}
