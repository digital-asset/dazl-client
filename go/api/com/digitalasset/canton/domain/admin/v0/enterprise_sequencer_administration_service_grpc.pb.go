// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v5.27.2
// source: com/digitalasset/canton/domain/admin/v0/enterprise_sequencer_administration_service.proto

package v0

import (
	context "context"
	v0 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/pruning/admin/v0"
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
	EnterpriseSequencerAdministrationService_Prune_FullMethodName                   = "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/Prune"
	EnterpriseSequencerAdministrationService_Snapshot_FullMethodName                = "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/Snapshot"
	EnterpriseSequencerAdministrationService_DisableMember_FullMethodName           = "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/DisableMember"
	EnterpriseSequencerAdministrationService_AuthorizeLedgerIdentity_FullMethodName = "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/AuthorizeLedgerIdentity"
	EnterpriseSequencerAdministrationService_SetSchedule_FullMethodName             = "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetSchedule"
	EnterpriseSequencerAdministrationService_SetCron_FullMethodName                 = "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetCron"
	EnterpriseSequencerAdministrationService_SetMaxDuration_FullMethodName          = "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetMaxDuration"
	EnterpriseSequencerAdministrationService_SetRetention_FullMethodName            = "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetRetention"
	EnterpriseSequencerAdministrationService_ClearSchedule_FullMethodName           = "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/ClearSchedule"
	EnterpriseSequencerAdministrationService_GetSchedule_FullMethodName             = "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/GetSchedule"
	EnterpriseSequencerAdministrationService_LocatePruningTimestamp_FullMethodName  = "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/LocatePruningTimestamp"
)

// EnterpriseSequencerAdministrationServiceClient is the client API for EnterpriseSequencerAdministrationService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type EnterpriseSequencerAdministrationServiceClient interface {
	Prune(ctx context.Context, in *Pruning_Request, opts ...grpc.CallOption) (*Pruning_Response, error)
	Snapshot(ctx context.Context, in *Snapshot_Request, opts ...grpc.CallOption) (*Snapshot_Response, error)
	DisableMember(ctx context.Context, in *DisableMemberRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	AuthorizeLedgerIdentity(ctx context.Context, in *LedgerIdentity_AuthorizeRequest, opts ...grpc.CallOption) (*LedgerIdentity_AuthorizeResponse, error)
	SetSchedule(ctx context.Context, in *v0.SetSchedule_Request, opts ...grpc.CallOption) (*v0.SetSchedule_Response, error)
	SetCron(ctx context.Context, in *v0.SetCron_Request, opts ...grpc.CallOption) (*v0.SetCron_Response, error)
	SetMaxDuration(ctx context.Context, in *v0.SetMaxDuration_Request, opts ...grpc.CallOption) (*v0.SetMaxDuration_Response, error)
	SetRetention(ctx context.Context, in *v0.SetRetention_Request, opts ...grpc.CallOption) (*v0.SetRetention_Response, error)
	ClearSchedule(ctx context.Context, in *v0.ClearSchedule_Request, opts ...grpc.CallOption) (*v0.ClearSchedule_Response, error)
	GetSchedule(ctx context.Context, in *v0.GetSchedule_Request, opts ...grpc.CallOption) (*v0.GetSchedule_Response, error)
	LocatePruningTimestamp(ctx context.Context, in *v0.LocatePruningTimestamp_Request, opts ...grpc.CallOption) (*v0.LocatePruningTimestamp_Response, error)
}

type enterpriseSequencerAdministrationServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewEnterpriseSequencerAdministrationServiceClient(cc grpc.ClientConnInterface) EnterpriseSequencerAdministrationServiceClient {
	return &enterpriseSequencerAdministrationServiceClient{cc}
}

func (c *enterpriseSequencerAdministrationServiceClient) Prune(ctx context.Context, in *Pruning_Request, opts ...grpc.CallOption) (*Pruning_Response, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(Pruning_Response)
	err := c.cc.Invoke(ctx, EnterpriseSequencerAdministrationService_Prune_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) Snapshot(ctx context.Context, in *Snapshot_Request, opts ...grpc.CallOption) (*Snapshot_Response, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(Snapshot_Response)
	err := c.cc.Invoke(ctx, EnterpriseSequencerAdministrationService_Snapshot_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) DisableMember(ctx context.Context, in *DisableMemberRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, EnterpriseSequencerAdministrationService_DisableMember_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) AuthorizeLedgerIdentity(ctx context.Context, in *LedgerIdentity_AuthorizeRequest, opts ...grpc.CallOption) (*LedgerIdentity_AuthorizeResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(LedgerIdentity_AuthorizeResponse)
	err := c.cc.Invoke(ctx, EnterpriseSequencerAdministrationService_AuthorizeLedgerIdentity_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) SetSchedule(ctx context.Context, in *v0.SetSchedule_Request, opts ...grpc.CallOption) (*v0.SetSchedule_Response, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(v0.SetSchedule_Response)
	err := c.cc.Invoke(ctx, EnterpriseSequencerAdministrationService_SetSchedule_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) SetCron(ctx context.Context, in *v0.SetCron_Request, opts ...grpc.CallOption) (*v0.SetCron_Response, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(v0.SetCron_Response)
	err := c.cc.Invoke(ctx, EnterpriseSequencerAdministrationService_SetCron_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) SetMaxDuration(ctx context.Context, in *v0.SetMaxDuration_Request, opts ...grpc.CallOption) (*v0.SetMaxDuration_Response, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(v0.SetMaxDuration_Response)
	err := c.cc.Invoke(ctx, EnterpriseSequencerAdministrationService_SetMaxDuration_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) SetRetention(ctx context.Context, in *v0.SetRetention_Request, opts ...grpc.CallOption) (*v0.SetRetention_Response, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(v0.SetRetention_Response)
	err := c.cc.Invoke(ctx, EnterpriseSequencerAdministrationService_SetRetention_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) ClearSchedule(ctx context.Context, in *v0.ClearSchedule_Request, opts ...grpc.CallOption) (*v0.ClearSchedule_Response, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(v0.ClearSchedule_Response)
	err := c.cc.Invoke(ctx, EnterpriseSequencerAdministrationService_ClearSchedule_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) GetSchedule(ctx context.Context, in *v0.GetSchedule_Request, opts ...grpc.CallOption) (*v0.GetSchedule_Response, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(v0.GetSchedule_Response)
	err := c.cc.Invoke(ctx, EnterpriseSequencerAdministrationService_GetSchedule_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) LocatePruningTimestamp(ctx context.Context, in *v0.LocatePruningTimestamp_Request, opts ...grpc.CallOption) (*v0.LocatePruningTimestamp_Response, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(v0.LocatePruningTimestamp_Response)
	err := c.cc.Invoke(ctx, EnterpriseSequencerAdministrationService_LocatePruningTimestamp_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// EnterpriseSequencerAdministrationServiceServer is the server API for EnterpriseSequencerAdministrationService service.
// All implementations must embed UnimplementedEnterpriseSequencerAdministrationServiceServer
// for forward compatibility.
type EnterpriseSequencerAdministrationServiceServer interface {
	Prune(context.Context, *Pruning_Request) (*Pruning_Response, error)
	Snapshot(context.Context, *Snapshot_Request) (*Snapshot_Response, error)
	DisableMember(context.Context, *DisableMemberRequest) (*emptypb.Empty, error)
	AuthorizeLedgerIdentity(context.Context, *LedgerIdentity_AuthorizeRequest) (*LedgerIdentity_AuthorizeResponse, error)
	SetSchedule(context.Context, *v0.SetSchedule_Request) (*v0.SetSchedule_Response, error)
	SetCron(context.Context, *v0.SetCron_Request) (*v0.SetCron_Response, error)
	SetMaxDuration(context.Context, *v0.SetMaxDuration_Request) (*v0.SetMaxDuration_Response, error)
	SetRetention(context.Context, *v0.SetRetention_Request) (*v0.SetRetention_Response, error)
	ClearSchedule(context.Context, *v0.ClearSchedule_Request) (*v0.ClearSchedule_Response, error)
	GetSchedule(context.Context, *v0.GetSchedule_Request) (*v0.GetSchedule_Response, error)
	LocatePruningTimestamp(context.Context, *v0.LocatePruningTimestamp_Request) (*v0.LocatePruningTimestamp_Response, error)
	mustEmbedUnimplementedEnterpriseSequencerAdministrationServiceServer()
}

// UnimplementedEnterpriseSequencerAdministrationServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedEnterpriseSequencerAdministrationServiceServer struct{}

func (UnimplementedEnterpriseSequencerAdministrationServiceServer) Prune(context.Context, *Pruning_Request) (*Pruning_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Prune not implemented")
}
func (UnimplementedEnterpriseSequencerAdministrationServiceServer) Snapshot(context.Context, *Snapshot_Request) (*Snapshot_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Snapshot not implemented")
}
func (UnimplementedEnterpriseSequencerAdministrationServiceServer) DisableMember(context.Context, *DisableMemberRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DisableMember not implemented")
}
func (UnimplementedEnterpriseSequencerAdministrationServiceServer) AuthorizeLedgerIdentity(context.Context, *LedgerIdentity_AuthorizeRequest) (*LedgerIdentity_AuthorizeResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AuthorizeLedgerIdentity not implemented")
}
func (UnimplementedEnterpriseSequencerAdministrationServiceServer) SetSchedule(context.Context, *v0.SetSchedule_Request) (*v0.SetSchedule_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SetSchedule not implemented")
}
func (UnimplementedEnterpriseSequencerAdministrationServiceServer) SetCron(context.Context, *v0.SetCron_Request) (*v0.SetCron_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SetCron not implemented")
}
func (UnimplementedEnterpriseSequencerAdministrationServiceServer) SetMaxDuration(context.Context, *v0.SetMaxDuration_Request) (*v0.SetMaxDuration_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SetMaxDuration not implemented")
}
func (UnimplementedEnterpriseSequencerAdministrationServiceServer) SetRetention(context.Context, *v0.SetRetention_Request) (*v0.SetRetention_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SetRetention not implemented")
}
func (UnimplementedEnterpriseSequencerAdministrationServiceServer) ClearSchedule(context.Context, *v0.ClearSchedule_Request) (*v0.ClearSchedule_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ClearSchedule not implemented")
}
func (UnimplementedEnterpriseSequencerAdministrationServiceServer) GetSchedule(context.Context, *v0.GetSchedule_Request) (*v0.GetSchedule_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetSchedule not implemented")
}
func (UnimplementedEnterpriseSequencerAdministrationServiceServer) LocatePruningTimestamp(context.Context, *v0.LocatePruningTimestamp_Request) (*v0.LocatePruningTimestamp_Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method LocatePruningTimestamp not implemented")
}
func (UnimplementedEnterpriseSequencerAdministrationServiceServer) mustEmbedUnimplementedEnterpriseSequencerAdministrationServiceServer() {
}
func (UnimplementedEnterpriseSequencerAdministrationServiceServer) testEmbeddedByValue() {}

// UnsafeEnterpriseSequencerAdministrationServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to EnterpriseSequencerAdministrationServiceServer will
// result in compilation errors.
type UnsafeEnterpriseSequencerAdministrationServiceServer interface {
	mustEmbedUnimplementedEnterpriseSequencerAdministrationServiceServer()
}

func RegisterEnterpriseSequencerAdministrationServiceServer(s grpc.ServiceRegistrar, srv EnterpriseSequencerAdministrationServiceServer) {
	// If the following call pancis, it indicates UnimplementedEnterpriseSequencerAdministrationServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&EnterpriseSequencerAdministrationService_ServiceDesc, srv)
}

func _EnterpriseSequencerAdministrationService_Prune_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Pruning_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnterpriseSequencerAdministrationServiceServer).Prune(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EnterpriseSequencerAdministrationService_Prune_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnterpriseSequencerAdministrationServiceServer).Prune(ctx, req.(*Pruning_Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _EnterpriseSequencerAdministrationService_Snapshot_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Snapshot_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnterpriseSequencerAdministrationServiceServer).Snapshot(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EnterpriseSequencerAdministrationService_Snapshot_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnterpriseSequencerAdministrationServiceServer).Snapshot(ctx, req.(*Snapshot_Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _EnterpriseSequencerAdministrationService_DisableMember_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DisableMemberRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnterpriseSequencerAdministrationServiceServer).DisableMember(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EnterpriseSequencerAdministrationService_DisableMember_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnterpriseSequencerAdministrationServiceServer).DisableMember(ctx, req.(*DisableMemberRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _EnterpriseSequencerAdministrationService_AuthorizeLedgerIdentity_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(LedgerIdentity_AuthorizeRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnterpriseSequencerAdministrationServiceServer).AuthorizeLedgerIdentity(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EnterpriseSequencerAdministrationService_AuthorizeLedgerIdentity_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnterpriseSequencerAdministrationServiceServer).AuthorizeLedgerIdentity(ctx, req.(*LedgerIdentity_AuthorizeRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _EnterpriseSequencerAdministrationService_SetSchedule_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v0.SetSchedule_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnterpriseSequencerAdministrationServiceServer).SetSchedule(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EnterpriseSequencerAdministrationService_SetSchedule_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnterpriseSequencerAdministrationServiceServer).SetSchedule(ctx, req.(*v0.SetSchedule_Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _EnterpriseSequencerAdministrationService_SetCron_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v0.SetCron_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnterpriseSequencerAdministrationServiceServer).SetCron(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EnterpriseSequencerAdministrationService_SetCron_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnterpriseSequencerAdministrationServiceServer).SetCron(ctx, req.(*v0.SetCron_Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _EnterpriseSequencerAdministrationService_SetMaxDuration_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v0.SetMaxDuration_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnterpriseSequencerAdministrationServiceServer).SetMaxDuration(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EnterpriseSequencerAdministrationService_SetMaxDuration_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnterpriseSequencerAdministrationServiceServer).SetMaxDuration(ctx, req.(*v0.SetMaxDuration_Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _EnterpriseSequencerAdministrationService_SetRetention_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v0.SetRetention_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnterpriseSequencerAdministrationServiceServer).SetRetention(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EnterpriseSequencerAdministrationService_SetRetention_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnterpriseSequencerAdministrationServiceServer).SetRetention(ctx, req.(*v0.SetRetention_Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _EnterpriseSequencerAdministrationService_ClearSchedule_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v0.ClearSchedule_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnterpriseSequencerAdministrationServiceServer).ClearSchedule(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EnterpriseSequencerAdministrationService_ClearSchedule_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnterpriseSequencerAdministrationServiceServer).ClearSchedule(ctx, req.(*v0.ClearSchedule_Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _EnterpriseSequencerAdministrationService_GetSchedule_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v0.GetSchedule_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnterpriseSequencerAdministrationServiceServer).GetSchedule(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EnterpriseSequencerAdministrationService_GetSchedule_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnterpriseSequencerAdministrationServiceServer).GetSchedule(ctx, req.(*v0.GetSchedule_Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _EnterpriseSequencerAdministrationService_LocatePruningTimestamp_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v0.LocatePruningTimestamp_Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnterpriseSequencerAdministrationServiceServer).LocatePruningTimestamp(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EnterpriseSequencerAdministrationService_LocatePruningTimestamp_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnterpriseSequencerAdministrationServiceServer).LocatePruningTimestamp(ctx, req.(*v0.LocatePruningTimestamp_Request))
	}
	return interceptor(ctx, in, info, handler)
}

// EnterpriseSequencerAdministrationService_ServiceDesc is the grpc.ServiceDesc for EnterpriseSequencerAdministrationService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var EnterpriseSequencerAdministrationService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService",
	HandlerType: (*EnterpriseSequencerAdministrationServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Prune",
			Handler:    _EnterpriseSequencerAdministrationService_Prune_Handler,
		},
		{
			MethodName: "Snapshot",
			Handler:    _EnterpriseSequencerAdministrationService_Snapshot_Handler,
		},
		{
			MethodName: "DisableMember",
			Handler:    _EnterpriseSequencerAdministrationService_DisableMember_Handler,
		},
		{
			MethodName: "AuthorizeLedgerIdentity",
			Handler:    _EnterpriseSequencerAdministrationService_AuthorizeLedgerIdentity_Handler,
		},
		{
			MethodName: "SetSchedule",
			Handler:    _EnterpriseSequencerAdministrationService_SetSchedule_Handler,
		},
		{
			MethodName: "SetCron",
			Handler:    _EnterpriseSequencerAdministrationService_SetCron_Handler,
		},
		{
			MethodName: "SetMaxDuration",
			Handler:    _EnterpriseSequencerAdministrationService_SetMaxDuration_Handler,
		},
		{
			MethodName: "SetRetention",
			Handler:    _EnterpriseSequencerAdministrationService_SetRetention_Handler,
		},
		{
			MethodName: "ClearSchedule",
			Handler:    _EnterpriseSequencerAdministrationService_ClearSchedule_Handler,
		},
		{
			MethodName: "GetSchedule",
			Handler:    _EnterpriseSequencerAdministrationService_GetSchedule_Handler,
		},
		{
			MethodName: "LocatePruningTimestamp",
			Handler:    _EnterpriseSequencerAdministrationService_LocatePruningTimestamp_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/digitalasset/canton/domain/admin/v0/enterprise_sequencer_administration_service.proto",
}
