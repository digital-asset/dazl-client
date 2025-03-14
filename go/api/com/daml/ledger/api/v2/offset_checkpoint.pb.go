// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/daml/ledger/api/v2/offset_checkpoint.proto

package v2

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	timestamppb "google.golang.org/protobuf/types/known/timestamppb"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type OffsetCheckpoint struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Offset      int64         `protobuf:"varint,1,opt,name=offset,proto3" json:"offset,omitempty"`
	DomainTimes []*DomainTime `protobuf:"bytes,2,rep,name=domain_times,json=domainTimes,proto3" json:"domain_times,omitempty"`
}

func (x *OffsetCheckpoint) Reset() {
	*x = OffsetCheckpoint{}
	mi := &file_com_daml_ledger_api_v2_offset_checkpoint_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *OffsetCheckpoint) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*OffsetCheckpoint) ProtoMessage() {}

func (x *OffsetCheckpoint) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_offset_checkpoint_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use OffsetCheckpoint.ProtoReflect.Descriptor instead.
func (*OffsetCheckpoint) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_offset_checkpoint_proto_rawDescGZIP(), []int{0}
}

func (x *OffsetCheckpoint) GetOffset() int64 {
	if x != nil {
		return x.Offset
	}
	return 0
}

func (x *OffsetCheckpoint) GetDomainTimes() []*DomainTime {
	if x != nil {
		return x.DomainTimes
	}
	return nil
}

type DomainTime struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	DomainId   string                 `protobuf:"bytes,1,opt,name=domain_id,json=domainId,proto3" json:"domain_id,omitempty"`
	RecordTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=record_time,json=recordTime,proto3" json:"record_time,omitempty"`
}

func (x *DomainTime) Reset() {
	*x = DomainTime{}
	mi := &file_com_daml_ledger_api_v2_offset_checkpoint_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *DomainTime) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DomainTime) ProtoMessage() {}

func (x *DomainTime) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_offset_checkpoint_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DomainTime.ProtoReflect.Descriptor instead.
func (*DomainTime) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_offset_checkpoint_proto_rawDescGZIP(), []int{1}
}

func (x *DomainTime) GetDomainId() string {
	if x != nil {
		return x.DomainId
	}
	return ""
}

func (x *DomainTime) GetRecordTime() *timestamppb.Timestamp {
	if x != nil {
		return x.RecordTime
	}
	return nil
}

var File_com_daml_ledger_api_v2_offset_checkpoint_proto protoreflect.FileDescriptor

var file_com_daml_ledger_api_v2_offset_checkpoint_proto_rawDesc = []byte{
	0x0a, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x32, 0x2f, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x5f,
	0x63, 0x68, 0x65, 0x63, 0x6b, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x12, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65,
	0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74,
	0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x71, 0x0a, 0x10, 0x4f, 0x66, 0x66,
	0x73, 0x65, 0x74, 0x43, 0x68, 0x65, 0x63, 0x6b, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x12, 0x16, 0x0a,
	0x06, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x03, 0x52, 0x06, 0x6f,
	0x66, 0x66, 0x73, 0x65, 0x74, 0x12, 0x45, 0x0a, 0x0c, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x5f,
	0x74, 0x69, 0x6d, 0x65, 0x73, 0x18, 0x02, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x22, 0x2e, 0x63, 0x6f,
	0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70,
	0x69, 0x2e, 0x76, 0x32, 0x2e, 0x44, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x54, 0x69, 0x6d, 0x65, 0x52,
	0x0b, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x22, 0x66, 0x0a, 0x0a,
	0x44, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x54, 0x69, 0x6d, 0x65, 0x12, 0x1b, 0x0a, 0x09, 0x64, 0x6f,
	0x6d, 0x61, 0x69, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x64,
	0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x49, 0x64, 0x12, 0x3b, 0x0a, 0x0b, 0x72, 0x65, 0x63, 0x6f, 0x72,
	0x64, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67,
	0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54,
	0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x0a, 0x72, 0x65, 0x63, 0x6f, 0x72, 0x64,
	0x54, 0x69, 0x6d, 0x65, 0x42, 0x94, 0x01, 0x0a, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d,
	0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x42,
	0x1a, 0x4f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x43, 0x68, 0x65, 0x63, 0x6b, 0x70, 0x6f, 0x69, 0x6e,
	0x74, 0x4f, 0x75, 0x74, 0x65, 0x72, 0x43, 0x6c, 0x61, 0x73, 0x73, 0x5a, 0x45, 0x67, 0x69, 0x74,
	0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d,
	0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e,
	0x74, 0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f,
	0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f,
	0x76, 0x32, 0xaa, 0x02, 0x16, 0x43, 0x6f, 0x6d, 0x2e, 0x44, 0x61, 0x6d, 0x6c, 0x2e, 0x4c, 0x65,
	0x64, 0x67, 0x65, 0x72, 0x2e, 0x41, 0x70, 0x69, 0x2e, 0x56, 0x32, 0x62, 0x06, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x33,
}

var (
	file_com_daml_ledger_api_v2_offset_checkpoint_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v2_offset_checkpoint_proto_rawDescData = file_com_daml_ledger_api_v2_offset_checkpoint_proto_rawDesc
)

func file_com_daml_ledger_api_v2_offset_checkpoint_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v2_offset_checkpoint_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v2_offset_checkpoint_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_ledger_api_v2_offset_checkpoint_proto_rawDescData)
	})
	return file_com_daml_ledger_api_v2_offset_checkpoint_proto_rawDescData
}

var file_com_daml_ledger_api_v2_offset_checkpoint_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_com_daml_ledger_api_v2_offset_checkpoint_proto_goTypes = []any{
	(*OffsetCheckpoint)(nil),      // 0: com.daml.ledger.api.v2.OffsetCheckpoint
	(*DomainTime)(nil),            // 1: com.daml.ledger.api.v2.DomainTime
	(*timestamppb.Timestamp)(nil), // 2: google.protobuf.Timestamp
}
var file_com_daml_ledger_api_v2_offset_checkpoint_proto_depIdxs = []int32{
	1, // 0: com.daml.ledger.api.v2.OffsetCheckpoint.domain_times:type_name -> com.daml.ledger.api.v2.DomainTime
	2, // 1: com.daml.ledger.api.v2.DomainTime.record_time:type_name -> google.protobuf.Timestamp
	2, // [2:2] is the sub-list for method output_type
	2, // [2:2] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v2_offset_checkpoint_proto_init() }
func file_com_daml_ledger_api_v2_offset_checkpoint_proto_init() {
	if File_com_daml_ledger_api_v2_offset_checkpoint_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_daml_ledger_api_v2_offset_checkpoint_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_daml_ledger_api_v2_offset_checkpoint_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v2_offset_checkpoint_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v2_offset_checkpoint_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v2_offset_checkpoint_proto = out.File
	file_com_daml_ledger_api_v2_offset_checkpoint_proto_rawDesc = nil
	file_com_daml_ledger_api_v2_offset_checkpoint_proto_goTypes = nil
	file_com_daml_ledger_api_v2_offset_checkpoint_proto_depIdxs = nil
}
