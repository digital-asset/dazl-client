// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.34.2
// 	protoc        v5.27.2
// source: com/digitalasset/canton/domain/admin/v0/sequencer_administration_service.proto

package v0

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
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

type SequencerMemberStatus struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Member           string                 `protobuf:"bytes,1,opt,name=member,proto3" json:"member,omitempty"`
	RegisteredAt     *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=registered_at,json=registeredAt,proto3" json:"registered_at,omitempty"`
	LastAcknowledged *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=last_acknowledged,json=lastAcknowledged,proto3" json:"last_acknowledged,omitempty"`
	Enabled          bool                   `protobuf:"varint,4,opt,name=enabled,proto3" json:"enabled,omitempty"`
}

func (x *SequencerMemberStatus) Reset() {
	*x = SequencerMemberStatus{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SequencerMemberStatus) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerMemberStatus) ProtoMessage() {}

func (x *SequencerMemberStatus) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
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
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Now                    *timestamppb.Timestamp   `protobuf:"bytes,1,opt,name=now,proto3" json:"now,omitempty"`
	EarliestEventTimestamp *timestamppb.Timestamp   `protobuf:"bytes,2,opt,name=earliest_event_timestamp,json=earliestEventTimestamp,proto3" json:"earliest_event_timestamp,omitempty"`
	Members                []*SequencerMemberStatus `protobuf:"bytes,3,rep,name=members,proto3" json:"members,omitempty"`
}

func (x *SequencerPruningStatus) Reset() {
	*x = SequencerPruningStatus{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SequencerPruningStatus) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerPruningStatus) ProtoMessage() {}

func (x *SequencerPruningStatus) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
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

var file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDesc = []byte{
	0x0a, 0x4e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e,
	0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x76, 0x30, 0x2f, 0x73, 0x65, 0x71, 0x75, 0x65, 0x6e,
	0x63, 0x65, 0x72, 0x5f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x69, 0x73, 0x74, 0x72, 0x61, 0x74, 0x69,
	0x6f, 0x6e, 0x5f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x12, 0x27, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e,
	0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x1a, 0x1b, 0x67, 0x6f, 0x6f, 0x67, 0x6c,
	0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x65, 0x6d, 0x70, 0x74, 0x79,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d,
	0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xd3, 0x01, 0x0a, 0x15, 0x53, 0x65, 0x71, 0x75,
	0x65, 0x6e, 0x63, 0x65, 0x72, 0x4d, 0x65, 0x6d, 0x62, 0x65, 0x72, 0x53, 0x74, 0x61, 0x74, 0x75,
	0x73, 0x12, 0x16, 0x0a, 0x06, 0x6d, 0x65, 0x6d, 0x62, 0x65, 0x72, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x06, 0x6d, 0x65, 0x6d, 0x62, 0x65, 0x72, 0x12, 0x3f, 0x0a, 0x0d, 0x72, 0x65, 0x67,
	0x69, 0x73, 0x74, 0x65, 0x72, 0x65, 0x64, 0x5f, 0x61, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62,
	0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x0c, 0x72, 0x65,
	0x67, 0x69, 0x73, 0x74, 0x65, 0x72, 0x65, 0x64, 0x41, 0x74, 0x12, 0x47, 0x0a, 0x11, 0x6c, 0x61,
	0x73, 0x74, 0x5f, 0x61, 0x63, 0x6b, 0x6e, 0x6f, 0x77, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x64, 0x18,
	0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d,
	0x70, 0x52, 0x10, 0x6c, 0x61, 0x73, 0x74, 0x41, 0x63, 0x6b, 0x6e, 0x6f, 0x77, 0x6c, 0x65, 0x64,
	0x67, 0x65, 0x64, 0x12, 0x18, 0x0a, 0x07, 0x65, 0x6e, 0x61, 0x62, 0x6c, 0x65, 0x64, 0x18, 0x04,
	0x20, 0x01, 0x28, 0x08, 0x52, 0x07, 0x65, 0x6e, 0x61, 0x62, 0x6c, 0x65, 0x64, 0x22, 0xf6, 0x01,
	0x0a, 0x16, 0x53, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x65, 0x72, 0x50, 0x72, 0x75, 0x6e, 0x69,
	0x6e, 0x67, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x12, 0x2c, 0x0a, 0x03, 0x6e, 0x6f, 0x77, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d,
	0x70, 0x52, 0x03, 0x6e, 0x6f, 0x77, 0x12, 0x54, 0x0a, 0x18, 0x65, 0x61, 0x72, 0x6c, 0x69, 0x65,
	0x73, 0x74, 0x5f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61,
	0x6d, 0x70, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c,
	0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73,
	0x74, 0x61, 0x6d, 0x70, 0x52, 0x16, 0x65, 0x61, 0x72, 0x6c, 0x69, 0x65, 0x73, 0x74, 0x45, 0x76,
	0x65, 0x6e, 0x74, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x12, 0x58, 0x0a, 0x07,
	0x6d, 0x65, 0x6d, 0x62, 0x65, 0x72, 0x73, 0x18, 0x03, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x3e, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2e, 0x61,
	0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x65,
	0x72, 0x4d, 0x65, 0x6d, 0x62, 0x65, 0x72, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x52, 0x07, 0x6d,
	0x65, 0x6d, 0x62, 0x65, 0x72, 0x73, 0x32, 0x8a, 0x01, 0x0a, 0x1e, 0x53, 0x65, 0x71, 0x75, 0x65,
	0x6e, 0x63, 0x65, 0x72, 0x41, 0x64, 0x6d, 0x69, 0x6e, 0x69, 0x73, 0x74, 0x72, 0x61, 0x74, 0x69,
	0x6f, 0x6e, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x68, 0x0a, 0x0d, 0x50, 0x72, 0x75,
	0x6e, 0x69, 0x6e, 0x67, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x12, 0x16, 0x2e, 0x67, 0x6f, 0x6f,
	0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70,
	0x74, 0x79, 0x1a, 0x3f, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c,
	0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d,
	0x61, 0x69, 0x6e, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x65, 0x71,
	0x75, 0x65, 0x6e, 0x63, 0x65, 0x72, 0x50, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x53, 0x74, 0x61,
	0x74, 0x75, 0x73, 0x42, 0x58, 0x5a, 0x56, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f,
	0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f,
	0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x37, 0x2f, 0x67,
	0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61,
	0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x64, 0x6f,
	0x6d, 0x61, 0x69, 0x6e, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x76, 0x30, 0x62, 0x06, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDescData = file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDesc
)

func file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDescData)
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
	if !protoimpl.UnsafeEnabled {
		file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_msgTypes[0].Exporter = func(v any, i int) any {
			switch v := v.(*SequencerMemberStatus); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_msgTypes[1].Exporter = func(v any, i int) any {
			switch v := v.(*SequencerPruningStatus); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDesc,
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
	file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_rawDesc = nil
	file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_goTypes = nil
	file_com_digitalasset_canton_domain_admin_v0_sequencer_administration_service_proto_depIdxs = nil
}
