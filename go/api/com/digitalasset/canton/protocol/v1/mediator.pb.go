// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v5.27.2
// source: com/digitalasset/canton/protocol/v1/mediator.proto

package v1

import (
	v0 "github.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/protocol/v0"
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

type TransactionResultMessage struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	RequestId        *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
	Verdict          *Verdict               `protobuf:"bytes,2,opt,name=verdict,proto3" json:"verdict,omitempty"`
	NotificationTree *InformeeTree          `protobuf:"bytes,5,opt,name=notification_tree,json=notificationTree,proto3" json:"notification_tree,omitempty"`
}

func (x *TransactionResultMessage) Reset() {
	*x = TransactionResultMessage{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TransactionResultMessage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransactionResultMessage) ProtoMessage() {}

func (x *TransactionResultMessage) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TransactionResultMessage.ProtoReflect.Descriptor instead.
func (*TransactionResultMessage) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDescGZIP(), []int{0}
}

func (x *TransactionResultMessage) GetRequestId() *timestamppb.Timestamp {
	if x != nil {
		return x.RequestId
	}
	return nil
}

func (x *TransactionResultMessage) GetVerdict() *Verdict {
	if x != nil {
		return x.Verdict
	}
	return nil
}

func (x *TransactionResultMessage) GetNotificationTree() *InformeeTree {
	if x != nil {
		return x.NotificationTree
	}
	return nil
}

type Verdict struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to SomeVerdict:
	//
	//	*Verdict_Approve
	//	*Verdict_ParticipantReject
	//	*Verdict_MediatorReject
	SomeVerdict isVerdict_SomeVerdict `protobuf_oneof:"some_verdict"`
}

func (x *Verdict) Reset() {
	*x = Verdict{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Verdict) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Verdict) ProtoMessage() {}

func (x *Verdict) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Verdict.ProtoReflect.Descriptor instead.
func (*Verdict) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDescGZIP(), []int{1}
}

func (m *Verdict) GetSomeVerdict() isVerdict_SomeVerdict {
	if m != nil {
		return m.SomeVerdict
	}
	return nil
}

func (x *Verdict) GetApprove() *emptypb.Empty {
	if x, ok := x.GetSomeVerdict().(*Verdict_Approve); ok {
		return x.Approve
	}
	return nil
}

func (x *Verdict) GetParticipantReject() *ParticipantReject {
	if x, ok := x.GetSomeVerdict().(*Verdict_ParticipantReject); ok {
		return x.ParticipantReject
	}
	return nil
}

func (x *Verdict) GetMediatorReject() *MediatorReject {
	if x, ok := x.GetSomeVerdict().(*Verdict_MediatorReject); ok {
		return x.MediatorReject
	}
	return nil
}

type isVerdict_SomeVerdict interface {
	isVerdict_SomeVerdict()
}

type Verdict_Approve struct {
	Approve *emptypb.Empty `protobuf:"bytes,1,opt,name=approve,proto3,oneof"`
}

type Verdict_ParticipantReject struct {
	ParticipantReject *ParticipantReject `protobuf:"bytes,2,opt,name=participant_reject,json=participantReject,proto3,oneof"`
}

type Verdict_MediatorReject struct {
	MediatorReject *MediatorReject `protobuf:"bytes,3,opt,name=mediator_reject,json=mediatorReject,proto3,oneof"`
}

func (*Verdict_Approve) isVerdict_SomeVerdict() {}

func (*Verdict_ParticipantReject) isVerdict_SomeVerdict() {}

func (*Verdict_MediatorReject) isVerdict_SomeVerdict() {}

type InformeeTree struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Tree *GenTransactionTree `protobuf:"bytes,1,opt,name=tree,proto3" json:"tree,omitempty"`
}

func (x *InformeeTree) Reset() {
	*x = InformeeTree{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *InformeeTree) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*InformeeTree) ProtoMessage() {}

func (x *InformeeTree) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use InformeeTree.ProtoReflect.Descriptor instead.
func (*InformeeTree) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDescGZIP(), []int{2}
}

func (x *InformeeTree) GetTree() *GenTransactionTree {
	if x != nil {
		return x.Tree
	}
	return nil
}

type ParticipantReject struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Reasons []*v0.RejectionReason `protobuf:"bytes,1,rep,name=reasons,proto3" json:"reasons,omitempty"`
}

func (x *ParticipantReject) Reset() {
	*x = ParticipantReject{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ParticipantReject) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ParticipantReject) ProtoMessage() {}

func (x *ParticipantReject) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ParticipantReject.ProtoReflect.Descriptor instead.
func (*ParticipantReject) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDescGZIP(), []int{3}
}

func (x *ParticipantReject) GetReasons() []*v0.RejectionReason {
	if x != nil {
		return x.Reasons
	}
	return nil
}

type MediatorReject struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Cause         string `protobuf:"bytes,2,opt,name=cause,proto3" json:"cause,omitempty"`
	ErrorCode     string `protobuf:"bytes,3,opt,name=error_code,json=errorCode,proto3" json:"error_code,omitempty"`
	ErrorCategory uint32 `protobuf:"varint,4,opt,name=error_category,json=errorCategory,proto3" json:"error_category,omitempty"`
}

func (x *MediatorReject) Reset() {
	*x = MediatorReject{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *MediatorReject) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MediatorReject) ProtoMessage() {}

func (x *MediatorReject) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use MediatorReject.ProtoReflect.Descriptor instead.
func (*MediatorReject) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDescGZIP(), []int{4}
}

func (x *MediatorReject) GetCause() string {
	if x != nil {
		return x.Cause
	}
	return ""
}

func (x *MediatorReject) GetErrorCode() string {
	if x != nil {
		return x.ErrorCode
	}
	return ""
}

func (x *MediatorReject) GetErrorCategory() uint32 {
	if x != nil {
		return x.ErrorCategory
	}
	return 0
}

type MalformedMediatorRequestResult struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	RequestId *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
	DomainId  string                 `protobuf:"bytes,2,opt,name=domain_id,json=domainId,proto3" json:"domain_id,omitempty"`
	ViewType  v0.ViewType            `protobuf:"varint,3,opt,name=view_type,json=viewType,proto3,enum=com.digitalasset.canton.protocol.v0.ViewType" json:"view_type,omitempty"`
	Rejection *MediatorReject        `protobuf:"bytes,4,opt,name=rejection,proto3" json:"rejection,omitempty"`
}

func (x *MalformedMediatorRequestResult) Reset() {
	*x = MalformedMediatorRequestResult{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *MalformedMediatorRequestResult) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MalformedMediatorRequestResult) ProtoMessage() {}

func (x *MalformedMediatorRequestResult) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use MalformedMediatorRequestResult.ProtoReflect.Descriptor instead.
func (*MalformedMediatorRequestResult) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDescGZIP(), []int{5}
}

func (x *MalformedMediatorRequestResult) GetRequestId() *timestamppb.Timestamp {
	if x != nil {
		return x.RequestId
	}
	return nil
}

func (x *MalformedMediatorRequestResult) GetDomainId() string {
	if x != nil {
		return x.DomainId
	}
	return ""
}

func (x *MalformedMediatorRequestResult) GetViewType() v0.ViewType {
	if x != nil {
		return x.ViewType
	}
	return v0.ViewType(0)
}

func (x *MalformedMediatorRequestResult) GetRejection() *MediatorReject {
	if x != nil {
		return x.Rejection
	}
	return nil
}

type TransferResult struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	RequestId *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
	// Types that are assignable to Domain:
	//
	//	*TransferResult_OriginDomain
	//	*TransferResult_TargetDomain
	Domain    isTransferResult_Domain `protobuf_oneof:"domain"`
	Informees []string                `protobuf:"bytes,4,rep,name=informees,proto3" json:"informees,omitempty"`
	Verdict   *Verdict                `protobuf:"bytes,5,opt,name=verdict,proto3" json:"verdict,omitempty"`
}

func (x *TransferResult) Reset() {
	*x = TransferResult{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TransferResult) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransferResult) ProtoMessage() {}

func (x *TransferResult) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TransferResult.ProtoReflect.Descriptor instead.
func (*TransferResult) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDescGZIP(), []int{6}
}

func (x *TransferResult) GetRequestId() *timestamppb.Timestamp {
	if x != nil {
		return x.RequestId
	}
	return nil
}

func (m *TransferResult) GetDomain() isTransferResult_Domain {
	if m != nil {
		return m.Domain
	}
	return nil
}

func (x *TransferResult) GetOriginDomain() string {
	if x, ok := x.GetDomain().(*TransferResult_OriginDomain); ok {
		return x.OriginDomain
	}
	return ""
}

func (x *TransferResult) GetTargetDomain() string {
	if x, ok := x.GetDomain().(*TransferResult_TargetDomain); ok {
		return x.TargetDomain
	}
	return ""
}

func (x *TransferResult) GetInformees() []string {
	if x != nil {
		return x.Informees
	}
	return nil
}

func (x *TransferResult) GetVerdict() *Verdict {
	if x != nil {
		return x.Verdict
	}
	return nil
}

type isTransferResult_Domain interface {
	isTransferResult_Domain()
}

type TransferResult_OriginDomain struct {
	OriginDomain string `protobuf:"bytes,2,opt,name=origin_domain,json=originDomain,proto3,oneof"`
}

type TransferResult_TargetDomain struct {
	TargetDomain string `protobuf:"bytes,3,opt,name=target_domain,json=targetDomain,proto3,oneof"`
}

func (*TransferResult_OriginDomain) isTransferResult_Domain() {}

func (*TransferResult_TargetDomain) isTransferResult_Domain() {}

var File_com_digitalasset_canton_protocol_v1_mediator_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDesc = []byte{
	0x0a, 0x32, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63,
	0x6f, 0x6c, 0x2f, 0x76, 0x31, 0x2f, 0x6d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x12, 0x23, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61,
	0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x31, 0x1a, 0x30, 0x63, 0x6f, 0x6d, 0x2f, 0x64,
	0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74,
	0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x30, 0x2f, 0x63,
	0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x32, 0x63, 0x6f, 0x6d,
	0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x30,
	0x2f, 0x6d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a,
	0x30, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65,
	0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f,
	0x6c, 0x2f, 0x76, 0x31, 0x2f, 0x6d, 0x65, 0x72, 0x6b, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x1a, 0x1b, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62,
	0x75, 0x66, 0x2f, 0x65, 0x6d, 0x70, 0x74, 0x79, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1f,
	0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f,
	0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22,
	0xfd, 0x01, 0x0a, 0x18, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x52,
	0x65, 0x73, 0x75, 0x6c, 0x74, 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x12, 0x39, 0x0a, 0x0a,
	0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62,
	0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x09, 0x72, 0x65,
	0x71, 0x75, 0x65, 0x73, 0x74, 0x49, 0x64, 0x12, 0x46, 0x0a, 0x07, 0x76, 0x65, 0x72, 0x64, 0x69,
	0x63, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2c, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74,
	0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x31, 0x2e, 0x56,
	0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x52, 0x07, 0x76, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x12,
	0x5e, 0x0a, 0x11, 0x6e, 0x6f, 0x74, 0x69, 0x66, 0x69, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x5f,
	0x74, 0x72, 0x65, 0x65, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x31, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x31,
	0x2e, 0x49, 0x6e, 0x66, 0x6f, 0x72, 0x6d, 0x65, 0x65, 0x54, 0x72, 0x65, 0x65, 0x52, 0x10, 0x6e,
	0x6f, 0x74, 0x69, 0x66, 0x69, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x54, 0x72, 0x65, 0x65, 0x22,
	0x9c, 0x02, 0x0a, 0x07, 0x56, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x12, 0x32, 0x0a, 0x07, 0x61,
	0x70, 0x70, 0x72, 0x6f, 0x76, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x16, 0x2e, 0x67,
	0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x45,
	0x6d, 0x70, 0x74, 0x79, 0x48, 0x00, 0x52, 0x07, 0x61, 0x70, 0x70, 0x72, 0x6f, 0x76, 0x65, 0x12,
	0x67, 0x0a, 0x12, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x5f, 0x72,
	0x65, 0x6a, 0x65, 0x63, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x36, 0x2e, 0x63, 0x6f,
	0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63,
	0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76,
	0x31, 0x2e, 0x50, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x52, 0x65, 0x6a,
	0x65, 0x63, 0x74, 0x48, 0x00, 0x52, 0x11, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61,
	0x6e, 0x74, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x12, 0x5e, 0x0a, 0x0f, 0x6d, 0x65, 0x64, 0x69,
	0x61, 0x74, 0x6f, 0x72, 0x5f, 0x72, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x18, 0x03, 0x20, 0x01, 0x28,
	0x0b, 0x32, 0x33, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x31, 0x2e, 0x4d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72,
	0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x48, 0x00, 0x52, 0x0e, 0x6d, 0x65, 0x64, 0x69, 0x61, 0x74,
	0x6f, 0x72, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x42, 0x0e, 0x0a, 0x0c, 0x73, 0x6f, 0x6d, 0x65,
	0x5f, 0x76, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x4a, 0x04, 0x08, 0x04, 0x10, 0x05, 0x22, 0x5b,
	0x0a, 0x0c, 0x49, 0x6e, 0x66, 0x6f, 0x72, 0x6d, 0x65, 0x65, 0x54, 0x72, 0x65, 0x65, 0x12, 0x4b,
	0x0a, 0x04, 0x74, 0x72, 0x65, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x37, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e,
	0x76, 0x31, 0x2e, 0x47, 0x65, 0x6e, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f,
	0x6e, 0x54, 0x72, 0x65, 0x65, 0x52, 0x04, 0x74, 0x72, 0x65, 0x65, 0x22, 0x63, 0x0a, 0x11, 0x50,
	0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74,
	0x12, 0x4e, 0x0a, 0x07, 0x72, 0x65, 0x61, 0x73, 0x6f, 0x6e, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28,
	0x0b, 0x32, 0x34, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x69, 0x6f,
	0x6e, 0x52, 0x65, 0x61, 0x73, 0x6f, 0x6e, 0x52, 0x07, 0x72, 0x65, 0x61, 0x73, 0x6f, 0x6e, 0x73,
	0x22, 0x72, 0x0a, 0x0e, 0x4d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x52, 0x65, 0x6a, 0x65,
	0x63, 0x74, 0x12, 0x14, 0x0a, 0x05, 0x63, 0x61, 0x75, 0x73, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x05, 0x63, 0x61, 0x75, 0x73, 0x65, 0x12, 0x1d, 0x0a, 0x0a, 0x65, 0x72, 0x72, 0x6f,
	0x72, 0x5f, 0x63, 0x6f, 0x64, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x65, 0x72,
	0x72, 0x6f, 0x72, 0x43, 0x6f, 0x64, 0x65, 0x12, 0x25, 0x0a, 0x0e, 0x65, 0x72, 0x72, 0x6f, 0x72,
	0x5f, 0x63, 0x61, 0x74, 0x65, 0x67, 0x6f, 0x72, 0x79, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0d, 0x52,
	0x0d, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x43, 0x61, 0x74, 0x65, 0x67, 0x6f, 0x72, 0x79, 0x4a, 0x04,
	0x08, 0x01, 0x10, 0x02, 0x22, 0x97, 0x02, 0x0a, 0x1e, 0x4d, 0x61, 0x6c, 0x66, 0x6f, 0x72, 0x6d,
	0x65, 0x64, 0x4d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x52, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x12, 0x39, 0x0a, 0x0a, 0x72, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f,
	0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69,
	0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x09, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74,
	0x49, 0x64, 0x12, 0x1b, 0x0a, 0x09, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x5f, 0x69, 0x64, 0x18,
	0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x49, 0x64, 0x12,
	0x4a, 0x0a, 0x09, 0x76, 0x69, 0x65, 0x77, 0x5f, 0x74, 0x79, 0x70, 0x65, 0x18, 0x03, 0x20, 0x01,
	0x28, 0x0e, 0x32, 0x2d, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c,
	0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x56, 0x69, 0x65, 0x77, 0x54, 0x79, 0x70,
	0x65, 0x52, 0x08, 0x76, 0x69, 0x65, 0x77, 0x54, 0x79, 0x70, 0x65, 0x12, 0x51, 0x0a, 0x09, 0x72,
	0x65, 0x6a, 0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x33,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65,
	0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f,
	0x6c, 0x2e, 0x76, 0x31, 0x2e, 0x4d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x52, 0x65, 0x6a,
	0x65, 0x63, 0x74, 0x52, 0x09, 0x72, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x22, 0x89,
	0x02, 0x0a, 0x0e, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x52, 0x65, 0x73, 0x75, 0x6c,
	0x74, 0x12, 0x39, 0x0a, 0x0a, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x5f, 0x69, 0x64, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d,
	0x70, 0x52, 0x09, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x49, 0x64, 0x12, 0x25, 0x0a, 0x0d,
	0x6f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x5f, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x18, 0x02, 0x20,
	0x01, 0x28, 0x09, 0x48, 0x00, 0x52, 0x0c, 0x6f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x44, 0x6f, 0x6d,
	0x61, 0x69, 0x6e, 0x12, 0x25, 0x0a, 0x0d, 0x74, 0x61, 0x72, 0x67, 0x65, 0x74, 0x5f, 0x64, 0x6f,
	0x6d, 0x61, 0x69, 0x6e, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52, 0x0c, 0x74, 0x61,
	0x72, 0x67, 0x65, 0x74, 0x44, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x12, 0x1c, 0x0a, 0x09, 0x69, 0x6e,
	0x66, 0x6f, 0x72, 0x6d, 0x65, 0x65, 0x73, 0x18, 0x04, 0x20, 0x03, 0x28, 0x09, 0x52, 0x09, 0x69,
	0x6e, 0x66, 0x6f, 0x72, 0x6d, 0x65, 0x65, 0x73, 0x12, 0x46, 0x0a, 0x07, 0x76, 0x65, 0x72, 0x64,
	0x69, 0x63, 0x74, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2c, 0x2e, 0x63, 0x6f, 0x6d, 0x2e,
	0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e,
	0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x31, 0x2e,
	0x56, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x52, 0x07, 0x76, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74,
	0x42, 0x08, 0x0a, 0x06, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x42, 0x54, 0x5a, 0x52, 0x67, 0x69,
	0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c,
	0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65,
	0x6e, 0x74, 0x2f, 0x76, 0x37, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d,
	0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x31,
	0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDescData = file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDesc
)

func file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDescData)
	})
	return file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDescData
}

var file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes = make([]protoimpl.MessageInfo, 7)
var file_com_digitalasset_canton_protocol_v1_mediator_proto_goTypes = []interface{}{
	(*TransactionResultMessage)(nil),       // 0: com.digitalasset.canton.protocol.v1.TransactionResultMessage
	(*Verdict)(nil),                        // 1: com.digitalasset.canton.protocol.v1.Verdict
	(*InformeeTree)(nil),                   // 2: com.digitalasset.canton.protocol.v1.InformeeTree
	(*ParticipantReject)(nil),              // 3: com.digitalasset.canton.protocol.v1.ParticipantReject
	(*MediatorReject)(nil),                 // 4: com.digitalasset.canton.protocol.v1.MediatorReject
	(*MalformedMediatorRequestResult)(nil), // 5: com.digitalasset.canton.protocol.v1.MalformedMediatorRequestResult
	(*TransferResult)(nil),                 // 6: com.digitalasset.canton.protocol.v1.TransferResult
	(*timestamppb.Timestamp)(nil),          // 7: google.protobuf.Timestamp
	(*emptypb.Empty)(nil),                  // 8: google.protobuf.Empty
	(*GenTransactionTree)(nil),             // 9: com.digitalasset.canton.protocol.v1.GenTransactionTree
	(*v0.RejectionReason)(nil),             // 10: com.digitalasset.canton.protocol.v0.RejectionReason
	(v0.ViewType)(0),                       // 11: com.digitalasset.canton.protocol.v0.ViewType
}
var file_com_digitalasset_canton_protocol_v1_mediator_proto_depIdxs = []int32{
	7,  // 0: com.digitalasset.canton.protocol.v1.TransactionResultMessage.request_id:type_name -> google.protobuf.Timestamp
	1,  // 1: com.digitalasset.canton.protocol.v1.TransactionResultMessage.verdict:type_name -> com.digitalasset.canton.protocol.v1.Verdict
	2,  // 2: com.digitalasset.canton.protocol.v1.TransactionResultMessage.notification_tree:type_name -> com.digitalasset.canton.protocol.v1.InformeeTree
	8,  // 3: com.digitalasset.canton.protocol.v1.Verdict.approve:type_name -> google.protobuf.Empty
	3,  // 4: com.digitalasset.canton.protocol.v1.Verdict.participant_reject:type_name -> com.digitalasset.canton.protocol.v1.ParticipantReject
	4,  // 5: com.digitalasset.canton.protocol.v1.Verdict.mediator_reject:type_name -> com.digitalasset.canton.protocol.v1.MediatorReject
	9,  // 6: com.digitalasset.canton.protocol.v1.InformeeTree.tree:type_name -> com.digitalasset.canton.protocol.v1.GenTransactionTree
	10, // 7: com.digitalasset.canton.protocol.v1.ParticipantReject.reasons:type_name -> com.digitalasset.canton.protocol.v0.RejectionReason
	7,  // 8: com.digitalasset.canton.protocol.v1.MalformedMediatorRequestResult.request_id:type_name -> google.protobuf.Timestamp
	11, // 9: com.digitalasset.canton.protocol.v1.MalformedMediatorRequestResult.view_type:type_name -> com.digitalasset.canton.protocol.v0.ViewType
	4,  // 10: com.digitalasset.canton.protocol.v1.MalformedMediatorRequestResult.rejection:type_name -> com.digitalasset.canton.protocol.v1.MediatorReject
	7,  // 11: com.digitalasset.canton.protocol.v1.TransferResult.request_id:type_name -> google.protobuf.Timestamp
	1,  // 12: com.digitalasset.canton.protocol.v1.TransferResult.verdict:type_name -> com.digitalasset.canton.protocol.v1.Verdict
	13, // [13:13] is the sub-list for method output_type
	13, // [13:13] is the sub-list for method input_type
	13, // [13:13] is the sub-list for extension type_name
	13, // [13:13] is the sub-list for extension extendee
	0,  // [0:13] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_protocol_v1_mediator_proto_init() }
func file_com_digitalasset_canton_protocol_v1_mediator_proto_init() {
	if File_com_digitalasset_canton_protocol_v1_mediator_proto != nil {
		return
	}
	file_com_digitalasset_canton_protocol_v1_merkle_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TransactionResultMessage); i {
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
		file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Verdict); i {
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
		file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*InformeeTree); i {
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
		file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ParticipantReject); i {
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
		file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*MediatorReject); i {
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
		file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*MalformedMediatorRequestResult); i {
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
		file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[6].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TransferResult); i {
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
	file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[1].OneofWrappers = []interface{}{
		(*Verdict_Approve)(nil),
		(*Verdict_ParticipantReject)(nil),
		(*Verdict_MediatorReject)(nil),
	}
	file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes[6].OneofWrappers = []interface{}{
		(*TransferResult_OriginDomain)(nil),
		(*TransferResult_TargetDomain)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   7,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_protocol_v1_mediator_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_protocol_v1_mediator_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_protocol_v1_mediator_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_protocol_v1_mediator_proto = out.File
	file_com_digitalasset_canton_protocol_v1_mediator_proto_rawDesc = nil
	file_com_digitalasset_canton_protocol_v1_mediator_proto_goTypes = nil
	file_com_digitalasset_canton_protocol_v1_mediator_proto_depIdxs = nil
}
