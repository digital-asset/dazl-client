// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/digitalasset/canton/admin/participant/v30/traffic_control_service.proto

package v30

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
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

type TrafficControlStateRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	DomainId string `protobuf:"bytes,1,opt,name=domain_id,json=domainId,proto3" json:"domain_id,omitempty"`
}

func (x *TrafficControlStateRequest) Reset() {
	*x = TrafficControlStateRequest{}
	mi := &file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TrafficControlStateRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TrafficControlStateRequest) ProtoMessage() {}

func (x *TrafficControlStateRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TrafficControlStateRequest.ProtoReflect.Descriptor instead.
func (*TrafficControlStateRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_rawDescGZIP(), []int{0}
}

func (x *TrafficControlStateRequest) GetDomainId() string {
	if x != nil {
		return x.DomainId
	}
	return ""
}

type TrafficControlStateResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	TrafficState *TrafficState `protobuf:"bytes,1,opt,name=traffic_state,json=trafficState,proto3" json:"traffic_state,omitempty"`
}

func (x *TrafficControlStateResponse) Reset() {
	*x = TrafficControlStateResponse{}
	mi := &file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TrafficControlStateResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TrafficControlStateResponse) ProtoMessage() {}

func (x *TrafficControlStateResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TrafficControlStateResponse.ProtoReflect.Descriptor instead.
func (*TrafficControlStateResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_rawDescGZIP(), []int{1}
}

func (x *TrafficControlStateResponse) GetTrafficState() *TrafficState {
	if x != nil {
		return x.TrafficState
	}
	return nil
}

type TrafficState struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ExtraTrafficPurchased int64                   `protobuf:"varint,1,opt,name=extra_traffic_purchased,json=extraTrafficPurchased,proto3" json:"extra_traffic_purchased,omitempty"`
	ExtraTrafficConsumed  int64                   `protobuf:"varint,2,opt,name=extra_traffic_consumed,json=extraTrafficConsumed,proto3" json:"extra_traffic_consumed,omitempty"`
	BaseTrafficRemainder  int64                   `protobuf:"varint,3,opt,name=base_traffic_remainder,json=baseTrafficRemainder,proto3" json:"base_traffic_remainder,omitempty"`
	LastConsumedCost      uint64                  `protobuf:"varint,4,opt,name=last_consumed_cost,json=lastConsumedCost,proto3" json:"last_consumed_cost,omitempty"`
	Timestamp             int64                   `protobuf:"varint,5,opt,name=timestamp,proto3" json:"timestamp,omitempty"`
	Serial                *wrapperspb.UInt32Value `protobuf:"bytes,6,opt,name=serial,proto3" json:"serial,omitempty"`
}

func (x *TrafficState) Reset() {
	*x = TrafficState{}
	mi := &file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TrafficState) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TrafficState) ProtoMessage() {}

func (x *TrafficState) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TrafficState.ProtoReflect.Descriptor instead.
func (*TrafficState) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_rawDescGZIP(), []int{2}
}

func (x *TrafficState) GetExtraTrafficPurchased() int64 {
	if x != nil {
		return x.ExtraTrafficPurchased
	}
	return 0
}

func (x *TrafficState) GetExtraTrafficConsumed() int64 {
	if x != nil {
		return x.ExtraTrafficConsumed
	}
	return 0
}

func (x *TrafficState) GetBaseTrafficRemainder() int64 {
	if x != nil {
		return x.BaseTrafficRemainder
	}
	return 0
}

func (x *TrafficState) GetLastConsumedCost() uint64 {
	if x != nil {
		return x.LastConsumedCost
	}
	return 0
}

func (x *TrafficState) GetTimestamp() int64 {
	if x != nil {
		return x.Timestamp
	}
	return 0
}

func (x *TrafficState) GetSerial() *wrapperspb.UInt32Value {
	if x != nil {
		return x.Serial
	}
	return nil
}

var File_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_rawDesc = []byte{
	0x0a, 0x4b, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f,
	0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x2f, 0x76, 0x33, 0x30, 0x2f,
	0x74, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x5f, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x6f, 0x6c, 0x5f,
	0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x2d, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x70, 0x61, 0x72,
	0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x2e, 0x76, 0x33, 0x30, 0x1a, 0x1e, 0x67, 0x6f,
	0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x77, 0x72,
	0x61, 0x70, 0x70, 0x65, 0x72, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x39, 0x0a, 0x1a,
	0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x6f, 0x6c, 0x53, 0x74,
	0x61, 0x74, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x1b, 0x0a, 0x09, 0x64, 0x6f,
	0x6d, 0x61, 0x69, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x64,
	0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x49, 0x64, 0x22, 0x7f, 0x0a, 0x1b, 0x54, 0x72, 0x61, 0x66, 0x66,
	0x69, 0x63, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x6f, 0x6c, 0x53, 0x74, 0x61, 0x74, 0x65, 0x52, 0x65,
	0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x60, 0x0a, 0x0d, 0x74, 0x72, 0x61, 0x66, 0x66, 0x69,
	0x63, 0x5f, 0x73, 0x74, 0x61, 0x74, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x3b, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x70, 0x61,
	0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x2e, 0x76, 0x33, 0x30, 0x2e, 0x54, 0x72,
	0x61, 0x66, 0x66, 0x69, 0x63, 0x53, 0x74, 0x61, 0x74, 0x65, 0x52, 0x0c, 0x74, 0x72, 0x61, 0x66,
	0x66, 0x69, 0x63, 0x53, 0x74, 0x61, 0x74, 0x65, 0x22, 0xb4, 0x02, 0x0a, 0x0c, 0x54, 0x72, 0x61,
	0x66, 0x66, 0x69, 0x63, 0x53, 0x74, 0x61, 0x74, 0x65, 0x12, 0x36, 0x0a, 0x17, 0x65, 0x78, 0x74,
	0x72, 0x61, 0x5f, 0x74, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x5f, 0x70, 0x75, 0x72, 0x63, 0x68,
	0x61, 0x73, 0x65, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x03, 0x52, 0x15, 0x65, 0x78, 0x74, 0x72,
	0x61, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x50, 0x75, 0x72, 0x63, 0x68, 0x61, 0x73, 0x65,
	0x64, 0x12, 0x34, 0x0a, 0x16, 0x65, 0x78, 0x74, 0x72, 0x61, 0x5f, 0x74, 0x72, 0x61, 0x66, 0x66,
	0x69, 0x63, 0x5f, 0x63, 0x6f, 0x6e, 0x73, 0x75, 0x6d, 0x65, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28,
	0x03, 0x52, 0x14, 0x65, 0x78, 0x74, 0x72, 0x61, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x43,
	0x6f, 0x6e, 0x73, 0x75, 0x6d, 0x65, 0x64, 0x12, 0x34, 0x0a, 0x16, 0x62, 0x61, 0x73, 0x65, 0x5f,
	0x74, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x5f, 0x72, 0x65, 0x6d, 0x61, 0x69, 0x6e, 0x64, 0x65,
	0x72, 0x18, 0x03, 0x20, 0x01, 0x28, 0x03, 0x52, 0x14, 0x62, 0x61, 0x73, 0x65, 0x54, 0x72, 0x61,
	0x66, 0x66, 0x69, 0x63, 0x52, 0x65, 0x6d, 0x61, 0x69, 0x6e, 0x64, 0x65, 0x72, 0x12, 0x2c, 0x0a,
	0x12, 0x6c, 0x61, 0x73, 0x74, 0x5f, 0x63, 0x6f, 0x6e, 0x73, 0x75, 0x6d, 0x65, 0x64, 0x5f, 0x63,
	0x6f, 0x73, 0x74, 0x18, 0x04, 0x20, 0x01, 0x28, 0x04, 0x52, 0x10, 0x6c, 0x61, 0x73, 0x74, 0x43,
	0x6f, 0x6e, 0x73, 0x75, 0x6d, 0x65, 0x64, 0x43, 0x6f, 0x73, 0x74, 0x12, 0x1c, 0x0a, 0x09, 0x74,
	0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x18, 0x05, 0x20, 0x01, 0x28, 0x03, 0x52, 0x09,
	0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x12, 0x34, 0x0a, 0x06, 0x73, 0x65, 0x72,
	0x69, 0x61, 0x6c, 0x18, 0x06, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1c, 0x2e, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x55, 0x49, 0x6e, 0x74,
	0x33, 0x32, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x06, 0x73, 0x65, 0x72, 0x69, 0x61, 0x6c, 0x32,
	0xc6, 0x01, 0x0a, 0x15, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x43, 0x6f, 0x6e, 0x74, 0x72,
	0x6f, 0x6c, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0xac, 0x01, 0x0a, 0x13, 0x54, 0x72,
	0x61, 0x66, 0x66, 0x69, 0x63, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x6f, 0x6c, 0x53, 0x74, 0x61, 0x74,
	0x65, 0x12, 0x49, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x61, 0x64, 0x6d, 0x69,
	0x6e, 0x2e, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x2e, 0x76, 0x33,
	0x30, 0x2e, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x6f, 0x6c,
	0x53, 0x74, 0x61, 0x74, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x4a, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x70, 0x61, 0x72,
	0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x2e, 0x76, 0x33, 0x30, 0x2e, 0x54, 0x72, 0x61,
	0x66, 0x66, 0x69, 0x63, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x6f, 0x6c, 0x53, 0x74, 0x61, 0x74, 0x65,
	0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x42, 0x5e, 0x5a, 0x5c, 0x67, 0x69, 0x74, 0x68,
	0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74,
	0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64,
	0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74,
	0x6f, 0x6e, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69,
	0x70, 0x61, 0x6e, 0x74, 0x2f, 0x76, 0x33, 0x30, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_rawDescData = file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_rawDesc
)

func file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_rawDescData)
	})
	return file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_rawDescData
}

var file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_goTypes = []any{
	(*TrafficControlStateRequest)(nil),  // 0: com.digitalasset.canton.admin.participant.v30.TrafficControlStateRequest
	(*TrafficControlStateResponse)(nil), // 1: com.digitalasset.canton.admin.participant.v30.TrafficControlStateResponse
	(*TrafficState)(nil),                // 2: com.digitalasset.canton.admin.participant.v30.TrafficState
	(*wrapperspb.UInt32Value)(nil),      // 3: google.protobuf.UInt32Value
}
var file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_depIdxs = []int32{
	2, // 0: com.digitalasset.canton.admin.participant.v30.TrafficControlStateResponse.traffic_state:type_name -> com.digitalasset.canton.admin.participant.v30.TrafficState
	3, // 1: com.digitalasset.canton.admin.participant.v30.TrafficState.serial:type_name -> google.protobuf.UInt32Value
	0, // 2: com.digitalasset.canton.admin.participant.v30.TrafficControlService.TrafficControlState:input_type -> com.digitalasset.canton.admin.participant.v30.TrafficControlStateRequest
	1, // 3: com.digitalasset.canton.admin.participant.v30.TrafficControlService.TrafficControlState:output_type -> com.digitalasset.canton.admin.participant.v30.TrafficControlStateResponse
	3, // [3:4] is the sub-list for method output_type
	2, // [2:3] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_init() }
func file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_init() {
	if File_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto = out.File
	file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_rawDesc = nil
	file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_goTypes = nil
	file_com_digitalasset_canton_admin_participant_v30_traffic_control_service_proto_depIdxs = nil
}
