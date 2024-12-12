// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v5.27.2
// source: com/digitalasset/canton/participant/admin/v0/participant_repair_service.proto

package v0

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
	ParticipantRepairService_Download_FullMethodName               = "/com.digitalasset.canton.participant.admin.v0.ParticipantRepairService/Download"
	ParticipantRepairService_ExportAcs_FullMethodName              = "/com.digitalasset.canton.participant.admin.v0.ParticipantRepairService/ExportAcs"
	ParticipantRepairService_Upload_FullMethodName                 = "/com.digitalasset.canton.participant.admin.v0.ParticipantRepairService/Upload"
	ParticipantRepairService_ImportAcs_FullMethodName              = "/com.digitalasset.canton.participant.admin.v0.ParticipantRepairService/ImportAcs"
	ParticipantRepairService_PurgeContracts_FullMethodName         = "/com.digitalasset.canton.participant.admin.v0.ParticipantRepairService/PurgeContracts"
	ParticipantRepairService_MigrateDomain_FullMethodName          = "/com.digitalasset.canton.participant.admin.v0.ParticipantRepairService/MigrateDomain"
	ParticipantRepairService_PurgeDeactivatedDomain_FullMethodName = "/com.digitalasset.canton.participant.admin.v0.ParticipantRepairService/PurgeDeactivatedDomain"
	ParticipantRepairService_IgnoreEvents_FullMethodName           = "/com.digitalasset.canton.participant.admin.v0.ParticipantRepairService/IgnoreEvents"
	ParticipantRepairService_UnignoreEvents_FullMethodName         = "/com.digitalasset.canton.participant.admin.v0.ParticipantRepairService/UnignoreEvents"
)

// ParticipantRepairServiceClient is the client API for ParticipantRepairService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ParticipantRepairServiceClient interface {
	Download(ctx context.Context, in *DownloadRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[AcsSnapshotChunk], error)
	ExportAcs(ctx context.Context, in *ExportAcsRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[ExportAcsResponse], error)
	Upload(ctx context.Context, opts ...grpc.CallOption) (grpc.ClientStreamingClient[UploadRequest, UploadResponse], error)
	ImportAcs(ctx context.Context, opts ...grpc.CallOption) (grpc.ClientStreamingClient[ImportAcsRequest, ImportAcsResponse], error)
	PurgeContracts(ctx context.Context, in *PurgeContractsRequest, opts ...grpc.CallOption) (*PurgeContractsResponse, error)
	MigrateDomain(ctx context.Context, in *MigrateDomainRequest, opts ...grpc.CallOption) (*MigrateDomainResponse, error)
	PurgeDeactivatedDomain(ctx context.Context, in *PurgeDeactivatedDomainRequest, opts ...grpc.CallOption) (*PurgeDeactivatedDomainResponse, error)
	IgnoreEvents(ctx context.Context, in *IgnoreEventsRequest, opts ...grpc.CallOption) (*IgnoreEventsResponse, error)
	UnignoreEvents(ctx context.Context, in *UnignoreEventsRequest, opts ...grpc.CallOption) (*UnignoreEventsResponse, error)
}

type participantRepairServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewParticipantRepairServiceClient(cc grpc.ClientConnInterface) ParticipantRepairServiceClient {
	return &participantRepairServiceClient{cc}
}

func (c *participantRepairServiceClient) Download(ctx context.Context, in *DownloadRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[AcsSnapshotChunk], error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	stream, err := c.cc.NewStream(ctx, &ParticipantRepairService_ServiceDesc.Streams[0], ParticipantRepairService_Download_FullMethodName, cOpts...)
	if err != nil {
		return nil, err
	}
	x := &grpc.GenericClientStream[DownloadRequest, AcsSnapshotChunk]{ClientStream: stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type ParticipantRepairService_DownloadClient = grpc.ServerStreamingClient[AcsSnapshotChunk]

func (c *participantRepairServiceClient) ExportAcs(ctx context.Context, in *ExportAcsRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[ExportAcsResponse], error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	stream, err := c.cc.NewStream(ctx, &ParticipantRepairService_ServiceDesc.Streams[1], ParticipantRepairService_ExportAcs_FullMethodName, cOpts...)
	if err != nil {
		return nil, err
	}
	x := &grpc.GenericClientStream[ExportAcsRequest, ExportAcsResponse]{ClientStream: stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type ParticipantRepairService_ExportAcsClient = grpc.ServerStreamingClient[ExportAcsResponse]

func (c *participantRepairServiceClient) Upload(ctx context.Context, opts ...grpc.CallOption) (grpc.ClientStreamingClient[UploadRequest, UploadResponse], error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	stream, err := c.cc.NewStream(ctx, &ParticipantRepairService_ServiceDesc.Streams[2], ParticipantRepairService_Upload_FullMethodName, cOpts...)
	if err != nil {
		return nil, err
	}
	x := &grpc.GenericClientStream[UploadRequest, UploadResponse]{ClientStream: stream}
	return x, nil
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type ParticipantRepairService_UploadClient = grpc.ClientStreamingClient[UploadRequest, UploadResponse]

func (c *participantRepairServiceClient) ImportAcs(ctx context.Context, opts ...grpc.CallOption) (grpc.ClientStreamingClient[ImportAcsRequest, ImportAcsResponse], error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	stream, err := c.cc.NewStream(ctx, &ParticipantRepairService_ServiceDesc.Streams[3], ParticipantRepairService_ImportAcs_FullMethodName, cOpts...)
	if err != nil {
		return nil, err
	}
	x := &grpc.GenericClientStream[ImportAcsRequest, ImportAcsResponse]{ClientStream: stream}
	return x, nil
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type ParticipantRepairService_ImportAcsClient = grpc.ClientStreamingClient[ImportAcsRequest, ImportAcsResponse]

func (c *participantRepairServiceClient) PurgeContracts(ctx context.Context, in *PurgeContractsRequest, opts ...grpc.CallOption) (*PurgeContractsResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(PurgeContractsResponse)
	err := c.cc.Invoke(ctx, ParticipantRepairService_PurgeContracts_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *participantRepairServiceClient) MigrateDomain(ctx context.Context, in *MigrateDomainRequest, opts ...grpc.CallOption) (*MigrateDomainResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(MigrateDomainResponse)
	err := c.cc.Invoke(ctx, ParticipantRepairService_MigrateDomain_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *participantRepairServiceClient) PurgeDeactivatedDomain(ctx context.Context, in *PurgeDeactivatedDomainRequest, opts ...grpc.CallOption) (*PurgeDeactivatedDomainResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(PurgeDeactivatedDomainResponse)
	err := c.cc.Invoke(ctx, ParticipantRepairService_PurgeDeactivatedDomain_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *participantRepairServiceClient) IgnoreEvents(ctx context.Context, in *IgnoreEventsRequest, opts ...grpc.CallOption) (*IgnoreEventsResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(IgnoreEventsResponse)
	err := c.cc.Invoke(ctx, ParticipantRepairService_IgnoreEvents_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *participantRepairServiceClient) UnignoreEvents(ctx context.Context, in *UnignoreEventsRequest, opts ...grpc.CallOption) (*UnignoreEventsResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(UnignoreEventsResponse)
	err := c.cc.Invoke(ctx, ParticipantRepairService_UnignoreEvents_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ParticipantRepairServiceServer is the server API for ParticipantRepairService service.
// All implementations must embed UnimplementedParticipantRepairServiceServer
// for forward compatibility.
type ParticipantRepairServiceServer interface {
	Download(*DownloadRequest, grpc.ServerStreamingServer[AcsSnapshotChunk]) error
	ExportAcs(*ExportAcsRequest, grpc.ServerStreamingServer[ExportAcsResponse]) error
	Upload(grpc.ClientStreamingServer[UploadRequest, UploadResponse]) error
	ImportAcs(grpc.ClientStreamingServer[ImportAcsRequest, ImportAcsResponse]) error
	PurgeContracts(context.Context, *PurgeContractsRequest) (*PurgeContractsResponse, error)
	MigrateDomain(context.Context, *MigrateDomainRequest) (*MigrateDomainResponse, error)
	PurgeDeactivatedDomain(context.Context, *PurgeDeactivatedDomainRequest) (*PurgeDeactivatedDomainResponse, error)
	IgnoreEvents(context.Context, *IgnoreEventsRequest) (*IgnoreEventsResponse, error)
	UnignoreEvents(context.Context, *UnignoreEventsRequest) (*UnignoreEventsResponse, error)
	mustEmbedUnimplementedParticipantRepairServiceServer()
}

// UnimplementedParticipantRepairServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedParticipantRepairServiceServer struct{}

func (UnimplementedParticipantRepairServiceServer) Download(*DownloadRequest, grpc.ServerStreamingServer[AcsSnapshotChunk]) error {
	return status.Errorf(codes.Unimplemented, "method Download not implemented")
}
func (UnimplementedParticipantRepairServiceServer) ExportAcs(*ExportAcsRequest, grpc.ServerStreamingServer[ExportAcsResponse]) error {
	return status.Errorf(codes.Unimplemented, "method ExportAcs not implemented")
}
func (UnimplementedParticipantRepairServiceServer) Upload(grpc.ClientStreamingServer[UploadRequest, UploadResponse]) error {
	return status.Errorf(codes.Unimplemented, "method Upload not implemented")
}
func (UnimplementedParticipantRepairServiceServer) ImportAcs(grpc.ClientStreamingServer[ImportAcsRequest, ImportAcsResponse]) error {
	return status.Errorf(codes.Unimplemented, "method ImportAcs not implemented")
}
func (UnimplementedParticipantRepairServiceServer) PurgeContracts(context.Context, *PurgeContractsRequest) (*PurgeContractsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method PurgeContracts not implemented")
}
func (UnimplementedParticipantRepairServiceServer) MigrateDomain(context.Context, *MigrateDomainRequest) (*MigrateDomainResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method MigrateDomain not implemented")
}
func (UnimplementedParticipantRepairServiceServer) PurgeDeactivatedDomain(context.Context, *PurgeDeactivatedDomainRequest) (*PurgeDeactivatedDomainResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method PurgeDeactivatedDomain not implemented")
}
func (UnimplementedParticipantRepairServiceServer) IgnoreEvents(context.Context, *IgnoreEventsRequest) (*IgnoreEventsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method IgnoreEvents not implemented")
}
func (UnimplementedParticipantRepairServiceServer) UnignoreEvents(context.Context, *UnignoreEventsRequest) (*UnignoreEventsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UnignoreEvents not implemented")
}
func (UnimplementedParticipantRepairServiceServer) mustEmbedUnimplementedParticipantRepairServiceServer() {
}
func (UnimplementedParticipantRepairServiceServer) testEmbeddedByValue() {}

// UnsafeParticipantRepairServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ParticipantRepairServiceServer will
// result in compilation errors.
type UnsafeParticipantRepairServiceServer interface {
	mustEmbedUnimplementedParticipantRepairServiceServer()
}

func RegisterParticipantRepairServiceServer(s grpc.ServiceRegistrar, srv ParticipantRepairServiceServer) {
	// If the following call pancis, it indicates UnimplementedParticipantRepairServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&ParticipantRepairService_ServiceDesc, srv)
}

func _ParticipantRepairService_Download_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(DownloadRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(ParticipantRepairServiceServer).Download(m, &grpc.GenericServerStream[DownloadRequest, AcsSnapshotChunk]{ServerStream: stream})
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type ParticipantRepairService_DownloadServer = grpc.ServerStreamingServer[AcsSnapshotChunk]

func _ParticipantRepairService_ExportAcs_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(ExportAcsRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(ParticipantRepairServiceServer).ExportAcs(m, &grpc.GenericServerStream[ExportAcsRequest, ExportAcsResponse]{ServerStream: stream})
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type ParticipantRepairService_ExportAcsServer = grpc.ServerStreamingServer[ExportAcsResponse]

func _ParticipantRepairService_Upload_Handler(srv interface{}, stream grpc.ServerStream) error {
	return srv.(ParticipantRepairServiceServer).Upload(&grpc.GenericServerStream[UploadRequest, UploadResponse]{ServerStream: stream})
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type ParticipantRepairService_UploadServer = grpc.ClientStreamingServer[UploadRequest, UploadResponse]

func _ParticipantRepairService_ImportAcs_Handler(srv interface{}, stream grpc.ServerStream) error {
	return srv.(ParticipantRepairServiceServer).ImportAcs(&grpc.GenericServerStream[ImportAcsRequest, ImportAcsResponse]{ServerStream: stream})
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type ParticipantRepairService_ImportAcsServer = grpc.ClientStreamingServer[ImportAcsRequest, ImportAcsResponse]

func _ParticipantRepairService_PurgeContracts_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PurgeContractsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ParticipantRepairServiceServer).PurgeContracts(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ParticipantRepairService_PurgeContracts_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ParticipantRepairServiceServer).PurgeContracts(ctx, req.(*PurgeContractsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ParticipantRepairService_MigrateDomain_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(MigrateDomainRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ParticipantRepairServiceServer).MigrateDomain(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ParticipantRepairService_MigrateDomain_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ParticipantRepairServiceServer).MigrateDomain(ctx, req.(*MigrateDomainRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ParticipantRepairService_PurgeDeactivatedDomain_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PurgeDeactivatedDomainRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ParticipantRepairServiceServer).PurgeDeactivatedDomain(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ParticipantRepairService_PurgeDeactivatedDomain_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ParticipantRepairServiceServer).PurgeDeactivatedDomain(ctx, req.(*PurgeDeactivatedDomainRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ParticipantRepairService_IgnoreEvents_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(IgnoreEventsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ParticipantRepairServiceServer).IgnoreEvents(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ParticipantRepairService_IgnoreEvents_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ParticipantRepairServiceServer).IgnoreEvents(ctx, req.(*IgnoreEventsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ParticipantRepairService_UnignoreEvents_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UnignoreEventsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ParticipantRepairServiceServer).UnignoreEvents(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ParticipantRepairService_UnignoreEvents_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ParticipantRepairServiceServer).UnignoreEvents(ctx, req.(*UnignoreEventsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// ParticipantRepairService_ServiceDesc is the grpc.ServiceDesc for ParticipantRepairService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var ParticipantRepairService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.digitalasset.canton.participant.admin.v0.ParticipantRepairService",
	HandlerType: (*ParticipantRepairServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "PurgeContracts",
			Handler:    _ParticipantRepairService_PurgeContracts_Handler,
		},
		{
			MethodName: "MigrateDomain",
			Handler:    _ParticipantRepairService_MigrateDomain_Handler,
		},
		{
			MethodName: "PurgeDeactivatedDomain",
			Handler:    _ParticipantRepairService_PurgeDeactivatedDomain_Handler,
		},
		{
			MethodName: "IgnoreEvents",
			Handler:    _ParticipantRepairService_IgnoreEvents_Handler,
		},
		{
			MethodName: "UnignoreEvents",
			Handler:    _ParticipantRepairService_UnignoreEvents_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "Download",
			Handler:       _ParticipantRepairService_Download_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "ExportAcs",
			Handler:       _ParticipantRepairService_ExportAcs_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "Upload",
			Handler:       _ParticipantRepairService_Upload_Handler,
			ClientStreams: true,
		},
		{
			StreamName:    "ImportAcs",
			Handler:       _ParticipantRepairService_ImportAcs_Handler,
			ClientStreams: true,
		},
	},
	Metadata: "com/digitalasset/canton/participant/admin/v0/participant_repair_service.proto",
}
