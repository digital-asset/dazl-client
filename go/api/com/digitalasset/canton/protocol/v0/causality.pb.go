// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/digitalasset/canton/protocol/v0/causality.proto

package v0

import (
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

type CausalityMessage struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	TargetDomainId string       `protobuf:"bytes,1,opt,name=target_domain_id,json=targetDomainId,proto3" json:"target_domain_id,omitempty"`
	TransferId     *TransferId  `protobuf:"bytes,2,opt,name=transfer_id,json=transferId,proto3" json:"transfer_id,omitempty"`
	Clock          *VectorClock `protobuf:"bytes,3,opt,name=clock,proto3" json:"clock,omitempty"`
}

func (x *CausalityMessage) Reset() {
	*x = CausalityMessage{}
	mi := &file_com_digitalasset_canton_protocol_v0_causality_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CausalityMessage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CausalityMessage) ProtoMessage() {}

func (x *CausalityMessage) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_causality_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CausalityMessage.ProtoReflect.Descriptor instead.
func (*CausalityMessage) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_causality_proto_rawDescGZIP(), []int{0}
}

func (x *CausalityMessage) GetTargetDomainId() string {
	if x != nil {
		return x.TargetDomainId
	}
	return ""
}

func (x *CausalityMessage) GetTransferId() *TransferId {
	if x != nil {
		return x.TransferId
	}
	return nil
}

func (x *CausalityMessage) GetClock() *VectorClock {
	if x != nil {
		return x.Clock
	}
	return nil
}

type VectorClock struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	OriginDomainId string                            `protobuf:"bytes,1,opt,name=origin_domain_id,json=originDomainId,proto3" json:"origin_domain_id,omitempty"`
	LocalTs        *timestamppb.Timestamp            `protobuf:"bytes,2,opt,name=local_ts,json=localTs,proto3" json:"local_ts,omitempty"`
	PartyId        string                            `protobuf:"bytes,4,opt,name=party_id,json=partyId,proto3" json:"party_id,omitempty"`
	Clock          map[string]*timestamppb.Timestamp `protobuf:"bytes,5,rep,name=clock,proto3" json:"clock,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
}

func (x *VectorClock) Reset() {
	*x = VectorClock{}
	mi := &file_com_digitalasset_canton_protocol_v0_causality_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *VectorClock) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*VectorClock) ProtoMessage() {}

func (x *VectorClock) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_causality_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use VectorClock.ProtoReflect.Descriptor instead.
func (*VectorClock) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_causality_proto_rawDescGZIP(), []int{1}
}

func (x *VectorClock) GetOriginDomainId() string {
	if x != nil {
		return x.OriginDomainId
	}
	return ""
}

func (x *VectorClock) GetLocalTs() *timestamppb.Timestamp {
	if x != nil {
		return x.LocalTs
	}
	return nil
}

func (x *VectorClock) GetPartyId() string {
	if x != nil {
		return x.PartyId
	}
	return ""
}

func (x *VectorClock) GetClock() map[string]*timestamppb.Timestamp {
	if x != nil {
		return x.Clock
	}
	return nil
}

type CausalityUpdate struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	InformeeStakeholders []string               `protobuf:"bytes,1,rep,name=informeeStakeholders,proto3" json:"informeeStakeholders,omitempty"`
	Ts                   *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=ts,proto3" json:"ts,omitempty"`
	DomainId             string                 `protobuf:"bytes,3,opt,name=domain_id,json=domainId,proto3" json:"domain_id,omitempty"`
	RequestCounter       int64                  `protobuf:"varint,4,opt,name=request_counter,json=requestCounter,proto3" json:"request_counter,omitempty"`
	// Types that are assignable to Tag:
	//
	//	*CausalityUpdate_TransactionUpdate
	//	*CausalityUpdate_TransferOutUpdate
	//	*CausalityUpdate_TransferInUpdate
	Tag isCausalityUpdate_Tag `protobuf_oneof:"tag"`
}

func (x *CausalityUpdate) Reset() {
	*x = CausalityUpdate{}
	mi := &file_com_digitalasset_canton_protocol_v0_causality_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CausalityUpdate) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CausalityUpdate) ProtoMessage() {}

func (x *CausalityUpdate) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_causality_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CausalityUpdate.ProtoReflect.Descriptor instead.
func (*CausalityUpdate) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_causality_proto_rawDescGZIP(), []int{2}
}

func (x *CausalityUpdate) GetInformeeStakeholders() []string {
	if x != nil {
		return x.InformeeStakeholders
	}
	return nil
}

func (x *CausalityUpdate) GetTs() *timestamppb.Timestamp {
	if x != nil {
		return x.Ts
	}
	return nil
}

func (x *CausalityUpdate) GetDomainId() string {
	if x != nil {
		return x.DomainId
	}
	return ""
}

func (x *CausalityUpdate) GetRequestCounter() int64 {
	if x != nil {
		return x.RequestCounter
	}
	return 0
}

func (m *CausalityUpdate) GetTag() isCausalityUpdate_Tag {
	if m != nil {
		return m.Tag
	}
	return nil
}

func (x *CausalityUpdate) GetTransactionUpdate() *TransactionUpdate {
	if x, ok := x.GetTag().(*CausalityUpdate_TransactionUpdate); ok {
		return x.TransactionUpdate
	}
	return nil
}

func (x *CausalityUpdate) GetTransferOutUpdate() *TransferOutUpdate {
	if x, ok := x.GetTag().(*CausalityUpdate_TransferOutUpdate); ok {
		return x.TransferOutUpdate
	}
	return nil
}

func (x *CausalityUpdate) GetTransferInUpdate() *TransferInUpdate {
	if x, ok := x.GetTag().(*CausalityUpdate_TransferInUpdate); ok {
		return x.TransferInUpdate
	}
	return nil
}

type isCausalityUpdate_Tag interface {
	isCausalityUpdate_Tag()
}

type CausalityUpdate_TransactionUpdate struct {
	TransactionUpdate *TransactionUpdate `protobuf:"bytes,5,opt,name=transactionUpdate,proto3,oneof"`
}

type CausalityUpdate_TransferOutUpdate struct {
	TransferOutUpdate *TransferOutUpdate `protobuf:"bytes,6,opt,name=transferOutUpdate,proto3,oneof"`
}

type CausalityUpdate_TransferInUpdate struct {
	TransferInUpdate *TransferInUpdate `protobuf:"bytes,7,opt,name=transferInUpdate,proto3,oneof"`
}

func (*CausalityUpdate_TransactionUpdate) isCausalityUpdate_Tag() {}

func (*CausalityUpdate_TransferOutUpdate) isCausalityUpdate_Tag() {}

func (*CausalityUpdate_TransferInUpdate) isCausalityUpdate_Tag() {}

type TransactionUpdate struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *TransactionUpdate) Reset() {
	*x = TransactionUpdate{}
	mi := &file_com_digitalasset_canton_protocol_v0_causality_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TransactionUpdate) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransactionUpdate) ProtoMessage() {}

func (x *TransactionUpdate) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_causality_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TransactionUpdate.ProtoReflect.Descriptor instead.
func (*TransactionUpdate) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_causality_proto_rawDescGZIP(), []int{3}
}

type TransferOutUpdate struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	TransferId *TransferId `protobuf:"bytes,1,opt,name=transfer_id,json=transferId,proto3" json:"transfer_id,omitempty"`
}

func (x *TransferOutUpdate) Reset() {
	*x = TransferOutUpdate{}
	mi := &file_com_digitalasset_canton_protocol_v0_causality_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TransferOutUpdate) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransferOutUpdate) ProtoMessage() {}

func (x *TransferOutUpdate) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_causality_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TransferOutUpdate.ProtoReflect.Descriptor instead.
func (*TransferOutUpdate) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_causality_proto_rawDescGZIP(), []int{4}
}

func (x *TransferOutUpdate) GetTransferId() *TransferId {
	if x != nil {
		return x.TransferId
	}
	return nil
}

type TransferInUpdate struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	TransferId *TransferId `protobuf:"bytes,1,opt,name=transfer_id,json=transferId,proto3" json:"transfer_id,omitempty"`
}

func (x *TransferInUpdate) Reset() {
	*x = TransferInUpdate{}
	mi := &file_com_digitalasset_canton_protocol_v0_causality_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TransferInUpdate) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransferInUpdate) ProtoMessage() {}

func (x *TransferInUpdate) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_causality_proto_msgTypes[5]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TransferInUpdate.ProtoReflect.Descriptor instead.
func (*TransferInUpdate) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_causality_proto_rawDescGZIP(), []int{5}
}

func (x *TransferInUpdate) GetTransferId() *TransferId {
	if x != nil {
		return x.TransferId
	}
	return nil
}

var File_com_digitalasset_canton_protocol_v0_causality_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_protocol_v0_causality_proto_rawDesc = []byte{
	0x0a, 0x33, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63,
	0x6f, 0x6c, 0x2f, 0x76, 0x30, 0x2f, 0x63, 0x61, 0x75, 0x73, 0x61, 0x6c, 0x69, 0x74, 0x79, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x23, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74,
	0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x1a, 0x3e, 0x63, 0x6f, 0x6d, 0x2f,
	0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e,
	0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x30, 0x2f,
	0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x5f, 0x74, 0x72, 0x61, 0x6e,
	0x73, 0x66, 0x65, 0x72, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65,
	0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xd6, 0x01, 0x0a, 0x10,
	0x43, 0x61, 0x75, 0x73, 0x61, 0x6c, 0x69, 0x74, 0x79, 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65,
	0x12, 0x28, 0x0a, 0x10, 0x74, 0x61, 0x72, 0x67, 0x65, 0x74, 0x5f, 0x64, 0x6f, 0x6d, 0x61, 0x69,
	0x6e, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0e, 0x74, 0x61, 0x72, 0x67,
	0x65, 0x74, 0x44, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x49, 0x64, 0x12, 0x50, 0x0a, 0x0b, 0x74, 0x72,
	0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x2f, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63,
	0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x49, 0x64,
	0x52, 0x0a, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x49, 0x64, 0x12, 0x46, 0x0a, 0x05,
	0x63, 0x6c, 0x6f, 0x63, 0x6b, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x30, 0x2e, 0x63, 0x6f,
	0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63,
	0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76,
	0x30, 0x2e, 0x56, 0x65, 0x63, 0x74, 0x6f, 0x72, 0x43, 0x6c, 0x6f, 0x63, 0x6b, 0x52, 0x05, 0x63,
	0x6c, 0x6f, 0x63, 0x6b, 0x22, 0xb2, 0x02, 0x0a, 0x0b, 0x56, 0x65, 0x63, 0x74, 0x6f, 0x72, 0x43,
	0x6c, 0x6f, 0x63, 0x6b, 0x12, 0x28, 0x0a, 0x10, 0x6f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x5f, 0x64,
	0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0e,
	0x6f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x44, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x49, 0x64, 0x12, 0x35,
	0x0a, 0x08, 0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x5f, 0x74, 0x73, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62,
	0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x07, 0x6c, 0x6f,
	0x63, 0x61, 0x6c, 0x54, 0x73, 0x12, 0x19, 0x0a, 0x08, 0x70, 0x61, 0x72, 0x74, 0x79, 0x5f, 0x69,
	0x64, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x70, 0x61, 0x72, 0x74, 0x79, 0x49, 0x64,
	0x12, 0x51, 0x0a, 0x05, 0x63, 0x6c, 0x6f, 0x63, 0x6b, 0x18, 0x05, 0x20, 0x03, 0x28, 0x0b, 0x32,
	0x3b, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63,
	0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x56, 0x65, 0x63, 0x74, 0x6f, 0x72, 0x43, 0x6c, 0x6f, 0x63,
	0x6b, 0x2e, 0x43, 0x6c, 0x6f, 0x63, 0x6b, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x52, 0x05, 0x63, 0x6c,
	0x6f, 0x63, 0x6b, 0x1a, 0x54, 0x0a, 0x0a, 0x43, 0x6c, 0x6f, 0x63, 0x6b, 0x45, 0x6e, 0x74, 0x72,
	0x79, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03,
	0x6b, 0x65, 0x79, 0x12, 0x30, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x05,
	0x76, 0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38, 0x01, 0x22, 0xf3, 0x03, 0x0a, 0x0f, 0x43, 0x61,
	0x75, 0x73, 0x61, 0x6c, 0x69, 0x74, 0x79, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x12, 0x32, 0x0a,
	0x14, 0x69, 0x6e, 0x66, 0x6f, 0x72, 0x6d, 0x65, 0x65, 0x53, 0x74, 0x61, 0x6b, 0x65, 0x68, 0x6f,
	0x6c, 0x64, 0x65, 0x72, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x09, 0x52, 0x14, 0x69, 0x6e, 0x66,
	0x6f, 0x72, 0x6d, 0x65, 0x65, 0x53, 0x74, 0x61, 0x6b, 0x65, 0x68, 0x6f, 0x6c, 0x64, 0x65, 0x72,
	0x73, 0x12, 0x2a, 0x0a, 0x02, 0x74, 0x73, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e,
	0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e,
	0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x02, 0x74, 0x73, 0x12, 0x1b, 0x0a,
	0x09, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x08, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x49, 0x64, 0x12, 0x27, 0x0a, 0x0f, 0x72, 0x65,
	0x71, 0x75, 0x65, 0x73, 0x74, 0x5f, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x65, 0x72, 0x18, 0x04, 0x20,
	0x01, 0x28, 0x03, 0x52, 0x0e, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x43, 0x6f, 0x75, 0x6e,
	0x74, 0x65, 0x72, 0x12, 0x66, 0x0a, 0x11, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69,
	0x6f, 0x6e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x36,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65,
	0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f,
	0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e,
	0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x48, 0x00, 0x52, 0x11, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x61,
	0x63, 0x74, 0x69, 0x6f, 0x6e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x12, 0x66, 0x0a, 0x11, 0x74,
	0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x4f, 0x75, 0x74, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65,
	0x18, 0x06, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x36, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67,
	0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x54, 0x72, 0x61,
	0x6e, 0x73, 0x66, 0x65, 0x72, 0x4f, 0x75, 0x74, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x48, 0x00,
	0x52, 0x11, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x4f, 0x75, 0x74, 0x55, 0x70, 0x64,
	0x61, 0x74, 0x65, 0x12, 0x63, 0x0a, 0x10, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x49,
	0x6e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x18, 0x07, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x35, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c,
	0x2e, 0x76, 0x30, 0x2e, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x49, 0x6e, 0x55, 0x70,
	0x64, 0x61, 0x74, 0x65, 0x48, 0x00, 0x52, 0x10, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72,
	0x49, 0x6e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x42, 0x05, 0x0a, 0x03, 0x74, 0x61, 0x67, 0x22,
	0x13, 0x0a, 0x11, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x55, 0x70,
	0x64, 0x61, 0x74, 0x65, 0x22, 0x65, 0x0a, 0x11, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72,
	0x4f, 0x75, 0x74, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x12, 0x50, 0x0a, 0x0b, 0x74, 0x72, 0x61,
	0x6e, 0x73, 0x66, 0x65, 0x72, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2f,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65,
	0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f,
	0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x49, 0x64, 0x52,
	0x0a, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x49, 0x64, 0x22, 0x64, 0x0a, 0x10, 0x54,
	0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x49, 0x6e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x12,
	0x50, 0x0a, 0x0b, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x5f, 0x69, 0x64, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x2f, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74,
	0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x54, 0x72, 0x61, 0x6e, 0x73,
	0x66, 0x65, 0x72, 0x49, 0x64, 0x52, 0x0a, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x49,
	0x64, 0x42, 0x54, 0x5a, 0x52, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f,
	0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61,
	0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f,
	0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x30, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_protocol_v0_causality_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_protocol_v0_causality_proto_rawDescData = file_com_digitalasset_canton_protocol_v0_causality_proto_rawDesc
)

func file_com_digitalasset_canton_protocol_v0_causality_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_protocol_v0_causality_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_protocol_v0_causality_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_protocol_v0_causality_proto_rawDescData)
	})
	return file_com_digitalasset_canton_protocol_v0_causality_proto_rawDescData
}

var file_com_digitalasset_canton_protocol_v0_causality_proto_msgTypes = make([]protoimpl.MessageInfo, 7)
var file_com_digitalasset_canton_protocol_v0_causality_proto_goTypes = []any{
	(*CausalityMessage)(nil),      // 0: com.digitalasset.canton.protocol.v0.CausalityMessage
	(*VectorClock)(nil),           // 1: com.digitalasset.canton.protocol.v0.VectorClock
	(*CausalityUpdate)(nil),       // 2: com.digitalasset.canton.protocol.v0.CausalityUpdate
	(*TransactionUpdate)(nil),     // 3: com.digitalasset.canton.protocol.v0.TransactionUpdate
	(*TransferOutUpdate)(nil),     // 4: com.digitalasset.canton.protocol.v0.TransferOutUpdate
	(*TransferInUpdate)(nil),      // 5: com.digitalasset.canton.protocol.v0.TransferInUpdate
	nil,                           // 6: com.digitalasset.canton.protocol.v0.VectorClock.ClockEntry
	(*TransferId)(nil),            // 7: com.digitalasset.canton.protocol.v0.TransferId
	(*timestamppb.Timestamp)(nil), // 8: google.protobuf.Timestamp
}
var file_com_digitalasset_canton_protocol_v0_causality_proto_depIdxs = []int32{
	7,  // 0: com.digitalasset.canton.protocol.v0.CausalityMessage.transfer_id:type_name -> com.digitalasset.canton.protocol.v0.TransferId
	1,  // 1: com.digitalasset.canton.protocol.v0.CausalityMessage.clock:type_name -> com.digitalasset.canton.protocol.v0.VectorClock
	8,  // 2: com.digitalasset.canton.protocol.v0.VectorClock.local_ts:type_name -> google.protobuf.Timestamp
	6,  // 3: com.digitalasset.canton.protocol.v0.VectorClock.clock:type_name -> com.digitalasset.canton.protocol.v0.VectorClock.ClockEntry
	8,  // 4: com.digitalasset.canton.protocol.v0.CausalityUpdate.ts:type_name -> google.protobuf.Timestamp
	3,  // 5: com.digitalasset.canton.protocol.v0.CausalityUpdate.transactionUpdate:type_name -> com.digitalasset.canton.protocol.v0.TransactionUpdate
	4,  // 6: com.digitalasset.canton.protocol.v0.CausalityUpdate.transferOutUpdate:type_name -> com.digitalasset.canton.protocol.v0.TransferOutUpdate
	5,  // 7: com.digitalasset.canton.protocol.v0.CausalityUpdate.transferInUpdate:type_name -> com.digitalasset.canton.protocol.v0.TransferInUpdate
	7,  // 8: com.digitalasset.canton.protocol.v0.TransferOutUpdate.transfer_id:type_name -> com.digitalasset.canton.protocol.v0.TransferId
	7,  // 9: com.digitalasset.canton.protocol.v0.TransferInUpdate.transfer_id:type_name -> com.digitalasset.canton.protocol.v0.TransferId
	8,  // 10: com.digitalasset.canton.protocol.v0.VectorClock.ClockEntry.value:type_name -> google.protobuf.Timestamp
	11, // [11:11] is the sub-list for method output_type
	11, // [11:11] is the sub-list for method input_type
	11, // [11:11] is the sub-list for extension type_name
	11, // [11:11] is the sub-list for extension extendee
	0,  // [0:11] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_protocol_v0_causality_proto_init() }
func file_com_digitalasset_canton_protocol_v0_causality_proto_init() {
	if File_com_digitalasset_canton_protocol_v0_causality_proto != nil {
		return
	}
	file_com_digitalasset_canton_protocol_v0_participant_transfer_proto_init()
	file_com_digitalasset_canton_protocol_v0_causality_proto_msgTypes[2].OneofWrappers = []any{
		(*CausalityUpdate_TransactionUpdate)(nil),
		(*CausalityUpdate_TransferOutUpdate)(nil),
		(*CausalityUpdate_TransferInUpdate)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_protocol_v0_causality_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   7,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_protocol_v0_causality_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_protocol_v0_causality_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_protocol_v0_causality_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_protocol_v0_causality_proto = out.File
	file_com_digitalasset_canton_protocol_v0_causality_proto_rawDesc = nil
	file_com_digitalasset_canton_protocol_v0_causality_proto_goTypes = nil
	file_com_digitalasset_canton_protocol_v0_causality_proto_depIdxs = nil
}
