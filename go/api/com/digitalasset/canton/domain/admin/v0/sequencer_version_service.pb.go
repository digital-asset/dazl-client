// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v5.27.2
// source: com/digitalasset/canton/domain/admin/v0/sequencer_version_service.proto

package v0

import (
	v0 "github.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/protocol/v0"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

var File_com_digitalasset_canton_domain_admin_v0_sequencer_version_service_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_domain_admin_v0_sequencer_version_service_proto_rawDesc = []byte{
	0x0a, 0x47, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e,
	0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x76, 0x30, 0x2f, 0x73, 0x65, 0x71, 0x75, 0x65, 0x6e,
	0x63, 0x65, 0x72, 0x5f, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x5f, 0x73, 0x65, 0x72, 0x76,
	0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x27, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74,
	0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e,
	0x76, 0x30, 0x1a, 0x34, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x30, 0x2f, 0x73, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x69,
	0x6e, 0x67, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x32, 0x97, 0x01, 0x0a, 0x17, 0x53, 0x65, 0x71,
	0x75, 0x65, 0x6e, 0x63, 0x65, 0x72, 0x56, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x53, 0x65, 0x72,
	0x76, 0x69, 0x63, 0x65, 0x12, 0x7c, 0x0a, 0x09, 0x48, 0x61, 0x6e, 0x64, 0x73, 0x68, 0x61, 0x6b,
	0x65, 0x12, 0x36, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x48, 0x61, 0x6e, 0x64, 0x73, 0x68, 0x61, 0x6b,
	0x65, 0x2e, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x37, 0x2e, 0x63, 0x6f, 0x6d, 0x2e,
	0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e,
	0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e,
	0x48, 0x61, 0x6e, 0x64, 0x73, 0x68, 0x61, 0x6b, 0x65, 0x2e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e,
	0x73, 0x65, 0x42, 0x58, 0x5a, 0x56, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d,
	0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64,
	0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x37, 0x2f, 0x67, 0x6f,
	0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c,
	0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x64, 0x6f, 0x6d,
	0x61, 0x69, 0x6e, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x76, 0x30, 0x62, 0x06, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x33,
}

var file_com_digitalasset_canton_domain_admin_v0_sequencer_version_service_proto_goTypes = []interface{}{
	(*v0.Handshake_Request)(nil),  // 0: com.digitalasset.canton.protocol.v0.Handshake.Request
	(*v0.Handshake_Response)(nil), // 1: com.digitalasset.canton.protocol.v0.Handshake.Response
}
var file_com_digitalasset_canton_domain_admin_v0_sequencer_version_service_proto_depIdxs = []int32{
	0, // 0: com.digitalasset.canton.domain.admin.v0.SequencerVersionService.Handshake:input_type -> com.digitalasset.canton.protocol.v0.Handshake.Request
	1, // 1: com.digitalasset.canton.domain.admin.v0.SequencerVersionService.Handshake:output_type -> com.digitalasset.canton.protocol.v0.Handshake.Response
	1, // [1:2] is the sub-list for method output_type
	0, // [0:1] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_domain_admin_v0_sequencer_version_service_proto_init() }
func file_com_digitalasset_canton_domain_admin_v0_sequencer_version_service_proto_init() {
	if File_com_digitalasset_canton_domain_admin_v0_sequencer_version_service_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_domain_admin_v0_sequencer_version_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   0,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_digitalasset_canton_domain_admin_v0_sequencer_version_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_domain_admin_v0_sequencer_version_service_proto_depIdxs,
	}.Build()
	File_com_digitalasset_canton_domain_admin_v0_sequencer_version_service_proto = out.File
	file_com_digitalasset_canton_domain_admin_v0_sequencer_version_service_proto_rawDesc = nil
	file_com_digitalasset_canton_domain_admin_v0_sequencer_version_service_proto_goTypes = nil
	file_com_digitalasset_canton_domain_admin_v0_sequencer_version_service_proto_depIdxs = nil
}
