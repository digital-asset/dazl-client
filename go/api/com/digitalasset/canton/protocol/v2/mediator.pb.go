// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/digitalasset/canton/protocol/v2/mediator.proto

package v2

import (
	v0 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v0"
	v1 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v1"
	status "google.golang.org/genproto/googleapis/rpc/status"
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

	RequestId *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
	Verdict   *Verdict               `protobuf:"bytes,2,opt,name=verdict,proto3" json:"verdict,omitempty"`
	RootHash  []byte                 `protobuf:"bytes,3,opt,name=root_hash,json=rootHash,proto3" json:"root_hash,omitempty"`
	DomainId  string                 `protobuf:"bytes,4,opt,name=domain_id,json=domainId,proto3" json:"domain_id,omitempty"`
}

func (x *TransactionResultMessage) Reset() {
	*x = TransactionResultMessage{}
	mi := &file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TransactionResultMessage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransactionResultMessage) ProtoMessage() {}

func (x *TransactionResultMessage) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes[0]
	if x != nil {
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
	return file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDescGZIP(), []int{0}
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

func (x *TransactionResultMessage) GetRootHash() []byte {
	if x != nil {
		return x.RootHash
	}
	return nil
}

func (x *TransactionResultMessage) GetDomainId() string {
	if x != nil {
		return x.DomainId
	}
	return ""
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
	mi := &file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Verdict) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Verdict) ProtoMessage() {}

func (x *Verdict) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes[1]
	if x != nil {
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
	return file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDescGZIP(), []int{1}
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

func (x *Verdict) GetMediatorReject() *v1.MediatorReject {
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
	MediatorReject *v1.MediatorReject `protobuf:"bytes,3,opt,name=mediator_reject,json=mediatorReject,proto3,oneof"`
}

func (*Verdict_Approve) isVerdict_SomeVerdict() {}

func (*Verdict_ParticipantReject) isVerdict_SomeVerdict() {}

func (*Verdict_MediatorReject) isVerdict_SomeVerdict() {}

type ParticipantReject struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Reasons []*RejectionReason `protobuf:"bytes,1,rep,name=reasons,proto3" json:"reasons,omitempty"`
}

func (x *ParticipantReject) Reset() {
	*x = ParticipantReject{}
	mi := &file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ParticipantReject) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ParticipantReject) ProtoMessage() {}

func (x *ParticipantReject) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes[2]
	if x != nil {
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
	return file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDescGZIP(), []int{2}
}

func (x *ParticipantReject) GetReasons() []*RejectionReason {
	if x != nil {
		return x.Reasons
	}
	return nil
}

type RejectionReason struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Parties []string        `protobuf:"bytes,1,rep,name=parties,proto3" json:"parties,omitempty"`
	Reject  *v1.LocalReject `protobuf:"bytes,2,opt,name=reject,proto3" json:"reject,omitempty"`
}

func (x *RejectionReason) Reset() {
	*x = RejectionReason{}
	mi := &file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *RejectionReason) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RejectionReason) ProtoMessage() {}

func (x *RejectionReason) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RejectionReason.ProtoReflect.Descriptor instead.
func (*RejectionReason) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDescGZIP(), []int{3}
}

func (x *RejectionReason) GetParties() []string {
	if x != nil {
		return x.Parties
	}
	return nil
}

func (x *RejectionReason) GetReject() *v1.LocalReject {
	if x != nil {
		return x.Reject
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
	//	*TransferResult_SourceDomain
	//	*TransferResult_TargetDomain
	Domain    isTransferResult_Domain `protobuf_oneof:"domain"`
	Informees []string                `protobuf:"bytes,4,rep,name=informees,proto3" json:"informees,omitempty"`
	Verdict   *Verdict                `protobuf:"bytes,5,opt,name=verdict,proto3" json:"verdict,omitempty"`
}

func (x *TransferResult) Reset() {
	*x = TransferResult{}
	mi := &file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TransferResult) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransferResult) ProtoMessage() {}

func (x *TransferResult) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes[4]
	if x != nil {
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
	return file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDescGZIP(), []int{4}
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

func (x *TransferResult) GetSourceDomain() string {
	if x, ok := x.GetDomain().(*TransferResult_SourceDomain); ok {
		return x.SourceDomain
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

type TransferResult_SourceDomain struct {
	SourceDomain string `protobuf:"bytes,2,opt,name=source_domain,json=sourceDomain,proto3,oneof"`
}

type TransferResult_TargetDomain struct {
	TargetDomain string `protobuf:"bytes,3,opt,name=target_domain,json=targetDomain,proto3,oneof"`
}

func (*TransferResult_SourceDomain) isTransferResult_Domain() {}

func (*TransferResult_TargetDomain) isTransferResult_Domain() {}

type MediatorReject struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Reason *status.Status `protobuf:"bytes,1,opt,name=reason,proto3" json:"reason,omitempty"`
}

func (x *MediatorReject) Reset() {
	*x = MediatorReject{}
	mi := &file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *MediatorReject) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MediatorReject) ProtoMessage() {}

func (x *MediatorReject) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes[5]
	if x != nil {
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
	return file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDescGZIP(), []int{5}
}

func (x *MediatorReject) GetReason() *status.Status {
	if x != nil {
		return x.Reason
	}
	return nil
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
	mi := &file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes[6]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *MalformedMediatorRequestResult) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MalformedMediatorRequestResult) ProtoMessage() {}

func (x *MalformedMediatorRequestResult) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes[6]
	if x != nil {
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
	return file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDescGZIP(), []int{6}
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

var File_com_digitalasset_canton_protocol_v2_mediator_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDesc = []byte{
	0x0a, 0x32, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63,
	0x6f, 0x6c, 0x2f, 0x76, 0x32, 0x2f, 0x6d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x12, 0x23, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61,
	0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x32, 0x1a, 0x30, 0x63, 0x6f, 0x6d, 0x2f, 0x64,
	0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74,
	0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x30, 0x2f, 0x63,
	0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x32, 0x63, 0x6f, 0x6d,
	0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x31,
	0x2f, 0x6d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a,
	0x3b, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65,
	0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f,
	0x6c, 0x2f, 0x76, 0x31, 0x2f, 0x6d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x5f, 0x72, 0x65,
	0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1b, 0x67, 0x6f,
	0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x65, 0x6d,
	0x70, 0x74, 0x79, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c,
	0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73,
	0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x17, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2f, 0x72, 0x70, 0x63, 0x2f, 0x73, 0x74, 0x61, 0x74, 0x75, 0x73, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x22, 0xd7, 0x01, 0x0a, 0x18, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74,
	0x69, 0x6f, 0x6e, 0x52, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65,
	0x12, 0x39, 0x0a, 0x0a, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70,
	0x52, 0x09, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x49, 0x64, 0x12, 0x46, 0x0a, 0x07, 0x76,
	0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2c, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e,
	0x76, 0x32, 0x2e, 0x56, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x52, 0x07, 0x76, 0x65, 0x72, 0x64,
	0x69, 0x63, 0x74, 0x12, 0x1b, 0x0a, 0x09, 0x72, 0x6f, 0x6f, 0x74, 0x5f, 0x68, 0x61, 0x73, 0x68,
	0x18, 0x03, 0x20, 0x01, 0x28, 0x0c, 0x52, 0x08, 0x72, 0x6f, 0x6f, 0x74, 0x48, 0x61, 0x73, 0x68,
	0x12, 0x1b, 0x0a, 0x09, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x04, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x08, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x49, 0x64, 0x22, 0x96, 0x02,
	0x0a, 0x07, 0x56, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x12, 0x32, 0x0a, 0x07, 0x61, 0x70, 0x70,
	0x72, 0x6f, 0x76, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x16, 0x2e, 0x67, 0x6f, 0x6f,
	0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70,
	0x74, 0x79, 0x48, 0x00, 0x52, 0x07, 0x61, 0x70, 0x70, 0x72, 0x6f, 0x76, 0x65, 0x12, 0x67, 0x0a,
	0x12, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x5f, 0x72, 0x65, 0x6a,
	0x65, 0x63, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x36, 0x2e, 0x63, 0x6f, 0x6d, 0x2e,
	0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e,
	0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x32, 0x2e,
	0x50, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x52, 0x65, 0x6a, 0x65, 0x63,
	0x74, 0x48, 0x00, 0x52, 0x11, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74,
	0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x12, 0x5e, 0x0a, 0x0f, 0x6d, 0x65, 0x64, 0x69, 0x61, 0x74,
	0x6f, 0x72, 0x5f, 0x72, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x33, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63,
	0x6f, 0x6c, 0x2e, 0x76, 0x31, 0x2e, 0x4d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x52, 0x65,
	0x6a, 0x65, 0x63, 0x74, 0x48, 0x00, 0x52, 0x0e, 0x6d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72,
	0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x42, 0x0e, 0x0a, 0x0c, 0x73, 0x6f, 0x6d, 0x65, 0x5f, 0x76,
	0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x22, 0x63, 0x0a, 0x11, 0x50, 0x61, 0x72, 0x74, 0x69, 0x63,
	0x69, 0x70, 0x61, 0x6e, 0x74, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x12, 0x4e, 0x0a, 0x07, 0x72,
	0x65, 0x61, 0x73, 0x6f, 0x6e, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x34, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e,
	0x76, 0x32, 0x2e, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x65, 0x61, 0x73,
	0x6f, 0x6e, 0x52, 0x07, 0x72, 0x65, 0x61, 0x73, 0x6f, 0x6e, 0x73, 0x22, 0x75, 0x0a, 0x0f, 0x52,
	0x65, 0x6a, 0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x65, 0x61, 0x73, 0x6f, 0x6e, 0x12, 0x18,
	0x0a, 0x07, 0x70, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x09, 0x52,
	0x07, 0x70, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x12, 0x48, 0x0a, 0x06, 0x72, 0x65, 0x6a, 0x65,
	0x63, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x30, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74,
	0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x31, 0x2e, 0x4c,
	0x6f, 0x63, 0x61, 0x6c, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x52, 0x06, 0x72, 0x65, 0x6a, 0x65,
	0x63, 0x74, 0x22, 0x89, 0x02, 0x0a, 0x0e, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x52,
	0x65, 0x73, 0x75, 0x6c, 0x74, 0x12, 0x39, 0x0a, 0x0a, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74,
	0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65,
	0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x09, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x49, 0x64,
	0x12, 0x25, 0x0a, 0x0d, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x5f, 0x64, 0x6f, 0x6d, 0x61, 0x69,
	0x6e, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52, 0x0c, 0x73, 0x6f, 0x75, 0x72, 0x63,
	0x65, 0x44, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x12, 0x25, 0x0a, 0x0d, 0x74, 0x61, 0x72, 0x67, 0x65,
	0x74, 0x5f, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00,
	0x52, 0x0c, 0x74, 0x61, 0x72, 0x67, 0x65, 0x74, 0x44, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x12, 0x1c,
	0x0a, 0x09, 0x69, 0x6e, 0x66, 0x6f, 0x72, 0x6d, 0x65, 0x65, 0x73, 0x18, 0x04, 0x20, 0x03, 0x28,
	0x09, 0x52, 0x09, 0x69, 0x6e, 0x66, 0x6f, 0x72, 0x6d, 0x65, 0x65, 0x73, 0x12, 0x46, 0x0a, 0x07,
	0x76, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2c, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c,
	0x2e, 0x76, 0x32, 0x2e, 0x56, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x52, 0x07, 0x76, 0x65, 0x72,
	0x64, 0x69, 0x63, 0x74, 0x42, 0x08, 0x0a, 0x06, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x22, 0x3c,
	0x0a, 0x0e, 0x4d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74,
	0x12, 0x2a, 0x0a, 0x06, 0x72, 0x65, 0x61, 0x73, 0x6f, 0x6e, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x12, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x72, 0x70, 0x63, 0x2e, 0x53, 0x74,
	0x61, 0x74, 0x75, 0x73, 0x52, 0x06, 0x72, 0x65, 0x61, 0x73, 0x6f, 0x6e, 0x22, 0x97, 0x02, 0x0a,
	0x1e, 0x4d, 0x61, 0x6c, 0x66, 0x6f, 0x72, 0x6d, 0x65, 0x64, 0x4d, 0x65, 0x64, 0x69, 0x61, 0x74,
	0x6f, 0x72, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x52, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x12,
	0x39, 0x0a, 0x0a, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52,
	0x09, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x49, 0x64, 0x12, 0x1b, 0x0a, 0x09, 0x64, 0x6f,
	0x6d, 0x61, 0x69, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x64,
	0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x49, 0x64, 0x12, 0x4a, 0x0a, 0x09, 0x76, 0x69, 0x65, 0x77, 0x5f,
	0x74, 0x79, 0x70, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x2d, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30,
	0x2e, 0x56, 0x69, 0x65, 0x77, 0x54, 0x79, 0x70, 0x65, 0x52, 0x08, 0x76, 0x69, 0x65, 0x77, 0x54,
	0x79, 0x70, 0x65, 0x12, 0x51, 0x0a, 0x09, 0x72, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e,
	0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x33, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67,
	0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x32, 0x2e, 0x4d, 0x65, 0x64,
	0x69, 0x61, 0x74, 0x6f, 0x72, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x52, 0x09, 0x72, 0x65, 0x6a,
	0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x42, 0x54, 0x5a, 0x52, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62,
	0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76,
	0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67,
	0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e,
	0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x32, 0x62, 0x06, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDescData = file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDesc
)

func file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDescData)
	})
	return file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDescData
}

var file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes = make([]protoimpl.MessageInfo, 7)
var file_com_digitalasset_canton_protocol_v2_mediator_proto_goTypes = []any{
	(*TransactionResultMessage)(nil),       // 0: com.digitalasset.canton.protocol.v2.TransactionResultMessage
	(*Verdict)(nil),                        // 1: com.digitalasset.canton.protocol.v2.Verdict
	(*ParticipantReject)(nil),              // 2: com.digitalasset.canton.protocol.v2.ParticipantReject
	(*RejectionReason)(nil),                // 3: com.digitalasset.canton.protocol.v2.RejectionReason
	(*TransferResult)(nil),                 // 4: com.digitalasset.canton.protocol.v2.TransferResult
	(*MediatorReject)(nil),                 // 5: com.digitalasset.canton.protocol.v2.MediatorReject
	(*MalformedMediatorRequestResult)(nil), // 6: com.digitalasset.canton.protocol.v2.MalformedMediatorRequestResult
	(*timestamppb.Timestamp)(nil),          // 7: google.protobuf.Timestamp
	(*emptypb.Empty)(nil),                  // 8: google.protobuf.Empty
	(*v1.MediatorReject)(nil),              // 9: com.digitalasset.canton.protocol.v1.MediatorReject
	(*v1.LocalReject)(nil),                 // 10: com.digitalasset.canton.protocol.v1.LocalReject
	(*status.Status)(nil),                  // 11: google.rpc.Status
	(v0.ViewType)(0),                       // 12: com.digitalasset.canton.protocol.v0.ViewType
}
var file_com_digitalasset_canton_protocol_v2_mediator_proto_depIdxs = []int32{
	7,  // 0: com.digitalasset.canton.protocol.v2.TransactionResultMessage.request_id:type_name -> google.protobuf.Timestamp
	1,  // 1: com.digitalasset.canton.protocol.v2.TransactionResultMessage.verdict:type_name -> com.digitalasset.canton.protocol.v2.Verdict
	8,  // 2: com.digitalasset.canton.protocol.v2.Verdict.approve:type_name -> google.protobuf.Empty
	2,  // 3: com.digitalasset.canton.protocol.v2.Verdict.participant_reject:type_name -> com.digitalasset.canton.protocol.v2.ParticipantReject
	9,  // 4: com.digitalasset.canton.protocol.v2.Verdict.mediator_reject:type_name -> com.digitalasset.canton.protocol.v1.MediatorReject
	3,  // 5: com.digitalasset.canton.protocol.v2.ParticipantReject.reasons:type_name -> com.digitalasset.canton.protocol.v2.RejectionReason
	10, // 6: com.digitalasset.canton.protocol.v2.RejectionReason.reject:type_name -> com.digitalasset.canton.protocol.v1.LocalReject
	7,  // 7: com.digitalasset.canton.protocol.v2.TransferResult.request_id:type_name -> google.protobuf.Timestamp
	1,  // 8: com.digitalasset.canton.protocol.v2.TransferResult.verdict:type_name -> com.digitalasset.canton.protocol.v2.Verdict
	11, // 9: com.digitalasset.canton.protocol.v2.MediatorReject.reason:type_name -> google.rpc.Status
	7,  // 10: com.digitalasset.canton.protocol.v2.MalformedMediatorRequestResult.request_id:type_name -> google.protobuf.Timestamp
	12, // 11: com.digitalasset.canton.protocol.v2.MalformedMediatorRequestResult.view_type:type_name -> com.digitalasset.canton.protocol.v0.ViewType
	5,  // 12: com.digitalasset.canton.protocol.v2.MalformedMediatorRequestResult.rejection:type_name -> com.digitalasset.canton.protocol.v2.MediatorReject
	13, // [13:13] is the sub-list for method output_type
	13, // [13:13] is the sub-list for method input_type
	13, // [13:13] is the sub-list for extension type_name
	13, // [13:13] is the sub-list for extension extendee
	0,  // [0:13] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_protocol_v2_mediator_proto_init() }
func file_com_digitalasset_canton_protocol_v2_mediator_proto_init() {
	if File_com_digitalasset_canton_protocol_v2_mediator_proto != nil {
		return
	}
	file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes[1].OneofWrappers = []any{
		(*Verdict_Approve)(nil),
		(*Verdict_ParticipantReject)(nil),
		(*Verdict_MediatorReject)(nil),
	}
	file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes[4].OneofWrappers = []any{
		(*TransferResult_SourceDomain)(nil),
		(*TransferResult_TargetDomain)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   7,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_protocol_v2_mediator_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_protocol_v2_mediator_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_protocol_v2_mediator_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_protocol_v2_mediator_proto = out.File
	file_com_digitalasset_canton_protocol_v2_mediator_proto_rawDesc = nil
	file_com_digitalasset_canton_protocol_v2_mediator_proto_goTypes = nil
	file_com_digitalasset_canton_protocol_v2_mediator_proto_depIdxs = nil
}
