// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/domain/api/v0/domain_service.proto

package v0

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	unsafe "unsafe"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

var File_com_digitalasset_canton_domain_api_v0_domain_service_proto protoreflect.FileDescriptor

const file_com_digitalasset_canton_domain_api_v0_domain_service_proto_rawDesc = "" +
	"\n" +
	":com/digitalasset/canton/domain/api/v0/domain_service.proto\x12%com.digitalasset.canton.domain.api.v0\x1a=com/digitalasset/canton/domain/api/v0/service_agreement.proto2\xb3\x01\n" +
	"\rDomainService\x12\x9c\x01\n" +
	"\x13GetServiceAgreement\x12A.com.digitalasset.canton.domain.api.v0.GetServiceAgreementRequest\x1aB.com.digitalasset.canton.domain.api.v0.GetServiceAgreementResponse\x1a\x03\x88\x02\x01BVZTgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/api/v0b\x06proto3"

var file_com_digitalasset_canton_domain_api_v0_domain_service_proto_goTypes = []any{
	(*GetServiceAgreementRequest)(nil),  // 0: com.digitalasset.canton.domain.api.v0.GetServiceAgreementRequest
	(*GetServiceAgreementResponse)(nil), // 1: com.digitalasset.canton.domain.api.v0.GetServiceAgreementResponse
}
var file_com_digitalasset_canton_domain_api_v0_domain_service_proto_depIdxs = []int32{
	0, // 0: com.digitalasset.canton.domain.api.v0.DomainService.GetServiceAgreement:input_type -> com.digitalasset.canton.domain.api.v0.GetServiceAgreementRequest
	1, // 1: com.digitalasset.canton.domain.api.v0.DomainService.GetServiceAgreement:output_type -> com.digitalasset.canton.domain.api.v0.GetServiceAgreementResponse
	1, // [1:2] is the sub-list for method output_type
	0, // [0:1] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_domain_api_v0_domain_service_proto_init() }
func file_com_digitalasset_canton_domain_api_v0_domain_service_proto_init() {
	if File_com_digitalasset_canton_domain_api_v0_domain_service_proto != nil {
		return
	}
	file_com_digitalasset_canton_domain_api_v0_service_agreement_proto_init()
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_domain_api_v0_domain_service_proto_rawDesc), len(file_com_digitalasset_canton_domain_api_v0_domain_service_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   0,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_digitalasset_canton_domain_api_v0_domain_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_domain_api_v0_domain_service_proto_depIdxs,
	}.Build()
	File_com_digitalasset_canton_domain_api_v0_domain_service_proto = out.File
	file_com_digitalasset_canton_domain_api_v0_domain_service_proto_goTypes = nil
	file_com_digitalasset_canton_domain_api_v0_domain_service_proto_depIdxs = nil
}
