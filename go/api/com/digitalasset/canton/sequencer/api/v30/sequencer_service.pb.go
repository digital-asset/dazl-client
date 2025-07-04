// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/sequencer/api/v30/sequencer_service.proto

package v30

import (
	v302 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v30"
	v301 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/topology/admin/v30"
	v30 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/v30"
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

type SendAsyncRequest struct {
	state                   protoimpl.MessageState `protogen:"open.v1"`
	SignedSubmissionRequest []byte                 `protobuf:"bytes,1,opt,name=signed_submission_request,json=signedSubmissionRequest,proto3" json:"signed_submission_request,omitempty"`
	unknownFields           protoimpl.UnknownFields
	sizeCache               protoimpl.SizeCache
}

func (x *SendAsyncRequest) Reset() {
	*x = SendAsyncRequest{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SendAsyncRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SendAsyncRequest) ProtoMessage() {}

func (x *SendAsyncRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SendAsyncRequest.ProtoReflect.Descriptor instead.
func (*SendAsyncRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescGZIP(), []int{0}
}

func (x *SendAsyncRequest) GetSignedSubmissionRequest() []byte {
	if x != nil {
		return x.SignedSubmissionRequest
	}
	return nil
}

type TrafficControlErrorReason struct {
	state         protoimpl.MessageState           `protogen:"open.v1"`
	Error         *TrafficControlErrorReason_Error `protobuf:"bytes,1,opt,name=error,proto3" json:"error,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *TrafficControlErrorReason) Reset() {
	*x = TrafficControlErrorReason{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TrafficControlErrorReason) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TrafficControlErrorReason) ProtoMessage() {}

func (x *TrafficControlErrorReason) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TrafficControlErrorReason.ProtoReflect.Descriptor instead.
func (*TrafficControlErrorReason) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescGZIP(), []int{1}
}

func (x *TrafficControlErrorReason) GetError() *TrafficControlErrorReason_Error {
	if x != nil {
		return x.Error
	}
	return nil
}

type SendAsyncResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SendAsyncResponse) Reset() {
	*x = SendAsyncResponse{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SendAsyncResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SendAsyncResponse) ProtoMessage() {}

func (x *SendAsyncResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SendAsyncResponse.ProtoReflect.Descriptor instead.
func (*SendAsyncResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescGZIP(), []int{2}
}

type SubscriptionRequestV2 struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Member        string                 `protobuf:"bytes,1,opt,name=member,proto3" json:"member,omitempty"`
	Timestamp     *int64                 `protobuf:"varint,2,opt,name=timestamp,proto3,oneof" json:"timestamp,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SubscriptionRequestV2) Reset() {
	*x = SubscriptionRequestV2{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SubscriptionRequestV2) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SubscriptionRequestV2) ProtoMessage() {}

func (x *SubscriptionRequestV2) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SubscriptionRequestV2.ProtoReflect.Descriptor instead.
func (*SubscriptionRequestV2) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescGZIP(), []int{3}
}

func (x *SubscriptionRequestV2) GetMember() string {
	if x != nil {
		return x.Member
	}
	return ""
}

func (x *SubscriptionRequestV2) GetTimestamp() int64 {
	if x != nil && x.Timestamp != nil {
		return *x.Timestamp
	}
	return 0
}

type SubscriptionResponse struct {
	state                protoimpl.MessageState `protogen:"open.v1"`
	SignedSequencedEvent []byte                 `protobuf:"bytes,1,opt,name=signed_sequenced_event,json=signedSequencedEvent,proto3" json:"signed_sequenced_event,omitempty"`
	TraceContext         *v30.TraceContext      `protobuf:"bytes,2,opt,name=trace_context,json=traceContext,proto3" json:"trace_context,omitempty"`
	unknownFields        protoimpl.UnknownFields
	sizeCache            protoimpl.SizeCache
}

func (x *SubscriptionResponse) Reset() {
	*x = SubscriptionResponse{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SubscriptionResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SubscriptionResponse) ProtoMessage() {}

func (x *SubscriptionResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SubscriptionResponse.ProtoReflect.Descriptor instead.
func (*SubscriptionResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescGZIP(), []int{4}
}

func (x *SubscriptionResponse) GetSignedSequencedEvent() []byte {
	if x != nil {
		return x.SignedSequencedEvent
	}
	return nil
}

func (x *SubscriptionResponse) GetTraceContext() *v30.TraceContext {
	if x != nil {
		return x.TraceContext
	}
	return nil
}

type AcknowledgeRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Member        string                 `protobuf:"bytes,1,opt,name=member,proto3" json:"member,omitempty"`
	Timestamp     int64                  `protobuf:"varint,2,opt,name=timestamp,proto3" json:"timestamp,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *AcknowledgeRequest) Reset() {
	*x = AcknowledgeRequest{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *AcknowledgeRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*AcknowledgeRequest) ProtoMessage() {}

func (x *AcknowledgeRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[5]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use AcknowledgeRequest.ProtoReflect.Descriptor instead.
func (*AcknowledgeRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescGZIP(), []int{5}
}

func (x *AcknowledgeRequest) GetMember() string {
	if x != nil {
		return x.Member
	}
	return ""
}

func (x *AcknowledgeRequest) GetTimestamp() int64 {
	if x != nil {
		return x.Timestamp
	}
	return 0
}

type AcknowledgeResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *AcknowledgeResponse) Reset() {
	*x = AcknowledgeResponse{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[6]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *AcknowledgeResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*AcknowledgeResponse) ProtoMessage() {}

func (x *AcknowledgeResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[6]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use AcknowledgeResponse.ProtoReflect.Descriptor instead.
func (*AcknowledgeResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescGZIP(), []int{6}
}

type AcknowledgeSignedRequest struct {
	state                    protoimpl.MessageState `protogen:"open.v1"`
	SignedAcknowledgeRequest []byte                 `protobuf:"bytes,1,opt,name=signed_acknowledge_request,json=signedAcknowledgeRequest,proto3" json:"signed_acknowledge_request,omitempty"`
	unknownFields            protoimpl.UnknownFields
	sizeCache                protoimpl.SizeCache
}

func (x *AcknowledgeSignedRequest) Reset() {
	*x = AcknowledgeSignedRequest{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[7]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *AcknowledgeSignedRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*AcknowledgeSignedRequest) ProtoMessage() {}

func (x *AcknowledgeSignedRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[7]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use AcknowledgeSignedRequest.ProtoReflect.Descriptor instead.
func (*AcknowledgeSignedRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescGZIP(), []int{7}
}

func (x *AcknowledgeSignedRequest) GetSignedAcknowledgeRequest() []byte {
	if x != nil {
		return x.SignedAcknowledgeRequest
	}
	return nil
}

type AcknowledgeSignedResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *AcknowledgeSignedResponse) Reset() {
	*x = AcknowledgeSignedResponse{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[8]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *AcknowledgeSignedResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*AcknowledgeSignedResponse) ProtoMessage() {}

func (x *AcknowledgeSignedResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[8]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use AcknowledgeSignedResponse.ProtoReflect.Descriptor instead.
func (*AcknowledgeSignedResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescGZIP(), []int{8}
}

type DownloadTopologyStateForInitRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Member        string                 `protobuf:"bytes,1,opt,name=member,proto3" json:"member,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *DownloadTopologyStateForInitRequest) Reset() {
	*x = DownloadTopologyStateForInitRequest{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[9]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *DownloadTopologyStateForInitRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DownloadTopologyStateForInitRequest) ProtoMessage() {}

func (x *DownloadTopologyStateForInitRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[9]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DownloadTopologyStateForInitRequest.ProtoReflect.Descriptor instead.
func (*DownloadTopologyStateForInitRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescGZIP(), []int{9}
}

func (x *DownloadTopologyStateForInitRequest) GetMember() string {
	if x != nil {
		return x.Member
	}
	return ""
}

type DownloadTopologyStateForInitResponse struct {
	state                protoimpl.MessageState     `protogen:"open.v1"`
	TopologyTransactions *v301.TopologyTransactions `protobuf:"bytes,1,opt,name=topology_transactions,json=topologyTransactions,proto3" json:"topology_transactions,omitempty"`
	unknownFields        protoimpl.UnknownFields
	sizeCache            protoimpl.SizeCache
}

func (x *DownloadTopologyStateForInitResponse) Reset() {
	*x = DownloadTopologyStateForInitResponse{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[10]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *DownloadTopologyStateForInitResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DownloadTopologyStateForInitResponse) ProtoMessage() {}

func (x *DownloadTopologyStateForInitResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[10]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DownloadTopologyStateForInitResponse.ProtoReflect.Descriptor instead.
func (*DownloadTopologyStateForInitResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescGZIP(), []int{10}
}

func (x *DownloadTopologyStateForInitResponse) GetTopologyTransactions() *v301.TopologyTransactions {
	if x != nil {
		return x.TopologyTransactions
	}
	return nil
}

type GetTrafficStateForMemberRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Member        string                 `protobuf:"bytes,1,opt,name=member,proto3" json:"member,omitempty"`
	Timestamp     int64                  `protobuf:"varint,2,opt,name=timestamp,proto3" json:"timestamp,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetTrafficStateForMemberRequest) Reset() {
	*x = GetTrafficStateForMemberRequest{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[11]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetTrafficStateForMemberRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetTrafficStateForMemberRequest) ProtoMessage() {}

func (x *GetTrafficStateForMemberRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[11]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetTrafficStateForMemberRequest.ProtoReflect.Descriptor instead.
func (*GetTrafficStateForMemberRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescGZIP(), []int{11}
}

func (x *GetTrafficStateForMemberRequest) GetMember() string {
	if x != nil {
		return x.Member
	}
	return ""
}

func (x *GetTrafficStateForMemberRequest) GetTimestamp() int64 {
	if x != nil {
		return x.Timestamp
	}
	return 0
}

type GetTrafficStateForMemberResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	TrafficState  *v302.TrafficState     `protobuf:"bytes,1,opt,name=traffic_state,json=trafficState,proto3" json:"traffic_state,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetTrafficStateForMemberResponse) Reset() {
	*x = GetTrafficStateForMemberResponse{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[12]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetTrafficStateForMemberResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetTrafficStateForMemberResponse) ProtoMessage() {}

func (x *GetTrafficStateForMemberResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[12]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetTrafficStateForMemberResponse.ProtoReflect.Descriptor instead.
func (*GetTrafficStateForMemberResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescGZIP(), []int{12}
}

func (x *GetTrafficStateForMemberResponse) GetTrafficState() *v302.TrafficState {
	if x != nil {
		return x.TrafficState
	}
	return nil
}

type TrafficControlErrorReason_Error struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// Types that are valid to be assigned to Reason:
	//
	//	*TrafficControlErrorReason_Error_InsufficientTraffic
	//	*TrafficControlErrorReason_Error_OutdatedTrafficCost
	Reason        isTrafficControlErrorReason_Error_Reason `protobuf_oneof:"reason"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *TrafficControlErrorReason_Error) Reset() {
	*x = TrafficControlErrorReason_Error{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[13]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TrafficControlErrorReason_Error) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TrafficControlErrorReason_Error) ProtoMessage() {}

func (x *TrafficControlErrorReason_Error) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[13]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TrafficControlErrorReason_Error.ProtoReflect.Descriptor instead.
func (*TrafficControlErrorReason_Error) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescGZIP(), []int{1, 0}
}

func (x *TrafficControlErrorReason_Error) GetReason() isTrafficControlErrorReason_Error_Reason {
	if x != nil {
		return x.Reason
	}
	return nil
}

func (x *TrafficControlErrorReason_Error) GetInsufficientTraffic() string {
	if x != nil {
		if x, ok := x.Reason.(*TrafficControlErrorReason_Error_InsufficientTraffic); ok {
			return x.InsufficientTraffic
		}
	}
	return ""
}

func (x *TrafficControlErrorReason_Error) GetOutdatedTrafficCost() string {
	if x != nil {
		if x, ok := x.Reason.(*TrafficControlErrorReason_Error_OutdatedTrafficCost); ok {
			return x.OutdatedTrafficCost
		}
	}
	return ""
}

type isTrafficControlErrorReason_Error_Reason interface {
	isTrafficControlErrorReason_Error_Reason()
}

type TrafficControlErrorReason_Error_InsufficientTraffic struct {
	InsufficientTraffic string `protobuf:"bytes,1,opt,name=insufficient_traffic,json=insufficientTraffic,proto3,oneof"`
}

type TrafficControlErrorReason_Error_OutdatedTrafficCost struct {
	OutdatedTrafficCost string `protobuf:"bytes,2,opt,name=outdated_traffic_cost,json=outdatedTrafficCost,proto3,oneof"`
}

func (*TrafficControlErrorReason_Error_InsufficientTraffic) isTrafficControlErrorReason_Error_Reason() {
}

func (*TrafficControlErrorReason_Error_OutdatedTrafficCost) isTrafficControlErrorReason_Error_Reason() {
}

var File_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto protoreflect.FileDescriptor

const file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDesc = "" +
	"\n" +
	"Acom/digitalasset/canton/sequencer/api/v30/sequencer_service.proto\x12)com.digitalasset.canton.sequencer.api.v30\x1aEcom/digitalasset/canton/protocol/v30/traffic_control_parameters.proto\x1a7com/digitalasset/canton/topology/admin/v30/common.proto\x1a/com/digitalasset/canton/v30/trace_context.proto\"N\n" +
	"\x10SendAsyncRequest\x12:\n" +
	"\x19signed_submission_request\x18\x01 \x01(\fR\x17signedSubmissionRequest\"\xfb\x01\n" +
	"\x19TrafficControlErrorReason\x12`\n" +
	"\x05error\x18\x01 \x01(\v2J.com.digitalasset.canton.sequencer.api.v30.TrafficControlErrorReason.ErrorR\x05error\x1a|\n" +
	"\x05Error\x123\n" +
	"\x14insufficient_traffic\x18\x01 \x01(\tH\x00R\x13insufficientTraffic\x124\n" +
	"\x15outdated_traffic_cost\x18\x02 \x01(\tH\x00R\x13outdatedTrafficCostB\b\n" +
	"\x06reason\"\x13\n" +
	"\x11SendAsyncResponse\"`\n" +
	"\x15SubscriptionRequestV2\x12\x16\n" +
	"\x06member\x18\x01 \x01(\tR\x06member\x12!\n" +
	"\ttimestamp\x18\x02 \x01(\x03H\x00R\ttimestamp\x88\x01\x01B\f\n" +
	"\n" +
	"_timestamp\"\x9c\x01\n" +
	"\x14SubscriptionResponse\x124\n" +
	"\x16signed_sequenced_event\x18\x01 \x01(\fR\x14signedSequencedEvent\x12N\n" +
	"\rtrace_context\x18\x02 \x01(\v2).com.digitalasset.canton.v30.TraceContextR\ftraceContext\"J\n" +
	"\x12AcknowledgeRequest\x12\x16\n" +
	"\x06member\x18\x01 \x01(\tR\x06member\x12\x1c\n" +
	"\ttimestamp\x18\x02 \x01(\x03R\ttimestamp\"\x15\n" +
	"\x13AcknowledgeResponse\"X\n" +
	"\x18AcknowledgeSignedRequest\x12<\n" +
	"\x1asigned_acknowledge_request\x18\x01 \x01(\fR\x18signedAcknowledgeRequest\"\x1b\n" +
	"\x19AcknowledgeSignedResponse\"=\n" +
	"#DownloadTopologyStateForInitRequest\x12\x16\n" +
	"\x06member\x18\x01 \x01(\tR\x06member\"\x9d\x01\n" +
	"$DownloadTopologyStateForInitResponse\x12u\n" +
	"\x15topology_transactions\x18\x01 \x01(\v2@.com.digitalasset.canton.topology.admin.v30.TopologyTransactionsR\x14topologyTransactions\"W\n" +
	"\x1fGetTrafficStateForMemberRequest\x12\x16\n" +
	"\x06member\x18\x01 \x01(\tR\x06member\x12\x1c\n" +
	"\ttimestamp\x18\x02 \x01(\x03R\ttimestamp\"{\n" +
	" GetTrafficStateForMemberResponse\x12W\n" +
	"\rtraffic_state\x18\x01 \x01(\v22.com.digitalasset.canton.protocol.v30.TrafficStateR\ftrafficState2\xcb\x06\n" +
	"\x10SequencerService\x12\x86\x01\n" +
	"\tSendAsync\x12;.com.digitalasset.canton.sequencer.api.v30.SendAsyncRequest\x1a<.com.digitalasset.canton.sequencer.api.v30.SendAsyncResponse\x12\x92\x01\n" +
	"\vSubscribeV2\x12@.com.digitalasset.canton.sequencer.api.v30.SubscriptionRequestV2\x1a?.com.digitalasset.canton.sequencer.api.v30.SubscriptionResponse0\x01\x12\x9e\x01\n" +
	"\x11AcknowledgeSigned\x12C.com.digitalasset.canton.sequencer.api.v30.AcknowledgeSignedRequest\x1aD.com.digitalasset.canton.sequencer.api.v30.AcknowledgeSignedResponse\x12\xc1\x01\n" +
	"\x1cDownloadTopologyStateForInit\x12N.com.digitalasset.canton.sequencer.api.v30.DownloadTopologyStateForInitRequest\x1aO.com.digitalasset.canton.sequencer.api.v30.DownloadTopologyStateForInitResponse0\x01\x12\xb3\x01\n" +
	"\x18GetTrafficStateForMember\x12J.com.digitalasset.canton.sequencer.api.v30.GetTrafficStateForMemberRequest\x1aK.com.digitalasset.canton.sequencer.api.v30.GetTrafficStateForMemberResponseBZZXgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/sequencer/api/v30b\x06proto3"

var (
	file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescData []byte
)

func file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDesc), len(file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDesc)))
	})
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDescData
}

var file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes = make([]protoimpl.MessageInfo, 14)
var file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_goTypes = []any{
	(*SendAsyncRequest)(nil),                     // 0: com.digitalasset.canton.sequencer.api.v30.SendAsyncRequest
	(*TrafficControlErrorReason)(nil),            // 1: com.digitalasset.canton.sequencer.api.v30.TrafficControlErrorReason
	(*SendAsyncResponse)(nil),                    // 2: com.digitalasset.canton.sequencer.api.v30.SendAsyncResponse
	(*SubscriptionRequestV2)(nil),                // 3: com.digitalasset.canton.sequencer.api.v30.SubscriptionRequestV2
	(*SubscriptionResponse)(nil),                 // 4: com.digitalasset.canton.sequencer.api.v30.SubscriptionResponse
	(*AcknowledgeRequest)(nil),                   // 5: com.digitalasset.canton.sequencer.api.v30.AcknowledgeRequest
	(*AcknowledgeResponse)(nil),                  // 6: com.digitalasset.canton.sequencer.api.v30.AcknowledgeResponse
	(*AcknowledgeSignedRequest)(nil),             // 7: com.digitalasset.canton.sequencer.api.v30.AcknowledgeSignedRequest
	(*AcknowledgeSignedResponse)(nil),            // 8: com.digitalasset.canton.sequencer.api.v30.AcknowledgeSignedResponse
	(*DownloadTopologyStateForInitRequest)(nil),  // 9: com.digitalasset.canton.sequencer.api.v30.DownloadTopologyStateForInitRequest
	(*DownloadTopologyStateForInitResponse)(nil), // 10: com.digitalasset.canton.sequencer.api.v30.DownloadTopologyStateForInitResponse
	(*GetTrafficStateForMemberRequest)(nil),      // 11: com.digitalasset.canton.sequencer.api.v30.GetTrafficStateForMemberRequest
	(*GetTrafficStateForMemberResponse)(nil),     // 12: com.digitalasset.canton.sequencer.api.v30.GetTrafficStateForMemberResponse
	(*TrafficControlErrorReason_Error)(nil),      // 13: com.digitalasset.canton.sequencer.api.v30.TrafficControlErrorReason.Error
	(*v30.TraceContext)(nil),                     // 14: com.digitalasset.canton.v30.TraceContext
	(*v301.TopologyTransactions)(nil),            // 15: com.digitalasset.canton.topology.admin.v30.TopologyTransactions
	(*v302.TrafficState)(nil),                    // 16: com.digitalasset.canton.protocol.v30.TrafficState
}
var file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_depIdxs = []int32{
	13, // 0: com.digitalasset.canton.sequencer.api.v30.TrafficControlErrorReason.error:type_name -> com.digitalasset.canton.sequencer.api.v30.TrafficControlErrorReason.Error
	14, // 1: com.digitalasset.canton.sequencer.api.v30.SubscriptionResponse.trace_context:type_name -> com.digitalasset.canton.v30.TraceContext
	15, // 2: com.digitalasset.canton.sequencer.api.v30.DownloadTopologyStateForInitResponse.topology_transactions:type_name -> com.digitalasset.canton.topology.admin.v30.TopologyTransactions
	16, // 3: com.digitalasset.canton.sequencer.api.v30.GetTrafficStateForMemberResponse.traffic_state:type_name -> com.digitalasset.canton.protocol.v30.TrafficState
	0,  // 4: com.digitalasset.canton.sequencer.api.v30.SequencerService.SendAsync:input_type -> com.digitalasset.canton.sequencer.api.v30.SendAsyncRequest
	3,  // 5: com.digitalasset.canton.sequencer.api.v30.SequencerService.SubscribeV2:input_type -> com.digitalasset.canton.sequencer.api.v30.SubscriptionRequestV2
	7,  // 6: com.digitalasset.canton.sequencer.api.v30.SequencerService.AcknowledgeSigned:input_type -> com.digitalasset.canton.sequencer.api.v30.AcknowledgeSignedRequest
	9,  // 7: com.digitalasset.canton.sequencer.api.v30.SequencerService.DownloadTopologyStateForInit:input_type -> com.digitalasset.canton.sequencer.api.v30.DownloadTopologyStateForInitRequest
	11, // 8: com.digitalasset.canton.sequencer.api.v30.SequencerService.GetTrafficStateForMember:input_type -> com.digitalasset.canton.sequencer.api.v30.GetTrafficStateForMemberRequest
	2,  // 9: com.digitalasset.canton.sequencer.api.v30.SequencerService.SendAsync:output_type -> com.digitalasset.canton.sequencer.api.v30.SendAsyncResponse
	4,  // 10: com.digitalasset.canton.sequencer.api.v30.SequencerService.SubscribeV2:output_type -> com.digitalasset.canton.sequencer.api.v30.SubscriptionResponse
	8,  // 11: com.digitalasset.canton.sequencer.api.v30.SequencerService.AcknowledgeSigned:output_type -> com.digitalasset.canton.sequencer.api.v30.AcknowledgeSignedResponse
	10, // 12: com.digitalasset.canton.sequencer.api.v30.SequencerService.DownloadTopologyStateForInit:output_type -> com.digitalasset.canton.sequencer.api.v30.DownloadTopologyStateForInitResponse
	12, // 13: com.digitalasset.canton.sequencer.api.v30.SequencerService.GetTrafficStateForMember:output_type -> com.digitalasset.canton.sequencer.api.v30.GetTrafficStateForMemberResponse
	9,  // [9:14] is the sub-list for method output_type
	4,  // [4:9] is the sub-list for method input_type
	4,  // [4:4] is the sub-list for extension type_name
	4,  // [4:4] is the sub-list for extension extendee
	0,  // [0:4] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_init() }
func file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_init() {
	if File_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto != nil {
		return
	}
	file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[3].OneofWrappers = []any{}
	file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes[13].OneofWrappers = []any{
		(*TrafficControlErrorReason_Error_InsufficientTraffic)(nil),
		(*TrafficControlErrorReason_Error_OutdatedTrafficCost)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDesc), len(file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   14,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto = out.File
	file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_goTypes = nil
	file_com_digitalasset_canton_sequencer_api_v30_sequencer_service_proto_depIdxs = nil
}
