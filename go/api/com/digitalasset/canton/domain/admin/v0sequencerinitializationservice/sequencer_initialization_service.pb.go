// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/domain/admin/v0/sequencer_initialization_service.proto

package v0

import (
	v01 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/crypto/v0"
	v0snapshot "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/admin/v0"
	v1 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/admin/v1"
	v0 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v0"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
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

type InitRequest struct {
	state            protoimpl.MessageState     `protogen:"open.v1"`
	DomainId         string                     `protobuf:"bytes,1,opt,name=domain_id,json=domainId,proto3" json:"domain_id,omitempty"`
	TopologySnapshot *v0.TopologyTransactions   `protobuf:"bytes,2,opt,name=topology_snapshot,json=topologySnapshot,proto3" json:"topology_snapshot,omitempty"`
	DomainParameters *v0.StaticDomainParameters `protobuf:"bytes,4,opt,name=domain_parameters,json=domainParameters,proto3" json:"domain_parameters,omitempty"`
	Snapshot         *v0snapshot.SequencerSnapshot         `protobuf:"bytes,3,opt,name=snapshot,proto3" json:"snapshot,omitempty"`
	unknownFields    protoimpl.UnknownFields
	sizeCache        protoimpl.SizeCache
}

func (x *InitRequest) Reset() {
	*x = InitRequest{}
	mi := &file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *InitRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*InitRequest) ProtoMessage() {}

func (x *InitRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use InitRequest.ProtoReflect.Descriptor instead.
func (*InitRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_rawDescGZIP(), []int{0}
}

func (x *InitRequest) GetDomainId() string {
	if x != nil {
		return x.DomainId
	}
	return ""
}

func (x *InitRequest) GetTopologySnapshot() *v0.TopologyTransactions {
	if x != nil {
		return x.TopologySnapshot
	}
	return nil
}

func (x *InitRequest) GetDomainParameters() *v0.StaticDomainParameters {
	if x != nil {
		return x.DomainParameters
	}
	return nil
}

func (x *InitRequest) GetSnapshot() *v0snapshot.SequencerSnapshot {
	if x != nil {
		return x.Snapshot
	}
	return nil
}

type InitResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	KeyId         string                 `protobuf:"bytes,1,opt,name=key_id,json=keyId,proto3" json:"key_id,omitempty"`
	PublicKey     *v01.SigningPublicKey  `protobuf:"bytes,2,opt,name=public_key,json=publicKey,proto3" json:"public_key,omitempty"`
	Replicated    bool                   `protobuf:"varint,3,opt,name=replicated,proto3" json:"replicated,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *InitResponse) Reset() {
	*x = InitResponse{}
	mi := &file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *InitResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*InitResponse) ProtoMessage() {}

func (x *InitResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use InitResponse.ProtoReflect.Descriptor instead.
func (*InitResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_rawDescGZIP(), []int{1}
}

func (x *InitResponse) GetKeyId() string {
	if x != nil {
		return x.KeyId
	}
	return ""
}

func (x *InitResponse) GetPublicKey() *v01.SigningPublicKey {
	if x != nil {
		return x.PublicKey
	}
	return nil
}

func (x *InitResponse) GetReplicated() bool {
	if x != nil {
		return x.Replicated
	}
	return false
}

type TopologyBootstrapRequest struct {
	state                   protoimpl.MessageState   `protogen:"open.v1"`
	InitialTopologySnapshot *v0.TopologyTransactions `protobuf:"bytes,1,opt,name=initial_topology_snapshot,json=initialTopologySnapshot,proto3" json:"initial_topology_snapshot,omitempty"`
	unknownFields           protoimpl.UnknownFields
	sizeCache               protoimpl.SizeCache
}

func (x *TopologyBootstrapRequest) Reset() {
	*x = TopologyBootstrapRequest{}
	mi := &file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TopologyBootstrapRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TopologyBootstrapRequest) ProtoMessage() {}

func (x *TopologyBootstrapRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TopologyBootstrapRequest.ProtoReflect.Descriptor instead.
func (*TopologyBootstrapRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_rawDescGZIP(), []int{2}
}

func (x *TopologyBootstrapRequest) GetInitialTopologySnapshot() *v0.TopologyTransactions {
	if x != nil {
		return x.InitialTopologySnapshot
	}
	return nil
}

var File_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto protoreflect.FileDescriptor

const file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_rawDesc = "" +
	"\n" +
	"Ncom/digitalasset/canton/domain/admin/v0/sequencer_initialization_service.proto\x12'com.digitalasset.canton.domain.admin.v0\x1a.com/digitalasset/canton/crypto/v0/crypto.proto\x1aOcom/digitalasset/canton/domain/admin/v0/sequencer_initialization_snapshot.proto\x1aNcom/digitalasset/canton/domain/admin/v1/sequencer_initialization_service.proto\x1a4com/digitalasset/canton/protocol/v0/sequencing.proto\x1a6com/digitalasset/canton/protocol/v0/topology_ext.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xd4\x02\n" +
	"\vInitRequest\x12\x1b\n" +
	"\tdomain_id\x18\x01 \x01(\tR\bdomainId\x12f\n" +
	"\x11topology_snapshot\x18\x02 \x01(\v29.com.digitalasset.canton.protocol.v0.TopologyTransactionsR\x10topologySnapshot\x12h\n" +
	"\x11domain_parameters\x18\x04 \x01(\v2;.com.digitalasset.canton.protocol.v0.StaticDomainParametersR\x10domainParameters\x12V\n" +
	"\bsnapshot\x18\x03 \x01(\v2:.com.digitalasset.canton.domain.admin.v0.SequencerSnapshotR\bsnapshot\"\x99\x01\n" +
	"\fInitResponse\x12\x15\n" +
	"\x06key_id\x18\x01 \x01(\tR\x05keyId\x12R\n" +
	"\n" +
	"public_key\x18\x02 \x01(\v23.com.digitalasset.canton.crypto.v0.SigningPublicKeyR\tpublicKey\x12\x1e\n" +
	"\n" +
	"replicated\x18\x03 \x01(\bR\n" +
	"replicated\"\x91\x01\n" +
	"\x18TopologyBootstrapRequest\x12u\n" +
	"\x19initial_topology_snapshot\x18\x01 \x01(\v29.com.digitalasset.canton.protocol.v0.TopologyTransactionsR\x17initialTopologySnapshot2\x8c\x02\n" +
	"\x1eSequencerInitializationService\x12s\n" +
	"\x04Init\x124.com.digitalasset.canton.domain.admin.v0.InitRequest\x1a5.com.digitalasset.canton.domain.admin.v0.InitResponse\x12u\n" +
	"\x06InitV1\x124.com.digitalasset.canton.domain.admin.v1.InitRequest\x1a5.com.digitalasset.canton.domain.admin.v0.InitResponse2\x82\x01\n" +
	"\x18TopologyBootstrapService\x12f\n" +
	"\tBootstrap\x12A.com.digitalasset.canton.domain.admin.v0.TopologyBootstrapRequest\x1a\x16.google.protobuf.EmptyBXZVgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/admin/v0b\x06proto3"

var (
	file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_rawDescData []byte
)

func file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_rawDesc), len(file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_rawDesc)))
	})
	return file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_rawDescData
}

var file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_goTypes = []any{
	(*InitRequest)(nil),               // 0: com.digitalasset.canton.domain.admin.v0.InitRequest
	(*InitResponse)(nil),              // 1: com.digitalasset.canton.domain.admin.v0.InitResponse
	(*TopologyBootstrapRequest)(nil),  // 2: com.digitalasset.canton.domain.admin.v0.TopologyBootstrapRequest
	(*v0.TopologyTransactions)(nil),   // 3: com.digitalasset.canton.protocol.v0.TopologyTransactions
	(*v0.StaticDomainParameters)(nil), // 4: com.digitalasset.canton.protocol.v0.StaticDomainParameters
	(*v0snapshot.SequencerSnapshot)(nil),         // 5: com.digitalasset.canton.domain.admin.v0.SequencerSnapshot
	(*v01.SigningPublicKey)(nil),      // 6: com.digitalasset.canton.crypto.v0.SigningPublicKey
	(*v1.InitRequest)(nil),            // 7: com.digitalasset.canton.domain.admin.v1.InitRequest
	(*emptypb.Empty)(nil),             // 8: google.protobuf.Empty
}
var file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_depIdxs = []int32{
	3, // 0: com.digitalasset.canton.domain.admin.v0.InitRequest.topology_snapshot:type_name -> com.digitalasset.canton.protocol.v0.TopologyTransactions
	4, // 1: com.digitalasset.canton.domain.admin.v0.InitRequest.domain_parameters:type_name -> com.digitalasset.canton.protocol.v0.StaticDomainParameters
	5, // 2: com.digitalasset.canton.domain.admin.v0.InitRequest.snapshot:type_name -> com.digitalasset.canton.domain.admin.v0.SequencerSnapshot
	6, // 3: com.digitalasset.canton.domain.admin.v0.InitResponse.public_key:type_name -> com.digitalasset.canton.crypto.v0.SigningPublicKey
	3, // 4: com.digitalasset.canton.domain.admin.v0.TopologyBootstrapRequest.initial_topology_snapshot:type_name -> com.digitalasset.canton.protocol.v0.TopologyTransactions
	0, // 5: com.digitalasset.canton.domain.admin.v0.SequencerInitializationService.Init:input_type -> com.digitalasset.canton.domain.admin.v0.InitRequest
	7, // 6: com.digitalasset.canton.domain.admin.v0.SequencerInitializationService.InitV1:input_type -> com.digitalasset.canton.domain.admin.v1.InitRequest
	2, // 7: com.digitalasset.canton.domain.admin.v0.TopologyBootstrapService.Bootstrap:input_type -> com.digitalasset.canton.domain.admin.v0.TopologyBootstrapRequest
	1, // 8: com.digitalasset.canton.domain.admin.v0.SequencerInitializationService.Init:output_type -> com.digitalasset.canton.domain.admin.v0.InitResponse
	1, // 9: com.digitalasset.canton.domain.admin.v0.SequencerInitializationService.InitV1:output_type -> com.digitalasset.canton.domain.admin.v0.InitResponse
	8, // 10: com.digitalasset.canton.domain.admin.v0.TopologyBootstrapService.Bootstrap:output_type -> google.protobuf.Empty
	8, // [8:11] is the sub-list for method output_type
	5, // [5:8] is the sub-list for method input_type
	5, // [5:5] is the sub-list for extension type_name
	5, // [5:5] is the sub-list for extension extendee
	0, // [0:5] is the sub-list for field type_name
}

func init() {
	file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_init()
}
func file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_init() {
	if File_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto != nil {
		return
	}
	//file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_snapshot_proto_init()
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_rawDesc), len(file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   2,
		},
		GoTypes:           file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto = out.File
	file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_goTypes = nil
	file_com_digitalasset_canton_domain_admin_v0_sequencer_initialization_service_proto_depIdxs = nil
}
