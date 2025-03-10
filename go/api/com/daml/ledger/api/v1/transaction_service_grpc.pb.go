// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v5.27.2
// source: com/daml/ledger/api/v1/transaction_service.proto

package v1

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
	TransactionService_GetTransactions_FullMethodName             = "/com.daml.ledger.api.v1.TransactionService/GetTransactions"
	TransactionService_GetTransactionTrees_FullMethodName         = "/com.daml.ledger.api.v1.TransactionService/GetTransactionTrees"
	TransactionService_GetTransactionByEventId_FullMethodName     = "/com.daml.ledger.api.v1.TransactionService/GetTransactionByEventId"
	TransactionService_GetTransactionById_FullMethodName          = "/com.daml.ledger.api.v1.TransactionService/GetTransactionById"
	TransactionService_GetFlatTransactionByEventId_FullMethodName = "/com.daml.ledger.api.v1.TransactionService/GetFlatTransactionByEventId"
	TransactionService_GetFlatTransactionById_FullMethodName      = "/com.daml.ledger.api.v1.TransactionService/GetFlatTransactionById"
	TransactionService_GetLedgerEnd_FullMethodName                = "/com.daml.ledger.api.v1.TransactionService/GetLedgerEnd"
	TransactionService_GetLatestPrunedOffsets_FullMethodName      = "/com.daml.ledger.api.v1.TransactionService/GetLatestPrunedOffsets"
)

// TransactionServiceClient is the client API for TransactionService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type TransactionServiceClient interface {
	GetTransactions(ctx context.Context, in *GetTransactionsRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[GetTransactionsResponse], error)
	GetTransactionTrees(ctx context.Context, in *GetTransactionsRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[GetTransactionTreesResponse], error)
	GetTransactionByEventId(ctx context.Context, in *GetTransactionByEventIdRequest, opts ...grpc.CallOption) (*GetTransactionResponse, error)
	GetTransactionById(ctx context.Context, in *GetTransactionByIdRequest, opts ...grpc.CallOption) (*GetTransactionResponse, error)
	GetFlatTransactionByEventId(ctx context.Context, in *GetTransactionByEventIdRequest, opts ...grpc.CallOption) (*GetFlatTransactionResponse, error)
	GetFlatTransactionById(ctx context.Context, in *GetTransactionByIdRequest, opts ...grpc.CallOption) (*GetFlatTransactionResponse, error)
	GetLedgerEnd(ctx context.Context, in *GetLedgerEndRequest, opts ...grpc.CallOption) (*GetLedgerEndResponse, error)
	GetLatestPrunedOffsets(ctx context.Context, in *GetLatestPrunedOffsetsRequest, opts ...grpc.CallOption) (*GetLatestPrunedOffsetsResponse, error)
}

type transactionServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewTransactionServiceClient(cc grpc.ClientConnInterface) TransactionServiceClient {
	return &transactionServiceClient{cc}
}

func (c *transactionServiceClient) GetTransactions(ctx context.Context, in *GetTransactionsRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[GetTransactionsResponse], error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	stream, err := c.cc.NewStream(ctx, &TransactionService_ServiceDesc.Streams[0], TransactionService_GetTransactions_FullMethodName, cOpts...)
	if err != nil {
		return nil, err
	}
	x := &grpc.GenericClientStream[GetTransactionsRequest, GetTransactionsResponse]{ClientStream: stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type TransactionService_GetTransactionsClient = grpc.ServerStreamingClient[GetTransactionsResponse]

func (c *transactionServiceClient) GetTransactionTrees(ctx context.Context, in *GetTransactionsRequest, opts ...grpc.CallOption) (grpc.ServerStreamingClient[GetTransactionTreesResponse], error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	stream, err := c.cc.NewStream(ctx, &TransactionService_ServiceDesc.Streams[1], TransactionService_GetTransactionTrees_FullMethodName, cOpts...)
	if err != nil {
		return nil, err
	}
	x := &grpc.GenericClientStream[GetTransactionsRequest, GetTransactionTreesResponse]{ClientStream: stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type TransactionService_GetTransactionTreesClient = grpc.ServerStreamingClient[GetTransactionTreesResponse]

func (c *transactionServiceClient) GetTransactionByEventId(ctx context.Context, in *GetTransactionByEventIdRequest, opts ...grpc.CallOption) (*GetTransactionResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GetTransactionResponse)
	err := c.cc.Invoke(ctx, TransactionService_GetTransactionByEventId_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transactionServiceClient) GetTransactionById(ctx context.Context, in *GetTransactionByIdRequest, opts ...grpc.CallOption) (*GetTransactionResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GetTransactionResponse)
	err := c.cc.Invoke(ctx, TransactionService_GetTransactionById_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transactionServiceClient) GetFlatTransactionByEventId(ctx context.Context, in *GetTransactionByEventIdRequest, opts ...grpc.CallOption) (*GetFlatTransactionResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GetFlatTransactionResponse)
	err := c.cc.Invoke(ctx, TransactionService_GetFlatTransactionByEventId_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transactionServiceClient) GetFlatTransactionById(ctx context.Context, in *GetTransactionByIdRequest, opts ...grpc.CallOption) (*GetFlatTransactionResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GetFlatTransactionResponse)
	err := c.cc.Invoke(ctx, TransactionService_GetFlatTransactionById_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transactionServiceClient) GetLedgerEnd(ctx context.Context, in *GetLedgerEndRequest, opts ...grpc.CallOption) (*GetLedgerEndResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GetLedgerEndResponse)
	err := c.cc.Invoke(ctx, TransactionService_GetLedgerEnd_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transactionServiceClient) GetLatestPrunedOffsets(ctx context.Context, in *GetLatestPrunedOffsetsRequest, opts ...grpc.CallOption) (*GetLatestPrunedOffsetsResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(GetLatestPrunedOffsetsResponse)
	err := c.cc.Invoke(ctx, TransactionService_GetLatestPrunedOffsets_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// TransactionServiceServer is the server API for TransactionService service.
// All implementations must embed UnimplementedTransactionServiceServer
// for forward compatibility.
type TransactionServiceServer interface {
	GetTransactions(*GetTransactionsRequest, grpc.ServerStreamingServer[GetTransactionsResponse]) error
	GetTransactionTrees(*GetTransactionsRequest, grpc.ServerStreamingServer[GetTransactionTreesResponse]) error
	GetTransactionByEventId(context.Context, *GetTransactionByEventIdRequest) (*GetTransactionResponse, error)
	GetTransactionById(context.Context, *GetTransactionByIdRequest) (*GetTransactionResponse, error)
	GetFlatTransactionByEventId(context.Context, *GetTransactionByEventIdRequest) (*GetFlatTransactionResponse, error)
	GetFlatTransactionById(context.Context, *GetTransactionByIdRequest) (*GetFlatTransactionResponse, error)
	GetLedgerEnd(context.Context, *GetLedgerEndRequest) (*GetLedgerEndResponse, error)
	GetLatestPrunedOffsets(context.Context, *GetLatestPrunedOffsetsRequest) (*GetLatestPrunedOffsetsResponse, error)
	mustEmbedUnimplementedTransactionServiceServer()
}

// UnimplementedTransactionServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedTransactionServiceServer struct{}

func (UnimplementedTransactionServiceServer) GetTransactions(*GetTransactionsRequest, grpc.ServerStreamingServer[GetTransactionsResponse]) error {
	return status.Errorf(codes.Unimplemented, "method GetTransactions not implemented")
}
func (UnimplementedTransactionServiceServer) GetTransactionTrees(*GetTransactionsRequest, grpc.ServerStreamingServer[GetTransactionTreesResponse]) error {
	return status.Errorf(codes.Unimplemented, "method GetTransactionTrees not implemented")
}
func (UnimplementedTransactionServiceServer) GetTransactionByEventId(context.Context, *GetTransactionByEventIdRequest) (*GetTransactionResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetTransactionByEventId not implemented")
}
func (UnimplementedTransactionServiceServer) GetTransactionById(context.Context, *GetTransactionByIdRequest) (*GetTransactionResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetTransactionById not implemented")
}
func (UnimplementedTransactionServiceServer) GetFlatTransactionByEventId(context.Context, *GetTransactionByEventIdRequest) (*GetFlatTransactionResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetFlatTransactionByEventId not implemented")
}
func (UnimplementedTransactionServiceServer) GetFlatTransactionById(context.Context, *GetTransactionByIdRequest) (*GetFlatTransactionResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetFlatTransactionById not implemented")
}
func (UnimplementedTransactionServiceServer) GetLedgerEnd(context.Context, *GetLedgerEndRequest) (*GetLedgerEndResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetLedgerEnd not implemented")
}
func (UnimplementedTransactionServiceServer) GetLatestPrunedOffsets(context.Context, *GetLatestPrunedOffsetsRequest) (*GetLatestPrunedOffsetsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetLatestPrunedOffsets not implemented")
}
func (UnimplementedTransactionServiceServer) mustEmbedUnimplementedTransactionServiceServer() {}
func (UnimplementedTransactionServiceServer) testEmbeddedByValue()                            {}

// UnsafeTransactionServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to TransactionServiceServer will
// result in compilation errors.
type UnsafeTransactionServiceServer interface {
	mustEmbedUnimplementedTransactionServiceServer()
}

func RegisterTransactionServiceServer(s grpc.ServiceRegistrar, srv TransactionServiceServer) {
	// If the following call pancis, it indicates UnimplementedTransactionServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&TransactionService_ServiceDesc, srv)
}

func _TransactionService_GetTransactions_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(GetTransactionsRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(TransactionServiceServer).GetTransactions(m, &grpc.GenericServerStream[GetTransactionsRequest, GetTransactionsResponse]{ServerStream: stream})
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type TransactionService_GetTransactionsServer = grpc.ServerStreamingServer[GetTransactionsResponse]

func _TransactionService_GetTransactionTrees_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(GetTransactionsRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(TransactionServiceServer).GetTransactionTrees(m, &grpc.GenericServerStream[GetTransactionsRequest, GetTransactionTreesResponse]{ServerStream: stream})
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type TransactionService_GetTransactionTreesServer = grpc.ServerStreamingServer[GetTransactionTreesResponse]

func _TransactionService_GetTransactionByEventId_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetTransactionByEventIdRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransactionServiceServer).GetTransactionByEventId(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: TransactionService_GetTransactionByEventId_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransactionServiceServer).GetTransactionByEventId(ctx, req.(*GetTransactionByEventIdRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TransactionService_GetTransactionById_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetTransactionByIdRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransactionServiceServer).GetTransactionById(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: TransactionService_GetTransactionById_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransactionServiceServer).GetTransactionById(ctx, req.(*GetTransactionByIdRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TransactionService_GetFlatTransactionByEventId_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetTransactionByEventIdRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransactionServiceServer).GetFlatTransactionByEventId(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: TransactionService_GetFlatTransactionByEventId_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransactionServiceServer).GetFlatTransactionByEventId(ctx, req.(*GetTransactionByEventIdRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TransactionService_GetFlatTransactionById_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetTransactionByIdRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransactionServiceServer).GetFlatTransactionById(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: TransactionService_GetFlatTransactionById_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransactionServiceServer).GetFlatTransactionById(ctx, req.(*GetTransactionByIdRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TransactionService_GetLedgerEnd_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetLedgerEndRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransactionServiceServer).GetLedgerEnd(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: TransactionService_GetLedgerEnd_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransactionServiceServer).GetLedgerEnd(ctx, req.(*GetLedgerEndRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _TransactionService_GetLatestPrunedOffsets_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetLatestPrunedOffsetsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransactionServiceServer).GetLatestPrunedOffsets(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: TransactionService_GetLatestPrunedOffsets_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransactionServiceServer).GetLatestPrunedOffsets(ctx, req.(*GetLatestPrunedOffsetsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// TransactionService_ServiceDesc is the grpc.ServiceDesc for TransactionService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var TransactionService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.daml.ledger.api.v1.TransactionService",
	HandlerType: (*TransactionServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetTransactionByEventId",
			Handler:    _TransactionService_GetTransactionByEventId_Handler,
		},
		{
			MethodName: "GetTransactionById",
			Handler:    _TransactionService_GetTransactionById_Handler,
		},
		{
			MethodName: "GetFlatTransactionByEventId",
			Handler:    _TransactionService_GetFlatTransactionByEventId_Handler,
		},
		{
			MethodName: "GetFlatTransactionById",
			Handler:    _TransactionService_GetFlatTransactionById_Handler,
		},
		{
			MethodName: "GetLedgerEnd",
			Handler:    _TransactionService_GetLedgerEnd_Handler,
		},
		{
			MethodName: "GetLatestPrunedOffsets",
			Handler:    _TransactionService_GetLatestPrunedOffsets_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "GetTransactions",
			Handler:       _TransactionService_GetTransactions_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "GetTransactionTrees",
			Handler:       _TransactionService_GetTransactionTrees_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "com/daml/ledger/api/v1/transaction_service.proto",
}
