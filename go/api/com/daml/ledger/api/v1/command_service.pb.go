// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/daml/ledger/api/v1/command_service.proto

package v1

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
	reflect "reflect"
	sync "sync"
	unsafe "unsafe"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type SubmitAndWaitRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Commands      *Commands              `protobuf:"bytes,1,opt,name=commands,proto3" json:"commands,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SubmitAndWaitRequest) Reset() {
	*x = SubmitAndWaitRequest{}
	mi := &file_com_daml_ledger_api_v1_command_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SubmitAndWaitRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SubmitAndWaitRequest) ProtoMessage() {}

func (x *SubmitAndWaitRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_command_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SubmitAndWaitRequest.ProtoReflect.Descriptor instead.
func (*SubmitAndWaitRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_command_service_proto_rawDescGZIP(), []int{0}
}

func (x *SubmitAndWaitRequest) GetCommands() *Commands {
	if x != nil {
		return x.Commands
	}
	return nil
}

type SubmitAndWaitForTransactionIdResponse struct {
	state            protoimpl.MessageState `protogen:"open.v1"`
	TransactionId    string                 `protobuf:"bytes,1,opt,name=transaction_id,json=transactionId,proto3" json:"transaction_id,omitempty"`
	CompletionOffset string                 `protobuf:"bytes,2,opt,name=completion_offset,json=completionOffset,proto3" json:"completion_offset,omitempty"`
	unknownFields    protoimpl.UnknownFields
	sizeCache        protoimpl.SizeCache
}

func (x *SubmitAndWaitForTransactionIdResponse) Reset() {
	*x = SubmitAndWaitForTransactionIdResponse{}
	mi := &file_com_daml_ledger_api_v1_command_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SubmitAndWaitForTransactionIdResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SubmitAndWaitForTransactionIdResponse) ProtoMessage() {}

func (x *SubmitAndWaitForTransactionIdResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_command_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SubmitAndWaitForTransactionIdResponse.ProtoReflect.Descriptor instead.
func (*SubmitAndWaitForTransactionIdResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_command_service_proto_rawDescGZIP(), []int{1}
}

func (x *SubmitAndWaitForTransactionIdResponse) GetTransactionId() string {
	if x != nil {
		return x.TransactionId
	}
	return ""
}

func (x *SubmitAndWaitForTransactionIdResponse) GetCompletionOffset() string {
	if x != nil {
		return x.CompletionOffset
	}
	return ""
}

type SubmitAndWaitForTransactionResponse struct {
	state            protoimpl.MessageState `protogen:"open.v1"`
	Transaction      *Transaction           `protobuf:"bytes,1,opt,name=transaction,proto3" json:"transaction,omitempty"`
	CompletionOffset string                 `protobuf:"bytes,2,opt,name=completion_offset,json=completionOffset,proto3" json:"completion_offset,omitempty"`
	unknownFields    protoimpl.UnknownFields
	sizeCache        protoimpl.SizeCache
}

func (x *SubmitAndWaitForTransactionResponse) Reset() {
	*x = SubmitAndWaitForTransactionResponse{}
	mi := &file_com_daml_ledger_api_v1_command_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SubmitAndWaitForTransactionResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SubmitAndWaitForTransactionResponse) ProtoMessage() {}

func (x *SubmitAndWaitForTransactionResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_command_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SubmitAndWaitForTransactionResponse.ProtoReflect.Descriptor instead.
func (*SubmitAndWaitForTransactionResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_command_service_proto_rawDescGZIP(), []int{2}
}

func (x *SubmitAndWaitForTransactionResponse) GetTransaction() *Transaction {
	if x != nil {
		return x.Transaction
	}
	return nil
}

func (x *SubmitAndWaitForTransactionResponse) GetCompletionOffset() string {
	if x != nil {
		return x.CompletionOffset
	}
	return ""
}

type SubmitAndWaitForTransactionTreeResponse struct {
	state            protoimpl.MessageState `protogen:"open.v1"`
	Transaction      *TransactionTree       `protobuf:"bytes,1,opt,name=transaction,proto3" json:"transaction,omitempty"`
	CompletionOffset string                 `protobuf:"bytes,2,opt,name=completion_offset,json=completionOffset,proto3" json:"completion_offset,omitempty"`
	unknownFields    protoimpl.UnknownFields
	sizeCache        protoimpl.SizeCache
}

func (x *SubmitAndWaitForTransactionTreeResponse) Reset() {
	*x = SubmitAndWaitForTransactionTreeResponse{}
	mi := &file_com_daml_ledger_api_v1_command_service_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SubmitAndWaitForTransactionTreeResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SubmitAndWaitForTransactionTreeResponse) ProtoMessage() {}

func (x *SubmitAndWaitForTransactionTreeResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_command_service_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SubmitAndWaitForTransactionTreeResponse.ProtoReflect.Descriptor instead.
func (*SubmitAndWaitForTransactionTreeResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_command_service_proto_rawDescGZIP(), []int{3}
}

func (x *SubmitAndWaitForTransactionTreeResponse) GetTransaction() *TransactionTree {
	if x != nil {
		return x.Transaction
	}
	return nil
}

func (x *SubmitAndWaitForTransactionTreeResponse) GetCompletionOffset() string {
	if x != nil {
		return x.CompletionOffset
	}
	return ""
}

var File_com_daml_ledger_api_v1_command_service_proto protoreflect.FileDescriptor

const file_com_daml_ledger_api_v1_command_service_proto_rawDesc = "" +
	"\n" +
	",com/daml/ledger/api/v1/command_service.proto\x12\x16com.daml.ledger.api.v1\x1a%com/daml/ledger/api/v1/commands.proto\x1a(com/daml/ledger/api/v1/transaction.proto\x1a\x1bgoogle/protobuf/empty.proto\"T\n" +
	"\x14SubmitAndWaitRequest\x12<\n" +
	"\bcommands\x18\x01 \x01(\v2 .com.daml.ledger.api.v1.CommandsR\bcommands\"{\n" +
	"%SubmitAndWaitForTransactionIdResponse\x12%\n" +
	"\x0etransaction_id\x18\x01 \x01(\tR\rtransactionId\x12+\n" +
	"\x11completion_offset\x18\x02 \x01(\tR\x10completionOffset\"\x99\x01\n" +
	"#SubmitAndWaitForTransactionResponse\x12E\n" +
	"\vtransaction\x18\x01 \x01(\v2#.com.daml.ledger.api.v1.TransactionR\vtransaction\x12+\n" +
	"\x11completion_offset\x18\x02 \x01(\tR\x10completionOffset\"\xa1\x01\n" +
	"'SubmitAndWaitForTransactionTreeResponse\x12I\n" +
	"\vtransaction\x18\x01 \x01(\v2'.com.daml.ledger.api.v1.TransactionTreeR\vtransaction\x12+\n" +
	"\x11completion_offset\x18\x02 \x01(\tR\x10completionOffset2\x94\x04\n" +
	"\x0eCommandService\x12U\n" +
	"\rSubmitAndWait\x12,.com.daml.ledger.api.v1.SubmitAndWaitRequest\x1a\x16.google.protobuf.Empty\x12\x8c\x01\n" +
	"\x1dSubmitAndWaitForTransactionId\x12,.com.daml.ledger.api.v1.SubmitAndWaitRequest\x1a=.com.daml.ledger.api.v1.SubmitAndWaitForTransactionIdResponse\x12\x88\x01\n" +
	"\x1bSubmitAndWaitForTransaction\x12,.com.daml.ledger.api.v1.SubmitAndWaitRequest\x1a;.com.daml.ledger.api.v1.SubmitAndWaitForTransactionResponse\x12\x90\x01\n" +
	"\x1fSubmitAndWaitForTransactionTree\x12,.com.daml.ledger.api.v1.SubmitAndWaitRequest\x1a?.com.daml.ledger.api.v1.SubmitAndWaitForTransactionTreeResponseB\x92\x01\n" +
	"\x16com.daml.ledger.api.v1B\x18CommandServiceOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v1\xaa\x02\x16Com.Daml.Ledger.Api.V1b\x06proto3"

var (
	file_com_daml_ledger_api_v1_command_service_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v1_command_service_proto_rawDescData []byte
)

func file_com_daml_ledger_api_v1_command_service_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v1_command_service_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v1_command_service_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_daml_ledger_api_v1_command_service_proto_rawDesc), len(file_com_daml_ledger_api_v1_command_service_proto_rawDesc)))
	})
	return file_com_daml_ledger_api_v1_command_service_proto_rawDescData
}

var file_com_daml_ledger_api_v1_command_service_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_com_daml_ledger_api_v1_command_service_proto_goTypes = []any{
	(*SubmitAndWaitRequest)(nil),                    // 0: com.daml.ledger.api.v1.SubmitAndWaitRequest
	(*SubmitAndWaitForTransactionIdResponse)(nil),   // 1: com.daml.ledger.api.v1.SubmitAndWaitForTransactionIdResponse
	(*SubmitAndWaitForTransactionResponse)(nil),     // 2: com.daml.ledger.api.v1.SubmitAndWaitForTransactionResponse
	(*SubmitAndWaitForTransactionTreeResponse)(nil), // 3: com.daml.ledger.api.v1.SubmitAndWaitForTransactionTreeResponse
	(*Commands)(nil),                                // 4: com.daml.ledger.api.v1.Commands
	(*Transaction)(nil),                             // 5: com.daml.ledger.api.v1.Transaction
	(*TransactionTree)(nil),                         // 6: com.daml.ledger.api.v1.TransactionTree
	(*emptypb.Empty)(nil),                           // 7: google.protobuf.Empty
}
var file_com_daml_ledger_api_v1_command_service_proto_depIdxs = []int32{
	4, // 0: com.daml.ledger.api.v1.SubmitAndWaitRequest.commands:type_name -> com.daml.ledger.api.v1.Commands
	5, // 1: com.daml.ledger.api.v1.SubmitAndWaitForTransactionResponse.transaction:type_name -> com.daml.ledger.api.v1.Transaction
	6, // 2: com.daml.ledger.api.v1.SubmitAndWaitForTransactionTreeResponse.transaction:type_name -> com.daml.ledger.api.v1.TransactionTree
	0, // 3: com.daml.ledger.api.v1.CommandService.SubmitAndWait:input_type -> com.daml.ledger.api.v1.SubmitAndWaitRequest
	0, // 4: com.daml.ledger.api.v1.CommandService.SubmitAndWaitForTransactionId:input_type -> com.daml.ledger.api.v1.SubmitAndWaitRequest
	0, // 5: com.daml.ledger.api.v1.CommandService.SubmitAndWaitForTransaction:input_type -> com.daml.ledger.api.v1.SubmitAndWaitRequest
	0, // 6: com.daml.ledger.api.v1.CommandService.SubmitAndWaitForTransactionTree:input_type -> com.daml.ledger.api.v1.SubmitAndWaitRequest
	7, // 7: com.daml.ledger.api.v1.CommandService.SubmitAndWait:output_type -> google.protobuf.Empty
	1, // 8: com.daml.ledger.api.v1.CommandService.SubmitAndWaitForTransactionId:output_type -> com.daml.ledger.api.v1.SubmitAndWaitForTransactionIdResponse
	2, // 9: com.daml.ledger.api.v1.CommandService.SubmitAndWaitForTransaction:output_type -> com.daml.ledger.api.v1.SubmitAndWaitForTransactionResponse
	3, // 10: com.daml.ledger.api.v1.CommandService.SubmitAndWaitForTransactionTree:output_type -> com.daml.ledger.api.v1.SubmitAndWaitForTransactionTreeResponse
	7, // [7:11] is the sub-list for method output_type
	3, // [3:7] is the sub-list for method input_type
	3, // [3:3] is the sub-list for extension type_name
	3, // [3:3] is the sub-list for extension extendee
	0, // [0:3] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v1_command_service_proto_init() }
func file_com_daml_ledger_api_v1_command_service_proto_init() {
	if File_com_daml_ledger_api_v1_command_service_proto != nil {
		return
	}
	file_com_daml_ledger_api_v1_commands_proto_init()
	file_com_daml_ledger_api_v1_transaction_proto_init()
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_daml_ledger_api_v1_command_service_proto_rawDesc), len(file_com_daml_ledger_api_v1_command_service_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_daml_ledger_api_v1_command_service_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v1_command_service_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v1_command_service_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v1_command_service_proto = out.File
	file_com_daml_ledger_api_v1_command_service_proto_goTypes = nil
	file_com_daml_ledger_api_v1_command_service_proto_depIdxs = nil
}
