// Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v4.24.3
// source: com/digitalasset/canton/domain/admin/v0/enterprise_sequencer_administration_service.proto

package v0

import (
	context "context"
	v0 "github.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/pruning/admin/v0"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// EnterpriseSequencerAdministrationServiceClient is the client API for EnterpriseSequencerAdministrationService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type EnterpriseSequencerAdministrationServiceClient interface {
	// Remove data from the Sequencer
	Prune(ctx context.Context, in *Pruning_Request, opts ...grpc.CallOption) (*Pruning_Response, error)
	// fetch a snapshot of the sequencer state based on the given timestamp
	Snapshot(ctx context.Context, in *Snapshot_Request, opts ...grpc.CallOption) (*Snapshot_Response, error)
	// Disable members at the sequencer. Will prevent existing and new instances from connecting, and permit removing their data.
	DisableMember(ctx context.Context, in *DisableMemberRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	AuthorizeLedgerIdentity(ctx context.Context, in *LedgerIdentity_AuthorizeRequest, opts ...grpc.CallOption) (*LedgerIdentity_AuthorizeResponse, error)
	// Enable automatic pruning using the specified schedule parameters
	// The following errors may occur on the SetSchedule or Update commands:
	// - ``INVALID_ARGUMENT``: if a parameter is missing or an invalid cron expression
	//   or duration.
	// - ``FAILED_PRECONDITION``: if automatic background pruning has not been enabled
	//   or if invoked on a participant running the Community Edition.
	SetSchedule(ctx context.Context, in *v0.SetSchedule_Request, opts ...grpc.CallOption) (*v0.SetSchedule_Response, error)
	// Modify individual pruning schedule parameters.
	// - ``INVALID_ARGUMENT``: if the payload is malformed or no schedule is configured
	SetCron(ctx context.Context, in *v0.SetCron_Request, opts ...grpc.CallOption) (*v0.SetCron_Response, error)
	SetMaxDuration(ctx context.Context, in *v0.SetMaxDuration_Request, opts ...grpc.CallOption) (*v0.SetMaxDuration_Response, error)
	SetRetention(ctx context.Context, in *v0.SetRetention_Request, opts ...grpc.CallOption) (*v0.SetRetention_Response, error)
	// Disable automatic pruning and remove the persisted schedule configuration.
	ClearSchedule(ctx context.Context, in *v0.ClearSchedule_Request, opts ...grpc.CallOption) (*v0.ClearSchedule_Response, error)
	// Retrieve the automatic pruning configuration.
	GetSchedule(ctx context.Context, in *v0.GetSchedule_Request, opts ...grpc.CallOption) (*v0.GetSchedule_Response, error)
	// Retrieve pruning timestamp at or near the "beginning" of events.
	LocatePruningTimestamp(ctx context.Context, in *v0.LocatePruningTimestamp_Request, opts ...grpc.CallOption) (*v0.LocatePruningTimestamp_Response, error)
}

type enterpriseSequencerAdministrationServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewEnterpriseSequencerAdministrationServiceClient(cc grpc.ClientConnInterface) EnterpriseSequencerAdministrationServiceClient {
	return &enterpriseSequencerAdministrationServiceClient{cc}
}

func (c *enterpriseSequencerAdministrationServiceClient) Prune(ctx context.Context, in *Pruning_Request, opts ...grpc.CallOption) (*Pruning_Response, error) {
	out := new(Pruning_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/Prune", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) Snapshot(ctx context.Context, in *Snapshot_Request, opts ...grpc.CallOption) (*Snapshot_Response, error) {
	out := new(Snapshot_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/Snapshot", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) DisableMember(ctx context.Context, in *DisableMemberRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/DisableMember", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) AuthorizeLedgerIdentity(ctx context.Context, in *LedgerIdentity_AuthorizeRequest, opts ...grpc.CallOption) (*LedgerIdentity_AuthorizeResponse, error) {
	out := new(LedgerIdentity_AuthorizeResponse)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/AuthorizeLedgerIdentity", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) SetSchedule(ctx context.Context, in *v0.SetSchedule_Request, opts ...grpc.CallOption) (*v0.SetSchedule_Response, error) {
	out := new(v0.SetSchedule_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetSchedule", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) SetCron(ctx context.Context, in *v0.SetCron_Request, opts ...grpc.CallOption) (*v0.SetCron_Response, error) {
	out := new(v0.SetCron_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetCron", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) SetMaxDuration(ctx context.Context, in *v0.SetMaxDuration_Request, opts ...grpc.CallOption) (*v0.SetMaxDuration_Response, error) {
	out := new(v0.SetMaxDuration_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetMaxDuration", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) SetRetention(ctx context.Context, in *v0.SetRetention_Request, opts ...grpc.CallOption) (*v0.SetRetention_Response, error) {
	out := new(v0.SetRetention_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetRetention", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) ClearSchedule(ctx context.Context, in *v0.ClearSchedule_Request, opts ...grpc.CallOption) (*v0.ClearSchedule_Response, error) {
	out := new(v0.ClearSchedule_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/ClearSchedule", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) GetSchedule(ctx context.Context, in *v0.GetSchedule_Request, opts ...grpc.CallOption) (*v0.GetSchedule_Response, error) {
	out := new(v0.GetSchedule_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/GetSchedule", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enterpriseSequencerAdministrationServiceClient) LocatePruningTimestamp(ctx context.Context, in *v0.LocatePruningTimestamp_Request, opts ...grpc.CallOption) (*v0.LocatePruningTimestamp_Response, error) {
	out := new(v0.LocatePruningTimestamp_Response)
	err := c.cc.Invoke(ctx, "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/LocatePruningTimestamp", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// EnterpriseSequencerAdministrationServiceServer is the server API for EnterpriseSequencerAdministrationService service.
// All implementations must embed UnimplementedEnterpriseSequencerAdministrationServiceServer
// for forward compatibility
type EnterpriseSequencerAdministrationServiceServer interface {
	// Remove data from the Sequencer
	Prune(context.Context, *Pruning_Request) (*Pruning_Response, error)
	// fetch a snapshot of the sequencer state based on the given timestamp
	Snapshot(context.Context, *Snapshot_Request) (*Snapshot_Response, error)
	// Disable members at the sequencer. Will prevent existing and new instances from connecting, and permit removing their data.
	DisableMember(context.Context, *DisableMemberRequest) (*emptypb.Empty, error)
	AuthorizeLedgerIdentity(context.Context, *LedgerIdentity_AuthorizeRequest) (*LedgerIdentity_AuthorizeResponse, error)
	// Enable automatic pruning using the specified schedule parameters
	// The following errors may occur on the SetSchedule or Update commands:
	// - ``INVALID_ARGUMENT``: if a parameter is missing or an invalid cron expression
	//   or duration.
	// - ``FAILED_PRECONDITION``: if automatic background pruning has not been enabled
	//   or if invoked on a participant running the Community Edition.
	SetSchedule(context.Context, *v0.SetSchedule_Request) (*v0.SetSchedule_Response, error)
	// Modify individual pruning schedule parameters.
	// - ``INVALID_ARGUMENT``: if the payload is malformed or no schedule is configured
	SetCron(context.Context, *v0.SetCron_Request) (*v0.SetCron_Response, error)
	SetMaxDuration(context.Context, *v0.SetMaxDuration_Request) (*v0.SetMaxDuration_Response, error)
	SetRetention(context.Context, *v0.SetRetention_Request) (*v0.SetRetention_Response, error)
	// Disable automatic pruning and remove the persisted schedule configuration.
	ClearSchedule(context.Context, *v0.ClearSchedule_Request) (*v0.ClearSchedule_Response, error)
	// Retrieve the automatic pruning configuration.
	GetSchedule(context.Context, *v0.GetSchedule_Request) (*v0.GetSchedule_Response, error)
	// Retrieve pruning timestamp at or near the "beginning" of events.
	LocatePruningTimestamp(context.Context, *v0.LocatePruningTimestamp_Request) (*v0.LocatePruningTimestamp_Response, error)
	mustEmbedUnimplementedEnterpriseSequencerAdministrationServiceServer()
}

// UnimplementedEnterpriseSequencerAdministrationServiceServer must be embedded to have forward compatible implementations.
type UnimplementedEnterpriseSequencerAdministrationServiceServer struct {
}

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

// UnsafeEnterpriseSequencerAdministrationServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to EnterpriseSequencerAdministrationServiceServer will
// result in compilation errors.
type UnsafeEnterpriseSequencerAdministrationServiceServer interface {
	mustEmbedUnimplementedEnterpriseSequencerAdministrationServiceServer()
}

func RegisterEnterpriseSequencerAdministrationServiceServer(s grpc.ServiceRegistrar, srv EnterpriseSequencerAdministrationServiceServer) {
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
		FullMethod: "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/Prune",
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
		FullMethod: "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/Snapshot",
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
		FullMethod: "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/DisableMember",
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
		FullMethod: "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/AuthorizeLedgerIdentity",
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
		FullMethod: "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetSchedule",
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
		FullMethod: "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetCron",
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
		FullMethod: "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetMaxDuration",
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
		FullMethod: "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/SetRetention",
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
		FullMethod: "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/ClearSchedule",
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
		FullMethod: "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/GetSchedule",
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
		FullMethod: "/com.digitalasset.canton.domain.admin.v0.EnterpriseSequencerAdministrationService/LocatePruningTimestamp",
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
