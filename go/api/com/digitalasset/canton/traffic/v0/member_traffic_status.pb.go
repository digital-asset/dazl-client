// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/digitalasset/canton/traffic/v0/member_traffic_status.proto

package v0

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	timestamppb "google.golang.org/protobuf/types/known/timestamppb"
	wrapperspb "google.golang.org/protobuf/types/known/wrapperspb"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type MemberTrafficStatus struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Member                    string                            `protobuf:"bytes,1,opt,name=member,proto3" json:"member,omitempty"`
	TotalExtraTrafficLimit    *wrapperspb.UInt64Value           `protobuf:"bytes,2,opt,name=total_extra_traffic_limit,json=totalExtraTrafficLimit,proto3" json:"total_extra_traffic_limit,omitempty"`
	TotalExtraTrafficConsumed uint64                            `protobuf:"varint,3,opt,name=total_extra_traffic_consumed,json=totalExtraTrafficConsumed,proto3" json:"total_extra_traffic_consumed,omitempty"`
	TopUpEvents               []*MemberTrafficStatus_TopUpEvent `protobuf:"bytes,4,rep,name=top_up_events,json=topUpEvents,proto3" json:"top_up_events,omitempty"`
	Ts                        *timestamppb.Timestamp            `protobuf:"bytes,5,opt,name=ts,proto3" json:"ts,omitempty"`
}

func (x *MemberTrafficStatus) Reset() {
	*x = MemberTrafficStatus{}
	mi := &file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *MemberTrafficStatus) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MemberTrafficStatus) ProtoMessage() {}

func (x *MemberTrafficStatus) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use MemberTrafficStatus.ProtoReflect.Descriptor instead.
func (*MemberTrafficStatus) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_rawDescGZIP(), []int{0}
}

func (x *MemberTrafficStatus) GetMember() string {
	if x != nil {
		return x.Member
	}
	return ""
}

func (x *MemberTrafficStatus) GetTotalExtraTrafficLimit() *wrapperspb.UInt64Value {
	if x != nil {
		return x.TotalExtraTrafficLimit
	}
	return nil
}

func (x *MemberTrafficStatus) GetTotalExtraTrafficConsumed() uint64 {
	if x != nil {
		return x.TotalExtraTrafficConsumed
	}
	return 0
}

func (x *MemberTrafficStatus) GetTopUpEvents() []*MemberTrafficStatus_TopUpEvent {
	if x != nil {
		return x.TopUpEvents
	}
	return nil
}

func (x *MemberTrafficStatus) GetTs() *timestamppb.Timestamp {
	if x != nil {
		return x.Ts
	}
	return nil
}

type MemberTrafficStatus_TopUpEvent struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	EffectiveAt       *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=effective_at,json=effectiveAt,proto3" json:"effective_at,omitempty"`
	Serial            uint32                 `protobuf:"varint,2,opt,name=serial,proto3" json:"serial,omitempty"`
	ExtraTrafficLimit uint64                 `protobuf:"varint,3,opt,name=extra_traffic_limit,json=extraTrafficLimit,proto3" json:"extra_traffic_limit,omitempty"`
}

func (x *MemberTrafficStatus_TopUpEvent) Reset() {
	*x = MemberTrafficStatus_TopUpEvent{}
	mi := &file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *MemberTrafficStatus_TopUpEvent) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MemberTrafficStatus_TopUpEvent) ProtoMessage() {}

func (x *MemberTrafficStatus_TopUpEvent) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use MemberTrafficStatus_TopUpEvent.ProtoReflect.Descriptor instead.
func (*MemberTrafficStatus_TopUpEvent) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_rawDescGZIP(), []int{0, 0}
}

func (x *MemberTrafficStatus_TopUpEvent) GetEffectiveAt() *timestamppb.Timestamp {
	if x != nil {
		return x.EffectiveAt
	}
	return nil
}

func (x *MemberTrafficStatus_TopUpEvent) GetSerial() uint32 {
	if x != nil {
		return x.Serial
	}
	return 0
}

func (x *MemberTrafficStatus_TopUpEvent) GetExtraTrafficLimit() uint64 {
	if x != nil {
		return x.ExtraTrafficLimit
	}
	return 0
}

var File_com_digitalasset_canton_traffic_v0_member_traffic_status_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_rawDesc = []byte{
	0x0a, 0x3e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x74, 0x72, 0x61, 0x66, 0x66, 0x69,
	0x63, 0x2f, 0x76, 0x30, 0x2f, 0x6d, 0x65, 0x6d, 0x62, 0x65, 0x72, 0x5f, 0x74, 0x72, 0x61, 0x66,
	0x66, 0x69, 0x63, 0x5f, 0x73, 0x74, 0x61, 0x74, 0x75, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x12, 0x22, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x74, 0x72, 0x61, 0x66, 0x66, 0x69,
	0x63, 0x2e, 0x76, 0x30, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x77, 0x72, 0x61, 0x70, 0x70, 0x65, 0x72, 0x73, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xf1, 0x03, 0x0a, 0x13, 0x4d, 0x65, 0x6d, 0x62, 0x65, 0x72,
	0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x12, 0x16, 0x0a,
	0x06, 0x6d, 0x65, 0x6d, 0x62, 0x65, 0x72, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x6d,
	0x65, 0x6d, 0x62, 0x65, 0x72, 0x12, 0x57, 0x0a, 0x19, 0x74, 0x6f, 0x74, 0x61, 0x6c, 0x5f, 0x65,
	0x78, 0x74, 0x72, 0x61, 0x5f, 0x74, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x5f, 0x6c, 0x69, 0x6d,
	0x69, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1c, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c,
	0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x55, 0x49, 0x6e, 0x74, 0x36,
	0x34, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x16, 0x74, 0x6f, 0x74, 0x61, 0x6c, 0x45, 0x78, 0x74,
	0x72, 0x61, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x4c, 0x69, 0x6d, 0x69, 0x74, 0x12, 0x3f,
	0x0a, 0x1c, 0x74, 0x6f, 0x74, 0x61, 0x6c, 0x5f, 0x65, 0x78, 0x74, 0x72, 0x61, 0x5f, 0x74, 0x72,
	0x61, 0x66, 0x66, 0x69, 0x63, 0x5f, 0x63, 0x6f, 0x6e, 0x73, 0x75, 0x6d, 0x65, 0x64, 0x18, 0x03,
	0x20, 0x01, 0x28, 0x04, 0x52, 0x19, 0x74, 0x6f, 0x74, 0x61, 0x6c, 0x45, 0x78, 0x74, 0x72, 0x61,
	0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x43, 0x6f, 0x6e, 0x73, 0x75, 0x6d, 0x65, 0x64, 0x12,
	0x66, 0x0a, 0x0d, 0x74, 0x6f, 0x70, 0x5f, 0x75, 0x70, 0x5f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x73,
	0x18, 0x04, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x42, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67,
	0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e,
	0x2e, 0x74, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x2e, 0x76, 0x30, 0x2e, 0x4d, 0x65, 0x6d, 0x62,
	0x65, 0x72, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x2e,
	0x54, 0x6f, 0x70, 0x55, 0x70, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x52, 0x0b, 0x74, 0x6f, 0x70, 0x55,
	0x70, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x73, 0x12, 0x2a, 0x0a, 0x02, 0x74, 0x73, 0x18, 0x05, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52,
	0x02, 0x74, 0x73, 0x1a, 0x93, 0x01, 0x0a, 0x0a, 0x54, 0x6f, 0x70, 0x55, 0x70, 0x45, 0x76, 0x65,
	0x6e, 0x74, 0x12, 0x3d, 0x0a, 0x0c, 0x65, 0x66, 0x66, 0x65, 0x63, 0x74, 0x69, 0x76, 0x65, 0x5f,
	0x61, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c,
	0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73,
	0x74, 0x61, 0x6d, 0x70, 0x52, 0x0b, 0x65, 0x66, 0x66, 0x65, 0x63, 0x74, 0x69, 0x76, 0x65, 0x41,
	0x74, 0x12, 0x16, 0x0a, 0x06, 0x73, 0x65, 0x72, 0x69, 0x61, 0x6c, 0x18, 0x02, 0x20, 0x01, 0x28,
	0x0d, 0x52, 0x06, 0x73, 0x65, 0x72, 0x69, 0x61, 0x6c, 0x12, 0x2e, 0x0a, 0x13, 0x65, 0x78, 0x74,
	0x72, 0x61, 0x5f, 0x74, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x5f, 0x6c, 0x69, 0x6d, 0x69, 0x74,
	0x18, 0x03, 0x20, 0x01, 0x28, 0x04, 0x52, 0x11, 0x65, 0x78, 0x74, 0x72, 0x61, 0x54, 0x72, 0x61,
	0x66, 0x66, 0x69, 0x63, 0x4c, 0x69, 0x6d, 0x69, 0x74, 0x42, 0x53, 0x5a, 0x51, 0x67, 0x69, 0x74,
	0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d,
	0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e,
	0x74, 0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f,
	0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e,
	0x74, 0x6f, 0x6e, 0x2f, 0x74, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x2f, 0x76, 0x30, 0x62, 0x06,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_rawDescData = file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_rawDesc
)

func file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_rawDescData)
	})
	return file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_rawDescData
}

var file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_goTypes = []any{
	(*MemberTrafficStatus)(nil),            // 0: com.digitalasset.canton.traffic.v0.MemberTrafficStatus
	(*MemberTrafficStatus_TopUpEvent)(nil), // 1: com.digitalasset.canton.traffic.v0.MemberTrafficStatus.TopUpEvent
	(*wrapperspb.UInt64Value)(nil),         // 2: google.protobuf.UInt64Value
	(*timestamppb.Timestamp)(nil),          // 3: google.protobuf.Timestamp
}
var file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_depIdxs = []int32{
	2, // 0: com.digitalasset.canton.traffic.v0.MemberTrafficStatus.total_extra_traffic_limit:type_name -> google.protobuf.UInt64Value
	1, // 1: com.digitalasset.canton.traffic.v0.MemberTrafficStatus.top_up_events:type_name -> com.digitalasset.canton.traffic.v0.MemberTrafficStatus.TopUpEvent
	3, // 2: com.digitalasset.canton.traffic.v0.MemberTrafficStatus.ts:type_name -> google.protobuf.Timestamp
	3, // 3: com.digitalasset.canton.traffic.v0.MemberTrafficStatus.TopUpEvent.effective_at:type_name -> google.protobuf.Timestamp
	4, // [4:4] is the sub-list for method output_type
	4, // [4:4] is the sub-list for method input_type
	4, // [4:4] is the sub-list for extension type_name
	4, // [4:4] is the sub-list for extension extendee
	0, // [0:4] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_init() }
func file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_init() {
	if File_com_digitalasset_canton_traffic_v0_member_traffic_status_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_traffic_v0_member_traffic_status_proto = out.File
	file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_rawDesc = nil
	file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_goTypes = nil
	file_com_digitalasset_canton_traffic_v0_member_traffic_status_proto_depIdxs = nil
}
