// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.4.0
// - protoc             v5.27.2
// source: com/daml/ledger/api/v2/package_service.proto

package v2

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.62.0 or later.
const _ = grpc.SupportPackageIsVersion8

const (
	PackageService_ListPackages_FullMethodName     = "/com.daml.ledger.api.v2.PackageService/ListPackages"
	PackageService_GetPackage_FullMethodName       = "/com.daml.ledger.api.v2.PackageService/GetPackage"
	PackageService_GetPackageStatus_FullMethodName = "/com.daml.ledger.api.v2.PackageService/GetPackageStatus"
)

// PackageServiceClient is the client API for PackageService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type PackageServiceClient interface {
	ListPackages(ctx context.Context, in *ListPackagesRequest, opts ...grpc.CallOption) (*ListPackagesResponse, error)
	GetPackage(ctx context.Context, in *GetPackageRequest, opts ...grpc.CallOption) (*GetPackageResponse, error)
	GetPackageStatus(ctx context.Context, in *GetPackageStatusRequest, opts ...grpc.CallOption) (*GetPackageStatusResponse, error)
}

type packageServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewPackageServiceClient(cc grpc.ClientConnInterface) PackageServiceClient {
	return &packageServiceClient{cc}
}

func (c *packageServiceClient) ListPackages(ctx context.Context, in *ListPackagesRequest, opts ...grpc.CallOption) (*ListPackagesResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(ListPackagesResponse)
	err := c.cc.Invoke(ctx, PackageService_ListPackages_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *packageServiceClient) GetPackage(ctx context.Context, in *GetPackageRequest, opts ...grpc.CallOption) (*GetPackageResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GetPackageResponse)
	err := c.cc.Invoke(ctx, PackageService_GetPackage_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *packageServiceClient) GetPackageStatus(ctx context.Context, in *GetPackageStatusRequest, opts ...grpc.CallOption) (*GetPackageStatusResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GetPackageStatusResponse)
	err := c.cc.Invoke(ctx, PackageService_GetPackageStatus_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// PackageServiceServer is the server API for PackageService service.
// All implementations must embed UnimplementedPackageServiceServer
// for forward compatibility
type PackageServiceServer interface {
	ListPackages(context.Context, *ListPackagesRequest) (*ListPackagesResponse, error)
	GetPackage(context.Context, *GetPackageRequest) (*GetPackageResponse, error)
	GetPackageStatus(context.Context, *GetPackageStatusRequest) (*GetPackageStatusResponse, error)
	mustEmbedUnimplementedPackageServiceServer()
}

// UnimplementedPackageServiceServer must be embedded to have forward compatible implementations.
type UnimplementedPackageServiceServer struct {
}

func (UnimplementedPackageServiceServer) ListPackages(context.Context, *ListPackagesRequest) (*ListPackagesResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListPackages not implemented")
}
func (UnimplementedPackageServiceServer) GetPackage(context.Context, *GetPackageRequest) (*GetPackageResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetPackage not implemented")
}
func (UnimplementedPackageServiceServer) GetPackageStatus(context.Context, *GetPackageStatusRequest) (*GetPackageStatusResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetPackageStatus not implemented")
}
func (UnimplementedPackageServiceServer) mustEmbedUnimplementedPackageServiceServer() {}

// UnsafePackageServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to PackageServiceServer will
// result in compilation errors.
type UnsafePackageServiceServer interface {
	mustEmbedUnimplementedPackageServiceServer()
}

func RegisterPackageServiceServer(s grpc.ServiceRegistrar, srv PackageServiceServer) {
	s.RegisterService(&PackageService_ServiceDesc, srv)
}

func _PackageService_ListPackages_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListPackagesRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PackageServiceServer).ListPackages(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PackageService_ListPackages_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PackageServiceServer).ListPackages(ctx, req.(*ListPackagesRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PackageService_GetPackage_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetPackageRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PackageServiceServer).GetPackage(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PackageService_GetPackage_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PackageServiceServer).GetPackage(ctx, req.(*GetPackageRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PackageService_GetPackageStatus_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetPackageStatusRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PackageServiceServer).GetPackageStatus(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PackageService_GetPackageStatus_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PackageServiceServer).GetPackageStatus(ctx, req.(*GetPackageStatusRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// PackageService_ServiceDesc is the grpc.ServiceDesc for PackageService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var PackageService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.daml.ledger.api.v2.PackageService",
	HandlerType: (*PackageServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "ListPackages",
			Handler:    _PackageService_ListPackages_Handler,
		},
		{
			MethodName: "GetPackage",
			Handler:    _PackageService_GetPackage_Handler,
		},
		{
			MethodName: "GetPackageStatus",
			Handler:    _PackageService_GetPackageStatus_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/daml/ledger/api/v2/package_service.proto",
}
