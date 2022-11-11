// Copyright (c) 2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.21.6
// source: com/daml/daml_lf_1_15/daml_lf.proto

package daml_lf_1_15

import (
	daml_lf_15 "github.com/digital-asset/dazl-client/v7/go/api/com/daml/daml_lf_15"
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

type HashFunction int32

const (
	HashFunction_SHA256 HashFunction = 0
)

// Enum value maps for HashFunction.
var (
	HashFunction_name = map[int32]string{
		0: "SHA256",
	}
	HashFunction_value = map[string]int32{
		"SHA256": 0,
	}
)

func (x HashFunction) Enum() *HashFunction {
	p := new(HashFunction)
	*p = x
	return p
}

func (x HashFunction) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (HashFunction) Descriptor() protoreflect.EnumDescriptor {
	return file_com_daml_daml_lf_1_15_daml_lf_proto_enumTypes[0].Descriptor()
}

func (HashFunction) Type() protoreflect.EnumType {
	return &file_com_daml_daml_lf_1_15_daml_lf_proto_enumTypes[0]
}

func (x HashFunction) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use HashFunction.Descriptor instead.
func (HashFunction) EnumDescriptor() ([]byte, []int) {
	return file_com_daml_daml_lf_1_15_daml_lf_proto_rawDescGZIP(), []int{0}
}

type ArchivePayload struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// this is number 3 for historical reasons -- we had
	// Daml-LF v0 and v1 before we had minor versions.
	Minor string `protobuf:"bytes,3,opt,name=minor,proto3" json:"minor,omitempty"`
	// Types that are assignable to Sum:
	//
	//	*ArchivePayload_DamlLf_1
	Sum isArchivePayload_Sum `protobuf_oneof:"Sum"`
}

func (x *ArchivePayload) Reset() {
	*x = ArchivePayload{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_daml_lf_1_15_daml_lf_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ArchivePayload) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ArchivePayload) ProtoMessage() {}

func (x *ArchivePayload) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_daml_lf_1_15_daml_lf_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ArchivePayload.ProtoReflect.Descriptor instead.
func (*ArchivePayload) Descriptor() ([]byte, []int) {
	return file_com_daml_daml_lf_1_15_daml_lf_proto_rawDescGZIP(), []int{0}
}

func (x *ArchivePayload) GetMinor() string {
	if x != nil {
		return x.Minor
	}
	return ""
}

func (m *ArchivePayload) GetSum() isArchivePayload_Sum {
	if m != nil {
		return m.Sum
	}
	return nil
}

func (x *ArchivePayload) GetDamlLf_1() *daml_lf_15.Package {
	if x, ok := x.GetSum().(*ArchivePayload_DamlLf_1); ok {
		return x.DamlLf_1
	}
	return nil
}

type isArchivePayload_Sum interface {
	isArchivePayload_Sum()
}

type ArchivePayload_DamlLf_1 struct {
	DamlLf_1 *daml_lf_15.Package `protobuf:"bytes,2,opt,name=daml_lf_1,json=damlLf1,proto3,oneof"`
}

func (*ArchivePayload_DamlLf_1) isArchivePayload_Sum() {}

type Archive struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	HashFunction HashFunction `protobuf:"varint,1,opt,name=hash_function,json=hashFunction,proto3,enum=daml_lf_dev.HashFunction" json:"hash_function,omitempty"`
	// Must be an encoded ArchivePayload. We store it as `bytes` to
	// simplify hashing and in future signing.
	Payload []byte `protobuf:"bytes,3,opt,name=payload,proto3" json:"payload,omitempty"`
	// The hash is simply the ascii7 lowercase hex-encoded hash of the bytes
	// according to the hash_function. We store it here for convenience, code
	// reading the Archive should verify that the hash is valid.
	//
	// Note that the hash is computed directly on the blob and not
	// on the decoded structure. This means that servers implementing
	// a Daml ledger need to store the blob as-is somewhere to be able
	// to always offer proof that they have a Daml package matching
	// the requested hash. We decided to go for this route rather than
	// relying on a canonical encoding of the AST since such a scheme
	// would be extremely hard (for example protobuf encoding is not
	// canonical) to maintain and does not buy us much.
	Hash string `protobuf:"bytes,4,opt,name=hash,proto3" json:"hash,omitempty"`
}

func (x *Archive) Reset() {
	*x = Archive{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_daml_lf_1_15_daml_lf_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Archive) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Archive) ProtoMessage() {}

func (x *Archive) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_daml_lf_1_15_daml_lf_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Archive.ProtoReflect.Descriptor instead.
func (*Archive) Descriptor() ([]byte, []int) {
	return file_com_daml_daml_lf_1_15_daml_lf_proto_rawDescGZIP(), []int{1}
}

func (x *Archive) GetHashFunction() HashFunction {
	if x != nil {
		return x.HashFunction
	}
	return HashFunction_SHA256
}

func (x *Archive) GetPayload() []byte {
	if x != nil {
		return x.Payload
	}
	return nil
}

func (x *Archive) GetHash() string {
	if x != nil {
		return x.Hash
	}
	return ""
}

var File_com_daml_daml_lf_1_15_daml_lf_proto protoreflect.FileDescriptor

var file_com_daml_daml_lf_1_15_daml_lf_proto_rawDesc = []byte{
	0x0a, 0x23, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x5f,
	0x6c, 0x66, 0x5f, 0x31, 0x5f, 0x31, 0x35, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x5f, 0x6c, 0x66, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x0b, 0x64, 0x61, 0x6d, 0x6c, 0x5f, 0x6c, 0x66, 0x5f, 0x64,
	0x65, 0x76, 0x1a, 0x25, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x64, 0x61, 0x6d,
	0x6c, 0x5f, 0x6c, 0x66, 0x5f, 0x31, 0x5f, 0x31, 0x35, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x5f, 0x6c,
	0x66, 0x5f, 0x31, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x6d, 0x0a, 0x0e, 0x41, 0x72, 0x63,
	0x68, 0x69, 0x76, 0x65, 0x50, 0x61, 0x79, 0x6c, 0x6f, 0x61, 0x64, 0x12, 0x14, 0x0a, 0x05, 0x6d,
	0x69, 0x6e, 0x6f, 0x72, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x6d, 0x69, 0x6e, 0x6f,
	0x72, 0x12, 0x30, 0x0a, 0x09, 0x64, 0x61, 0x6d, 0x6c, 0x5f, 0x6c, 0x66, 0x5f, 0x31, 0x18, 0x02,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x12, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x5f, 0x6c, 0x66, 0x5f, 0x31,
	0x2e, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x48, 0x00, 0x52, 0x07, 0x64, 0x61, 0x6d, 0x6c,
	0x4c, 0x66, 0x31, 0x42, 0x05, 0x0a, 0x03, 0x53, 0x75, 0x6d, 0x4a, 0x06, 0x08, 0x8f, 0x4e, 0x10,
	0x90, 0x4e, 0x4a, 0x04, 0x08, 0x01, 0x10, 0x02, 0x22, 0x77, 0x0a, 0x07, 0x41, 0x72, 0x63, 0x68,
	0x69, 0x76, 0x65, 0x12, 0x3e, 0x0a, 0x0d, 0x68, 0x61, 0x73, 0x68, 0x5f, 0x66, 0x75, 0x6e, 0x63,
	0x74, 0x69, 0x6f, 0x6e, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x19, 0x2e, 0x64, 0x61, 0x6d,
	0x6c, 0x5f, 0x6c, 0x66, 0x5f, 0x64, 0x65, 0x76, 0x2e, 0x48, 0x61, 0x73, 0x68, 0x46, 0x75, 0x6e,
	0x63, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x0c, 0x68, 0x61, 0x73, 0x68, 0x46, 0x75, 0x6e, 0x63, 0x74,
	0x69, 0x6f, 0x6e, 0x12, 0x18, 0x0a, 0x07, 0x70, 0x61, 0x79, 0x6c, 0x6f, 0x61, 0x64, 0x18, 0x03,
	0x20, 0x01, 0x28, 0x0c, 0x52, 0x07, 0x70, 0x61, 0x79, 0x6c, 0x6f, 0x61, 0x64, 0x12, 0x12, 0x0a,
	0x04, 0x68, 0x61, 0x73, 0x68, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x68, 0x61, 0x73,
	0x68, 0x2a, 0x1a, 0x0a, 0x0c, 0x48, 0x61, 0x73, 0x68, 0x46, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f,
	0x6e, 0x12, 0x0a, 0x0a, 0x06, 0x53, 0x48, 0x41, 0x32, 0x35, 0x36, 0x10, 0x00, 0x42, 0x7c, 0x0a,
	0x15, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x5f, 0x6c,
	0x66, 0x5f, 0x31, 0x5f, 0x31, 0x35, 0x5a, 0x44, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63,
	0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x37, 0x2f,
	0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f,
	0x64, 0x61, 0x6d, 0x6c, 0x5f, 0x6c, 0x66, 0x5f, 0x31, 0x5f, 0x31, 0x35, 0xaa, 0x02, 0x1c, 0x43,
	0x6f, 0x6d, 0x2e, 0x44, 0x61, 0x6d, 0x6c, 0x2e, 0x44, 0x61, 0x6d, 0x6c, 0x5f, 0x4c, 0x66, 0x5f,
	0x31, 0x5f, 0x31, 0x35, 0x2e, 0x44, 0x61, 0x6d, 0x6c, 0x4c, 0x66, 0x62, 0x06, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x33,
}

var (
	file_com_daml_daml_lf_1_15_daml_lf_proto_rawDescOnce sync.Once
	file_com_daml_daml_lf_1_15_daml_lf_proto_rawDescData = file_com_daml_daml_lf_1_15_daml_lf_proto_rawDesc
)

func file_com_daml_daml_lf_1_15_daml_lf_proto_rawDescGZIP() []byte {
	file_com_daml_daml_lf_1_15_daml_lf_proto_rawDescOnce.Do(func() {
		file_com_daml_daml_lf_1_15_daml_lf_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_daml_lf_1_15_daml_lf_proto_rawDescData)
	})
	return file_com_daml_daml_lf_1_15_daml_lf_proto_rawDescData
}

var file_com_daml_daml_lf_1_15_daml_lf_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_com_daml_daml_lf_1_15_daml_lf_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_com_daml_daml_lf_1_15_daml_lf_proto_goTypes = []interface{}{
	(HashFunction)(0),          // 0: daml_lf_dev.HashFunction
	(*ArchivePayload)(nil),     // 1: daml_lf_dev.ArchivePayload
	(*Archive)(nil),            // 2: daml_lf_dev.Archive
	(*daml_lf_15.Package)(nil), // 3: daml_lf_1.Package
}
var file_com_daml_daml_lf_1_15_daml_lf_proto_depIdxs = []int32{
	3, // 0: daml_lf_dev.ArchivePayload.daml_lf_1:type_name -> daml_lf_1.Package
	0, // 1: daml_lf_dev.Archive.hash_function:type_name -> daml_lf_dev.HashFunction
	2, // [2:2] is the sub-list for method output_type
	2, // [2:2] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_com_daml_daml_lf_1_15_daml_lf_proto_init() }
func file_com_daml_daml_lf_1_15_daml_lf_proto_init() {
	if File_com_daml_daml_lf_1_15_daml_lf_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_com_daml_daml_lf_1_15_daml_lf_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ArchivePayload); i {
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
		file_com_daml_daml_lf_1_15_daml_lf_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Archive); i {
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
	file_com_daml_daml_lf_1_15_daml_lf_proto_msgTypes[0].OneofWrappers = []interface{}{
		(*ArchivePayload_DamlLf_1)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_daml_daml_lf_1_15_daml_lf_proto_rawDesc,
			NumEnums:      1,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_daml_daml_lf_1_15_daml_lf_proto_goTypes,
		DependencyIndexes: file_com_daml_daml_lf_1_15_daml_lf_proto_depIdxs,
		EnumInfos:         file_com_daml_daml_lf_1_15_daml_lf_proto_enumTypes,
		MessageInfos:      file_com_daml_daml_lf_1_15_daml_lf_proto_msgTypes,
	}.Build()
	File_com_daml_daml_lf_1_15_daml_lf_proto = out.File
	file_com_daml_daml_lf_1_15_daml_lf_proto_rawDesc = nil
	file_com_daml_daml_lf_1_15_daml_lf_proto_goTypes = nil
	file_com_daml_daml_lf_1_15_daml_lf_proto_depIdxs = nil
}
