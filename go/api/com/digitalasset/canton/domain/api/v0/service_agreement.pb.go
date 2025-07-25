// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/domain/api/v0/service_agreement.proto

package v0

import (
	v0 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v0"
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

type GetServiceAgreementRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetServiceAgreementRequest) Reset() {
	*x = GetServiceAgreementRequest{}
	mi := &file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetServiceAgreementRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetServiceAgreementRequest) ProtoMessage() {}

func (x *GetServiceAgreementRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetServiceAgreementRequest.ProtoReflect.Descriptor instead.
func (*GetServiceAgreementRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_rawDescGZIP(), []int{0}
}

type GetServiceAgreementResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Agreement     *v0.ServiceAgreement   `protobuf:"bytes,1,opt,name=agreement,proto3" json:"agreement,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetServiceAgreementResponse) Reset() {
	*x = GetServiceAgreementResponse{}
	mi := &file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetServiceAgreementResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetServiceAgreementResponse) ProtoMessage() {}

func (x *GetServiceAgreementResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetServiceAgreementResponse.ProtoReflect.Descriptor instead.
func (*GetServiceAgreementResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_rawDescGZIP(), []int{1}
}

func (x *GetServiceAgreementResponse) GetAgreement() *v0.ServiceAgreement {
	if x != nil {
		return x.Agreement
	}
	return nil
}

var File_com_digitalasset_canton_domain_api_v0_service_agreement_proto protoreflect.FileDescriptor

const file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_rawDesc = "" +
	"\n" +
	"=com/digitalasset/canton/domain/api/v0/service_agreement.proto\x12%com.digitalasset.canton.domain.api.v0\x1a4com/digitalasset/canton/protocol/v0/sequencing.proto\"\x1c\n" +
	"\x1aGetServiceAgreementRequest\"r\n" +
	"\x1bGetServiceAgreementResponse\x12S\n" +
	"\tagreement\x18\x01 \x01(\v25.com.digitalasset.canton.protocol.v0.ServiceAgreementR\tagreementBVZTgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/api/v0b\x06proto3"

var (
	file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_rawDescData []byte
)

func file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_rawDesc), len(file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_rawDesc)))
	})
	return file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_rawDescData
}

var file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_goTypes = []any{
	(*GetServiceAgreementRequest)(nil),  // 0: com.digitalasset.canton.domain.api.v0.GetServiceAgreementRequest
	(*GetServiceAgreementResponse)(nil), // 1: com.digitalasset.canton.domain.api.v0.GetServiceAgreementResponse
	(*v0.ServiceAgreement)(nil),         // 2: com.digitalasset.canton.protocol.v0.ServiceAgreement
}
var file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_depIdxs = []int32{
	2, // 0: com.digitalasset.canton.domain.api.v0.GetServiceAgreementResponse.agreement:type_name -> com.digitalasset.canton.protocol.v0.ServiceAgreement
	1, // [1:1] is the sub-list for method output_type
	1, // [1:1] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_init() }
func file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_init() {
	if File_com_digitalasset_canton_domain_api_v0_service_agreement_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_rawDesc), len(file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_domain_api_v0_service_agreement_proto = out.File
	file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_goTypes = nil
	file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_depIdxs = nil
}
