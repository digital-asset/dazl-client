// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v5.27.2
// source: com/digitalasset/canton/participant/admin/v0/domain_connectivity.proto

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

// DomainConnectivityServiceClient is the client API for DomainConnectivityService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type DomainConnectivityServiceClient interface {
	ReconnectDomains(ctx context.Context, in *ReconnectDomainsRequest, opts ...grpc.CallOption) (*ReconnectDomainsResponse, error)
	RegisterDomain(ctx context.Context, in *RegisterDomainRequest, opts ...grpc.CallOption) (*RegisterDomainResponse, error)
	ModifyDomain(ctx context.Context, in *ModifyDomainRequest, opts ...grpc.CallOption) (*ModifyDomainResponse, error)
	ConnectDomain(ctx context.Context, in *ConnectDomainRequest, opts ...grpc.CallOption) (*ConnectDomainResponse, error)
	DisconnectDomain(ctx context.Context, in *DisconnectDomainRequest, opts ...grpc.CallOption) (*DisconnectDomainResponse, error)
	ListConnectedDomains(ctx context.Context, in *ListConnectedDomainsRequest, opts ...grpc.CallOption) (*ListConnectedDomainsResponse, error)
	ListConfiguredDomains(ctx context.Context, in *ListConfiguredDomainsRequest, opts ...grpc.CallOption) (*ListConfiguredDomainsResponse, error)
	GetAgreement(ctx context.Context, in *GetAgreementRequest, opts ...grpc.CallOption) (*GetAgreementResponse, error)
	AcceptAgreement(ctx context.Context, in *AcceptAgreementRequest, opts ...grpc.CallOption) (*AcceptAgreementResponse, error)
	GetDomainId(ctx context.Context, in *GetDomainIdRequest, opts ...grpc.CallOption) (*GetDomainIdResponse, error)
}

type domainConnectivityServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewDomainConnectivityServiceClient(cc grpc.ClientConnInterface) DomainConnectivityServiceClient {
	return &domainConnectivityServiceClient{cc}
}

func (c *domainConnectivityServiceClient) ReconnectDomains(ctx context.Context, in *ReconnectDomainsRequest, opts ...grpc.CallOption) (*ReconnectDomainsResponse, error) {
	out := new(ReconnectDomainsResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ReconnectDomains", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *domainConnectivityServiceClient) RegisterDomain(ctx context.Context, in *RegisterDomainRequest, opts ...grpc.CallOption) (*RegisterDomainResponse, error) {
	out := new(RegisterDomainResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/RegisterDomain", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *domainConnectivityServiceClient) ModifyDomain(ctx context.Context, in *ModifyDomainRequest, opts ...grpc.CallOption) (*ModifyDomainResponse, error) {
	out := new(ModifyDomainResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ModifyDomain", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *domainConnectivityServiceClient) ConnectDomain(ctx context.Context, in *ConnectDomainRequest, opts ...grpc.CallOption) (*ConnectDomainResponse, error) {
	out := new(ConnectDomainResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ConnectDomain", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *domainConnectivityServiceClient) DisconnectDomain(ctx context.Context, in *DisconnectDomainRequest, opts ...grpc.CallOption) (*DisconnectDomainResponse, error) {
	out := new(DisconnectDomainResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/DisconnectDomain", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *domainConnectivityServiceClient) ListConnectedDomains(ctx context.Context, in *ListConnectedDomainsRequest, opts ...grpc.CallOption) (*ListConnectedDomainsResponse, error) {
	out := new(ListConnectedDomainsResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ListConnectedDomains", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *domainConnectivityServiceClient) ListConfiguredDomains(ctx context.Context, in *ListConfiguredDomainsRequest, opts ...grpc.CallOption) (*ListConfiguredDomainsResponse, error) {
	out := new(ListConfiguredDomainsResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ListConfiguredDomains", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *domainConnectivityServiceClient) GetAgreement(ctx context.Context, in *GetAgreementRequest, opts ...grpc.CallOption) (*GetAgreementResponse, error) {
	out := new(GetAgreementResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/GetAgreement", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *domainConnectivityServiceClient) AcceptAgreement(ctx context.Context, in *AcceptAgreementRequest, opts ...grpc.CallOption) (*AcceptAgreementResponse, error) {
	out := new(AcceptAgreementResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/AcceptAgreement", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *domainConnectivityServiceClient) GetDomainId(ctx context.Context, in *GetDomainIdRequest, opts ...grpc.CallOption) (*GetDomainIdResponse, error) {
	out := new(GetDomainIdResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/GetDomainId", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// DomainConnectivityServiceServer is the server API for DomainConnectivityService service.
// All implementations must embed UnimplementedDomainConnectivityServiceServer
// for forward compatibility
type DomainConnectivityServiceServer interface {
	ReconnectDomains(context.Context, *ReconnectDomainsRequest) (*ReconnectDomainsResponse, error)
	RegisterDomain(context.Context, *RegisterDomainRequest) (*RegisterDomainResponse, error)
	ModifyDomain(context.Context, *ModifyDomainRequest) (*ModifyDomainResponse, error)
	ConnectDomain(context.Context, *ConnectDomainRequest) (*ConnectDomainResponse, error)
	DisconnectDomain(context.Context, *DisconnectDomainRequest) (*DisconnectDomainResponse, error)
	ListConnectedDomains(context.Context, *ListConnectedDomainsRequest) (*ListConnectedDomainsResponse, error)
	ListConfiguredDomains(context.Context, *ListConfiguredDomainsRequest) (*ListConfiguredDomainsResponse, error)
	GetAgreement(context.Context, *GetAgreementRequest) (*GetAgreementResponse, error)
	AcceptAgreement(context.Context, *AcceptAgreementRequest) (*AcceptAgreementResponse, error)
	GetDomainId(context.Context, *GetDomainIdRequest) (*GetDomainIdResponse, error)
	mustEmbedUnimplementedDomainConnectivityServiceServer()
}

// UnimplementedDomainConnectivityServiceServer must be embedded to have forward compatible implementations.
type UnimplementedDomainConnectivityServiceServer struct {
}

func (UnimplementedDomainConnectivityServiceServer) ReconnectDomains(context.Context, *ReconnectDomainsRequest) (*ReconnectDomainsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ReconnectDomains not implemented")
}
func (UnimplementedDomainConnectivityServiceServer) RegisterDomain(context.Context, *RegisterDomainRequest) (*RegisterDomainResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RegisterDomain not implemented")
}
func (UnimplementedDomainConnectivityServiceServer) ModifyDomain(context.Context, *ModifyDomainRequest) (*ModifyDomainResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ModifyDomain not implemented")
}
func (UnimplementedDomainConnectivityServiceServer) ConnectDomain(context.Context, *ConnectDomainRequest) (*ConnectDomainResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ConnectDomain not implemented")
}
func (UnimplementedDomainConnectivityServiceServer) DisconnectDomain(context.Context, *DisconnectDomainRequest) (*DisconnectDomainResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DisconnectDomain not implemented")
}
func (UnimplementedDomainConnectivityServiceServer) ListConnectedDomains(context.Context, *ListConnectedDomainsRequest) (*ListConnectedDomainsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListConnectedDomains not implemented")
}
func (UnimplementedDomainConnectivityServiceServer) ListConfiguredDomains(context.Context, *ListConfiguredDomainsRequest) (*ListConfiguredDomainsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListConfiguredDomains not implemented")
}
func (UnimplementedDomainConnectivityServiceServer) GetAgreement(context.Context, *GetAgreementRequest) (*GetAgreementResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetAgreement not implemented")
}
func (UnimplementedDomainConnectivityServiceServer) AcceptAgreement(context.Context, *AcceptAgreementRequest) (*AcceptAgreementResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AcceptAgreement not implemented")
}
func (UnimplementedDomainConnectivityServiceServer) GetDomainId(context.Context, *GetDomainIdRequest) (*GetDomainIdResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetDomainId not implemented")
}
func (UnimplementedDomainConnectivityServiceServer) mustEmbedUnimplementedDomainConnectivityServiceServer() {
}

// UnsafeDomainConnectivityServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to DomainConnectivityServiceServer will
// result in compilation errors.
type UnsafeDomainConnectivityServiceServer interface {
	mustEmbedUnimplementedDomainConnectivityServiceServer()
}

func RegisterDomainConnectivityServiceServer(s grpc.ServiceRegistrar, srv DomainConnectivityServiceServer) {
	s.RegisterService(&DomainConnectivityService_ServiceDesc, srv)
}

func _DomainConnectivityService_ReconnectDomains_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ReconnectDomainsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DomainConnectivityServiceServer).ReconnectDomains(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ReconnectDomains",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DomainConnectivityServiceServer).ReconnectDomains(ctx, req.(*ReconnectDomainsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DomainConnectivityService_RegisterDomain_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(RegisterDomainRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DomainConnectivityServiceServer).RegisterDomain(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/RegisterDomain",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DomainConnectivityServiceServer).RegisterDomain(ctx, req.(*RegisterDomainRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DomainConnectivityService_ModifyDomain_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ModifyDomainRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DomainConnectivityServiceServer).ModifyDomain(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ModifyDomain",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DomainConnectivityServiceServer).ModifyDomain(ctx, req.(*ModifyDomainRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DomainConnectivityService_ConnectDomain_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ConnectDomainRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DomainConnectivityServiceServer).ConnectDomain(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ConnectDomain",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DomainConnectivityServiceServer).ConnectDomain(ctx, req.(*ConnectDomainRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DomainConnectivityService_DisconnectDomain_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DisconnectDomainRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DomainConnectivityServiceServer).DisconnectDomain(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/DisconnectDomain",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DomainConnectivityServiceServer).DisconnectDomain(ctx, req.(*DisconnectDomainRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DomainConnectivityService_ListConnectedDomains_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListConnectedDomainsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DomainConnectivityServiceServer).ListConnectedDomains(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ListConnectedDomains",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DomainConnectivityServiceServer).ListConnectedDomains(ctx, req.(*ListConnectedDomainsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DomainConnectivityService_ListConfiguredDomains_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListConfiguredDomainsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DomainConnectivityServiceServer).ListConfiguredDomains(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ListConfiguredDomains",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DomainConnectivityServiceServer).ListConfiguredDomains(ctx, req.(*ListConfiguredDomainsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DomainConnectivityService_GetAgreement_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetAgreementRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DomainConnectivityServiceServer).GetAgreement(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/GetAgreement",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DomainConnectivityServiceServer).GetAgreement(ctx, req.(*GetAgreementRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DomainConnectivityService_AcceptAgreement_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AcceptAgreementRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DomainConnectivityServiceServer).AcceptAgreement(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/AcceptAgreement",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DomainConnectivityServiceServer).AcceptAgreement(ctx, req.(*AcceptAgreementRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DomainConnectivityService_GetDomainId_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetDomainIdRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DomainConnectivityServiceServer).GetDomainId(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/GetDomainId",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DomainConnectivityServiceServer).GetDomainId(ctx, req.(*GetDomainIdRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// DomainConnectivityService_ServiceDesc is the grpc.ServiceDesc for DomainConnectivityService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var DomainConnectivityService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.participant.admin.v0.DomainConnectivityService",
	HandlerType: (*DomainConnectivityServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "ReconnectDomains",
			Handler:    _DomainConnectivityService_ReconnectDomains_Handler,
		},
		{
			MethodName: "RegisterDomain",
			Handler:    _DomainConnectivityService_RegisterDomain_Handler,
		},
		{
			MethodName: "ModifyDomain",
			Handler:    _DomainConnectivityService_ModifyDomain_Handler,
		},
		{
			MethodName: "ConnectDomain",
			Handler:    _DomainConnectivityService_ConnectDomain_Handler,
		},
		{
			MethodName: "DisconnectDomain",
			Handler:    _DomainConnectivityService_DisconnectDomain_Handler,
		},
		{
			MethodName: "ListConnectedDomains",
			Handler:    _DomainConnectivityService_ListConnectedDomains_Handler,
		},
		{
			MethodName: "ListConfiguredDomains",
			Handler:    _DomainConnectivityService_ListConfiguredDomains_Handler,
		},
		{
			MethodName: "GetAgreement",
			Handler:    _DomainConnectivityService_GetAgreement_Handler,
		},
		{
			MethodName: "AcceptAgreement",
			Handler:    _DomainConnectivityService_AcceptAgreement_Handler,
		},
		{
			MethodName: "GetDomainId",
			Handler:    _DomainConnectivityService_GetDomainId_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/digitalasset/canton/participant/admin/v0/domain_connectivity.proto",
}
