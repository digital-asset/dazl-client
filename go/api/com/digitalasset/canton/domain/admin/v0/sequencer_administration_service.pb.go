// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/domain/admin/v0/sequencer_administration_service.proto

package v0

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
	timestamppb "google.golang.org/protobuf/types/known/timestamppb"
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

type SequencerMemberStatus struct {
	state            protoimpl.MessageState `protogen:"open.v1"`
	Member           string                 `protobuf:"bytes,1,opt,name=member,proto3" json:"member,omitempty"`
	RegisteredAt     *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=registered_at,json=registeredAt,proto3" json:"registered_at,omitempty"`
	LastAcknowledged *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=last_acknowledged,json=lastAcknowledged,proto3" json:"last_acknowledged,omitempty"`
	Enabled          bool                   `protobuf:"varint,4,opt,name=enabled,proto3" json:"enabled,omitempty"`
	unknownFields    protoimpl.UnknownFields
	sizeCache        protoimpl.SizeCache
}

func (x *SequencerMemberStatus) Reset() {
	*x = SequencerMemberStatus{}
	mi := &file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SequencerMemberStatus) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerMemberStatus) ProtoMessage() {}

func (x *SequencerMemberStatus) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SequencerMemberStatus.ProtoReflect.Descriptor instead.
func (*SequencerMemberStatus) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDescGZIP(), []int{0}
}

func (x *SequencerMemberStatus) GetMember() string {
	if x != nil {
		return x.Member
	}
	return ""
}

func (x *SequencerMemberStatus) GetRegisteredAt() *timestamppb.Timestamp {
	if x != nil {
		return x.RegisteredAt
	}
	return nil
}

func (x *SequencerMemberStatus) GetLastAcknowledged() *timestamppb.Timestamp {
	if x != nil {
		return x.LastAcknowledged
	}
	return nil
}

func (x *SequencerMemberStatus) GetEnabled() bool {
	if x != nil {
		return x.Enabled
	}
	return false
}

type SequencerPruningStatus struct {
	state                  protoimpl.MessageState   `protogen:"open.v1"`
	Now                    *timestamppb.Timestamp   `protobuf:"bytes,1,opt,name=now,proto3" json:"now,omitempty"`
	EarliestEventTimestamp *timestamppb.Timestamp   `protobuf:"bytes,2,opt,name=earliest_event_timestamp,json=earliestEventTimestamp,proto3" json:"earliest_event_timestamp,omitempty"`
	Members                []*SequencerMemberStatus `protobuf:"bytes,3,rep,name=members,proto3" json:"members,omitempty"`
	unknownFields          protoimpl.UnknownFields
	sizeCache              protoimpl.SizeCache
}

func (x *SequencerPruningStatus) Reset() {
	*x = SequencerPruningStatus{}
	mi := &file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SequencerPruningStatus) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerPruningStatus) ProtoMessage() {}

func (x *SequencerPruningStatus) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SequencerPruningStatus.ProtoReflect.Descriptor instead.
func (*SequencerPruningStatus) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDescGZIP(), []int{1}
}

func (x *SequencerPruningStatus) GetNow() *timestamppb.Timestamp {
	if x != nil {
		return x.Now
	}
	return nil
}

func (x *SequencerPruningStatus) GetEarliestEventTimestamp() *timestamppb.Timestamp {
	if x != nil {
		return x.EarliestEventTimestamp
	}
	return nil
}

func (x *SequencerPruningStatus) GetMembers() []*SequencerMemberStatus {
	if x != nil {
		return x.Members
	}
	return nil
}

var File_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto protoreflect.FileDescriptor

const file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDesc = "" +
	"\n" +
	"Ncom/digitalasset/canton/domain/admin/v0/sequencer_administration_service.proto\x12'com.digitalasset.canton.domain.admin.v0\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd3\x01\n" +
	"\x15SequencerMemberStatus\x12\x16\n" +
	"\x06member\x18\x01 \x01(\tR\x06member\x12?\n" +
	"\rregistered_at\x18\x02 \x01(\v2\x1a.google.protobuf.TimestampR\fregisteredAt\x12G\n" +
	"\x11last_acknowledged\x18\x03 \x01(\v2\x1a.google.protobuf.TimestampR\x10lastAcknowledged\x12\x18\n" +
	"\aenabled\x18\x04 \x01(\bR\aenabled\"\xf6\x01\n" +
	"\x16SequencerPruningStatus\x12,\n" +
	"\x03now\x18\x01 \x01(\v2\x1a.google.protobuf.TimestampR\x03now\x12T\n" +
	"\x18earliest_event_timestamp\x18\x02 \x01(\v2\x1a.google.protobuf.TimestampR\x16earliestEventTimestamp\x12X\n" +
	"\amembers\x18\x03 \x03(\v2>.com.digitalasset.canton.domain.admin.v0.SequencerMemberStatusR\amembers2\x8a\x01\n" +
	"\x1eSequencerAdministrationService\x12h\n" +
	"\rPruningStatus\x12\x16.google.protobuf.Empty\x1a?.com.digitalasset.canton.domain.admin.v0.SequencerPruningStatusBXZVgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/admin/v0b\x06proto3"

var (
	file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDescData []byte
)

func file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDesc), len(file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDesc)))
	})
	return file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDescData
}

var file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_goTypes = []any{
	(*SequencerMemberStatus)(nil),  // 0: com.digitalasset.canton.domain.admin.v0.SequencerMemberStatus
	(*SequencerPruningStatus)(nil), // 1: com.digitalasset.canton.domain.admin.v0.SequencerPruningStatus
	(*timestamppb.Timestamp)(nil),  // 2: google.protobuf.Timestamp
	(*emptypb.Empty)(nil),          // 3: google.protobuf.Empty
}
var file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_depIdxs = []int32{
	2, // 0: com.digitalasset.canton.domain.admin.v0.SequencerMemberStatus.registered_at:type_name -> google.protobuf.Timestamp
	2, // 1: com.digitalasset.canton.domain.admin.v0.SequencerMemberStatus.last_acknowledged:type_name -> google.protobuf.Timestamp
	2, // 2: com.digitalasset.canton.domain.admin.v0.SequencerPruningStatus.now:type_name -> google.protobuf.Timestamp
	2, // 3: com.digitalasset.canton.domain.admin.v0.SequencerPruningStatus.earliest_event_timestamp:type_name -> google.protobuf.Timestamp
	0, // 4: com.digitalasset.canton.domain.admin.v0.SequencerPruningStatus.members:type_name -> com.digitalasset.canton.domain.admin.v0.SequencerMemberStatus
	3, // 5: com.digitalasset.canton.domain.admin.v0.SequencerAdministrationService.PruningStatus:input_type -> google.protobuf.Empty
	1, // 6: com.digitalasset.canton.domain.admin.v0.SequencerAdministrationService.PruningStatus:output_type -> com.digitalasset.canton.domain.admin.v0.SequencerPruningStatus
	6, // [6:7] is the sub-list for method output_type
	5, // [5:6] is the sub-list for method input_type
	5, // [5:5] is the sub-list for extension type_name
	5, // [5:5] is the sub-list for extension extendee
	0, // [0:5] is the sub-list for field type_name
}

func init() {
	file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_init()
}
func file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_init() {
	if File_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDesc), len(file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto = out.File
	file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_goTypes = nil
	file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_depIdxs = nil
}
