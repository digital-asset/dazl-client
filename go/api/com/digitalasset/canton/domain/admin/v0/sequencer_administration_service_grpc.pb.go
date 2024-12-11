// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.4.0
// - protoc             v5.27.2
// source: com/digitalasset/canton/domain/admin/v0/sequencer_administration_service.proto

package v0

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.62.0 or later.
const _ = grpc.SupportPackageIsVersion8

const (
	SequencerAdministrationService_PruningStatus_FullMethodName = "/com.digitalasset.canton.domain.admin.v0.SequencerAdministrationService/PruningStatus"
)

// SequencerAdministrationServiceClient is the client API for SequencerAdministrationService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type SequencerAdministrationServiceClient interface {
	PruningStatus(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*SequencerPruningStatus, error)
}

type sequencerAdministrationServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewSequencerAdministrationServiceClient(cc grpc.ClientConnInterface) SequencerAdministrationServiceClient {
	return &sequencerAdministrationServiceClient{cc}
}

func (c *sequencerAdministrationServiceClient) PruningStatus(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*SequencerPruningStatus, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(SequencerPruningStatus)
	err := c.cc.Invoke(ctx, SequencerAdministrationService_PruningStatus_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// SequencerAdministrationServiceServer is the server API for SequencerAdministrationService service.
// All implementations must embed UnimplementedSequencerAdministrationServiceServer
// for forward compatibility
type SequencerAdministrationServiceServer interface {
	PruningStatus(context.Context, *emptypb.Empty) (*SequencerPruningStatus, error)
	mustEmbedUnimplementedSequencerAdministrationServiceServer()
}

// UnimplementedSequencerAdministrationServiceServer must be embedded to have forward compatible implementations.
type UnimplementedSequencerAdministrationServiceServer struct {
}

func (UnimplementedSequencerAdministrationServiceServer) PruningStatus(context.Context, *emptypb.Empty) (*SequencerPruningStatus, error) {
	return nil, status.Errorf(codes.Unimplemented, "method PruningStatus not implemented")
}
func (UnimplementedSequencerAdministrationServiceServer) mustEmbedUnimplementedSequencerAdministrationServiceServer() {
}

// UnsafeSequencerAdministrationServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to SequencerAdministrationServiceServer will
// result in compilation errors.
type UnsafeSequencerAdministrationServiceServer interface {
	mustEmbedUnimplementedSequencerAdministrationServiceServer()
}

func RegisterSequencerAdministrationServiceServer(s grpc.ServiceRegistrar, srv SequencerAdministrationServiceServer) {
	s.RegisterService(&SequencerAdministrationService_ServiceDesc, srv)
}

func _SequencerAdministrationService_PruningStatus_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(emptypb.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SequencerAdministrationServiceServer).PruningStatus(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: SequencerAdministrationService_PruningStatus_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SequencerAdministrationServiceServer).PruningStatus(ctx, req.(*emptypb.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

// SequencerAdministrationService_ServiceDesc is the grpc.ServiceDesc for SequencerAdministrationService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var SequencerAdministrationService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.domain.admin.v0.SequencerAdministrationService",
	HandlerType: (*SequencerAdministrationServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "PruningStatus",
			Handler:    _SequencerAdministrationService_PruningStatus_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/digitalasset/canton/domain/admin/v0/sequencer_administration_service.proto",
}
