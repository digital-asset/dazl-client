// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v4.24.3
// source: com/daml/ledger/api/v1/admin/object_meta.proto

package admin

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

// Represents metadata corresponding to a participant resource (e.g. a participant user or participant local information about a party).
//
// Based on ``ObjectMeta`` meta used in Kubernetes API.
// See https://github.com/kubernetes/apimachinery/blob/master/pkg/apis/meta/v1/generated.proto#L640
type ObjectMeta struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// An opaque, non-empty value, populated by a participant server which represents the internal version of the resource
	// this ``ObjectMeta`` message is attached to. The participant server will change it to a unique value each time the corresponding resource is updated.
	// You must not rely on the format of resource version. The participant server might change it without notice.
	// You can obtain the newest resource version value by issuing a read request.
	// You may use it for concurrent change detection by passing it back unmodified in an update request.
	// The participant server will then compare the passed value with the value maintained by the system to determine
	// if any other updates took place since you had read the resource version.
	// Upon a successful update you are guaranteed that no other update took place during your read-modify-write sequence.
	// However, if another update took place during your read-modify-write sequence then your update will fail with an appropriate error.
	// Concurrent change control is optional. It will be applied only if you include a resource version in an update request.
	// When creating a new instance of a resource you must leave the resource version empty.
	// Its value will be populated by the participant server upon successful resource creation.
	// Optional
	ResourceVersion string `protobuf:"bytes,6,opt,name=resource_version,json=resourceVersion,proto3" json:"resource_version,omitempty"`
	// A set of modifiable key-value pairs that can be used to represent arbitrary, client-specific metadata.
	// Constraints:
	// 1. The total size over all keys and values cannot exceed 256kb in UTF-8 encoding.
	// 2. Keys are composed of an optional prefix segment and a required name segment such that:
	//    - key prefix, when present, must be a valid DNS subdomain with at most 253 characters, followed by a '/' (forward slash) character,
	//    - name segment must have at most 63 characters that are either alphanumeric ([a-z0-9A-Z]), or a '.' (dot), '-' (dash) or '_' (underscore);
	//      and it must start and end with an alphanumeric character.
	// 2. Values can be any non-empty strings.
	// Keys with empty prefix are reserved for end-users.
	// Properties set by external tools or internally by the participant server must use non-empty key prefixes.
	// Duplicate keys are disallowed by the semantics of the protobuf3 maps.
	// See: https://developers.google.com/protocol-buffers/docs/proto3#maps
	// Annotations may be a part of a modifiable resource.
	// Use the resource's update RPC to update its annotations.
	// In order to add a new annotation or update an existing one using an update RPC, provide the desired annotation in the update request.
	// In order to remove an annotation using an update RPC, provide the target annotation's key but set its value to the empty string in the update request.
	// Optional
	// Modifiable
	Annotations map[string]string `protobuf:"bytes,12,rep,name=annotations,proto3" json:"annotations,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
}

func (x *ObjectMeta) Reset() {
	*x = ObjectMeta{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_object_meta_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ObjectMeta) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ObjectMeta) ProtoMessage() {}

func (x *ObjectMeta) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_object_meta_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ObjectMeta.ProtoReflect.Descriptor instead.
func (*ObjectMeta) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_object_meta_proto_rawDescGZIP(), []int{0}
}

func (x *ObjectMeta) GetResourceVersion() string {
	if x != nil {
		return x.ResourceVersion
	}
	return ""
}

func (x *ObjectMeta) GetAnnotations() map[string]string {
	if x != nil {
		return x.Annotations
	}
	return nil
}

var File_com_daml_ledger_api_v1_admin_object_meta_proto protoreflect.FileDescriptor

var file_com_daml_ledger_api_v1_admin_object_meta_proto_rawDesc = []byte{
	0x0a, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x6f,
	0x62, 0x6a, 0x65, 0x63, 0x74, 0x5f, 0x6d, 0x65, 0x74, 0x61, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x12, 0x1c, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x22, 0xd4,
	0x01, 0x0a, 0x0a, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x4d, 0x65, 0x74, 0x61, 0x12, 0x29, 0x0a,
	0x10, 0x72, 0x65, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x5f, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f,
	0x6e, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0f, 0x72, 0x65, 0x73, 0x6f, 0x75, 0x72, 0x63,
	0x65, 0x56, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x12, 0x5b, 0x0a, 0x0b, 0x61, 0x6e, 0x6e, 0x6f,
	0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x18, 0x0c, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x39, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e,
	0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x4f, 0x62, 0x6a,
	0x65, 0x63, 0x74, 0x4d, 0x65, 0x74, 0x61, 0x2e, 0x41, 0x6e, 0x6e, 0x6f, 0x74, 0x61, 0x74, 0x69,
	0x6f, 0x6e, 0x73, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x52, 0x0b, 0x61, 0x6e, 0x6e, 0x6f, 0x74, 0x61,
	0x74, 0x69, 0x6f, 0x6e, 0x73, 0x1a, 0x3e, 0x0a, 0x10, 0x41, 0x6e, 0x6e, 0x6f, 0x74, 0x61, 0x74,
	0x69, 0x6f, 0x6e, 0x73, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x12, 0x14, 0x0a, 0x05, 0x76,
	0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75,
	0x65, 0x3a, 0x02, 0x38, 0x01, 0x42, 0xa0, 0x01, 0x0a, 0x1c, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61,
	0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31,
	0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x42, 0x14, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x4d, 0x65,
	0x74, 0x61, 0x4f, 0x75, 0x74, 0x65, 0x72, 0x43, 0x6c, 0x61, 0x73, 0x73, 0x5a, 0x4b, 0x67, 0x69,
	0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c,
	0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65,
	0x6e, 0x74, 0x2f, 0x76, 0x37, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d,
	0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69,
	0x2f, 0x76, 0x31, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0xaa, 0x02, 0x1c, 0x43, 0x6f, 0x6d, 0x2e,
	0x44, 0x61, 0x6d, 0x6c, 0x2e, 0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x41, 0x70, 0x69, 0x2e,
	0x56, 0x31, 0x2e, 0x41, 0x64, 0x6d, 0x69, 0x6e, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_daml_ledger_api_v1_admin_object_meta_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v1_admin_object_meta_proto_rawDescData = file_com_daml_ledger_api_v1_admin_object_meta_proto_rawDesc
)

func file_com_daml_ledger_api_v1_admin_object_meta_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v1_admin_object_meta_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v1_admin_object_meta_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_ledger_api_v1_admin_object_meta_proto_rawDescData)
	})
	return file_com_daml_ledger_api_v1_admin_object_meta_proto_rawDescData
}

var file_com_daml_ledger_api_v1_admin_object_meta_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_com_daml_ledger_api_v1_admin_object_meta_proto_goTypes = []interface{}{
	(*ObjectMeta)(nil), // 0: com.daml.ledger.api.v1.admin.ObjectMeta
	nil,                // 1: com.daml.ledger.api.v1.admin.ObjectMeta.AnnotationsEntry
}
var file_com_daml_ledger_api_v1_admin_object_meta_proto_depIdxs = []int32{
	1, // 0: com.daml.ledger.api.v1.admin.ObjectMeta.annotations:type_name -> com.daml.ledger.api.v1.admin.ObjectMeta.AnnotationsEntry
	1, // [1:1] is the sub-list for method output_type
	1, // [1:1] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v1_admin_object_meta_proto_init() }
func file_com_daml_ledger_api_v1_admin_object_meta_proto_init() {
	if File_com_daml_ledger_api_v1_admin_object_meta_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_com_daml_ledger_api_v1_admin_object_meta_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ObjectMeta); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_daml_ledger_api_v1_admin_object_meta_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_daml_ledger_api_v1_admin_object_meta_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v1_admin_object_meta_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v1_admin_object_meta_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v1_admin_object_meta_proto = out.File
	file_com_daml_ledger_api_v1_admin_object_meta_proto_rawDesc = nil
	file_com_daml_ledger_api_v1_admin_object_meta_proto_goTypes = nil
	file_com_daml_ledger_api_v1_admin_object_meta_proto_depIdxs = nil
}
