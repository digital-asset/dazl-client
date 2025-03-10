// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/digitalasset/canton/domain/protocol/v30/aggregation.proto

package v30

import (
	v30 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/crypto/v30"
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

type AggregatedSignaturesOfSender struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	SignaturesByEnvelope []*AggregatedSignaturesOfSender_SignaturesForEnvelope `protobuf:"bytes,1,rep,name=signatures_by_envelope,json=signaturesByEnvelope,proto3" json:"signatures_by_envelope,omitempty"`
}

func (x *AggregatedSignaturesOfSender) Reset() {
	*x = AggregatedSignaturesOfSender{}
	mi := &file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *AggregatedSignaturesOfSender) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*AggregatedSignaturesOfSender) ProtoMessage() {}

func (x *AggregatedSignaturesOfSender) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use AggregatedSignaturesOfSender.ProtoReflect.Descriptor instead.
func (*AggregatedSignaturesOfSender) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_rawDescGZIP(), []int{0}
}

func (x *AggregatedSignaturesOfSender) GetSignaturesByEnvelope() []*AggregatedSignaturesOfSender_SignaturesForEnvelope {
	if x != nil {
		return x.SignaturesByEnvelope
	}
	return nil
}

type AggregatedSignaturesOfSender_SignaturesForEnvelope struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Signatures []*v30.Signature `protobuf:"bytes,3,rep,name=signatures,proto3" json:"signatures,omitempty"`
}

func (x *AggregatedSignaturesOfSender_SignaturesForEnvelope) Reset() {
	*x = AggregatedSignaturesOfSender_SignaturesForEnvelope{}
	mi := &file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *AggregatedSignaturesOfSender_SignaturesForEnvelope) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*AggregatedSignaturesOfSender_SignaturesForEnvelope) ProtoMessage() {}

func (x *AggregatedSignaturesOfSender_SignaturesForEnvelope) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use AggregatedSignaturesOfSender_SignaturesForEnvelope.ProtoReflect.Descriptor instead.
func (*AggregatedSignaturesOfSender_SignaturesForEnvelope) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_rawDescGZIP(), []int{0, 0}
}

func (x *AggregatedSignaturesOfSender_SignaturesForEnvelope) GetSignatures() []*v30.Signature {
	if x != nil {
		return x.Signatures
	}
	return nil
}

var File_com_digitalasset_canton_domain_protocol_v30_aggregation_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_rawDesc = []byte{
	0x0a, 0x3d, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e,
	0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x33, 0x30, 0x2f, 0x61, 0x67,
	0x67, 0x72, 0x65, 0x67, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12,
	0x2b, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65,
	0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x33, 0x30, 0x1a, 0x2f, 0x63, 0x6f,
	0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63,
	0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x63, 0x72, 0x79, 0x70, 0x74, 0x6f, 0x2f, 0x76, 0x33, 0x30,
	0x2f, 0x63, 0x72, 0x79, 0x70, 0x74, 0x6f, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x9e, 0x02,
	0x0a, 0x1c, 0x41, 0x67, 0x67, 0x72, 0x65, 0x67, 0x61, 0x74, 0x65, 0x64, 0x53, 0x69, 0x67, 0x6e,
	0x61, 0x74, 0x75, 0x72, 0x65, 0x73, 0x4f, 0x66, 0x53, 0x65, 0x6e, 0x64, 0x65, 0x72, 0x12, 0x95,
	0x01, 0x0a, 0x16, 0x73, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x75, 0x72, 0x65, 0x73, 0x5f, 0x62, 0x79,
	0x5f, 0x65, 0x6e, 0x76, 0x65, 0x6c, 0x6f, 0x70, 0x65, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32,
	0x5f, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x33, 0x30, 0x2e, 0x41, 0x67,
	0x67, 0x72, 0x65, 0x67, 0x61, 0x74, 0x65, 0x64, 0x53, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x75, 0x72,
	0x65, 0x73, 0x4f, 0x66, 0x53, 0x65, 0x6e, 0x64, 0x65, 0x72, 0x2e, 0x53, 0x69, 0x67, 0x6e, 0x61,
	0x74, 0x75, 0x72, 0x65, 0x73, 0x46, 0x6f, 0x72, 0x45, 0x6e, 0x76, 0x65, 0x6c, 0x6f, 0x70, 0x65,
	0x52, 0x14, 0x73, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x75, 0x72, 0x65, 0x73, 0x42, 0x79, 0x45, 0x6e,
	0x76, 0x65, 0x6c, 0x6f, 0x70, 0x65, 0x1a, 0x66, 0x0a, 0x15, 0x53, 0x69, 0x67, 0x6e, 0x61, 0x74,
	0x75, 0x72, 0x65, 0x73, 0x46, 0x6f, 0x72, 0x45, 0x6e, 0x76, 0x65, 0x6c, 0x6f, 0x70, 0x65, 0x12,
	0x4d, 0x0a, 0x0a, 0x73, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x75, 0x72, 0x65, 0x73, 0x18, 0x03, 0x20,
	0x03, 0x28, 0x0b, 0x32, 0x2d, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61,
	0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x63, 0x72,
	0x79, 0x70, 0x74, 0x6f, 0x2e, 0x76, 0x33, 0x30, 0x2e, 0x53, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x75,
	0x72, 0x65, 0x52, 0x0a, 0x73, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x75, 0x72, 0x65, 0x73, 0x42, 0x5c,
	0x5a, 0x5a, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67,
	0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d,
	0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69,
	0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65,
	0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2f,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x33, 0x30, 0x62, 0x06, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_rawDescData = file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_rawDesc
)

func file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_rawDescData)
	})
	return file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_rawDescData
}

var file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_goTypes = []any{
	(*AggregatedSignaturesOfSender)(nil),                       // 0: com.digitalasset.canton.domain.protocol.v30.AggregatedSignaturesOfSender
	(*AggregatedSignaturesOfSender_SignaturesForEnvelope)(nil), // 1: com.digitalasset.canton.domain.protocol.v30.AggregatedSignaturesOfSender.SignaturesForEnvelope
	(*v30.Signature)(nil),                                      // 2: com.digitalasset.canton.crypto.v30.Signature
}
var file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_depIdxs = []int32{
	1, // 0: com.digitalasset.canton.domain.protocol.v30.AggregatedSignaturesOfSender.signatures_by_envelope:type_name -> com.digitalasset.canton.domain.protocol.v30.AggregatedSignaturesOfSender.SignaturesForEnvelope
	2, // 1: com.digitalasset.canton.domain.protocol.v30.AggregatedSignaturesOfSender.SignaturesForEnvelope.signatures:type_name -> com.digitalasset.canton.crypto.v30.Signature
	2, // [2:2] is the sub-list for method output_type
	2, // [2:2] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_init() }
func file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_init() {
	if File_com_digitalasset_canton_domain_protocol_v30_aggregation_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_domain_protocol_v30_aggregation_proto = out.File
	file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_rawDesc = nil
	file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_goTypes = nil
	file_com_digitalasset_canton_domain_protocol_v30_aggregation_proto_depIdxs = nil
}
