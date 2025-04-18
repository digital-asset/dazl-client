// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/digitalasset/canton/protocol/v30/mediator.proto

package v30

import (
	status "google.golang.org/genproto/googleapis/rpc/status"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type InformeeTree struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Tree *GenTransactionTree `protobuf:"bytes,1,opt,name=tree,proto3" json:"tree,omitempty"`
}

func (x *InformeeTree) Reset() {
	*x = InformeeTree{}
	mi := &file_com_digitalasset_canton_protocol_v30_mediator_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *InformeeTree) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*InformeeTree) ProtoMessage() {}

func (x *InformeeTree) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v30_mediator_proto_msgTypes[0]
	if x != nil {
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
	return file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDescGZIP(), []int{0}
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

	Reasons []*RejectionReason `protobuf:"bytes,1,rep,name=reasons,proto3" json:"reasons,omitempty"`
}

func (x *ParticipantReject) Reset() {
	*x = ParticipantReject{}
	mi := &file_com_digitalasset_canton_protocol_v30_mediator_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ParticipantReject) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ParticipantReject) ProtoMessage() {}

func (x *ParticipantReject) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v30_mediator_proto_msgTypes[1]
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
	return file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDescGZIP(), []int{1}
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

	Parties []string      `protobuf:"bytes,1,rep,name=parties,proto3" json:"parties,omitempty"`
	Reject  *LocalVerdict `protobuf:"bytes,2,opt,name=reject,proto3" json:"reject,omitempty"`
}

func (x *RejectionReason) Reset() {
	*x = RejectionReason{}
	mi := &file_com_digitalasset_canton_protocol_v30_mediator_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *RejectionReason) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RejectionReason) ProtoMessage() {}

func (x *RejectionReason) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v30_mediator_proto_msgTypes[2]
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
	return file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDescGZIP(), []int{2}
}

func (x *RejectionReason) GetParties() []string {
	if x != nil {
		return x.Parties
	}
	return nil
}

func (x *RejectionReason) GetReject() *LocalVerdict {
	if x != nil {
		return x.Reject
	}
	return nil
}

type MediatorReject struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Reason      *status.Status `protobuf:"bytes,1,opt,name=reason,proto3" json:"reason,omitempty"`
	IsMalformed bool           `protobuf:"varint,2,opt,name=is_malformed,json=isMalformed,proto3" json:"is_malformed,omitempty"`
}

func (x *MediatorReject) Reset() {
	*x = MediatorReject{}
	mi := &file_com_digitalasset_canton_protocol_v30_mediator_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *MediatorReject) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MediatorReject) ProtoMessage() {}

func (x *MediatorReject) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v30_mediator_proto_msgTypes[3]
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
	return file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDescGZIP(), []int{3}
}

func (x *MediatorReject) GetReason() *status.Status {
	if x != nil {
		return x.Reason
	}
	return nil
}

func (x *MediatorReject) GetIsMalformed() bool {
	if x != nil {
		return x.IsMalformed
	}
	return false
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
	mi := &file_com_digitalasset_canton_protocol_v30_mediator_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Verdict) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Verdict) ProtoMessage() {}

func (x *Verdict) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v30_mediator_proto_msgTypes[4]
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
	return file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDescGZIP(), []int{4}
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

type ConfirmationResultMessage struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	DomainId  string   `protobuf:"bytes,1,opt,name=domain_id,json=domainId,proto3" json:"domain_id,omitempty"`
	ViewType  ViewType `protobuf:"varint,2,opt,name=view_type,json=viewType,proto3,enum=com.digitalasset.canton.protocol.v30.ViewType" json:"view_type,omitempty"`
	RequestId int64    `protobuf:"varint,3,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
	RootHash  []byte   `protobuf:"bytes,4,opt,name=root_hash,json=rootHash,proto3" json:"root_hash,omitempty"`
	Verdict   *Verdict `protobuf:"bytes,5,opt,name=verdict,proto3" json:"verdict,omitempty"`
	Informees []string `protobuf:"bytes,6,rep,name=informees,proto3" json:"informees,omitempty"`
}

func (x *ConfirmationResultMessage) Reset() {
	*x = ConfirmationResultMessage{}
	mi := &file_com_digitalasset_canton_protocol_v30_mediator_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ConfirmationResultMessage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ConfirmationResultMessage) ProtoMessage() {}

func (x *ConfirmationResultMessage) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v30_mediator_proto_msgTypes[5]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ConfirmationResultMessage.ProtoReflect.Descriptor instead.
func (*ConfirmationResultMessage) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDescGZIP(), []int{5}
}

func (x *ConfirmationResultMessage) GetDomainId() string {
	if x != nil {
		return x.DomainId
	}
	return ""
}

func (x *ConfirmationResultMessage) GetViewType() ViewType {
	if x != nil {
		return x.ViewType
	}
	return ViewType_VIEW_TYPE_UNSPECIFIED
}

func (x *ConfirmationResultMessage) GetRequestId() int64 {
	if x != nil {
		return x.RequestId
	}
	return 0
}

func (x *ConfirmationResultMessage) GetRootHash() []byte {
	if x != nil {
		return x.RootHash
	}
	return nil
}

func (x *ConfirmationResultMessage) GetVerdict() *Verdict {
	if x != nil {
		return x.Verdict
	}
	return nil
}

func (x *ConfirmationResultMessage) GetInformees() []string {
	if x != nil {
		return x.Informees
	}
	return nil
}

var File_com_digitalasset_canton_protocol_v30_mediator_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDesc = []byte{
	0x0a, 0x33, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63,
	0x6f, 0x6c, 0x2f, 0x76, 0x33, 0x30, 0x2f, 0x6d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x24, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74,
	0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x33, 0x30, 0x1a, 0x31, 0x63, 0x6f, 0x6d,
	0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x33,
	0x30, 0x2f, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x40,
	0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c,
	0x2f, 0x76, 0x33, 0x30, 0x2f, 0x63, 0x6f, 0x6e, 0x66, 0x69, 0x72, 0x6d, 0x61, 0x74, 0x69, 0x6f,
	0x6e, 0x5f, 0x72, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x1a, 0x31, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63,
	0x6f, 0x6c, 0x2f, 0x76, 0x33, 0x30, 0x2f, 0x6d, 0x65, 0x72, 0x6b, 0x6c, 0x65, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x1a, 0x1b, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x62, 0x75, 0x66, 0x2f, 0x65, 0x6d, 0x70, 0x74, 0x79, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x1a, 0x17, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x72, 0x70, 0x63, 0x2f, 0x73, 0x74, 0x61,
	0x74, 0x75, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x5c, 0x0a, 0x0c, 0x49, 0x6e, 0x66,
	0x6f, 0x72, 0x6d, 0x65, 0x65, 0x54, 0x72, 0x65, 0x65, 0x12, 0x4c, 0x0a, 0x04, 0x74, 0x72, 0x65,
	0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x38, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69,
	0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f,
	0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x33, 0x30, 0x2e, 0x47,
	0x65, 0x6e, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x54, 0x72, 0x65,
	0x65, 0x52, 0x04, 0x74, 0x72, 0x65, 0x65, 0x22, 0x64, 0x0a, 0x11, 0x50, 0x61, 0x72, 0x74, 0x69,
	0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x12, 0x4f, 0x0a, 0x07,
	0x72, 0x65, 0x61, 0x73, 0x6f, 0x6e, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x35, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c,
	0x2e, 0x76, 0x33, 0x30, 0x2e, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x65,
	0x61, 0x73, 0x6f, 0x6e, 0x52, 0x07, 0x72, 0x65, 0x61, 0x73, 0x6f, 0x6e, 0x73, 0x22, 0x77, 0x0a,
	0x0f, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x65, 0x61, 0x73, 0x6f, 0x6e,
	0x12, 0x18, 0x0a, 0x07, 0x70, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28,
	0x09, 0x52, 0x07, 0x70, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x12, 0x4a, 0x0a, 0x06, 0x72, 0x65,
	0x6a, 0x65, 0x63, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x32, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x33,
	0x30, 0x2e, 0x4c, 0x6f, 0x63, 0x61, 0x6c, 0x56, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x52, 0x06,
	0x72, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x22, 0x5f, 0x0a, 0x0e, 0x4d, 0x65, 0x64, 0x69, 0x61, 0x74,
	0x6f, 0x72, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x12, 0x2a, 0x0a, 0x06, 0x72, 0x65, 0x61, 0x73,
	0x6f, 0x6e, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x12, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c,
	0x65, 0x2e, 0x72, 0x70, 0x63, 0x2e, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x52, 0x06, 0x72, 0x65,
	0x61, 0x73, 0x6f, 0x6e, 0x12, 0x21, 0x0a, 0x0c, 0x69, 0x73, 0x5f, 0x6d, 0x61, 0x6c, 0x66, 0x6f,
	0x72, 0x6d, 0x65, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x08, 0x52, 0x0b, 0x69, 0x73, 0x4d, 0x61,
	0x6c, 0x66, 0x6f, 0x72, 0x6d, 0x65, 0x64, 0x22, 0x98, 0x02, 0x0a, 0x07, 0x56, 0x65, 0x72, 0x64,
	0x69, 0x63, 0x74, 0x12, 0x32, 0x0a, 0x07, 0x61, 0x70, 0x70, 0x72, 0x6f, 0x76, 0x65, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x48, 0x00, 0x52, 0x07,
	0x61, 0x70, 0x70, 0x72, 0x6f, 0x76, 0x65, 0x12, 0x68, 0x0a, 0x12, 0x70, 0x61, 0x72, 0x74, 0x69,
	0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x5f, 0x72, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x18, 0x02, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x37, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61,
	0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x33, 0x30, 0x2e, 0x50, 0x61, 0x72, 0x74, 0x69,
	0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x48, 0x00, 0x52, 0x11,
	0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x52, 0x65, 0x6a, 0x65, 0x63,
	0x74, 0x12, 0x5f, 0x0a, 0x0f, 0x6d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x5f, 0x72, 0x65,
	0x6a, 0x65, 0x63, 0x74, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x34, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x33,
	0x30, 0x2e, 0x4d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74,
	0x48, 0x00, 0x52, 0x0e, 0x6d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x52, 0x65, 0x6a, 0x65,
	0x63, 0x74, 0x42, 0x0e, 0x0a, 0x0c, 0x73, 0x6f, 0x6d, 0x65, 0x5f, 0x76, 0x65, 0x72, 0x64, 0x69,
	0x63, 0x74, 0x22, 0xa8, 0x02, 0x0a, 0x19, 0x43, 0x6f, 0x6e, 0x66, 0x69, 0x72, 0x6d, 0x61, 0x74,
	0x69, 0x6f, 0x6e, 0x52, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65,
	0x12, 0x1b, 0x0a, 0x09, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x08, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x49, 0x64, 0x12, 0x4b, 0x0a,
	0x09, 0x76, 0x69, 0x65, 0x77, 0x5f, 0x74, 0x79, 0x70, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0e,
	0x32, 0x2e, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73,
	0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x33, 0x30, 0x2e, 0x56, 0x69, 0x65, 0x77, 0x54, 0x79, 0x70, 0x65,
	0x52, 0x08, 0x76, 0x69, 0x65, 0x77, 0x54, 0x79, 0x70, 0x65, 0x12, 0x1d, 0x0a, 0x0a, 0x72, 0x65,
	0x71, 0x75, 0x65, 0x73, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x03, 0x20, 0x01, 0x28, 0x03, 0x52, 0x09,
	0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x49, 0x64, 0x12, 0x1b, 0x0a, 0x09, 0x72, 0x6f, 0x6f,
	0x74, 0x5f, 0x68, 0x61, 0x73, 0x68, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0c, 0x52, 0x08, 0x72, 0x6f,
	0x6f, 0x74, 0x48, 0x61, 0x73, 0x68, 0x12, 0x47, 0x0a, 0x07, 0x76, 0x65, 0x72, 0x64, 0x69, 0x63,
	0x74, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2d, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69,
	0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f,
	0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x33, 0x30, 0x2e, 0x56,
	0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x52, 0x07, 0x76, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x12,
	0x1c, 0x0a, 0x09, 0x69, 0x6e, 0x66, 0x6f, 0x72, 0x6d, 0x65, 0x65, 0x73, 0x18, 0x06, 0x20, 0x03,
	0x28, 0x09, 0x52, 0x09, 0x69, 0x6e, 0x66, 0x6f, 0x72, 0x6d, 0x65, 0x65, 0x73, 0x42, 0x55, 0x5a,
	0x53, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69,
	0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63,
	0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f,
	0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c,
	0x2f, 0x76, 0x33, 0x30, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDescData = file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDesc
)

func file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDescData)
	})
	return file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDescData
}

var file_com_digitalasset_canton_protocol_v30_mediator_proto_msgTypes = make([]protoimpl.MessageInfo, 6)
var file_com_digitalasset_canton_protocol_v30_mediator_proto_goTypes = []any{
	(*InformeeTree)(nil),              // 0: com.digitalasset.canton.protocol.v30.InformeeTree
	(*ParticipantReject)(nil),         // 1: com.digitalasset.canton.protocol.v30.ParticipantReject
	(*RejectionReason)(nil),           // 2: com.digitalasset.canton.protocol.v30.RejectionReason
	(*MediatorReject)(nil),            // 3: com.digitalasset.canton.protocol.v30.MediatorReject
	(*Verdict)(nil),                   // 4: com.digitalasset.canton.protocol.v30.Verdict
	(*ConfirmationResultMessage)(nil), // 5: com.digitalasset.canton.protocol.v30.ConfirmationResultMessage
	(*GenTransactionTree)(nil),        // 6: com.digitalasset.canton.protocol.v30.GenTransactionTree
	(*LocalVerdict)(nil),              // 7: com.digitalasset.canton.protocol.v30.LocalVerdict
	(*status.Status)(nil),             // 8: google.rpc.Status
	(*emptypb.Empty)(nil),             // 9: google.protobuf.Empty
	(ViewType)(0),                     // 10: com.digitalasset.canton.protocol.v30.ViewType
}
var file_com_digitalasset_canton_protocol_v30_mediator_proto_depIdxs = []int32{
	6,  // 0: com.digitalasset.canton.protocol.v30.InformeeTree.tree:type_name -> com.digitalasset.canton.protocol.v30.GenTransactionTree
	2,  // 1: com.digitalasset.canton.protocol.v30.ParticipantReject.reasons:type_name -> com.digitalasset.canton.protocol.v30.RejectionReason
	7,  // 2: com.digitalasset.canton.protocol.v30.RejectionReason.reject:type_name -> com.digitalasset.canton.protocol.v30.LocalVerdict
	8,  // 3: com.digitalasset.canton.protocol.v30.MediatorReject.reason:type_name -> google.rpc.Status
	9,  // 4: com.digitalasset.canton.protocol.v30.Verdict.approve:type_name -> google.protobuf.Empty
	1,  // 5: com.digitalasset.canton.protocol.v30.Verdict.participant_reject:type_name -> com.digitalasset.canton.protocol.v30.ParticipantReject
	3,  // 6: com.digitalasset.canton.protocol.v30.Verdict.mediator_reject:type_name -> com.digitalasset.canton.protocol.v30.MediatorReject
	10, // 7: com.digitalasset.canton.protocol.v30.ConfirmationResultMessage.view_type:type_name -> com.digitalasset.canton.protocol.v30.ViewType
	4,  // 8: com.digitalasset.canton.protocol.v30.ConfirmationResultMessage.verdict:type_name -> com.digitalasset.canton.protocol.v30.Verdict
	9,  // [9:9] is the sub-list for method output_type
	9,  // [9:9] is the sub-list for method input_type
	9,  // [9:9] is the sub-list for extension type_name
	9,  // [9:9] is the sub-list for extension extendee
	0,  // [0:9] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_protocol_v30_mediator_proto_init() }
func file_com_digitalasset_canton_protocol_v30_mediator_proto_init() {
	if File_com_digitalasset_canton_protocol_v30_mediator_proto != nil {
		return
	}
	file_com_digitalasset_canton_protocol_v30_common_proto_init()
	file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_init()
	file_com_digitalasset_canton_protocol_v30_merkle_proto_init()
	file_com_digitalasset_canton_protocol_v30_mediator_proto_msgTypes[4].OneofWrappers = []any{
		(*Verdict_Approve)(nil),
		(*Verdict_ParticipantReject)(nil),
		(*Verdict_MediatorReject)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   6,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_protocol_v30_mediator_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_protocol_v30_mediator_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_protocol_v30_mediator_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_protocol_v30_mediator_proto = out.File
	file_com_digitalasset_canton_protocol_v30_mediator_proto_rawDesc = nil
	file_com_digitalasset_canton_protocol_v30_mediator_proto_goTypes = nil
	file_com_digitalasset_canton_protocol_v30_mediator_proto_depIdxs = nil
}
