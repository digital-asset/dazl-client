// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/daml/ledger/api/v2/command_submission_service.proto

package v2

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type SubmitRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Commands *Commands `protobuf:"bytes,1,opt,name=commands,proto3" json:"commands,omitempty"`
}

func (x *SubmitRequest) Reset() {
	*x = SubmitRequest{}
	mi := &file_com_daml_ledger_api_v2_command_submission_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SubmitRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SubmitRequest) ProtoMessage() {}

func (x *SubmitRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_command_submission_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SubmitRequest.ProtoReflect.Descriptor instead.
func (*SubmitRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_command_submission_service_proto_rawDescGZIP(), []int{0}
}

func (x *SubmitRequest) GetCommands() *Commands {
	if x != nil {
		return x.Commands
	}
	return nil
}

type SubmitResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *SubmitResponse) Reset() {
	*x = SubmitResponse{}
	mi := &file_com_daml_ledger_api_v2_command_submission_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SubmitResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SubmitResponse) ProtoMessage() {}

func (x *SubmitResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_command_submission_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SubmitResponse.ProtoReflect.Descriptor instead.
func (*SubmitResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_command_submission_service_proto_rawDescGZIP(), []int{1}
}

type SubmitReassignmentRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ReassignmentCommand *ReassignmentCommand `protobuf:"bytes,1,opt,name=reassignment_command,json=reassignmentCommand,proto3" json:"reassignment_command,omitempty"`
}

func (x *SubmitReassignmentRequest) Reset() {
	*x = SubmitReassignmentRequest{}
	mi := &file_com_daml_ledger_api_v2_command_submission_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SubmitReassignmentRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SubmitReassignmentRequest) ProtoMessage() {}

func (x *SubmitReassignmentRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_command_submission_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SubmitReassignmentRequest.ProtoReflect.Descriptor instead.
func (*SubmitReassignmentRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_command_submission_service_proto_rawDescGZIP(), []int{2}
}

func (x *SubmitReassignmentRequest) GetReassignmentCommand() *ReassignmentCommand {
	if x != nil {
		return x.ReassignmentCommand
	}
	return nil
}

type SubmitReassignmentResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *SubmitReassignmentResponse) Reset() {
	*x = SubmitReassignmentResponse{}
	mi := &file_com_daml_ledger_api_v2_command_submission_service_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SubmitReassignmentResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SubmitReassignmentResponse) ProtoMessage() {}

func (x *SubmitReassignmentResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_command_submission_service_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SubmitReassignmentResponse.ProtoReflect.Descriptor instead.
func (*SubmitReassignmentResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_command_submission_service_proto_rawDescGZIP(), []int{3}
}

var File_com_daml_ledger_api_v2_command_submission_service_proto protoreflect.FileDescriptor

var file_com_daml_ledger_api_v2_command_submission_service_proto_rawDesc = []byte{
	0x0a, 0x37, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x32, 0x2f, 0x63, 0x6f, 0x6d, 0x6d, 0x61, 0x6e, 0x64,
	0x5f, 0x73, 0x75, 0x62, 0x6d, 0x69, 0x73, 0x73, 0x69, 0x6f, 0x6e, 0x5f, 0x73, 0x65, 0x72, 0x76,
	0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76,
	0x32, 0x1a, 0x25, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x32, 0x2f, 0x63, 0x6f, 0x6d, 0x6d, 0x61, 0x6e,
	0x64, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x31, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61,
	0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x32,
	0x2f, 0x72, 0x65, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x6d, 0x65, 0x6e, 0x74, 0x5f, 0x63, 0x6f,
	0x6d, 0x6d, 0x61, 0x6e, 0x64, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x4d, 0x0a, 0x0d, 0x53,
	0x75, 0x62, 0x6d, 0x69, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x3c, 0x0a, 0x08,
	0x63, 0x6f, 0x6d, 0x6d, 0x61, 0x6e, 0x64, 0x73, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x20,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x43, 0x6f, 0x6d, 0x6d, 0x61, 0x6e, 0x64, 0x73,
	0x52, 0x08, 0x63, 0x6f, 0x6d, 0x6d, 0x61, 0x6e, 0x64, 0x73, 0x22, 0x10, 0x0a, 0x0e, 0x53, 0x75,
	0x62, 0x6d, 0x69, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x7b, 0x0a, 0x19,
	0x53, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x52, 0x65, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x6d, 0x65,
	0x6e, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x5e, 0x0a, 0x14, 0x72, 0x65, 0x61,
	0x73, 0x73, 0x69, 0x67, 0x6e, 0x6d, 0x65, 0x6e, 0x74, 0x5f, 0x63, 0x6f, 0x6d, 0x6d, 0x61, 0x6e,
	0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2b, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61,
	0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32,
	0x2e, 0x52, 0x65, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x6d, 0x65, 0x6e, 0x74, 0x43, 0x6f, 0x6d,
	0x6d, 0x61, 0x6e, 0x64, 0x52, 0x13, 0x72, 0x65, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x6d, 0x65,
	0x6e, 0x74, 0x43, 0x6f, 0x6d, 0x6d, 0x61, 0x6e, 0x64, 0x22, 0x1c, 0x0a, 0x1a, 0x53, 0x75, 0x62,
	0x6d, 0x69, 0x74, 0x52, 0x65, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x6d, 0x65, 0x6e, 0x74, 0x52,
	0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x32, 0xf0, 0x01, 0x0a, 0x18, 0x43, 0x6f, 0x6d, 0x6d,
	0x61, 0x6e, 0x64, 0x53, 0x75, 0x62, 0x6d, 0x69, 0x73, 0x73, 0x69, 0x6f, 0x6e, 0x53, 0x65, 0x72,
	0x76, 0x69, 0x63, 0x65, 0x12, 0x57, 0x0a, 0x06, 0x53, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x12, 0x25,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x53, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x52, 0x65,
	0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x26, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c,
	0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x53,
	0x75, 0x62, 0x6d, 0x69, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x7b, 0x0a,
	0x12, 0x53, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x52, 0x65, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x6d,
	0x65, 0x6e, 0x74, 0x12, 0x31, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c,
	0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x53, 0x75, 0x62,
	0x6d, 0x69, 0x74, 0x52, 0x65, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x6d, 0x65, 0x6e, 0x74, 0x52,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x32, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d,
	0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e,
	0x53, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x52, 0x65, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x6d, 0x65,
	0x6e, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x42, 0x9c, 0x01, 0x0a, 0x16, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61,
	0x70, 0x69, 0x2e, 0x76, 0x32, 0x42, 0x22, 0x43, 0x6f, 0x6d, 0x6d, 0x61, 0x6e, 0x64, 0x53, 0x75,
	0x62, 0x6d, 0x69, 0x73, 0x73, 0x69, 0x6f, 0x6e, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x4f,
	0x75, 0x74, 0x65, 0x72, 0x43, 0x6c, 0x61, 0x73, 0x73, 0x5a, 0x45, 0x67, 0x69, 0x74, 0x68, 0x75,
	0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73,
	0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f,
	0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61,
	0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x32,
	0xaa, 0x02, 0x16, 0x43, 0x6f, 0x6d, 0x2e, 0x44, 0x61, 0x6d, 0x6c, 0x2e, 0x4c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x2e, 0x41, 0x70, 0x69, 0x2e, 0x56, 0x32, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x33,
}

var (
	file_com_daml_ledger_api_v2_command_submission_service_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v2_command_submission_service_proto_rawDescData = file_com_daml_ledger_api_v2_command_submission_service_proto_rawDesc
)

func file_com_daml_ledger_api_v2_command_submission_service_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v2_command_submission_service_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v2_command_submission_service_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_ledger_api_v2_command_submission_service_proto_rawDescData)
	})
	return file_com_daml_ledger_api_v2_command_submission_service_proto_rawDescData
}

var file_com_daml_ledger_api_v2_command_submission_service_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_com_daml_ledger_api_v2_command_submission_service_proto_goTypes = []any{
	(*SubmitRequest)(nil),              // 0: com.daml.ledger.api.v2.SubmitRequest
	(*SubmitResponse)(nil),             // 1: com.daml.ledger.api.v2.SubmitResponse
	(*SubmitReassignmentRequest)(nil),  // 2: com.daml.ledger.api.v2.SubmitReassignmentRequest
	(*SubmitReassignmentResponse)(nil), // 3: com.daml.ledger.api.v2.SubmitReassignmentResponse
	(*Commands)(nil),                   // 4: com.daml.ledger.api.v2.Commands
	(*ReassignmentCommand)(nil),        // 5: com.daml.ledger.api.v2.ReassignmentCommand
}
var file_com_daml_ledger_api_v2_command_submission_service_proto_depIdxs = []int32{
	4, // 0: com.daml.ledger.api.v2.SubmitRequest.commands:type_name -> com.daml.ledger.api.v2.Commands
	5, // 1: com.daml.ledger.api.v2.SubmitReassignmentRequest.reassignment_command:type_name -> com.daml.ledger.api.v2.ReassignmentCommand
	0, // 2: com.daml.ledger.api.v2.CommandSubmissionService.Submit:input_type -> com.daml.ledger.api.v2.SubmitRequest
	2, // 3: com.daml.ledger.api.v2.CommandSubmissionService.SubmitReassignment:input_type -> com.daml.ledger.api.v2.SubmitReassignmentRequest
	1, // 4: com.daml.ledger.api.v2.CommandSubmissionService.Submit:output_type -> com.daml.ledger.api.v2.SubmitResponse
	3, // 5: com.daml.ledger.api.v2.CommandSubmissionService.SubmitReassignment:output_type -> com.daml.ledger.api.v2.SubmitReassignmentResponse
	4, // [4:6] is the sub-list for method output_type
	2, // [2:4] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v2_command_submission_service_proto_init() }
func file_com_daml_ledger_api_v2_command_submission_service_proto_init() {
	if File_com_daml_ledger_api_v2_command_submission_service_proto != nil {
		return
	}
	file_com_daml_ledger_api_v2_commands_proto_init()
	file_com_daml_ledger_api_v2_reassignment_command_proto_init()
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_daml_ledger_api_v2_command_submission_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_daml_ledger_api_v2_command_submission_service_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v2_command_submission_service_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v2_command_submission_service_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v2_command_submission_service_proto = out.File
	file_com_daml_ledger_api_v2_command_submission_service_proto_rawDesc = nil
	file_com_daml_ledger_api_v2_command_submission_service_proto_goTypes = nil
	file_com_daml_ledger_api_v2_command_submission_service_proto_depIdxs = nil
}
