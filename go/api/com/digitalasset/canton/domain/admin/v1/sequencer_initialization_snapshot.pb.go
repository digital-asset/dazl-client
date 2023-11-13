// Copyright (c) 2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v4.24.3
// source: com/digitalasset/canton/domain/admin/v1/sequencer_initialization_snapshot.proto

package v1

import (
	v02 "github.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/crypto/v0"
	v0 "github.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/domain/admin/v0"
	v01 "github.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/protocol/v0"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
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

type SequencerSnapshot struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	LatestTimestamp *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=latest_timestamp,json=latestTimestamp,proto3" json:"latest_timestamp,omitempty"`
	// Changed from map<string, int64> in v0 to explicit repeated so that we control the order of the entries
	HeadMemberCounters []*SequencerSnapshot_MemberCounter `protobuf:"bytes,2,rep,name=head_member_counters,json=headMemberCounters,proto3" json:"head_member_counters,omitempty"`
	Status             *v0.SequencerPruningStatus         `protobuf:"bytes,3,opt,name=status,proto3" json:"status,omitempty"`
	Additional         *v0.ImplementationSpecificInfo     `protobuf:"bytes,4,opt,name=additional,proto3" json:"additional,omitempty"`
	// New in v1
	InFlightAggregations []*SequencerSnapshot_InFlightAggregationWithId `protobuf:"bytes,5,rep,name=in_flight_aggregations,json=inFlightAggregations,proto3" json:"in_flight_aggregations,omitempty"`
	// New in v1
	TrafficSnapshots []*SequencerSnapshot_MemberTrafficSnapshot `protobuf:"bytes,6,rep,name=traffic_snapshots,json=trafficSnapshots,proto3" json:"traffic_snapshots,omitempty"`
}

func (x *SequencerSnapshot) Reset() {
	*x = SequencerSnapshot{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SequencerSnapshot) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerSnapshot) ProtoMessage() {}

func (x *SequencerSnapshot) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SequencerSnapshot.ProtoReflect.Descriptor instead.
func (*SequencerSnapshot) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDescGZIP(), []int{0}
}

func (x *SequencerSnapshot) GetLatestTimestamp() *timestamppb.Timestamp {
	if x != nil {
		return x.LatestTimestamp
	}
	return nil
}

func (x *SequencerSnapshot) GetHeadMemberCounters() []*SequencerSnapshot_MemberCounter {
	if x != nil {
		return x.HeadMemberCounters
	}
	return nil
}

func (x *SequencerSnapshot) GetStatus() *v0.SequencerPruningStatus {
	if x != nil {
		return x.Status
	}
	return nil
}

func (x *SequencerSnapshot) GetAdditional() *v0.ImplementationSpecificInfo {
	if x != nil {
		return x.Additional
	}
	return nil
}

func (x *SequencerSnapshot) GetInFlightAggregations() []*SequencerSnapshot_InFlightAggregationWithId {
	if x != nil {
		return x.InFlightAggregations
	}
	return nil
}

func (x *SequencerSnapshot) GetTrafficSnapshots() []*SequencerSnapshot_MemberTrafficSnapshot {
	if x != nil {
		return x.TrafficSnapshots
	}
	return nil
}

type SequencerSnapshot_MemberCounter struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Member           string `protobuf:"bytes,1,opt,name=member,proto3" json:"member,omitempty"`
	SequencerCounter int64  `protobuf:"varint,2,opt,name=sequencer_counter,json=sequencerCounter,proto3" json:"sequencer_counter,omitempty"`
}

func (x *SequencerSnapshot_MemberCounter) Reset() {
	*x = SequencerSnapshot_MemberCounter{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SequencerSnapshot_MemberCounter) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerSnapshot_MemberCounter) ProtoMessage() {}

func (x *SequencerSnapshot_MemberCounter) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SequencerSnapshot_MemberCounter.ProtoReflect.Descriptor instead.
func (*SequencerSnapshot_MemberCounter) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDescGZIP(), []int{0, 0}
}

func (x *SequencerSnapshot_MemberCounter) GetMember() string {
	if x != nil {
		return x.Member
	}
	return ""
}

func (x *SequencerSnapshot_MemberCounter) GetSequencerCounter() int64 {
	if x != nil {
		return x.SequencerCounter
	}
	return 0
}

type SequencerSnapshot_InFlightAggregationWithId struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	AggregationId     []byte                                   `protobuf:"bytes,1,opt,name=aggregation_id,json=aggregationId,proto3" json:"aggregation_id,omitempty"`
	AggregationRule   *v01.AggregationRule                     `protobuf:"bytes,2,opt,name=aggregation_rule,json=aggregationRule,proto3" json:"aggregation_rule,omitempty"`
	MaxSequencingTime *timestamppb.Timestamp                   `protobuf:"bytes,3,opt,name=max_sequencing_time,json=maxSequencingTime,proto3" json:"max_sequencing_time,omitempty"`
	AggregatedSenders []*SequencerSnapshot_AggregationBySender `protobuf:"bytes,4,rep,name=aggregated_senders,json=aggregatedSenders,proto3" json:"aggregated_senders,omitempty"`
}

func (x *SequencerSnapshot_InFlightAggregationWithId) Reset() {
	*x = SequencerSnapshot_InFlightAggregationWithId{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SequencerSnapshot_InFlightAggregationWithId) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerSnapshot_InFlightAggregationWithId) ProtoMessage() {}

func (x *SequencerSnapshot_InFlightAggregationWithId) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SequencerSnapshot_InFlightAggregationWithId.ProtoReflect.Descriptor instead.
func (*SequencerSnapshot_InFlightAggregationWithId) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDescGZIP(), []int{0, 1}
}

func (x *SequencerSnapshot_InFlightAggregationWithId) GetAggregationId() []byte {
	if x != nil {
		return x.AggregationId
	}
	return nil
}

func (x *SequencerSnapshot_InFlightAggregationWithId) GetAggregationRule() *v01.AggregationRule {
	if x != nil {
		return x.AggregationRule
	}
	return nil
}

func (x *SequencerSnapshot_InFlightAggregationWithId) GetMaxSequencingTime() *timestamppb.Timestamp {
	if x != nil {
		return x.MaxSequencingTime
	}
	return nil
}

func (x *SequencerSnapshot_InFlightAggregationWithId) GetAggregatedSenders() []*SequencerSnapshot_AggregationBySender {
	if x != nil {
		return x.AggregatedSenders
	}
	return nil
}

type SequencerSnapshot_AggregationBySender struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Sender               string                                     `protobuf:"bytes,1,opt,name=sender,proto3" json:"sender,omitempty"`
	SequencingTimestamp  *timestamppb.Timestamp                     `protobuf:"bytes,2,opt,name=sequencing_timestamp,json=sequencingTimestamp,proto3" json:"sequencing_timestamp,omitempty"`
	SignaturesByEnvelope []*SequencerSnapshot_SignaturesForEnvelope `protobuf:"bytes,3,rep,name=signatures_by_envelope,json=signaturesByEnvelope,proto3" json:"signatures_by_envelope,omitempty"`
}

func (x *SequencerSnapshot_AggregationBySender) Reset() {
	*x = SequencerSnapshot_AggregationBySender{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SequencerSnapshot_AggregationBySender) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerSnapshot_AggregationBySender) ProtoMessage() {}

func (x *SequencerSnapshot_AggregationBySender) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SequencerSnapshot_AggregationBySender.ProtoReflect.Descriptor instead.
func (*SequencerSnapshot_AggregationBySender) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDescGZIP(), []int{0, 2}
}

func (x *SequencerSnapshot_AggregationBySender) GetSender() string {
	if x != nil {
		return x.Sender
	}
	return ""
}

func (x *SequencerSnapshot_AggregationBySender) GetSequencingTimestamp() *timestamppb.Timestamp {
	if x != nil {
		return x.SequencingTimestamp
	}
	return nil
}

func (x *SequencerSnapshot_AggregationBySender) GetSignaturesByEnvelope() []*SequencerSnapshot_SignaturesForEnvelope {
	if x != nil {
		return x.SignaturesByEnvelope
	}
	return nil
}

type SequencerSnapshot_SignaturesForEnvelope struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Signatures []*v02.Signature `protobuf:"bytes,3,rep,name=signatures,proto3" json:"signatures,omitempty"`
}

func (x *SequencerSnapshot_SignaturesForEnvelope) Reset() {
	*x = SequencerSnapshot_SignaturesForEnvelope{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SequencerSnapshot_SignaturesForEnvelope) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerSnapshot_SignaturesForEnvelope) ProtoMessage() {}

func (x *SequencerSnapshot_SignaturesForEnvelope) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SequencerSnapshot_SignaturesForEnvelope.ProtoReflect.Descriptor instead.
func (*SequencerSnapshot_SignaturesForEnvelope) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDescGZIP(), []int{0, 3}
}

func (x *SequencerSnapshot_SignaturesForEnvelope) GetSignatures() []*v02.Signature {
	if x != nil {
		return x.Signatures
	}
	return nil
}

type SequencerSnapshot_MemberTrafficSnapshot struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Member                string                 `protobuf:"bytes,1,opt,name=member,proto3" json:"member,omitempty"`
	ExtraTrafficRemainder uint64                 `protobuf:"varint,2,opt,name=extra_traffic_remainder,json=extraTrafficRemainder,proto3" json:"extra_traffic_remainder,omitempty"`
	ExtraTrafficConsumed  uint64                 `protobuf:"varint,3,opt,name=extra_traffic_consumed,json=extraTrafficConsumed,proto3" json:"extra_traffic_consumed,omitempty"`
	BaseTrafficRemainder  uint64                 `protobuf:"varint,4,opt,name=base_traffic_remainder,json=baseTrafficRemainder,proto3" json:"base_traffic_remainder,omitempty"`
	SequencingTimestamp   *timestamppb.Timestamp `protobuf:"bytes,5,opt,name=sequencing_timestamp,json=sequencingTimestamp,proto3" json:"sequencing_timestamp,omitempty"`
}

func (x *SequencerSnapshot_MemberTrafficSnapshot) Reset() {
	*x = SequencerSnapshot_MemberTrafficSnapshot{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SequencerSnapshot_MemberTrafficSnapshot) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerSnapshot_MemberTrafficSnapshot) ProtoMessage() {}

func (x *SequencerSnapshot_MemberTrafficSnapshot) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SequencerSnapshot_MemberTrafficSnapshot.ProtoReflect.Descriptor instead.
func (*SequencerSnapshot_MemberTrafficSnapshot) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDescGZIP(), []int{0, 4}
}

func (x *SequencerSnapshot_MemberTrafficSnapshot) GetMember() string {
	if x != nil {
		return x.Member
	}
	return ""
}

func (x *SequencerSnapshot_MemberTrafficSnapshot) GetExtraTrafficRemainder() uint64 {
	if x != nil {
		return x.ExtraTrafficRemainder
	}
	return 0
}

func (x *SequencerSnapshot_MemberTrafficSnapshot) GetExtraTrafficConsumed() uint64 {
	if x != nil {
		return x.ExtraTrafficConsumed
	}
	return 0
}

func (x *SequencerSnapshot_MemberTrafficSnapshot) GetBaseTrafficRemainder() uint64 {
	if x != nil {
		return x.BaseTrafficRemainder
	}
	return 0
}

func (x *SequencerSnapshot_MemberTrafficSnapshot) GetSequencingTimestamp() *timestamppb.Timestamp {
	if x != nil {
		return x.SequencingTimestamp
	}
	return nil
}

var File_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDesc = []byte{
	0x0a, 0x4f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e,
	0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x76, 0x31, 0x2f, 0x73, 0x65, 0x71, 0x75, 0x65, 0x6e,
	0x63, 0x65, 0x72, 0x5f, 0x69, 0x6e, 0x69, 0x74, 0x69, 0x61, 0x6c, 0x69, 0x7a, 0x61, 0x74, 0x69,
	0x6f, 0x6e, 0x5f, 0x73, 0x6e, 0x61, 0x70, 0x73, 0x68, 0x6f, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x12, 0x27, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73,
	0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61, 0x69,
	0x6e, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x31, 0x1a, 0x2e, 0x63, 0x6f, 0x6d, 0x2f,
	0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e,
	0x74, 0x6f, 0x6e, 0x2f, 0x63, 0x72, 0x79, 0x70, 0x74, 0x6f, 0x2f, 0x76, 0x30, 0x2f, 0x63, 0x72,
	0x79, 0x70, 0x74, 0x6f, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x4e, 0x63, 0x6f, 0x6d, 0x2f,
	0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e,
	0x74, 0x6f, 0x6e, 0x2f, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e,
	0x2f, 0x76, 0x30, 0x2f, 0x73, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x65, 0x72, 0x5f, 0x61, 0x64,
	0x6d, 0x69, 0x6e, 0x69, 0x73, 0x74, 0x72, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x73, 0x65, 0x72,
	0x76, 0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x4f, 0x63, 0x6f, 0x6d, 0x2f,
	0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e,
	0x74, 0x6f, 0x6e, 0x2f, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e,
	0x2f, 0x76, 0x30, 0x2f, 0x73, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x65, 0x72, 0x5f, 0x69, 0x6e,
	0x69, 0x74, 0x69, 0x61, 0x6c, 0x69, 0x7a, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x73, 0x6e, 0x61,
	0x70, 0x73, 0x68, 0x6f, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x34, 0x63, 0x6f, 0x6d,
	0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x30,
	0x2f, 0x73, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x69, 0x6e, 0x67, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62,
	0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x22, 0xfb, 0x0d, 0x0a, 0x11, 0x53, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x65, 0x72,
	0x53, 0x6e, 0x61, 0x70, 0x73, 0x68, 0x6f, 0x74, 0x12, 0x45, 0x0a, 0x10, 0x6c, 0x61, 0x74, 0x65,
	0x73, 0x74, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x0f,
	0x6c, 0x61, 0x74, 0x65, 0x73, 0x74, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x12,
	0x7a, 0x0a, 0x14, 0x68, 0x65, 0x61, 0x64, 0x5f, 0x6d, 0x65, 0x6d, 0x62, 0x65, 0x72, 0x5f, 0x63,
	0x6f, 0x75, 0x6e, 0x74, 0x65, 0x72, 0x73, 0x18, 0x02, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x48, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2e, 0x61,
	0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x65,
	0x72, 0x53, 0x6e, 0x61, 0x70, 0x73, 0x68, 0x6f, 0x74, 0x2e, 0x4d, 0x65, 0x6d, 0x62, 0x65, 0x72,
	0x43, 0x6f, 0x75, 0x6e, 0x74, 0x65, 0x72, 0x52, 0x12, 0x68, 0x65, 0x61, 0x64, 0x4d, 0x65, 0x6d,
	0x62, 0x65, 0x72, 0x43, 0x6f, 0x75, 0x6e, 0x74, 0x65, 0x72, 0x73, 0x12, 0x57, 0x0a, 0x06, 0x73,
	0x74, 0x61, 0x74, 0x75, 0x73, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x3f, 0x2e, 0x63, 0x6f,
	0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63,
	0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2e, 0x61, 0x64, 0x6d,
	0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x65, 0x72, 0x50,
	0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x52, 0x06, 0x73, 0x74,
	0x61, 0x74, 0x75, 0x73, 0x12, 0x63, 0x0a, 0x0a, 0x61, 0x64, 0x64, 0x69, 0x74, 0x69, 0x6f, 0x6e,
	0x61, 0x6c, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x43, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74,
	0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e,
	0x76, 0x30, 0x2e, 0x49, 0x6d, 0x70, 0x6c, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x61, 0x74, 0x69, 0x6f,
	0x6e, 0x53, 0x70, 0x65, 0x63, 0x69, 0x66, 0x69, 0x63, 0x49, 0x6e, 0x66, 0x6f, 0x52, 0x0a, 0x61,
	0x64, 0x64, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x61, 0x6c, 0x12, 0x8a, 0x01, 0x0a, 0x16, 0x69, 0x6e,
	0x5f, 0x66, 0x6c, 0x69, 0x67, 0x68, 0x74, 0x5f, 0x61, 0x67, 0x67, 0x72, 0x65, 0x67, 0x61, 0x74,
	0x69, 0x6f, 0x6e, 0x73, 0x18, 0x05, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x54, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2e, 0x61, 0x64, 0x6d, 0x69,
	0x6e, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x65, 0x72, 0x53, 0x6e,
	0x61, 0x70, 0x73, 0x68, 0x6f, 0x74, 0x2e, 0x49, 0x6e, 0x46, 0x6c, 0x69, 0x67, 0x68, 0x74, 0x41,
	0x67, 0x67, 0x72, 0x65, 0x67, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x57, 0x69, 0x74, 0x68, 0x49, 0x64,
	0x52, 0x14, 0x69, 0x6e, 0x46, 0x6c, 0x69, 0x67, 0x68, 0x74, 0x41, 0x67, 0x67, 0x72, 0x65, 0x67,
	0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x12, 0x7d, 0x0a, 0x11, 0x74, 0x72, 0x61, 0x66, 0x66, 0x69,
	0x63, 0x5f, 0x73, 0x6e, 0x61, 0x70, 0x73, 0x68, 0x6f, 0x74, 0x73, 0x18, 0x06, 0x20, 0x03, 0x28,
	0x0b, 0x32, 0x50, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61,
	0x69, 0x6e, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x65, 0x71, 0x75,
	0x65, 0x6e, 0x63, 0x65, 0x72, 0x53, 0x6e, 0x61, 0x70, 0x73, 0x68, 0x6f, 0x74, 0x2e, 0x4d, 0x65,
	0x6d, 0x62, 0x65, 0x72, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x53, 0x6e, 0x61, 0x70, 0x73,
	0x68, 0x6f, 0x74, 0x52, 0x10, 0x74, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x53, 0x6e, 0x61, 0x70,
	0x73, 0x68, 0x6f, 0x74, 0x73, 0x1a, 0x54, 0x0a, 0x0d, 0x4d, 0x65, 0x6d, 0x62, 0x65, 0x72, 0x43,
	0x6f, 0x75, 0x6e, 0x74, 0x65, 0x72, 0x12, 0x16, 0x0a, 0x06, 0x6d, 0x65, 0x6d, 0x62, 0x65, 0x72,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x6d, 0x65, 0x6d, 0x62, 0x65, 0x72, 0x12, 0x2b,
	0x0a, 0x11, 0x73, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x65, 0x72, 0x5f, 0x63, 0x6f, 0x75, 0x6e,
	0x74, 0x65, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x03, 0x52, 0x10, 0x73, 0x65, 0x71, 0x75, 0x65,
	0x6e, 0x63, 0x65, 0x72, 0x43, 0x6f, 0x75, 0x6e, 0x74, 0x65, 0x72, 0x1a, 0xee, 0x02, 0x0a, 0x19,
	0x49, 0x6e, 0x46, 0x6c, 0x69, 0x67, 0x68, 0x74, 0x41, 0x67, 0x67, 0x72, 0x65, 0x67, 0x61, 0x74,
	0x69, 0x6f, 0x6e, 0x57, 0x69, 0x74, 0x68, 0x49, 0x64, 0x12, 0x25, 0x0a, 0x0e, 0x61, 0x67, 0x67,
	0x72, 0x65, 0x67, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x0c, 0x52, 0x0d, 0x61, 0x67, 0x67, 0x72, 0x65, 0x67, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x49, 0x64,
	0x12, 0x5f, 0x0a, 0x10, 0x61, 0x67, 0x67, 0x72, 0x65, 0x67, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x5f,
	0x72, 0x75, 0x6c, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x34, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30,
	0x2e, 0x41, 0x67, 0x67, 0x72, 0x65, 0x67, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x75, 0x6c, 0x65,
	0x52, 0x0f, 0x61, 0x67, 0x67, 0x72, 0x65, 0x67, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x75, 0x6c,
	0x65, 0x12, 0x4a, 0x0a, 0x13, 0x6d, 0x61, 0x78, 0x5f, 0x73, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63,
	0x69, 0x6e, 0x67, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a,
	0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66,
	0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x11, 0x6d, 0x61, 0x78, 0x53,
	0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x69, 0x6e, 0x67, 0x54, 0x69, 0x6d, 0x65, 0x12, 0x7d, 0x0a,
	0x12, 0x61, 0x67, 0x67, 0x72, 0x65, 0x67, 0x61, 0x74, 0x65, 0x64, 0x5f, 0x73, 0x65, 0x6e, 0x64,
	0x65, 0x72, 0x73, 0x18, 0x04, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x4e, 0x2e, 0x63, 0x6f, 0x6d, 0x2e,
	0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e,
	0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e,
	0x2e, 0x76, 0x31, 0x2e, 0x53, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x65, 0x72, 0x53, 0x6e, 0x61,
	0x70, 0x73, 0x68, 0x6f, 0x74, 0x2e, 0x41, 0x67, 0x67, 0x72, 0x65, 0x67, 0x61, 0x74, 0x69, 0x6f,
	0x6e, 0x42, 0x79, 0x53, 0x65, 0x6e, 0x64, 0x65, 0x72, 0x52, 0x11, 0x61, 0x67, 0x67, 0x72, 0x65,
	0x67, 0x61, 0x74, 0x65, 0x64, 0x53, 0x65, 0x6e, 0x64, 0x65, 0x72, 0x73, 0x1a, 0x85, 0x02, 0x0a,
	0x13, 0x41, 0x67, 0x67, 0x72, 0x65, 0x67, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x42, 0x79, 0x53, 0x65,
	0x6e, 0x64, 0x65, 0x72, 0x12, 0x16, 0x0a, 0x06, 0x73, 0x65, 0x6e, 0x64, 0x65, 0x72, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x73, 0x65, 0x6e, 0x64, 0x65, 0x72, 0x12, 0x4d, 0x0a, 0x14,
	0x73, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x69, 0x6e, 0x67, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x73,
	0x74, 0x61, 0x6d, 0x70, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f,
	0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d,
	0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x13, 0x73, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x69,
	0x6e, 0x67, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x12, 0x86, 0x01, 0x0a, 0x16,
	0x73, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x75, 0x72, 0x65, 0x73, 0x5f, 0x62, 0x79, 0x5f, 0x65, 0x6e,
	0x76, 0x65, 0x6c, 0x6f, 0x70, 0x65, 0x18, 0x03, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x50, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2e, 0x61, 0x64,
	0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x65, 0x72,
	0x53, 0x6e, 0x61, 0x70, 0x73, 0x68, 0x6f, 0x74, 0x2e, 0x53, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x75,
	0x72, 0x65, 0x73, 0x46, 0x6f, 0x72, 0x45, 0x6e, 0x76, 0x65, 0x6c, 0x6f, 0x70, 0x65, 0x52, 0x14,
	0x73, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x75, 0x72, 0x65, 0x73, 0x42, 0x79, 0x45, 0x6e, 0x76, 0x65,
	0x6c, 0x6f, 0x70, 0x65, 0x1a, 0x65, 0x0a, 0x15, 0x53, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x75, 0x72,
	0x65, 0x73, 0x46, 0x6f, 0x72, 0x45, 0x6e, 0x76, 0x65, 0x6c, 0x6f, 0x70, 0x65, 0x12, 0x4c, 0x0a,
	0x0a, 0x73, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x75, 0x72, 0x65, 0x73, 0x18, 0x03, 0x20, 0x03, 0x28,
	0x0b, 0x32, 0x2c, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x63, 0x72, 0x79, 0x70,
	0x74, 0x6f, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x75, 0x72, 0x65, 0x52,
	0x0a, 0x73, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x75, 0x72, 0x65, 0x73, 0x1a, 0xa2, 0x02, 0x0a, 0x15,
	0x4d, 0x65, 0x6d, 0x62, 0x65, 0x72, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x53, 0x6e, 0x61,
	0x70, 0x73, 0x68, 0x6f, 0x74, 0x12, 0x16, 0x0a, 0x06, 0x6d, 0x65, 0x6d, 0x62, 0x65, 0x72, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x6d, 0x65, 0x6d, 0x62, 0x65, 0x72, 0x12, 0x36, 0x0a,
	0x17, 0x65, 0x78, 0x74, 0x72, 0x61, 0x5f, 0x74, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x5f, 0x72,
	0x65, 0x6d, 0x61, 0x69, 0x6e, 0x64, 0x65, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x04, 0x52, 0x15,
	0x65, 0x78, 0x74, 0x72, 0x61, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x52, 0x65, 0x6d, 0x61,
	0x69, 0x6e, 0x64, 0x65, 0x72, 0x12, 0x34, 0x0a, 0x16, 0x65, 0x78, 0x74, 0x72, 0x61, 0x5f, 0x74,
	0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x5f, 0x63, 0x6f, 0x6e, 0x73, 0x75, 0x6d, 0x65, 0x64, 0x18,
	0x03, 0x20, 0x01, 0x28, 0x04, 0x52, 0x14, 0x65, 0x78, 0x74, 0x72, 0x61, 0x54, 0x72, 0x61, 0x66,
	0x66, 0x69, 0x63, 0x43, 0x6f, 0x6e, 0x73, 0x75, 0x6d, 0x65, 0x64, 0x12, 0x34, 0x0a, 0x16, 0x62,
	0x61, 0x73, 0x65, 0x5f, 0x74, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x5f, 0x72, 0x65, 0x6d, 0x61,
	0x69, 0x6e, 0x64, 0x65, 0x72, 0x18, 0x04, 0x20, 0x01, 0x28, 0x04, 0x52, 0x14, 0x62, 0x61, 0x73,
	0x65, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x52, 0x65, 0x6d, 0x61, 0x69, 0x6e, 0x64, 0x65,
	0x72, 0x12, 0x4d, 0x0a, 0x14, 0x73, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x69, 0x6e, 0x67, 0x5f,
	0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75,
	0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x13, 0x73, 0x65, 0x71,
	0x75, 0x65, 0x6e, 0x63, 0x69, 0x6e, 0x67, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70,
	0x42, 0x58, 0x5a, 0x56, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64,
	0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a,
	0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x37, 0x2f, 0x67, 0x6f, 0x2f, 0x61,
	0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73,
	0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x64, 0x6f, 0x6d, 0x61, 0x69,
	0x6e, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x76, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDescData = file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDesc
)

func file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDescData)
	})
	return file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDescData
}

var file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes = make([]protoimpl.MessageInfo, 6)
var file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_goTypes = []interface{}{
	(*SequencerSnapshot)(nil),                           // 0: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot
	(*SequencerSnapshot_MemberCounter)(nil),             // 1: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.MemberCounter
	(*SequencerSnapshot_InFlightAggregationWithId)(nil), // 2: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.InFlightAggregationWithId
	(*SequencerSnapshot_AggregationBySender)(nil),       // 3: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.AggregationBySender
	(*SequencerSnapshot_SignaturesForEnvelope)(nil),     // 4: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.SignaturesForEnvelope
	(*SequencerSnapshot_MemberTrafficSnapshot)(nil),     // 5: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.MemberTrafficSnapshot
	(*timestamppb.Timestamp)(nil),                       // 6: google.protobuf.Timestamp
	(*v0.SequencerPruningStatus)(nil),                   // 7: com.digitalasset.canton.domain.admin.v0.SequencerPruningStatus
	(*v0.ImplementationSpecificInfo)(nil),               // 8: com.digitalasset.canton.domain.admin.v0.ImplementationSpecificInfo
	(*v01.AggregationRule)(nil),                         // 9: com.digitalasset.canton.protocol.v0.AggregationRule
	(*v02.Signature)(nil),                               // 10: com.digitalasset.canton.crypto.v0.Signature
}
var file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_depIdxs = []int32{
	6,  // 0: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.latest_timestamp:type_name -> google.protobuf.Timestamp
	1,  // 1: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.head_member_counters:type_name -> com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.MemberCounter
	7,  // 2: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.status:type_name -> com.digitalasset.canton.domain.admin.v0.SequencerPruningStatus
	8,  // 3: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.additional:type_name -> com.digitalasset.canton.domain.admin.v0.ImplementationSpecificInfo
	2,  // 4: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.in_flight_aggregations:type_name -> com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.InFlightAggregationWithId
	5,  // 5: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.traffic_snapshots:type_name -> com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.MemberTrafficSnapshot
	9,  // 6: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.InFlightAggregationWithId.aggregation_rule:type_name -> com.digitalasset.canton.protocol.v0.AggregationRule
	6,  // 7: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.InFlightAggregationWithId.max_sequencing_time:type_name -> google.protobuf.Timestamp
	3,  // 8: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.InFlightAggregationWithId.aggregated_senders:type_name -> com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.AggregationBySender
	6,  // 9: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.AggregationBySender.sequencing_timestamp:type_name -> google.protobuf.Timestamp
	4,  // 10: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.AggregationBySender.signatures_by_envelope:type_name -> com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.SignaturesForEnvelope
	10, // 11: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.SignaturesForEnvelope.signatures:type_name -> com.digitalasset.canton.crypto.v0.Signature
	6,  // 12: com.digitalasset.canton.domain.admin.v1.SequencerSnapshot.MemberTrafficSnapshot.sequencing_timestamp:type_name -> google.protobuf.Timestamp
	13, // [13:13] is the sub-list for method output_type
	13, // [13:13] is the sub-list for method input_type
	13, // [13:13] is the sub-list for extension type_name
	13, // [13:13] is the sub-list for extension extendee
	0,  // [0:13] is the sub-list for field type_name
}

func init() {
	file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_init()
}
func file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_init() {
	if File_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SequencerSnapshot); i {
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
		file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SequencerSnapshot_MemberCounter); i {
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
		file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SequencerSnapshot_InFlightAggregationWithId); i {
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
		file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SequencerSnapshot_AggregationBySender); i {
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
		file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SequencerSnapshot_SignaturesForEnvelope); i {
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
		file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SequencerSnapshot_MemberTrafficSnapshot); i {
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
			RawDescriptor: file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   6,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto = out.File
	file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_rawDesc = nil
	file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_goTypes = nil
	file_com_digitalasset_canton_domain_admin_v1_sequencer_initialization_snapshot_proto_depIdxs = nil
}
