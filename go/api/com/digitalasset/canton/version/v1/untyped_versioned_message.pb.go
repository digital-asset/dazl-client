// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/digitalasset/canton/version/v1/untyped_versioned_message.proto

package v1

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

type UntypedVersionedMessage struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Wrapper:
	//
	//	*UntypedVersionedMessage_Data
	Wrapper isUntypedVersionedMessage_Wrapper `protobuf_oneof:"wrapper"`
	Version int32                             `protobuf:"varint,2,opt,name=version,proto3" json:"version,omitempty"`
}

func (x *UntypedVersionedMessage) Reset() {
	*x = UntypedVersionedMessage{}
	mi := &file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *UntypedVersionedMessage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UntypedVersionedMessage) ProtoMessage() {}

func (x *UntypedVersionedMessage) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UntypedVersionedMessage.ProtoReflect.Descriptor instead.
func (*UntypedVersionedMessage) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_rawDescGZIP(), []int{0}
}

func (m *UntypedVersionedMessage) GetWrapper() isUntypedVersionedMessage_Wrapper {
	if m != nil {
		return m.Wrapper
	}
	return nil
}

func (x *UntypedVersionedMessage) GetData() []byte {
	if x, ok := x.GetWrapper().(*UntypedVersionedMessage_Data); ok {
		return x.Data
	}
	return nil
}

func (x *UntypedVersionedMessage) GetVersion() int32 {
	if x != nil {
		return x.Version
	}
	return 0
}

type isUntypedVersionedMessage_Wrapper interface {
	isUntypedVersionedMessage_Wrapper()
}

type UntypedVersionedMessage_Data struct {
	Data []byte `protobuf:"bytes,1,opt,name=data,proto3,oneof"`
}

func (*UntypedVersionedMessage_Data) isUntypedVersionedMessage_Wrapper() {}

var File_com_digitalasset_canton_version_v1_untyped_versioned_message_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_rawDesc = []byte{
	0x0a, 0x42, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f,
	0x6e, 0x2f, 0x76, 0x31, 0x2f, 0x75, 0x6e, 0x74, 0x79, 0x70, 0x65, 0x64, 0x5f, 0x76, 0x65, 0x72,
	0x73, 0x69, 0x6f, 0x6e, 0x65, 0x64, 0x5f, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x12, 0x22, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61,
	0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x76, 0x65,
	0x72, 0x73, 0x69, 0x6f, 0x6e, 0x2e, 0x76, 0x31, 0x22, 0x54, 0x0a, 0x17, 0x55, 0x6e, 0x74, 0x79,
	0x70, 0x65, 0x64, 0x56, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x65, 0x64, 0x4d, 0x65, 0x73, 0x73,
	0x61, 0x67, 0x65, 0x12, 0x14, 0x0a, 0x04, 0x64, 0x61, 0x74, 0x61, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x0c, 0x48, 0x00, 0x52, 0x04, 0x64, 0x61, 0x74, 0x61, 0x12, 0x18, 0x0a, 0x07, 0x76, 0x65, 0x72,
	0x73, 0x69, 0x6f, 0x6e, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x07, 0x76, 0x65, 0x72, 0x73,
	0x69, 0x6f, 0x6e, 0x42, 0x09, 0x0a, 0x07, 0x77, 0x72, 0x61, 0x70, 0x70, 0x65, 0x72, 0x42, 0x53,
	0x5a, 0x51, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67,
	0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d,
	0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69,
	0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65,
	0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e,
	0x2f, 0x76, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_rawDescData = file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_rawDesc
)

func file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_rawDescData)
	})
	return file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_rawDescData
}

var file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_goTypes = []any{
	(*UntypedVersionedMessage)(nil), // 0: com.digitalasset.canton.version.v1.UntypedVersionedMessage
}
var file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_depIdxs = []int32{
	0, // [0:0] is the sub-list for method output_type
	0, // [0:0] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_init() }
func file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_init() {
	if File_com_digitalasset_canton_version_v1_untyped_versioned_message_proto != nil {
		return
	}
	file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_msgTypes[0].OneofWrappers = []any{
		(*UntypedVersionedMessage_Data)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_version_v1_untyped_versioned_message_proto = out.File
	file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_rawDesc = nil
	file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_goTypes = nil
	file_com_digitalasset_canton_version_v1_untyped_versioned_message_proto_depIdxs = nil
}
