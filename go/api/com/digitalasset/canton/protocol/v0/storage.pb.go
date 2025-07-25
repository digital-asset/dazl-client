// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/protocol/v0/storage.proto

package v0

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

type StoredParties struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Parties       []string               `protobuf:"bytes,1,rep,name=parties,proto3" json:"parties,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *StoredParties) Reset() {
	*x = StoredParties{}
	mi := &file_com_digitalasset_canton_protocol_v0_storage_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *StoredParties) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*StoredParties) ProtoMessage() {}

func (x *StoredParties) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_storage_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use StoredParties.ProtoReflect.Descriptor instead.
func (*StoredParties) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_storage_proto_rawDescGZIP(), []int{0}
}

func (x *StoredParties) GetParties() []string {
	if x != nil {
		return x.Parties
	}
	return nil
}

var File_com_digitalasset_canton_protocol_v0_storage_proto protoreflect.FileDescriptor

const file_com_digitalasset_canton_protocol_v0_storage_proto_rawDesc = "" +
	"\n" +
	"1com/digitalasset/canton/protocol/v0/storage.proto\x12#com.digitalasset.canton.protocol.v0\")\n" +
	"\rStoredParties\x12\x18\n" +
	"\aparties\x18\x01 \x03(\tR\apartiesBTZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v0b\x06proto3"

var (
	file_com_digitalasset_canton_protocol_v0_storage_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_protocol_v0_storage_proto_rawDescData []byte
)

func file_com_digitalasset_canton_protocol_v0_storage_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_protocol_v0_storage_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_protocol_v0_storage_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_protocol_v0_storage_proto_rawDesc), len(file_com_digitalasset_canton_protocol_v0_storage_proto_rawDesc)))
	})
	return file_com_digitalasset_canton_protocol_v0_storage_proto_rawDescData
}

var file_com_digitalasset_canton_protocol_v0_storage_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_com_digitalasset_canton_protocol_v0_storage_proto_goTypes = []any{
	(*StoredParties)(nil), // 0: com.digitalasset.canton.protocol.v0.StoredParties
}
var file_com_digitalasset_canton_protocol_v0_storage_proto_depIdxs = []int32{
	0, // [0:0] is the sub-list for method output_type
	0, // [0:0] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_protocol_v0_storage_proto_init() }
func file_com_digitalasset_canton_protocol_v0_storage_proto_init() {
	if File_com_digitalasset_canton_protocol_v0_storage_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_protocol_v0_storage_proto_rawDesc), len(file_com_digitalasset_canton_protocol_v0_storage_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_protocol_v0_storage_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_protocol_v0_storage_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_protocol_v0_storage_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_protocol_v0_storage_proto = out.File
	file_com_digitalasset_canton_protocol_v0_storage_proto_goTypes = nil
	file_com_digitalasset_canton_protocol_v0_storage_proto_depIdxs = nil
}
