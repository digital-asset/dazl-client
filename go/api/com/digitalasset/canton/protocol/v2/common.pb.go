// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/digitalasset/canton/protocol/v2/common.proto

package v2

import (
	v0 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/crypto/v0"
	v1 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v1"
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

type SerializableContract struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ContractId          string                 `protobuf:"bytes,1,opt,name=contract_id,json=contractId,proto3" json:"contract_id,omitempty"`
	RawContractInstance []byte                 `protobuf:"bytes,2,opt,name=raw_contract_instance,json=rawContractInstance,proto3" json:"raw_contract_instance,omitempty"`
	Metadata            *v1.Metadata           `protobuf:"bytes,3,opt,name=metadata,proto3" json:"metadata,omitempty"`
	LedgerCreateTime    *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=ledger_create_time,json=ledgerCreateTime,proto3" json:"ledger_create_time,omitempty"`
	ContractSalt        *v0.Salt               `protobuf:"bytes,5,opt,name=contract_salt,json=contractSalt,proto3" json:"contract_salt,omitempty"`
}

func (x *SerializableContract) Reset() {
	*x = SerializableContract{}
	mi := &file_com_digitalasset_canton_protocol_v2_common_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SerializableContract) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SerializableContract) ProtoMessage() {}

func (x *SerializableContract) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v2_common_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SerializableContract.ProtoReflect.Descriptor instead.
func (*SerializableContract) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v2_common_proto_rawDescGZIP(), []int{0}
}

func (x *SerializableContract) GetContractId() string {
	if x != nil {
		return x.ContractId
	}
	return ""
}

func (x *SerializableContract) GetRawContractInstance() []byte {
	if x != nil {
		return x.RawContractInstance
	}
	return nil
}

func (x *SerializableContract) GetMetadata() *v1.Metadata {
	if x != nil {
		return x.Metadata
	}
	return nil
}

func (x *SerializableContract) GetLedgerCreateTime() *timestamppb.Timestamp {
	if x != nil {
		return x.LedgerCreateTime
	}
	return nil
}

func (x *SerializableContract) GetContractSalt() *v0.Salt {
	if x != nil {
		return x.ContractSalt
	}
	return nil
}

var File_com_digitalasset_canton_protocol_v2_common_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_protocol_v2_common_proto_rawDesc = []byte{
	0x0a, 0x30, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63,
	0x6f, 0x6c, 0x2f, 0x76, 0x32, 0x2f, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x12, 0x23, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x32, 0x1a, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67,
	0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e,
	0x2f, 0x63, 0x72, 0x79, 0x70, 0x74, 0x6f, 0x2f, 0x76, 0x30, 0x2f, 0x63, 0x72, 0x79, 0x70, 0x74,
	0x6f, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x30, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67,
	0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e,
	0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x31, 0x2f, 0x63, 0x6f, 0x6d,
	0x6d, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c,
	0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73,
	0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xce, 0x02, 0x0a, 0x14, 0x53,
	0x65, 0x72, 0x69, 0x61, 0x6c, 0x69, 0x7a, 0x61, 0x62, 0x6c, 0x65, 0x43, 0x6f, 0x6e, 0x74, 0x72,
	0x61, 0x63, 0x74, 0x12, 0x1f, 0x0a, 0x0b, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x5f,
	0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61,
	0x63, 0x74, 0x49, 0x64, 0x12, 0x32, 0x0a, 0x15, 0x72, 0x61, 0x77, 0x5f, 0x63, 0x6f, 0x6e, 0x74,
	0x72, 0x61, 0x63, 0x74, 0x5f, 0x69, 0x6e, 0x73, 0x74, 0x61, 0x6e, 0x63, 0x65, 0x18, 0x02, 0x20,
	0x01, 0x28, 0x0c, 0x52, 0x13, 0x72, 0x61, 0x77, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74,
	0x49, 0x6e, 0x73, 0x74, 0x61, 0x6e, 0x63, 0x65, 0x12, 0x49, 0x0a, 0x08, 0x6d, 0x65, 0x74, 0x61,
	0x64, 0x61, 0x74, 0x61, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2d, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x31,
	0x2e, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x52, 0x08, 0x6d, 0x65, 0x74, 0x61, 0x64,
	0x61, 0x74, 0x61, 0x12, 0x48, 0x0a, 0x12, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x5f, 0x63, 0x72,
	0x65, 0x61, 0x74, 0x65, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75,
	0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x10, 0x6c, 0x65, 0x64,
	0x67, 0x65, 0x72, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x54, 0x69, 0x6d, 0x65, 0x12, 0x4c, 0x0a,
	0x0d, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x5f, 0x73, 0x61, 0x6c, 0x74, 0x18, 0x05,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x27, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74,
	0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x63,
	0x72, 0x79, 0x70, 0x74, 0x6f, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x61, 0x6c, 0x74, 0x52, 0x0c, 0x63,
	0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x53, 0x61, 0x6c, 0x74, 0x42, 0x54, 0x5a, 0x52, 0x67,
	0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61,
	0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69,
	0x65, 0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f,
	0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63,
	0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76,
	0x32, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_protocol_v2_common_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_protocol_v2_common_proto_rawDescData = file_com_digitalasset_canton_protocol_v2_common_proto_rawDesc
)

func file_com_digitalasset_canton_protocol_v2_common_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_protocol_v2_common_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_protocol_v2_common_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_protocol_v2_common_proto_rawDescData)
	})
	return file_com_digitalasset_canton_protocol_v2_common_proto_rawDescData
}

var file_com_digitalasset_canton_protocol_v2_common_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_com_digitalasset_canton_protocol_v2_common_proto_goTypes = []any{
	(*SerializableContract)(nil),  // 0: com.digitalasset.canton.protocol.v2.SerializableContract
	(*v1.Metadata)(nil),           // 1: com.digitalasset.canton.protocol.v1.Metadata
	(*timestamppb.Timestamp)(nil), // 2: google.protobuf.Timestamp
	(*v0.Salt)(nil),               // 3: com.digitalasset.canton.crypto.v0.Salt
}
var file_com_digitalasset_canton_protocol_v2_common_proto_depIdxs = []int32{
	1, // 0: com.digitalasset.canton.protocol.v2.SerializableContract.metadata:type_name -> com.digitalasset.canton.protocol.v1.Metadata
	2, // 1: com.digitalasset.canton.protocol.v2.SerializableContract.ledger_create_time:type_name -> google.protobuf.Timestamp
	3, // 2: com.digitalasset.canton.protocol.v2.SerializableContract.contract_salt:type_name -> com.digitalasset.canton.crypto.v0.Salt
	3, // [3:3] is the sub-list for method output_type
	3, // [3:3] is the sub-list for method input_type
	3, // [3:3] is the sub-list for extension type_name
	3, // [3:3] is the sub-list for extension extendee
	0, // [0:3] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_protocol_v2_common_proto_init() }
func file_com_digitalasset_canton_protocol_v2_common_proto_init() {
	if File_com_digitalasset_canton_protocol_v2_common_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_protocol_v2_common_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_protocol_v2_common_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_protocol_v2_common_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_protocol_v2_common_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_protocol_v2_common_proto = out.File
	file_com_digitalasset_canton_protocol_v2_common_proto_rawDesc = nil
	file_com_digitalasset_canton_protocol_v2_common_proto_goTypes = nil
	file_com_digitalasset_canton_protocol_v2_common_proto_depIdxs = nil
}
