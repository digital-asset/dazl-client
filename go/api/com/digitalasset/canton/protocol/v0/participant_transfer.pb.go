// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v4.24.3
// source: com/digitalasset/canton/protocol/v0/participant_transfer.proto

package v0

import (
	v0 "github.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/crypto/v0"
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

type TransferId struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	OriginDomain string                 `protobuf:"bytes,1,opt,name=origin_domain,json=originDomain,proto3" json:"origin_domain,omitempty"`
	Timestamp    *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=timestamp,proto3" json:"timestamp,omitempty"`
}

func (x *TransferId) Reset() {
	*x = TransferId{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TransferId) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransferId) ProtoMessage() {}

func (x *TransferId) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TransferId.ProtoReflect.Descriptor instead.
func (*TransferId) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDescGZIP(), []int{0}
}

func (x *TransferId) GetOriginDomain() string {
	if x != nil {
		return x.OriginDomain
	}
	return ""
}

func (x *TransferId) GetTimestamp() *timestamppb.Timestamp {
	if x != nil {
		return x.Timestamp
	}
	return nil
}

type TransferOutMediatorMessage struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Tree *TransferViewTree `protobuf:"bytes,1,opt,name=tree,proto3" json:"tree,omitempty"`
}

func (x *TransferOutMediatorMessage) Reset() {
	*x = TransferOutMediatorMessage{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TransferOutMediatorMessage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransferOutMediatorMessage) ProtoMessage() {}

func (x *TransferOutMediatorMessage) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TransferOutMediatorMessage.ProtoReflect.Descriptor instead.
func (*TransferOutMediatorMessage) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDescGZIP(), []int{1}
}

func (x *TransferOutMediatorMessage) GetTree() *TransferViewTree {
	if x != nil {
		return x.Tree
	}
	return nil
}

type TransferInMediatorMessage struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Tree *TransferViewTree `protobuf:"bytes,1,opt,name=tree,proto3" json:"tree,omitempty"`
}

func (x *TransferInMediatorMessage) Reset() {
	*x = TransferInMediatorMessage{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TransferInMediatorMessage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransferInMediatorMessage) ProtoMessage() {}

func (x *TransferInMediatorMessage) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TransferInMediatorMessage.ProtoReflect.Descriptor instead.
func (*TransferInMediatorMessage) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDescGZIP(), []int{2}
}

func (x *TransferInMediatorMessage) GetTree() *TransferViewTree {
	if x != nil {
		return x.Tree
	}
	return nil
}

type TransferViewTree struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	CommonData      *BlindableNode `protobuf:"bytes,1,opt,name=common_data,json=commonData,proto3" json:"common_data,omitempty"`
	ParticipantData *BlindableNode `protobuf:"bytes,2,opt,name=participant_data,json=participantData,proto3" json:"participant_data,omitempty"`
}

func (x *TransferViewTree) Reset() {
	*x = TransferViewTree{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TransferViewTree) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransferViewTree) ProtoMessage() {}

func (x *TransferViewTree) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TransferViewTree.ProtoReflect.Descriptor instead.
func (*TransferViewTree) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDescGZIP(), []int{3}
}

func (x *TransferViewTree) GetCommonData() *BlindableNode {
	if x != nil {
		return x.CommonData
	}
	return nil
}

func (x *TransferViewTree) GetParticipantData() *BlindableNode {
	if x != nil {
		return x.ParticipantData
	}
	return nil
}

type TransferOutCommonData struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Salt           *v0.Salt `protobuf:"bytes,1,opt,name=salt,proto3" json:"salt,omitempty"`
	OriginDomain   string   `protobuf:"bytes,2,opt,name=origin_domain,json=originDomain,proto3" json:"origin_domain,omitempty"`
	Stakeholders   []string `protobuf:"bytes,3,rep,name=stakeholders,proto3" json:"stakeholders,omitempty"`
	AdminParties   []string `protobuf:"bytes,4,rep,name=admin_parties,json=adminParties,proto3" json:"admin_parties,omitempty"`
	Uuid           string   `protobuf:"bytes,5,opt,name=uuid,proto3" json:"uuid,omitempty"`
	OriginMediator string   `protobuf:"bytes,6,opt,name=origin_mediator,json=originMediator,proto3" json:"origin_mediator,omitempty"`
}

func (x *TransferOutCommonData) Reset() {
	*x = TransferOutCommonData{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TransferOutCommonData) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransferOutCommonData) ProtoMessage() {}

func (x *TransferOutCommonData) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TransferOutCommonData.ProtoReflect.Descriptor instead.
func (*TransferOutCommonData) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDescGZIP(), []int{4}
}

func (x *TransferOutCommonData) GetSalt() *v0.Salt {
	if x != nil {
		return x.Salt
	}
	return nil
}

func (x *TransferOutCommonData) GetOriginDomain() string {
	if x != nil {
		return x.OriginDomain
	}
	return ""
}

func (x *TransferOutCommonData) GetStakeholders() []string {
	if x != nil {
		return x.Stakeholders
	}
	return nil
}

func (x *TransferOutCommonData) GetAdminParties() []string {
	if x != nil {
		return x.AdminParties
	}
	return nil
}

func (x *TransferOutCommonData) GetUuid() string {
	if x != nil {
		return x.Uuid
	}
	return ""
}

func (x *TransferOutCommonData) GetOriginMediator() string {
	if x != nil {
		return x.OriginMediator
	}
	return ""
}

type TransferOutView struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Salt            *v0.Salt       `protobuf:"bytes,1,opt,name=salt,proto3" json:"salt,omitempty"`
	Submitter       string         `protobuf:"bytes,2,opt,name=submitter,proto3" json:"submitter,omitempty"`
	ContractId      string         `protobuf:"bytes,3,opt,name=contract_id,json=contractId,proto3" json:"contract_id,omitempty"`
	TargetDomain    string         `protobuf:"bytes,4,opt,name=target_domain,json=targetDomain,proto3" json:"target_domain,omitempty"`
	TargetTimeProof *TimeProof `protobuf:"bytes,5,opt,name=target_time_proof,json=targetTimeProof,proto3" json:"target_time_proof,omitempty"`
}

func (x *TransferOutView) Reset() {
	*x = TransferOutView{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TransferOutView) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransferOutView) ProtoMessage() {}

func (x *TransferOutView) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TransferOutView.ProtoReflect.Descriptor instead.
func (*TransferOutView) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDescGZIP(), []int{5}
}

func (x *TransferOutView) GetSalt() *v0.Salt {
	if x != nil {
		return x.Salt
	}
	return nil
}

func (x *TransferOutView) GetSubmitter() string {
	if x != nil {
		return x.Submitter
	}
	return ""
}

func (x *TransferOutView) GetContractId() string {
	if x != nil {
		return x.ContractId
	}
	return ""
}

func (x *TransferOutView) GetTargetDomain() string {
	if x != nil {
		return x.TargetDomain
	}
	return ""
}

func (x *TransferOutView) GetTargetTimeProof() *TimeProof {
	if x != nil {
		return x.TargetTimeProof
	}
	return nil
}

type TransferInCommonData struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Salt           *v0.Salt `protobuf:"bytes,1,opt,name=salt,proto3" json:"salt,omitempty"`
	TargetDomain   string   `protobuf:"bytes,2,opt,name=target_domain,json=targetDomain,proto3" json:"target_domain,omitempty"`
	Stakeholders   []string `protobuf:"bytes,3,rep,name=stakeholders,proto3" json:"stakeholders,omitempty"`
	Uuid           string   `protobuf:"bytes,4,opt,name=uuid,proto3" json:"uuid,omitempty"`
	TargetMediator string   `protobuf:"bytes,6,opt,name=target_mediator,json=targetMediator,proto3" json:"target_mediator,omitempty"`
}

func (x *TransferInCommonData) Reset() {
	*x = TransferInCommonData{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TransferInCommonData) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransferInCommonData) ProtoMessage() {}

func (x *TransferInCommonData) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TransferInCommonData.ProtoReflect.Descriptor instead.
func (*TransferInCommonData) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDescGZIP(), []int{6}
}

func (x *TransferInCommonData) GetSalt() *v0.Salt {
	if x != nil {
		return x.Salt
	}
	return nil
}

func (x *TransferInCommonData) GetTargetDomain() string {
	if x != nil {
		return x.TargetDomain
	}
	return ""
}

func (x *TransferInCommonData) GetStakeholders() []string {
	if x != nil {
		return x.Stakeholders
	}
	return nil
}

func (x *TransferInCommonData) GetUuid() string {
	if x != nil {
		return x.Uuid
	}
	return ""
}

func (x *TransferInCommonData) GetTargetMediator() string {
	if x != nil {
		return x.TargetMediator
	}
	return ""
}

type TransferInView struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Salt                   *v0.Salt              `protobuf:"bytes,1,opt,name=salt,proto3" json:"salt,omitempty"`
	Submitter              string                `protobuf:"bytes,2,opt,name=submitter,proto3" json:"submitter,omitempty"`
	Contract               *SerializableContract `protobuf:"bytes,3,opt,name=contract,proto3" json:"contract,omitempty"`
	TransferOutResultEvent *SignedContent        `protobuf:"bytes,4,opt,name=transfer_out_result_event,json=transferOutResultEvent,proto3" json:"transfer_out_result_event,omitempty"`
	CreatingTransactionId  []byte                `protobuf:"bytes,5,opt,name=creating_transaction_id,json=creatingTransactionId,proto3" json:"creating_transaction_id,omitempty"`
}

func (x *TransferInView) Reset() {
	*x = TransferInView{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[7]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TransferInView) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransferInView) ProtoMessage() {}

func (x *TransferInView) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[7]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TransferInView.ProtoReflect.Descriptor instead.
func (*TransferInView) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDescGZIP(), []int{7}
}

func (x *TransferInView) GetSalt() *v0.Salt {
	if x != nil {
		return x.Salt
	}
	return nil
}

func (x *TransferInView) GetSubmitter() string {
	if x != nil {
		return x.Submitter
	}
	return ""
}

func (x *TransferInView) GetContract() *SerializableContract {
	if x != nil {
		return x.Contract
	}
	return nil
}

func (x *TransferInView) GetTransferOutResultEvent() *SignedContent {
	if x != nil {
		return x.TransferOutResultEvent
	}
	return nil
}

func (x *TransferInView) GetCreatingTransactionId() []byte {
	if x != nil {
		return x.CreatingTransactionId
	}
	return nil
}

var File_com_digitalasset_canton_protocol_v0_participant_transfer_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDesc = []byte{
	0x0a, 0x3e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63,
	0x6f, 0x6c, 0x2f, 0x76, 0x30, 0x2f, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e,
	0x74, 0x5f, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x12, 0x23, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63,
	0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x1a, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74,
	0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x63,
	0x72, 0x79, 0x70, 0x74, 0x6f, 0x2f, 0x76, 0x30, 0x2f, 0x63, 0x72, 0x79, 0x70, 0x74, 0x6f, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x30, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74,
	0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x30, 0x2f, 0x63, 0x6f, 0x6d, 0x6d, 0x6f,
	0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x30, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67,
	0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e,
	0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x30, 0x2f, 0x6d, 0x65, 0x72,
	0x6b, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x34, 0x63, 0x6f, 0x6d, 0x2f, 0x64,
	0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74,
	0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x30, 0x2f, 0x73,
	0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x69, 0x6e, 0x67, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a,
	0x30, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65,
	0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x2f, 0x76, 0x30,
	0x2f, 0x74, 0x69, 0x6d, 0x65, 0x5f, 0x70, 0x72, 0x6f, 0x6f, 0x66, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62,
	0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x22, 0x6b, 0x0a, 0x0a, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x49, 0x64,
	0x12, 0x23, 0x0a, 0x0d, 0x6f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x5f, 0x64, 0x6f, 0x6d, 0x61, 0x69,
	0x6e, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0c, 0x6f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x44,
	0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x12, 0x38, 0x0a, 0x09, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61,
	0x6d, 0x70, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c,
	0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73,
	0x74, 0x61, 0x6d, 0x70, 0x52, 0x09, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x22,
	0x67, 0x0a, 0x1a, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x4f, 0x75, 0x74, 0x4d, 0x65,
	0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x12, 0x49, 0x0a,
	0x04, 0x74, 0x72, 0x65, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x35, 0x2e, 0x63, 0x6f,
	0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63,
	0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76,
	0x30, 0x2e, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x56, 0x69, 0x65, 0x77, 0x54, 0x72,
	0x65, 0x65, 0x52, 0x04, 0x74, 0x72, 0x65, 0x65, 0x22, 0x66, 0x0a, 0x19, 0x54, 0x72, 0x61, 0x6e,
	0x73, 0x66, 0x65, 0x72, 0x49, 0x6e, 0x4d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x4d, 0x65,
	0x73, 0x73, 0x61, 0x67, 0x65, 0x12, 0x49, 0x0a, 0x04, 0x74, 0x72, 0x65, 0x65, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x35, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61,
	0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x66,
	0x65, 0x72, 0x56, 0x69, 0x65, 0x77, 0x54, 0x72, 0x65, 0x65, 0x52, 0x04, 0x74, 0x72, 0x65, 0x65,
	0x22, 0xc6, 0x01, 0x0a, 0x10, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x56, 0x69, 0x65,
	0x77, 0x54, 0x72, 0x65, 0x65, 0x12, 0x53, 0x0a, 0x0b, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x5f,
	0x64, 0x61, 0x74, 0x61, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x32, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30,
	0x2e, 0x42, 0x6c, 0x69, 0x6e, 0x64, 0x61, 0x62, 0x6c, 0x65, 0x4e, 0x6f, 0x64, 0x65, 0x52, 0x0a,
	0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x44, 0x61, 0x74, 0x61, 0x12, 0x5d, 0x0a, 0x10, 0x70, 0x61,
	0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x5f, 0x64, 0x61, 0x74, 0x61, 0x18, 0x02,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x32, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74,
	0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x42, 0x6c, 0x69, 0x6e, 0x64,
	0x61, 0x62, 0x6c, 0x65, 0x4e, 0x6f, 0x64, 0x65, 0x52, 0x0f, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63,
	0x69, 0x70, 0x61, 0x6e, 0x74, 0x44, 0x61, 0x74, 0x61, 0x22, 0xff, 0x01, 0x0a, 0x15, 0x54, 0x72,
	0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x4f, 0x75, 0x74, 0x43, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x44,
	0x61, 0x74, 0x61, 0x12, 0x3b, 0x0a, 0x04, 0x73, 0x61, 0x6c, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x0b, 0x32, 0x27, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x63, 0x72, 0x79, 0x70,
	0x74, 0x6f, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x61, 0x6c, 0x74, 0x52, 0x04, 0x73, 0x61, 0x6c, 0x74,
	0x12, 0x23, 0x0a, 0x0d, 0x6f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x5f, 0x64, 0x6f, 0x6d, 0x61, 0x69,
	0x6e, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0c, 0x6f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x44,
	0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x12, 0x22, 0x0a, 0x0c, 0x73, 0x74, 0x61, 0x6b, 0x65, 0x68, 0x6f,
	0x6c, 0x64, 0x65, 0x72, 0x73, 0x18, 0x03, 0x20, 0x03, 0x28, 0x09, 0x52, 0x0c, 0x73, 0x74, 0x61,
	0x6b, 0x65, 0x68, 0x6f, 0x6c, 0x64, 0x65, 0x72, 0x73, 0x12, 0x23, 0x0a, 0x0d, 0x61, 0x64, 0x6d,
	0x69, 0x6e, 0x5f, 0x70, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x18, 0x04, 0x20, 0x03, 0x28, 0x09,
	0x52, 0x0c, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x50, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x12, 0x12,
	0x0a, 0x04, 0x75, 0x75, 0x69, 0x64, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x75, 0x75,
	0x69, 0x64, 0x12, 0x27, 0x0a, 0x0f, 0x6f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x5f, 0x6d, 0x65, 0x64,
	0x69, 0x61, 0x74, 0x6f, 0x72, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0e, 0x6f, 0x72, 0x69,
	0x67, 0x69, 0x6e, 0x4d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x22, 0x8a, 0x02, 0x0a, 0x0f,
	0x54, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x4f, 0x75, 0x74, 0x56, 0x69, 0x65, 0x77, 0x12,
	0x3b, 0x0a, 0x04, 0x73, 0x61, 0x6c, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x27, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x63, 0x72, 0x79, 0x70, 0x74, 0x6f, 0x2e, 0x76,
	0x30, 0x2e, 0x53, 0x61, 0x6c, 0x74, 0x52, 0x04, 0x73, 0x61, 0x6c, 0x74, 0x12, 0x1c, 0x0a, 0x09,
	0x73, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x74, 0x65, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x09, 0x73, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x74, 0x65, 0x72, 0x12, 0x1f, 0x0a, 0x0b, 0x63, 0x6f,
	0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x0a, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x49, 0x64, 0x12, 0x23, 0x0a, 0x0d, 0x74,
	0x61, 0x72, 0x67, 0x65, 0x74, 0x5f, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x18, 0x04, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x0c, 0x74, 0x61, 0x72, 0x67, 0x65, 0x74, 0x44, 0x6f, 0x6d, 0x61, 0x69, 0x6e,
	0x12, 0x56, 0x0a, 0x11, 0x74, 0x61, 0x72, 0x67, 0x65, 0x74, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x5f,
	0x70, 0x72, 0x6f, 0x6f, 0x66, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2a, 0x2e, 0x63, 0x6f,
	0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63,
	0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x74, 0x69, 0x6d, 0x65, 0x2e, 0x76, 0x30, 0x2e, 0x54, 0x69,
	0x6d, 0x65, 0x50, 0x72, 0x6f, 0x6f, 0x66, 0x52, 0x0f, 0x74, 0x61, 0x72, 0x67, 0x65, 0x74, 0x54,
	0x69, 0x6d, 0x65, 0x50, 0x72, 0x6f, 0x6f, 0x66, 0x22, 0xd9, 0x01, 0x0a, 0x14, 0x54, 0x72, 0x61,
	0x6e, 0x73, 0x66, 0x65, 0x72, 0x49, 0x6e, 0x43, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x44, 0x61, 0x74,
	0x61, 0x12, 0x3b, 0x0a, 0x04, 0x73, 0x61, 0x6c, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x27, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x63, 0x72, 0x79, 0x70, 0x74, 0x6f,
	0x2e, 0x76, 0x30, 0x2e, 0x53, 0x61, 0x6c, 0x74, 0x52, 0x04, 0x73, 0x61, 0x6c, 0x74, 0x12, 0x23,
	0x0a, 0x0d, 0x74, 0x61, 0x72, 0x67, 0x65, 0x74, 0x5f, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x18,
	0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0c, 0x74, 0x61, 0x72, 0x67, 0x65, 0x74, 0x44, 0x6f, 0x6d,
	0x61, 0x69, 0x6e, 0x12, 0x22, 0x0a, 0x0c, 0x73, 0x74, 0x61, 0x6b, 0x65, 0x68, 0x6f, 0x6c, 0x64,
	0x65, 0x72, 0x73, 0x18, 0x03, 0x20, 0x03, 0x28, 0x09, 0x52, 0x0c, 0x73, 0x74, 0x61, 0x6b, 0x65,
	0x68, 0x6f, 0x6c, 0x64, 0x65, 0x72, 0x73, 0x12, 0x12, 0x0a, 0x04, 0x75, 0x75, 0x69, 0x64, 0x18,
	0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x75, 0x75, 0x69, 0x64, 0x12, 0x27, 0x0a, 0x0f, 0x74,
	0x61, 0x72, 0x67, 0x65, 0x74, 0x5f, 0x6d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x18, 0x06,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x0e, 0x74, 0x61, 0x72, 0x67, 0x65, 0x74, 0x4d, 0x65, 0x64, 0x69,
	0x61, 0x74, 0x6f, 0x72, 0x22, 0xe9, 0x02, 0x0a, 0x0e, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65,
	0x72, 0x49, 0x6e, 0x56, 0x69, 0x65, 0x77, 0x12, 0x3b, 0x0a, 0x04, 0x73, 0x61, 0x6c, 0x74, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x27, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69,
	0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e,
	0x63, 0x72, 0x79, 0x70, 0x74, 0x6f, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x61, 0x6c, 0x74, 0x52, 0x04,
	0x73, 0x61, 0x6c, 0x74, 0x12, 0x1c, 0x0a, 0x09, 0x73, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x74, 0x65,
	0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x73, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x74,
	0x65, 0x72, 0x12, 0x55, 0x0a, 0x08, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x18, 0x03,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x39, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74,
	0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x65, 0x72, 0x69, 0x61,
	0x6c, 0x69, 0x7a, 0x61, 0x62, 0x6c, 0x65, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x52,
	0x08, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x12, 0x6d, 0x0a, 0x19, 0x74, 0x72, 0x61,
	0x6e, 0x73, 0x66, 0x65, 0x72, 0x5f, 0x6f, 0x75, 0x74, 0x5f, 0x72, 0x65, 0x73, 0x75, 0x6c, 0x74,
	0x5f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x32, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e,
	0x76, 0x30, 0x2e, 0x53, 0x69, 0x67, 0x6e, 0x65, 0x64, 0x43, 0x6f, 0x6e, 0x74, 0x65, 0x6e, 0x74,
	0x52, 0x16, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x4f, 0x75, 0x74, 0x52, 0x65, 0x73,
	0x75, 0x6c, 0x74, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x12, 0x36, 0x0a, 0x17, 0x63, 0x72, 0x65, 0x61,
	0x74, 0x69, 0x6e, 0x67, 0x5f, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e,
	0x5f, 0x69, 0x64, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0c, 0x52, 0x15, 0x63, 0x72, 0x65, 0x61, 0x74,
	0x69, 0x6e, 0x67, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x49, 0x64,
	0x42, 0x54, 0x5a, 0x52, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64,
	0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a,
	0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x37, 0x2f, 0x67, 0x6f, 0x2f, 0x61,
	0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73,
	0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x30, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDescData = file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDesc
)

func file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDescData)
	})
	return file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDescData
}

var file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes = make([]protoimpl.MessageInfo, 8)
var file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_goTypes = []interface{}{
	(*TransferId)(nil),                 // 0: com.digitalasset.canton.protocol.v0.TransferId
	(*TransferOutMediatorMessage)(nil), // 1: com.digitalasset.canton.protocol.v0.TransferOutMediatorMessage
	(*TransferInMediatorMessage)(nil),  // 2: com.digitalasset.canton.protocol.v0.TransferInMediatorMessage
	(*TransferViewTree)(nil),           // 3: com.digitalasset.canton.protocol.v0.TransferViewTree
	(*TransferOutCommonData)(nil),      // 4: com.digitalasset.canton.protocol.v0.TransferOutCommonData
	(*TransferOutView)(nil),            // 5: com.digitalasset.canton.protocol.v0.TransferOutView
	(*TransferInCommonData)(nil),       // 6: com.digitalasset.canton.protocol.v0.TransferInCommonData
	(*TransferInView)(nil),             // 7: com.digitalasset.canton.protocol.v0.TransferInView
	(*timestamppb.Timestamp)(nil),      // 8: google.protobuf.Timestamp
	(*BlindableNode)(nil),              // 9: com.digitalasset.canton.protocol.v0.BlindableNode
	(*v0.Salt)(nil),                    // 10: com.digitalasset.canton.crypto.v0.Salt
	(*TimeProof)(nil),              // 11: com.digitalasset.canton.time.v0.TimeProof
	(*SerializableContract)(nil),       // 12: com.digitalasset.canton.protocol.v0.SerializableContract
	(*SignedContent)(nil),              // 13: com.digitalasset.canton.protocol.v0.SignedContent
}
var file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_depIdxs = []int32{
	8,  // 0: com.digitalasset.canton.protocol.v0.TransferId.timestamp:type_name -> google.protobuf.Timestamp
	3,  // 1: com.digitalasset.canton.protocol.v0.TransferOutMediatorMessage.tree:type_name -> com.digitalasset.canton.protocol.v0.TransferViewTree
	3,  // 2: com.digitalasset.canton.protocol.v0.TransferInMediatorMessage.tree:type_name -> com.digitalasset.canton.protocol.v0.TransferViewTree
	9,  // 3: com.digitalasset.canton.protocol.v0.TransferViewTree.common_data:type_name -> com.digitalasset.canton.protocol.v0.BlindableNode
	9,  // 4: com.digitalasset.canton.protocol.v0.TransferViewTree.participant_data:type_name -> com.digitalasset.canton.protocol.v0.BlindableNode
	10, // 5: com.digitalasset.canton.protocol.v0.TransferOutCommonData.salt:type_name -> com.digitalasset.canton.crypto.v0.Salt
	10, // 6: com.digitalasset.canton.protocol.v0.TransferOutView.salt:type_name -> com.digitalasset.canton.crypto.v0.Salt
	11, // 7: com.digitalasset.canton.protocol.v0.TransferOutView.target_time_proof:type_name -> com.digitalasset.canton.time.v0.TimeProof
	10, // 8: com.digitalasset.canton.protocol.v0.TransferInCommonData.salt:type_name -> com.digitalasset.canton.crypto.v0.Salt
	10, // 9: com.digitalasset.canton.protocol.v0.TransferInView.salt:type_name -> com.digitalasset.canton.crypto.v0.Salt
	12, // 10: com.digitalasset.canton.protocol.v0.TransferInView.contract:type_name -> com.digitalasset.canton.protocol.v0.SerializableContract
	13, // 11: com.digitalasset.canton.protocol.v0.TransferInView.transfer_out_result_event:type_name -> com.digitalasset.canton.protocol.v0.SignedContent
	12, // [12:12] is the sub-list for method output_type
	12, // [12:12] is the sub-list for method input_type
	12, // [12:12] is the sub-list for extension type_name
	12, // [12:12] is the sub-list for extension extendee
	0,  // [0:12] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_init() }
func file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_init() {
	if File_com_digitalasset_canton_protocol_v0_participant_transfer_proto != nil {
		return
	}
	file_com_digitalasset_canton_protocol_v0_common_proto_init()
	file_com_digitalasset_canton_protocol_v0_merkle_proto_init()
	file_com_digitalasset_canton_protocol_v0_sequencing_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TransferId); i {
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
		file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TransferOutMediatorMessage); i {
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
		file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TransferInMediatorMessage); i {
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
		file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TransferViewTree); i {
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
		file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TransferOutCommonData); i {
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
		file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TransferOutView); i {
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
		file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[6].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TransferInCommonData); i {
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
		file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes[7].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TransferInView); i {
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
			RawDescriptor: file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   8,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_protocol_v0_participant_transfer_proto = out.File
	file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_rawDesc = nil
	file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_goTypes = nil
	file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_depIdxs = nil
}
