// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/admin/participant/v30/enterprise_participant_replication_service.proto

package v30

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
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

type SetPassiveRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SetPassiveRequest) Reset() {
	*x = SetPassiveRequest{}
	mi := &file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SetPassiveRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SetPassiveRequest) ProtoMessage() {}

func (x *SetPassiveRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SetPassiveRequest.ProtoReflect.Descriptor instead.
func (*SetPassiveRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_rawDescGZIP(), []int{0}
}

type SetPassiveResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SetPassiveResponse) Reset() {
	*x = SetPassiveResponse{}
	mi := &file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SetPassiveResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SetPassiveResponse) ProtoMessage() {}

func (x *SetPassiveResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SetPassiveResponse.ProtoReflect.Descriptor instead.
func (*SetPassiveResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_rawDescGZIP(), []int{1}
}

var File_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto protoreflect.FileDescriptor

const file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_rawDesc = "" +
	"\n" +
	"^com/digitalasset/canton/admin/participant/v30/enterprise_participant_replication_service.proto\x12-com.digitalasset.canton.admin.participant.v30\"\x13\n" +
	"\x11SetPassiveRequest\"\x14\n" +
	"\x12SetPassiveResponse2\xbd\x01\n" +
	"'EnterpriseParticipantReplicationService\x12\x91\x01\n" +
	"\n" +
	"SetPassive\x12@.com.digitalasset.canton.admin.participant.v30.SetPassiveRequest\x1aA.com.digitalasset.canton.admin.participant.v30.SetPassiveResponseB^Z\\github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/admin/participant/v30b\x06proto3"

var (
	file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_rawDescData []byte
)

func file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_rawDesc), len(file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_rawDesc)))
	})
	return file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_rawDescData
}

var file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_goTypes = []any{
	(*SetPassiveRequest)(nil),  // 0: com.digitalasset.canton.admin.participant.v30.SetPassiveRequest
	(*SetPassiveResponse)(nil), // 1: com.digitalasset.canton.admin.participant.v30.SetPassiveResponse
}
var file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_depIdxs = []int32{
	0, // 0: com.digitalasset.canton.admin.participant.v30.EnterpriseParticipantReplicationService.SetPassive:input_type -> com.digitalasset.canton.admin.participant.v30.SetPassiveRequest
	1, // 1: com.digitalasset.canton.admin.participant.v30.EnterpriseParticipantReplicationService.SetPassive:output_type -> com.digitalasset.canton.admin.participant.v30.SetPassiveResponse
	1, // [1:2] is the sub-list for method output_type
	0, // [0:1] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() {
	file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_init()
}
func file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_init() {
	if File_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_rawDesc), len(file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto = out.File
	file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_goTypes = nil
	file_com_digitalasset_canton_admin_participant_v30_enterprise_participant_replication_service_proto_depIdxs = nil
}
