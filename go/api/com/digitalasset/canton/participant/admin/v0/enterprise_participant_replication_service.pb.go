// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/digitalasset/canton/participant/admin/v0/enterprise_participant_replication_service.proto

package v0

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

type SetPassive struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *SetPassive) Reset() {
	*x = SetPassive{}
	mi := &file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SetPassive) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SetPassive) ProtoMessage() {}

func (x *SetPassive) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SetPassive.ProtoReflect.Descriptor instead.
func (*SetPassive) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_rawDescGZIP(), []int{0}
}

type SetPassive_Request struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *SetPassive_Request) Reset() {
	*x = SetPassive_Request{}
	mi := &file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SetPassive_Request) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SetPassive_Request) ProtoMessage() {}

func (x *SetPassive_Request) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SetPassive_Request.ProtoReflect.Descriptor instead.
func (*SetPassive_Request) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_rawDescGZIP(), []int{0, 0}
}

type SetPassive_Response struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *SetPassive_Response) Reset() {
	*x = SetPassive_Response{}
	mi := &file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SetPassive_Response) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SetPassive_Response) ProtoMessage() {}

func (x *SetPassive_Response) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SetPassive_Response.ProtoReflect.Descriptor instead.
func (*SetPassive_Response) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_rawDescGZIP(), []int{0, 1}
}

var File_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_rawDesc = []byte{
	0x0a, 0x5d, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63,
	0x69, 0x70, 0x61, 0x6e, 0x74, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x76, 0x30, 0x2f, 0x65,
	0x6e, 0x74, 0x65, 0x72, 0x70, 0x72, 0x69, 0x73, 0x65, 0x5f, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63,
	0x69, 0x70, 0x61, 0x6e, 0x74, 0x5f, 0x72, 0x65, 0x70, 0x6c, 0x69, 0x63, 0x61, 0x74, 0x69, 0x6f,
	0x6e, 0x5f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12,
	0x2c, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65,
	0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69,
	0x70, 0x61, 0x6e, 0x74, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x22, 0x23, 0x0a,
	0x0a, 0x53, 0x65, 0x74, 0x50, 0x61, 0x73, 0x73, 0x69, 0x76, 0x65, 0x1a, 0x09, 0x0a, 0x07, 0x52,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x0a, 0x0a, 0x08, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e,
	0x73, 0x65, 0x32, 0xbd, 0x01, 0x0a, 0x27, 0x45, 0x6e, 0x74, 0x65, 0x72, 0x70, 0x72, 0x69, 0x73,
	0x65, 0x50, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x52, 0x65, 0x70, 0x6c,
	0x69, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x91,
	0x01, 0x0a, 0x0a, 0x53, 0x65, 0x74, 0x50, 0x61, 0x73, 0x73, 0x69, 0x76, 0x65, 0x12, 0x40, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70,
	0x61, 0x6e, 0x74, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x65, 0x74,
	0x50, 0x61, 0x73, 0x73, 0x69, 0x76, 0x65, 0x2e, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a,
	0x41, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63,
	0x69, 0x70, 0x61, 0x6e, 0x74, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x53,
	0x65, 0x74, 0x50, 0x61, 0x73, 0x73, 0x69, 0x76, 0x65, 0x2e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e,
	0x73, 0x65, 0x42, 0x5d, 0x5a, 0x5b, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d,
	0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64,
	0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f,
	0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c,
	0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x61, 0x72,
	0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x76,
	0x30, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_rawDescData = file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_rawDesc
)

func file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_rawDescData)
	})
	return file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_rawDescData
}

var file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_goTypes = []any{
	(*SetPassive)(nil),          // 0: com.digitalasset.canton.participant.admin.v0.SetPassive
	(*SetPassive_Request)(nil),  // 1: com.digitalasset.canton.participant.admin.v0.SetPassive.Request
	(*SetPassive_Response)(nil), // 2: com.digitalasset.canton.participant.admin.v0.SetPassive.Response
}
var file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_depIdxs = []int32{
	1, // 0: com.digitalasset.canton.participant.admin.v0.EnterpriseParticipantReplicationService.SetPassive:input_type -> com.digitalasset.canton.participant.admin.v0.SetPassive.Request
	2, // 1: com.digitalasset.canton.participant.admin.v0.EnterpriseParticipantReplicationService.SetPassive:output_type -> com.digitalasset.canton.participant.admin.v0.SetPassive.Response
	1, // [1:2] is the sub-list for method output_type
	0, // [0:1] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() {
	file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_init()
}
func file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_init() {
	if File_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto = out.File
	file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_rawDesc = nil
	file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_goTypes = nil
	file_com_digitalasset_canton_participant_admin_v0_enterprise_participant_replication_service_proto_depIdxs = nil
}
