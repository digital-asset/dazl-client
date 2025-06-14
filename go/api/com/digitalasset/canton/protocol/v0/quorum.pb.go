// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/protocol/v0/quorum.proto

package v0

import (
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

type Quorum struct {
	state               protoimpl.MessageState `protogen:"open.v1"`
	PartyIndexAndWeight []*PartyIndexAndWeight `protobuf:"bytes,1,rep,name=party_index_and_weight,json=partyIndexAndWeight,proto3" json:"party_index_and_weight,omitempty"`
	Threshold           int32                  `protobuf:"varint,2,opt,name=threshold,proto3" json:"threshold,omitempty"`
	unknownFields       protoimpl.UnknownFields
	sizeCache           protoimpl.SizeCache
}

func (x *Quorum) Reset() {
	*x = Quorum{}
	mi := &file_com_digitalasset_canton_protocol_v0_quorum_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Quorum) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Quorum) ProtoMessage() {}

func (x *Quorum) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_quorum_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Quorum.ProtoReflect.Descriptor instead.
func (*Quorum) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_quorum_proto_rawDescGZIP(), []int{0}
}

func (x *Quorum) GetPartyIndexAndWeight() []*PartyIndexAndWeight {
	if x != nil {
		return x.PartyIndexAndWeight
	}
	return nil
}

func (x *Quorum) GetThreshold() int32 {
	if x != nil {
		return x.Threshold
	}
	return 0
}

type PartyIndexAndWeight struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Index         int32                  `protobuf:"varint,1,opt,name=index,proto3" json:"index,omitempty"`
	Weight        int32                  `protobuf:"varint,2,opt,name=weight,proto3" json:"weight,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *PartyIndexAndWeight) Reset() {
	*x = PartyIndexAndWeight{}
	mi := &file_com_digitalasset_canton_protocol_v0_quorum_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PartyIndexAndWeight) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PartyIndexAndWeight) ProtoMessage() {}

func (x *PartyIndexAndWeight) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_quorum_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PartyIndexAndWeight.ProtoReflect.Descriptor instead.
func (*PartyIndexAndWeight) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_quorum_proto_rawDescGZIP(), []int{1}
}

func (x *PartyIndexAndWeight) GetIndex() int32 {
	if x != nil {
		return x.Index
	}
	return 0
}

func (x *PartyIndexAndWeight) GetWeight() int32 {
	if x != nil {
		return x.Weight
	}
	return 0
}

type TrustParty struct {
	state              protoimpl.MessageState `protogen:"open.v1"`
	Party              string                 `protobuf:"bytes,1,opt,name=party,proto3" json:"party,omitempty"`
	RequiredTrustLevel TrustLevel             `protobuf:"varint,2,opt,name=required_trust_level,json=requiredTrustLevel,proto3,enum=com.digitalasset.canton.protocol.v0.TrustLevel" json:"required_trust_level,omitempty"`
	unknownFields      protoimpl.UnknownFields
	sizeCache          protoimpl.SizeCache
}

func (x *TrustParty) Reset() {
	*x = TrustParty{}
	mi := &file_com_digitalasset_canton_protocol_v0_quorum_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TrustParty) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TrustParty) ProtoMessage() {}

func (x *TrustParty) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_quorum_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TrustParty.ProtoReflect.Descriptor instead.
func (*TrustParty) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_quorum_proto_rawDescGZIP(), []int{2}
}

func (x *TrustParty) GetParty() string {
	if x != nil {
		return x.Party
	}
	return ""
}

func (x *TrustParty) GetRequiredTrustLevel() TrustLevel {
	if x != nil {
		return x.RequiredTrustLevel
	}
	return TrustLevel_MissingTrustLevel
}

var File_com_digitalasset_canton_protocol_v0_quorum_proto protoreflect.FileDescriptor

const file_com_digitalasset_canton_protocol_v0_quorum_proto_rawDesc = "" +
	"\n" +
	"0com/digitalasset/canton/protocol/v0/quorum.proto\x12#com.digitalasset.canton.protocol.v0\x1a2com/digitalasset/canton/protocol/v0/topology.proto\"\x95\x01\n" +
	"\x06Quorum\x12m\n" +
	"\x16party_index_and_weight\x18\x01 \x03(\v28.com.digitalasset.canton.protocol.v0.PartyIndexAndWeightR\x13partyIndexAndWeight\x12\x1c\n" +
	"\tthreshold\x18\x02 \x01(\x05R\tthreshold\"C\n" +
	"\x13PartyIndexAndWeight\x12\x14\n" +
	"\x05index\x18\x01 \x01(\x05R\x05index\x12\x16\n" +
	"\x06weight\x18\x02 \x01(\x05R\x06weight\"\x85\x01\n" +
	"\n" +
	"TrustParty\x12\x14\n" +
	"\x05party\x18\x01 \x01(\tR\x05party\x12a\n" +
	"\x14required_trust_level\x18\x02 \x01(\x0e2/.com.digitalasset.canton.protocol.v0.TrustLevelR\x12requiredTrustLevelBTZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v0b\x06proto3"

var (
	file_com_digitalasset_canton_protocol_v0_quorum_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_protocol_v0_quorum_proto_rawDescData []byte
)

func file_com_digitalasset_canton_protocol_v0_quorum_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_protocol_v0_quorum_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_protocol_v0_quorum_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_protocol_v0_quorum_proto_rawDesc), len(file_com_digitalasset_canton_protocol_v0_quorum_proto_rawDesc)))
	})
	return file_com_digitalasset_canton_protocol_v0_quorum_proto_rawDescData
}

var file_com_digitalasset_canton_protocol_v0_quorum_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_com_digitalasset_canton_protocol_v0_quorum_proto_goTypes = []any{
	(*Quorum)(nil),              // 0: com.digitalasset.canton.protocol.v0.Quorum
	(*PartyIndexAndWeight)(nil), // 1: com.digitalasset.canton.protocol.v0.PartyIndexAndWeight
	(*TrustParty)(nil),          // 2: com.digitalasset.canton.protocol.v0.TrustParty
	(TrustLevel)(0),             // 3: com.digitalasset.canton.protocol.v0.TrustLevel
}
var file_com_digitalasset_canton_protocol_v0_quorum_proto_depIdxs = []int32{
	1, // 0: com.digitalasset.canton.protocol.v0.Quorum.party_index_and_weight:type_name -> com.digitalasset.canton.protocol.v0.PartyIndexAndWeight
	3, // 1: com.digitalasset.canton.protocol.v0.TrustParty.required_trust_level:type_name -> com.digitalasset.canton.protocol.v0.TrustLevel
	2, // [2:2] is the sub-list for method output_type
	2, // [2:2] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_protocol_v0_quorum_proto_init() }
func file_com_digitalasset_canton_protocol_v0_quorum_proto_init() {
	if File_com_digitalasset_canton_protocol_v0_quorum_proto != nil {
		return
	}
	file_com_digitalasset_canton_protocol_v0_topology_proto_init()
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_protocol_v0_quorum_proto_rawDesc), len(file_com_digitalasset_canton_protocol_v0_quorum_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_protocol_v0_quorum_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_protocol_v0_quorum_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_protocol_v0_quorum_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_protocol_v0_quorum_proto = out.File
	file_com_digitalasset_canton_protocol_v0_quorum_proto_goTypes = nil
	file_com_digitalasset_canton_protocol_v0_quorum_proto_depIdxs = nil
}
