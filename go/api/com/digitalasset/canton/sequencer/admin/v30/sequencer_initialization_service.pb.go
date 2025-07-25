// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/sequencer/admin/v30/sequencer_initialization_service.proto

package v30

import (
	v30 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v30"
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

type InitializeSequencerFromGenesisStateRequest struct {
	state                  protoimpl.MessageState            `protogen:"open.v1"`
	TopologySnapshot       []byte                            `protobuf:"bytes,1,opt,name=topology_snapshot,json=topologySnapshot,proto3" json:"topology_snapshot,omitempty"`
	SynchronizerParameters *v30.StaticSynchronizerParameters `protobuf:"bytes,2,opt,name=synchronizer_parameters,json=synchronizerParameters,proto3" json:"synchronizer_parameters,omitempty"`
	unknownFields          protoimpl.UnknownFields
	sizeCache              protoimpl.SizeCache
}

func (x *InitializeSequencerFromGenesisStateRequest) Reset() {
	*x = InitializeSequencerFromGenesisStateRequest{}
	mi := &file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *InitializeSequencerFromGenesisStateRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*InitializeSequencerFromGenesisStateRequest) ProtoMessage() {}

func (x *InitializeSequencerFromGenesisStateRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use InitializeSequencerFromGenesisStateRequest.ProtoReflect.Descriptor instead.
func (*InitializeSequencerFromGenesisStateRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_rawDescGZIP(), []int{0}
}

func (x *InitializeSequencerFromGenesisStateRequest) GetTopologySnapshot() []byte {
	if x != nil {
		return x.TopologySnapshot
	}
	return nil
}

func (x *InitializeSequencerFromGenesisStateRequest) GetSynchronizerParameters() *v30.StaticSynchronizerParameters {
	if x != nil {
		return x.SynchronizerParameters
	}
	return nil
}

type InitializeSequencerFromGenesisStateResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Replicated    bool                   `protobuf:"varint,1,opt,name=replicated,proto3" json:"replicated,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *InitializeSequencerFromGenesisStateResponse) Reset() {
	*x = InitializeSequencerFromGenesisStateResponse{}
	mi := &file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *InitializeSequencerFromGenesisStateResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*InitializeSequencerFromGenesisStateResponse) ProtoMessage() {}

func (x *InitializeSequencerFromGenesisStateResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use InitializeSequencerFromGenesisStateResponse.ProtoReflect.Descriptor instead.
func (*InitializeSequencerFromGenesisStateResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_rawDescGZIP(), []int{1}
}

func (x *InitializeSequencerFromGenesisStateResponse) GetReplicated() bool {
	if x != nil {
		return x.Replicated
	}
	return false
}

type InitializeSequencerFromOnboardingStateRequest struct {
	state           protoimpl.MessageState `protogen:"open.v1"`
	OnboardingState []byte                 `protobuf:"bytes,1,opt,name=onboarding_state,json=onboardingState,proto3" json:"onboarding_state,omitempty"`
	unknownFields   protoimpl.UnknownFields
	sizeCache       protoimpl.SizeCache
}

func (x *InitializeSequencerFromOnboardingStateRequest) Reset() {
	*x = InitializeSequencerFromOnboardingStateRequest{}
	mi := &file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *InitializeSequencerFromOnboardingStateRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*InitializeSequencerFromOnboardingStateRequest) ProtoMessage() {}

func (x *InitializeSequencerFromOnboardingStateRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use InitializeSequencerFromOnboardingStateRequest.ProtoReflect.Descriptor instead.
func (*InitializeSequencerFromOnboardingStateRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_rawDescGZIP(), []int{2}
}

func (x *InitializeSequencerFromOnboardingStateRequest) GetOnboardingState() []byte {
	if x != nil {
		return x.OnboardingState
	}
	return nil
}

type InitializeSequencerFromOnboardingStateResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Replicated    bool                   `protobuf:"varint,1,opt,name=replicated,proto3" json:"replicated,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *InitializeSequencerFromOnboardingStateResponse) Reset() {
	*x = InitializeSequencerFromOnboardingStateResponse{}
	mi := &file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *InitializeSequencerFromOnboardingStateResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*InitializeSequencerFromOnboardingStateResponse) ProtoMessage() {}

func (x *InitializeSequencerFromOnboardingStateResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use InitializeSequencerFromOnboardingStateResponse.ProtoReflect.Descriptor instead.
func (*InitializeSequencerFromOnboardingStateResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_rawDescGZIP(), []int{3}
}

func (x *InitializeSequencerFromOnboardingStateResponse) GetReplicated() bool {
	if x != nil {
		return x.Replicated
	}
	return false
}

var File_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto protoreflect.FileDescriptor

const file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_rawDesc = "" +
	"\n" +
	"Rcom/digitalasset/canton/sequencer/admin/v30/sequencer_initialization_service.proto\x12+com.digitalasset.canton.sequencer.admin.v30\x1a5com/digitalasset/canton/protocol/v30/sequencing.proto\"\xd6\x01\n" +
	"*InitializeSequencerFromGenesisStateRequest\x12+\n" +
	"\x11topology_snapshot\x18\x01 \x01(\fR\x10topologySnapshot\x12{\n" +
	"\x17synchronizer_parameters\x18\x02 \x01(\v2B.com.digitalasset.canton.protocol.v30.StaticSynchronizerParametersR\x16synchronizerParameters\"M\n" +
	"+InitializeSequencerFromGenesisStateResponse\x12\x1e\n" +
	"\n" +
	"replicated\x18\x01 \x01(\bR\n" +
	"replicated\"Z\n" +
	"-InitializeSequencerFromOnboardingStateRequest\x12)\n" +
	"\x10onboarding_state\x18\x01 \x01(\fR\x0fonboardingState\"P\n" +
	".InitializeSequencerFromOnboardingStateResponse\x12\x1e\n" +
	"\n" +
	"replicated\x18\x01 \x01(\bR\n" +
	"replicated2\xe3\x03\n" +
	"\x1eSequencerInitializationService\x12\xda\x01\n" +
	"#InitializeSequencerFromGenesisState\x12W.com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromGenesisStateRequest\x1aX.com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromGenesisStateResponse(\x01\x12\xe3\x01\n" +
	"&InitializeSequencerFromOnboardingState\x12Z.com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromOnboardingStateRequest\x1a[.com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromOnboardingStateResponse(\x01B\\ZZgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/sequencer/admin/v30b\x06proto3"

var (
	file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_rawDescData []byte
)

func file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_rawDesc), len(file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_rawDesc)))
	})
	return file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_rawDescData
}

var file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_goTypes = []any{
	(*InitializeSequencerFromGenesisStateRequest)(nil),     // 0: com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromGenesisStateRequest
	(*InitializeSequencerFromGenesisStateResponse)(nil),    // 1: com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromGenesisStateResponse
	(*InitializeSequencerFromOnboardingStateRequest)(nil),  // 2: com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromOnboardingStateRequest
	(*InitializeSequencerFromOnboardingStateResponse)(nil), // 3: com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromOnboardingStateResponse
	(*v30.StaticSynchronizerParameters)(nil),               // 4: com.digitalasset.canton.protocol.v30.StaticSynchronizerParameters
}
var file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_depIdxs = []int32{
	4, // 0: com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromGenesisStateRequest.synchronizer_parameters:type_name -> com.digitalasset.canton.protocol.v30.StaticSynchronizerParameters
	0, // 1: com.digitalasset.canton.sequencer.admin.v30.SequencerInitializationService.InitializeSequencerFromGenesisState:input_type -> com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromGenesisStateRequest
	2, // 2: com.digitalasset.canton.sequencer.admin.v30.SequencerInitializationService.InitializeSequencerFromOnboardingState:input_type -> com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromOnboardingStateRequest
	1, // 3: com.digitalasset.canton.sequencer.admin.v30.SequencerInitializationService.InitializeSequencerFromGenesisState:output_type -> com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromGenesisStateResponse
	3, // 4: com.digitalasset.canton.sequencer.admin.v30.SequencerInitializationService.InitializeSequencerFromOnboardingState:output_type -> com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromOnboardingStateResponse
	3, // [3:5] is the sub-list for method output_type
	1, // [1:3] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() {
	file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_init()
}
func file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_init() {
	if File_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_rawDesc), len(file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto = out.File
	file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_goTypes = nil
	file_com_digitalasset_canton_sequencer_admin_v30_sequencer_initialization_service_proto_depIdxs = nil
}
