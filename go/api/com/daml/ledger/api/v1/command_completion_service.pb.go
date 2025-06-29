// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/daml/ledger/api/v1/command_completion_service.proto

package v1

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	timestamppb "google.golang.org/protobuf/types/known/timestamppb"
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

type CompletionStreamRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	LedgerId      string                 `protobuf:"bytes,1,opt,name=ledger_id,json=ledgerId,proto3" json:"ledger_id,omitempty"`
	ApplicationId string                 `protobuf:"bytes,2,opt,name=application_id,json=applicationId,proto3" json:"application_id,omitempty"`
	Parties       []string               `protobuf:"bytes,3,rep,name=parties,proto3" json:"parties,omitempty"`
	Offset        *LedgerOffset          `protobuf:"bytes,4,opt,name=offset,proto3" json:"offset,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CompletionStreamRequest) Reset() {
	*x = CompletionStreamRequest{}
	mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CompletionStreamRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CompletionStreamRequest) ProtoMessage() {}

func (x *CompletionStreamRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CompletionStreamRequest.ProtoReflect.Descriptor instead.
func (*CompletionStreamRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescGZIP(), []int{0}
}

func (x *CompletionStreamRequest) GetLedgerId() string {
	if x != nil {
		return x.LedgerId
	}
	return ""
}

func (x *CompletionStreamRequest) GetApplicationId() string {
	if x != nil {
		return x.ApplicationId
	}
	return ""
}

func (x *CompletionStreamRequest) GetParties() []string {
	if x != nil {
		return x.Parties
	}
	return nil
}

func (x *CompletionStreamRequest) GetOffset() *LedgerOffset {
	if x != nil {
		return x.Offset
	}
	return nil
}

type CompletionStreamResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Checkpoint    *Checkpoint            `protobuf:"bytes,1,opt,name=checkpoint,proto3" json:"checkpoint,omitempty"`
	Completions   []*Completion          `protobuf:"bytes,2,rep,name=completions,proto3" json:"completions,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CompletionStreamResponse) Reset() {
	*x = CompletionStreamResponse{}
	mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CompletionStreamResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CompletionStreamResponse) ProtoMessage() {}

func (x *CompletionStreamResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CompletionStreamResponse.ProtoReflect.Descriptor instead.
func (*CompletionStreamResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescGZIP(), []int{1}
}

func (x *CompletionStreamResponse) GetCheckpoint() *Checkpoint {
	if x != nil {
		return x.Checkpoint
	}
	return nil
}

func (x *CompletionStreamResponse) GetCompletions() []*Completion {
	if x != nil {
		return x.Completions
	}
	return nil
}

type Checkpoint struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	RecordTime    *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=record_time,json=recordTime,proto3" json:"record_time,omitempty"`
	Offset        *LedgerOffset          `protobuf:"bytes,2,opt,name=offset,proto3" json:"offset,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *Checkpoint) Reset() {
	*x = Checkpoint{}
	mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Checkpoint) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Checkpoint) ProtoMessage() {}

func (x *Checkpoint) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Checkpoint.ProtoReflect.Descriptor instead.
func (*Checkpoint) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescGZIP(), []int{2}
}

func (x *Checkpoint) GetRecordTime() *timestamppb.Timestamp {
	if x != nil {
		return x.RecordTime
	}
	return nil
}

func (x *Checkpoint) GetOffset() *LedgerOffset {
	if x != nil {
		return x.Offset
	}
	return nil
}

type CompletionEndRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	LedgerId      string                 `protobuf:"bytes,1,opt,name=ledger_id,json=ledgerId,proto3" json:"ledger_id,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CompletionEndRequest) Reset() {
	*x = CompletionEndRequest{}
	mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CompletionEndRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CompletionEndRequest) ProtoMessage() {}

func (x *CompletionEndRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CompletionEndRequest.ProtoReflect.Descriptor instead.
func (*CompletionEndRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescGZIP(), []int{3}
}

func (x *CompletionEndRequest) GetLedgerId() string {
	if x != nil {
		return x.LedgerId
	}
	return ""
}

type CompletionEndResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Offset        *LedgerOffset          `protobuf:"bytes,1,opt,name=offset,proto3" json:"offset,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CompletionEndResponse) Reset() {
	*x = CompletionEndResponse{}
	mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CompletionEndResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CompletionEndResponse) ProtoMessage() {}

func (x *CompletionEndResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CompletionEndResponse.ProtoReflect.Descriptor instead.
func (*CompletionEndResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescGZIP(), []int{4}
}

func (x *CompletionEndResponse) GetOffset() *LedgerOffset {
	if x != nil {
		return x.Offset
	}
	return nil
}

var File_com_daml_ledger_api_v1_command_completion_service_proto protoreflect.FileDescriptor

const file_com_daml_ledger_api_v1_command_completion_service_proto_rawDesc = "" +
	"\n" +
	"7com/daml/ledger/api/v1/command_completion_service.proto\x12\x16com.daml.ledger.api.v1\x1a'com/daml/ledger/api/v1/completion.proto\x1a*com/daml/ledger/api/v1/ledger_offset.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb5\x01\n" +
	"\x17CompletionStreamRequest\x12\x1b\n" +
	"\tledger_id\x18\x01 \x01(\tR\bledgerId\x12%\n" +
	"\x0eapplication_id\x18\x02 \x01(\tR\rapplicationId\x12\x18\n" +
	"\aparties\x18\x03 \x03(\tR\aparties\x12<\n" +
	"\x06offset\x18\x04 \x01(\v2$.com.daml.ledger.api.v1.LedgerOffsetR\x06offset\"\xa4\x01\n" +
	"\x18CompletionStreamResponse\x12B\n" +
	"\n" +
	"checkpoint\x18\x01 \x01(\v2\".com.daml.ledger.api.v1.CheckpointR\n" +
	"checkpoint\x12D\n" +
	"\vcompletions\x18\x02 \x03(\v2\".com.daml.ledger.api.v1.CompletionR\vcompletions\"\x87\x01\n" +
	"\n" +
	"Checkpoint\x12;\n" +
	"\vrecord_time\x18\x01 \x01(\v2\x1a.google.protobuf.TimestampR\n" +
	"recordTime\x12<\n" +
	"\x06offset\x18\x02 \x01(\v2$.com.daml.ledger.api.v1.LedgerOffsetR\x06offset\"3\n" +
	"\x14CompletionEndRequest\x12\x1b\n" +
	"\tledger_id\x18\x01 \x01(\tR\bledgerId\"U\n" +
	"\x15CompletionEndResponse\x12<\n" +
	"\x06offset\x18\x01 \x01(\v2$.com.daml.ledger.api.v1.LedgerOffsetR\x06offset2\x81\x02\n" +
	"\x18CommandCompletionService\x12w\n" +
	"\x10CompletionStream\x12/.com.daml.ledger.api.v1.CompletionStreamRequest\x1a0.com.daml.ledger.api.v1.CompletionStreamResponse0\x01\x12l\n" +
	"\rCompletionEnd\x12,.com.daml.ledger.api.v1.CompletionEndRequest\x1a-.com.daml.ledger.api.v1.CompletionEndResponseB\x9c\x01\n" +
	"\x16com.daml.ledger.api.v1B\"CommandCompletionServiceOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v1\xaa\x02\x16Com.Daml.Ledger.Api.V1b\x06proto3"

var (
	file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescData []byte
)

func file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_daml_ledger_api_v1_command_completion_service_proto_rawDesc), len(file_com_daml_ledger_api_v1_command_completion_service_proto_rawDesc)))
	})
	return file_com_daml_ledger_api_v1_command_completion_service_proto_rawDescData
}

var file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes = make([]protoimpl.MessageInfo, 5)
var file_com_daml_ledger_api_v1_command_completion_service_proto_goTypes = []any{
	(*CompletionStreamRequest)(nil),  // 0: com.daml.ledger.api.v1.CompletionStreamRequest
	(*CompletionStreamResponse)(nil), // 1: com.daml.ledger.api.v1.CompletionStreamResponse
	(*Checkpoint)(nil),               // 2: com.daml.ledger.api.v1.Checkpoint
	(*CompletionEndRequest)(nil),     // 3: com.daml.ledger.api.v1.CompletionEndRequest
	(*CompletionEndResponse)(nil),    // 4: com.daml.ledger.api.v1.CompletionEndResponse
	(*LedgerOffset)(nil),             // 5: com.daml.ledger.api.v1.LedgerOffset
	(*Completion)(nil),               // 6: com.daml.ledger.api.v1.Completion
	(*timestamppb.Timestamp)(nil),    // 7: google.protobuf.Timestamp
}
var file_com_daml_ledger_api_v1_command_completion_service_proto_depIdxs = []int32{
	5, // 0: com.daml.ledger.api.v1.CompletionStreamRequest.offset:type_name -> com.daml.ledger.api.v1.LedgerOffset
	2, // 1: com.daml.ledger.api.v1.CompletionStreamResponse.checkpoint:type_name -> com.daml.ledger.api.v1.Checkpoint
	6, // 2: com.daml.ledger.api.v1.CompletionStreamResponse.completions:type_name -> com.daml.ledger.api.v1.Completion
	7, // 3: com.daml.ledger.api.v1.Checkpoint.record_time:type_name -> google.protobuf.Timestamp
	5, // 4: com.daml.ledger.api.v1.Checkpoint.offset:type_name -> com.daml.ledger.api.v1.LedgerOffset
	5, // 5: com.daml.ledger.api.v1.CompletionEndResponse.offset:type_name -> com.daml.ledger.api.v1.LedgerOffset
	0, // 6: com.daml.ledger.api.v1.CommandCompletionService.CompletionStream:input_type -> com.daml.ledger.api.v1.CompletionStreamRequest
	3, // 7: com.daml.ledger.api.v1.CommandCompletionService.CompletionEnd:input_type -> com.daml.ledger.api.v1.CompletionEndRequest
	1, // 8: com.daml.ledger.api.v1.CommandCompletionService.CompletionStream:output_type -> com.daml.ledger.api.v1.CompletionStreamResponse
	4, // 9: com.daml.ledger.api.v1.CommandCompletionService.CompletionEnd:output_type -> com.daml.ledger.api.v1.CompletionEndResponse
	8, // [8:10] is the sub-list for method output_type
	6, // [6:8] is the sub-list for method input_type
	6, // [6:6] is the sub-list for extension type_name
	6, // [6:6] is the sub-list for extension extendee
	0, // [0:6] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v1_command_completion_service_proto_init() }
func file_com_daml_ledger_api_v1_command_completion_service_proto_init() {
	if File_com_daml_ledger_api_v1_command_completion_service_proto != nil {
		return
	}
	file_com_daml_ledger_api_v1_completion_proto_init()
	file_com_daml_ledger_api_v1_ledger_offset_proto_init()
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_daml_ledger_api_v1_command_completion_service_proto_rawDesc), len(file_com_daml_ledger_api_v1_command_completion_service_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   5,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_daml_ledger_api_v1_command_completion_service_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v1_command_completion_service_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v1_command_completion_service_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v1_command_completion_service_proto = out.File
	file_com_daml_ledger_api_v1_command_completion_service_proto_goTypes = nil
	file_com_daml_ledger_api_v1_command_completion_service_proto_depIdxs = nil
}
