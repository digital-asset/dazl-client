// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/digitalasset/canton/protocol/v30/confirmation_response.proto

package v30

import (
	status "google.golang.org/genproto/googleapis/rpc/status"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type LocalVerdict_VerdictCode int32

const (
	LocalVerdict_VERDICT_CODE_UNSPECIFIED     LocalVerdict_VerdictCode = 0
	LocalVerdict_VERDICT_CODE_LOCAL_APPROVE   LocalVerdict_VerdictCode = 1
	LocalVerdict_VERDICT_CODE_LOCAL_REJECT    LocalVerdict_VerdictCode = 2
	LocalVerdict_VERDICT_CODE_LOCAL_MALFORMED LocalVerdict_VerdictCode = 3
)

// Enum value maps for LocalVerdict_VerdictCode.
var (
	LocalVerdict_VerdictCode_name = map[int32]string{
		0: "VERDICT_CODE_UNSPECIFIED",
		1: "VERDICT_CODE_LOCAL_APPROVE",
		2: "VERDICT_CODE_LOCAL_REJECT",
		3: "VERDICT_CODE_LOCAL_MALFORMED",
	}
	LocalVerdict_VerdictCode_value = map[string]int32{
		"VERDICT_CODE_UNSPECIFIED":     0,
		"VERDICT_CODE_LOCAL_APPROVE":   1,
		"VERDICT_CODE_LOCAL_REJECT":    2,
		"VERDICT_CODE_LOCAL_MALFORMED": 3,
	}
)

func (x LocalVerdict_VerdictCode) Enum() *LocalVerdict_VerdictCode {
	p := new(LocalVerdict_VerdictCode)
	*p = x
	return p
}

func (x LocalVerdict_VerdictCode) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (LocalVerdict_VerdictCode) Descriptor() protoreflect.EnumDescriptor {
	return file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_enumTypes[0].Descriptor()
}

func (LocalVerdict_VerdictCode) Type() protoreflect.EnumType {
	return &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_enumTypes[0]
}

func (x LocalVerdict_VerdictCode) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use LocalVerdict_VerdictCode.Descriptor instead.
func (LocalVerdict_VerdictCode) EnumDescriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescGZIP(), []int{0, 0}
}

type LocalVerdict struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Code   LocalVerdict_VerdictCode `protobuf:"varint,1,opt,name=code,proto3,enum=com.digitalasset.canton.protocol.v30.LocalVerdict_VerdictCode" json:"code,omitempty"`
	Reason *status.Status           `protobuf:"bytes,2,opt,name=reason,proto3" json:"reason,omitempty"`
}

func (x *LocalVerdict) Reset() {
	*x = LocalVerdict{}
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *LocalVerdict) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*LocalVerdict) ProtoMessage() {}

func (x *LocalVerdict) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use LocalVerdict.ProtoReflect.Descriptor instead.
func (*LocalVerdict) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescGZIP(), []int{0}
}

func (x *LocalVerdict) GetCode() LocalVerdict_VerdictCode {
	if x != nil {
		return x.Code
	}
	return LocalVerdict_VERDICT_CODE_UNSPECIFIED
}

func (x *LocalVerdict) GetReason() *status.Status {
	if x != nil {
		return x.Reason
	}
	return nil
}

type ConfirmationResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	RequestId         int64         `protobuf:"varint,1,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
	Sender            string        `protobuf:"bytes,2,opt,name=sender,proto3" json:"sender,omitempty"`
	LocalVerdict      *LocalVerdict `protobuf:"bytes,3,opt,name=local_verdict,json=localVerdict,proto3" json:"local_verdict,omitempty"`
	RootHash          []byte        `protobuf:"bytes,4,opt,name=root_hash,json=rootHash,proto3" json:"root_hash,omitempty"`
	ConfirmingParties []string      `protobuf:"bytes,5,rep,name=confirming_parties,json=confirmingParties,proto3" json:"confirming_parties,omitempty"`
	DomainId          string        `protobuf:"bytes,6,opt,name=domain_id,json=domainId,proto3" json:"domain_id,omitempty"`
	ViewPosition      *ViewPosition `protobuf:"bytes,7,opt,name=view_position,json=viewPosition,proto3" json:"view_position,omitempty"`
}

func (x *ConfirmationResponse) Reset() {
	*x = ConfirmationResponse{}
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ConfirmationResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ConfirmationResponse) ProtoMessage() {}

func (x *ConfirmationResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ConfirmationResponse.ProtoReflect.Descriptor instead.
func (*ConfirmationResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescGZIP(), []int{1}
}

func (x *ConfirmationResponse) GetRequestId() int64 {
	if x != nil {
		return x.RequestId
	}
	return 0
}

func (x *ConfirmationResponse) GetSender() string {
	if x != nil {
		return x.Sender
	}
	return ""
}

func (x *ConfirmationResponse) GetLocalVerdict() *LocalVerdict {
	if x != nil {
		return x.LocalVerdict
	}
	return nil
}

func (x *ConfirmationResponse) GetRootHash() []byte {
	if x != nil {
		return x.RootHash
	}
	return nil
}

func (x *ConfirmationResponse) GetConfirmingParties() []string {
	if x != nil {
		return x.ConfirmingParties
	}
	return nil
}

func (x *ConfirmationResponse) GetDomainId() string {
	if x != nil {
		return x.DomainId
	}
	return ""
}

func (x *ConfirmationResponse) GetViewPosition() *ViewPosition {
	if x != nil {
		return x.ViewPosition
	}
	return nil
}

type ViewPosition struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Position []*MerkleSeqIndex `protobuf:"bytes,1,rep,name=position,proto3" json:"position,omitempty"`
}

func (x *ViewPosition) Reset() {
	*x = ViewPosition{}
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ViewPosition) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ViewPosition) ProtoMessage() {}

func (x *ViewPosition) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ViewPosition.ProtoReflect.Descriptor instead.
func (*ViewPosition) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescGZIP(), []int{2}
}

func (x *ViewPosition) GetPosition() []*MerkleSeqIndex {
	if x != nil {
		return x.Position
	}
	return nil
}

type MerkleSeqIndex struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	IsRight []bool `protobuf:"varint,1,rep,packed,name=is_right,json=isRight,proto3" json:"is_right,omitempty"`
}

func (x *MerkleSeqIndex) Reset() {
	*x = MerkleSeqIndex{}
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *MerkleSeqIndex) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MerkleSeqIndex) ProtoMessage() {}

func (x *MerkleSeqIndex) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use MerkleSeqIndex.ProtoReflect.Descriptor instead.
func (*MerkleSeqIndex) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescGZIP(), []int{3}
}

func (x *MerkleSeqIndex) GetIsRight() []bool {
	if x != nil {
		return x.IsRight
	}
	return nil
}

var File_com_digitalasset_canton_protocol_v30_confirmation_response_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDesc = []byte{
	0x0a, 0x40, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63,
	0x6f, 0x6c, 0x2f, 0x76, 0x33, 0x30, 0x2f, 0x63, 0x6f, 0x6e, 0x66, 0x69, 0x72, 0x6d, 0x61, 0x74,
	0x69, 0x6f, 0x6e, 0x5f, 0x72, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x12, 0x24, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x33, 0x30, 0x1a, 0x17, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65,
	0x2f, 0x72, 0x70, 0x63, 0x2f, 0x73, 0x74, 0x61, 0x74, 0x75, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x22, 0x9d, 0x02, 0x0a, 0x0c, 0x4c, 0x6f, 0x63, 0x61, 0x6c, 0x56, 0x65, 0x72, 0x64, 0x69,
	0x63, 0x74, 0x12, 0x52, 0x0a, 0x04, 0x63, 0x6f, 0x64, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0e,
	0x32, 0x3e, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73,
	0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x33, 0x30, 0x2e, 0x4c, 0x6f, 0x63, 0x61, 0x6c, 0x56, 0x65, 0x72,
	0x64, 0x69, 0x63, 0x74, 0x2e, 0x56, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x43, 0x6f, 0x64, 0x65,
	0x52, 0x04, 0x63, 0x6f, 0x64, 0x65, 0x12, 0x2a, 0x0a, 0x06, 0x72, 0x65, 0x61, 0x73, 0x6f, 0x6e,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x12, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e,
	0x72, 0x70, 0x63, 0x2e, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x52, 0x06, 0x72, 0x65, 0x61, 0x73,
	0x6f, 0x6e, 0x22, 0x8c, 0x01, 0x0a, 0x0b, 0x56, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x43, 0x6f,
	0x64, 0x65, 0x12, 0x1c, 0x0a, 0x18, 0x56, 0x45, 0x52, 0x44, 0x49, 0x43, 0x54, 0x5f, 0x43, 0x4f,
	0x44, 0x45, 0x5f, 0x55, 0x4e, 0x53, 0x50, 0x45, 0x43, 0x49, 0x46, 0x49, 0x45, 0x44, 0x10, 0x00,
	0x12, 0x1e, 0x0a, 0x1a, 0x56, 0x45, 0x52, 0x44, 0x49, 0x43, 0x54, 0x5f, 0x43, 0x4f, 0x44, 0x45,
	0x5f, 0x4c, 0x4f, 0x43, 0x41, 0x4c, 0x5f, 0x41, 0x50, 0x50, 0x52, 0x4f, 0x56, 0x45, 0x10, 0x01,
	0x12, 0x1d, 0x0a, 0x19, 0x56, 0x45, 0x52, 0x44, 0x49, 0x43, 0x54, 0x5f, 0x43, 0x4f, 0x44, 0x45,
	0x5f, 0x4c, 0x4f, 0x43, 0x41, 0x4c, 0x5f, 0x52, 0x45, 0x4a, 0x45, 0x43, 0x54, 0x10, 0x02, 0x12,
	0x20, 0x0a, 0x1c, 0x56, 0x45, 0x52, 0x44, 0x49, 0x43, 0x54, 0x5f, 0x43, 0x4f, 0x44, 0x45, 0x5f,
	0x4c, 0x4f, 0x43, 0x41, 0x4c, 0x5f, 0x4d, 0x41, 0x4c, 0x46, 0x4f, 0x52, 0x4d, 0x45, 0x44, 0x10,
	0x03, 0x22, 0xe8, 0x02, 0x0a, 0x14, 0x43, 0x6f, 0x6e, 0x66, 0x69, 0x72, 0x6d, 0x61, 0x74, 0x69,
	0x6f, 0x6e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x1d, 0x0a, 0x0a, 0x72, 0x65,
	0x71, 0x75, 0x65, 0x73, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x03, 0x52, 0x09,
	0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x49, 0x64, 0x12, 0x16, 0x0a, 0x06, 0x73, 0x65, 0x6e,
	0x64, 0x65, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x73, 0x65, 0x6e, 0x64, 0x65,
	0x72, 0x12, 0x57, 0x0a, 0x0d, 0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x5f, 0x76, 0x65, 0x72, 0x64, 0x69,
	0x63, 0x74, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x32, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74,
	0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x33, 0x30, 0x2e,
	0x4c, 0x6f, 0x63, 0x61, 0x6c, 0x56, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x52, 0x0c, 0x6c, 0x6f,
	0x63, 0x61, 0x6c, 0x56, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x12, 0x1b, 0x0a, 0x09, 0x72, 0x6f,
	0x6f, 0x74, 0x5f, 0x68, 0x61, 0x73, 0x68, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0c, 0x52, 0x08, 0x72,
	0x6f, 0x6f, 0x74, 0x48, 0x61, 0x73, 0x68, 0x12, 0x2d, 0x0a, 0x12, 0x63, 0x6f, 0x6e, 0x66, 0x69,
	0x72, 0x6d, 0x69, 0x6e, 0x67, 0x5f, 0x70, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x18, 0x05, 0x20,
	0x03, 0x28, 0x09, 0x52, 0x11, 0x63, 0x6f, 0x6e, 0x66, 0x69, 0x72, 0x6d, 0x69, 0x6e, 0x67, 0x50,
	0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x12, 0x1b, 0x0a, 0x09, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e,
	0x5f, 0x69, 0x64, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x64, 0x6f, 0x6d, 0x61, 0x69,
	0x6e, 0x49, 0x64, 0x12, 0x57, 0x0a, 0x0d, 0x76, 0x69, 0x65, 0x77, 0x5f, 0x70, 0x6f, 0x73, 0x69,
	0x74, 0x69, 0x6f, 0x6e, 0x18, 0x07, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x32, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x33,
	0x30, 0x2e, 0x56, 0x69, 0x65, 0x77, 0x50, 0x6f, 0x73, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x0c,
	0x76, 0x69, 0x65, 0x77, 0x50, 0x6f, 0x73, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x22, 0x60, 0x0a, 0x0c,
	0x56, 0x69, 0x65, 0x77, 0x50, 0x6f, 0x73, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x50, 0x0a, 0x08,
	0x70, 0x6f, 0x73, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x34,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65,
	0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f,
	0x6c, 0x2e, 0x76, 0x33, 0x30, 0x2e, 0x4d, 0x65, 0x72, 0x6b, 0x6c, 0x65, 0x53, 0x65, 0x71, 0x49,
	0x6e, 0x64, 0x65, 0x78, 0x52, 0x08, 0x70, 0x6f, 0x73, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x22, 0x2b,
	0x0a, 0x0e, 0x4d, 0x65, 0x72, 0x6b, 0x6c, 0x65, 0x53, 0x65, 0x71, 0x49, 0x6e, 0x64, 0x65, 0x78,
	0x12, 0x19, 0x0a, 0x08, 0x69, 0x73, 0x5f, 0x72, 0x69, 0x67, 0x68, 0x74, 0x18, 0x01, 0x20, 0x03,
	0x28, 0x08, 0x52, 0x07, 0x69, 0x73, 0x52, 0x69, 0x67, 0x68, 0x74, 0x42, 0x55, 0x5a, 0x53, 0x67,
	0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61,
	0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69,
	0x65, 0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f,
	0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63,
	0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76,
	0x33, 0x30, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescData = file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDesc
)

func file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescData)
	})
	return file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescData
}

var file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_goTypes = []any{
	(LocalVerdict_VerdictCode)(0), // 0: com.digitalasset.canton.protocol.v30.LocalVerdict.VerdictCode
	(*LocalVerdict)(nil),          // 1: com.digitalasset.canton.protocol.v30.LocalVerdict
	(*ConfirmationResponse)(nil),  // 2: com.digitalasset.canton.protocol.v30.ConfirmationResponse
	(*ViewPosition)(nil),          // 3: com.digitalasset.canton.protocol.v30.ViewPosition
	(*MerkleSeqIndex)(nil),        // 4: com.digitalasset.canton.protocol.v30.MerkleSeqIndex
	(*status.Status)(nil),         // 5: google.rpc.Status
}
var file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_depIdxs = []int32{
	0, // 0: com.digitalasset.canton.protocol.v30.LocalVerdict.code:type_name -> com.digitalasset.canton.protocol.v30.LocalVerdict.VerdictCode
	5, // 1: com.digitalasset.canton.protocol.v30.LocalVerdict.reason:type_name -> google.rpc.Status
	1, // 2: com.digitalasset.canton.protocol.v30.ConfirmationResponse.local_verdict:type_name -> com.digitalasset.canton.protocol.v30.LocalVerdict
	3, // 3: com.digitalasset.canton.protocol.v30.ConfirmationResponse.view_position:type_name -> com.digitalasset.canton.protocol.v30.ViewPosition
	4, // 4: com.digitalasset.canton.protocol.v30.ViewPosition.position:type_name -> com.digitalasset.canton.protocol.v30.MerkleSeqIndex
	5, // [5:5] is the sub-list for method output_type
	5, // [5:5] is the sub-list for method input_type
	5, // [5:5] is the sub-list for extension type_name
	5, // [5:5] is the sub-list for extension extendee
	0, // [0:5] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_init() }
func file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_init() {
	if File_com_digitalasset_canton_protocol_v30_confirmation_response_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDesc,
			NumEnums:      1,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_depIdxs,
		EnumInfos:         file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_enumTypes,
		MessageInfos:      file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_protocol_v30_confirmation_response_proto = out.File
	file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDesc = nil
	file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_goTypes = nil
	file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_depIdxs = nil
}
