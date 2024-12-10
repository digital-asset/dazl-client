// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.4.0
// - protoc             v5.27.2
// source: com/daml/ledger/api/v2/admin/participant_pruning_service.proto

package admin

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
	ParticipantPruningService_Prune_FullMethodName = "/com.daml.ledger.api.v2.admin.ParticipantPruningService/Prune"
)

// ParticipantPruningServiceClient is the client API for ParticipantPruningService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ParticipantPruningServiceClient interface {
	Prune(ctx context.Context, in *PruneRequest, opts ...grpc.CallOption) (*PruneResponse, error)
}

type participantPruningServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewParticipantPruningServiceClient(cc grpc.ClientConnInterface) ParticipantPruningServiceClient {
	return &participantPruningServiceClient{cc}
}

func (c *participantPruningServiceClient) Prune(ctx context.Context, in *PruneRequest, opts ...grpc.CallOption) (*PruneResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(PruneResponse)
	err := c.cc.Invoke(ctx, ParticipantPruningService_Prune_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ParticipantPruningServiceServer is the server API for ParticipantPruningService service.
// All implementations must embed UnimplementedParticipantPruningServiceServer
// for forward compatibility
type ParticipantPruningServiceServer interface {
	Prune(context.Context, *PruneRequest) (*PruneResponse, error)
	mustEmbedUnimplementedParticipantPruningServiceServer()
}

// UnimplementedParticipantPruningServiceServer must be embedded to have forward compatible implementations.
type UnimplementedParticipantPruningServiceServer struct {
}

func (UnimplementedParticipantPruningServiceServer) Prune(context.Context, *PruneRequest) (*PruneResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Prune not implemented")
}
func (UnimplementedParticipantPruningServiceServer) mustEmbedUnimplementedParticipantPruningServiceServer() {
}

// UnsafeParticipantPruningServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ParticipantPruningServiceServer will
// result in compilation errors.
type UnsafeParticipantPruningServiceServer interface {
	mustEmbedUnimplementedParticipantPruningServiceServer()
}

func RegisterParticipantPruningServiceServer(s grpc.ServiceRegistrar, srv ParticipantPruningServiceServer) {
	s.RegisterService(&ParticipantPruningService_ServiceDesc, srv)
}

func _ParticipantPruningService_Prune_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PruneRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ParticipantPruningServiceServer).Prune(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ParticipantPruningService_Prune_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ParticipantPruningServiceServer).Prune(ctx, req.(*PruneRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// ParticipantPruningService_ServiceDesc is the grpc.ServiceDesc for ParticipantPruningService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var ParticipantPruningService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.daml.ledger.api.v2.admin.ParticipantPruningService",
	HandlerType: (*ParticipantPruningServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Prune",
			Handler:    _ParticipantPruningService_Prune_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/daml/ledger/api/v2/admin/participant_pruning_service.proto",
}