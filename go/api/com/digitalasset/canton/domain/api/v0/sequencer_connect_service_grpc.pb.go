// Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v4.24.3
// source: com/digitalasset/canton/domain/api/v0/sequencer_connect_service.proto

package v0

import (
	context "context"
	v0 "github.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/protocol/v0"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// SequencerConnectServiceClient is the client API for SequencerConnectService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type SequencerConnectServiceClient interface {
	Handshake(ctx context.Context, in *v0.Handshake_Request, opts ...grpc.CallOption) (*v0.Handshake_Response, error)
	GetDomainId(ctx context.Context, in *SequencerConnect_GetDomainId_Request, opts ...grpc.CallOption) (*SequencerConnect_GetDomainId_Response, error)
	GetDomainParameters(ctx context.Context, in *SequencerConnect_GetDomainParameters_Request, opts ...grpc.CallOption) (*SequencerConnect_GetDomainParameters_Response, error)
	VerifyActive(ctx context.Context, in *SequencerConnect_VerifyActive_Request, opts ...grpc.CallOption) (*SequencerConnect_VerifyActive_Response, error)
	GetServiceAgreement(ctx context.Context, in *GetServiceAgreementRequest, opts ...grpc.CallOption) (*GetServiceAgreementResponse, error)
}

type sequencerConnectServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewSequencerConnectServiceClient(cc grpc.ClientConnInterface) SequencerConnectServiceClient {
	return &sequencerConnectServiceClient{cc}
}

func (c *sequencerConnectServiceClient) Handshake(ctx context.Context, in *v0.Handshake_Request, opts ...grpc.CallOption) (*v0.Handshake_Response, error) {
	out := new(v0.Handshake_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.domain.api.v0.SequencerConnectService/Handshake", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sequencerConnectServiceClient) GetDomainId(ctx context.Context, in *SequencerConnect_GetDomainId_Request, opts ...grpc.CallOption) (*SequencerConnect_GetDomainId_Response, error) {
	out := new(SequencerConnect_GetDomainId_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.domain.api.v0.SequencerConnectService/GetDomainId", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sequencerConnectServiceClient) GetDomainParameters(ctx context.Context, in *SequencerConnect_GetDomainParameters_Request, opts ...grpc.CallOption) (*SequencerConnect_GetDomainParameters_Response, error) {
	out := new(SequencerConnect_GetDomainParameters_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.domain.api.v0.SequencerConnectService/GetDomainParameters", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sequencerConnectServiceClient) VerifyActive(ctx context.Context, in *SequencerConnect_VerifyActive_Request, opts ...grpc.CallOption) (*SequencerConnect_VerifyActive_Response, error) {
	out := new(SequencerConnect_VerifyActive_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.domain.api.v0.SequencerConnectService/VerifyActive", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sequencerConnectServiceClient) GetServiceAgreement(ctx context.Context, in *GetServiceAgreementRequest, opts ...grpc.CallOption) (*GetServiceAgreementResponse, error) {
	out := new(GetServiceAgreementResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.domain.api.v0.SequencerConnectService/GetServiceAgreement", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// SequencerConnectServiceServer is the server API for SequencerConnectService service.
// All implementations must embed UnimplementedSequencerConnectServiceServer
// for forward compatibility
type SequencerConnectServiceServer interface {
	Handshake(context.Context, *v0.Handshake_Request) (*v0.Handshake_Response, error)
	GetDomainId(context.Context, *SequencerConnect_GetDomainId_Request) (*SequencerConnect_GetDomainId_Response, error)
	GetDomainParameters(context.Context, *SequencerConnect_GetDomainParameters_Request) (*SequencerConnect_GetDomainParameters_Response, error)
	VerifyActive(context.Context, *SequencerConnect_VerifyActive_Request) (*SequencerConnect_VerifyActive_Response, error)
	GetServiceAgreement(context.Context, *GetServiceAgreementRequest) (*GetServiceAgreementResponse, error)
	mustEmbedUnimplementedSequencerConnectServiceServer()
}

// UnimplementedSequencerConnectServiceServer must be embedded to have forward compatible implementations.
type UnimplementedSequencerConnectServiceServer struct {
}

func (UnimplementedSequencerConnectServiceServer) Handshake(context.Context, *v0.Handshake_Request) (*v0.Handshake_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Handshake not implemented")
}
func (UnimplementedSequencerConnectServiceServer) GetDomainId(context.Context, *SequencerConnect_GetDomainId_Request) (*SequencerConnect_GetDomainId_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetDomainId not implemented")
}
func (UnimplementedSequencerConnectServiceServer) GetDomainParameters(context.Context, *SequencerConnect_GetDomainParameters_Request) (*SequencerConnect_GetDomainParameters_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetDomainParameters not implemented")
}
func (UnimplementedSequencerConnectServiceServer) VerifyActive(context.Context, *SequencerConnect_VerifyActive_Request) (*SequencerConnect_VerifyActive_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method VerifyActive not implemented")
}
func (UnimplementedSequencerConnectServiceServer) GetServiceAgreement(context.Context, *GetServiceAgreementRequest) (*GetServiceAgreementResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetServiceAgreement not implemented")
}
func (UnimplementedSequencerConnectServiceServer) mustEmbedUnimplementedSequencerConnectServiceServer() {
}

// UnsafeSequencerConnectServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to SequencerConnectServiceServer will
// result in compilation errors.
type UnsafeSequencerConnectServiceServer interface {
	mustEmbedUnimplementedSequencerConnectServiceServer()
}

func RegisterSequencerConnectServiceServer(s grpc.ServiceRegistrar, srv SequencerConnectServiceServer) {
	s.RegisterService(&SequencerConnectService_ServiceDesc, srv)
}

func _SequencerConnectService_Handshake_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v0.Handshake_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerConnectServiceServer).Handshake(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.domain.api.v0.SequencerConnectService/Handshake",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerConnectServiceServer).Handshake(ctx, req.(*v0.Handshake_Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _SequencerConnectService_GetDomainId_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SequencerConnect_GetDomainId_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerConnectServiceServer).GetDomainId(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.domain.api.v0.SequencerConnectService/GetDomainId",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerConnectServiceServer).GetDomainId(ctx, req.(*SequencerConnect_GetDomainId_Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _SequencerConnectService_GetDomainParameters_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SequencerConnect_GetDomainParameters_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerConnectServiceServer).GetDomainParameters(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.domain.api.v0.SequencerConnectService/GetDomainParameters",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerConnectServiceServer).GetDomainParameters(ctx, req.(*SequencerConnect_GetDomainParameters_Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _SequencerConnectService_VerifyActive_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SequencerConnect_VerifyActive_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerConnectServiceServer).VerifyActive(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.domain.api.v0.SequencerConnectService/VerifyActive",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerConnectServiceServer).VerifyActive(ctx, req.(*SequencerConnect_VerifyActive_Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _SequencerConnectService_GetServiceAgreement_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetServiceAgreementRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerConnectServiceServer).GetServiceAgreement(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.domain.api.v0.SequencerConnectService/GetServiceAgreement",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerConnectServiceServer).GetServiceAgreement(ctx, req.(*GetServiceAgreementRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// SequencerConnectService_ServiceDesc is the grpc.ServiceDesc for SequencerConnectService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var SequencerConnectService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.domain.api.v0.SequencerConnectService",
	HandlerType: (*SequencerConnectServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Handshake",
			Handler:    _SequencerConnectService_Handshake_Handler,
		},
		{
			MethodName: "GetDomainId",
			Handler:    _SequencerConnectService_GetDomainId_Handler,
		},
		{
			MethodName: "GetDomainParameters",
			Handler:    _SequencerConnectService_GetDomainParameters_Handler,
		},
		{
			MethodName: "VerifyActive",
			Handler:    _SequencerConnectService_VerifyActive_Handler,
		},
		{
			MethodName: "GetServiceAgreement",
			Handler:    _SequencerConnectService_GetServiceAgreement_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/digitalasset/canton/domain/api/v0/sequencer_connect_service.proto",
}