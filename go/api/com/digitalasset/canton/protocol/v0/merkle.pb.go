// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/digitalasset/canton/protocol/v0/merkle.proto

package v0

import (
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

type GenTransactionTree struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	SubmitterMetadata   *BlindableNode `protobuf:"bytes,1,opt,name=submitter_metadata,json=submitterMetadata,proto3" json:"submitter_metadata,omitempty"`
	CommonMetadata      *BlindableNode `protobuf:"bytes,2,opt,name=common_metadata,json=commonMetadata,proto3" json:"common_metadata,omitempty"`
	ParticipantMetadata *BlindableNode `protobuf:"bytes,3,opt,name=participant_metadata,json=participantMetadata,proto3" json:"participant_metadata,omitempty"`
	RootViews           *MerkleSeq     `protobuf:"bytes,4,opt,name=root_views,json=rootViews,proto3" json:"root_views,omitempty"`
}

func (x *GenTransactionTree) Reset() {
	*x = GenTransactionTree{}
	mi := &file_com_digitalasset_canton_protocol_v0_merkle_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GenTransactionTree) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GenTransactionTree) ProtoMessage() {}

func (x *GenTransactionTree) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_merkle_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GenTransactionTree.ProtoReflect.Descriptor instead.
func (*GenTransactionTree) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_merkle_proto_rawDescGZIP(), []int{0}
}

func (x *GenTransactionTree) GetSubmitterMetadata() *BlindableNode {
	if x != nil {
		return x.SubmitterMetadata
	}
	return nil
}

func (x *GenTransactionTree) GetCommonMetadata() *BlindableNode {
	if x != nil {
		return x.CommonMetadata
	}
	return nil
}

func (x *GenTransactionTree) GetParticipantMetadata() *BlindableNode {
	if x != nil {
		return x.ParticipantMetadata
	}
	return nil
}

func (x *GenTransactionTree) GetRootViews() *MerkleSeq {
	if x != nil {
		return x.RootViews
	}
	return nil
}

type BlindableNode struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to BlindedOrNot:
	//
	//	*BlindableNode_Unblinded
	//	*BlindableNode_BlindedHash
	BlindedOrNot isBlindableNode_BlindedOrNot `protobuf_oneof:"blinded_or_not"`
}

func (x *BlindableNode) Reset() {
	*x = BlindableNode{}
	mi := &file_com_digitalasset_canton_protocol_v0_merkle_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *BlindableNode) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*BlindableNode) ProtoMessage() {}

func (x *BlindableNode) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_merkle_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use BlindableNode.ProtoReflect.Descriptor instead.
func (*BlindableNode) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_merkle_proto_rawDescGZIP(), []int{1}
}

func (m *BlindableNode) GetBlindedOrNot() isBlindableNode_BlindedOrNot {
	if m != nil {
		return m.BlindedOrNot
	}
	return nil
}

func (x *BlindableNode) GetUnblinded() []byte {
	if x, ok := x.GetBlindedOrNot().(*BlindableNode_Unblinded); ok {
		return x.Unblinded
	}
	return nil
}

func (x *BlindableNode) GetBlindedHash() []byte {
	if x, ok := x.GetBlindedOrNot().(*BlindableNode_BlindedHash); ok {
		return x.BlindedHash
	}
	return nil
}

type isBlindableNode_BlindedOrNot interface {
	isBlindableNode_BlindedOrNot()
}

type BlindableNode_Unblinded struct {
	Unblinded []byte `protobuf:"bytes,1,opt,name=unblinded,proto3,oneof"`
}

type BlindableNode_BlindedHash struct {
	BlindedHash []byte `protobuf:"bytes,2,opt,name=blinded_hash,json=blindedHash,proto3,oneof"`
}

func (*BlindableNode_Unblinded) isBlindableNode_BlindedOrNot() {}

func (*BlindableNode_BlindedHash) isBlindableNode_BlindedOrNot() {}

type MerkleSeq struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	RootOrEmpty *BlindableNode `protobuf:"bytes,1,opt,name=root_or_empty,json=rootOrEmpty,proto3" json:"root_or_empty,omitempty"`
}

func (x *MerkleSeq) Reset() {
	*x = MerkleSeq{}
	mi := &file_com_digitalasset_canton_protocol_v0_merkle_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *MerkleSeq) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MerkleSeq) ProtoMessage() {}

func (x *MerkleSeq) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_merkle_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use MerkleSeq.ProtoReflect.Descriptor instead.
func (*MerkleSeq) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_merkle_proto_rawDescGZIP(), []int{2}
}

func (x *MerkleSeq) GetRootOrEmpty() *BlindableNode {
	if x != nil {
		return x.RootOrEmpty
	}
	return nil
}

type MerkleSeqElement struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	First  *BlindableNode `protobuf:"bytes,1,opt,name=first,proto3" json:"first,omitempty"`
	Second *BlindableNode `protobuf:"bytes,2,opt,name=second,proto3" json:"second,omitempty"`
	Data   *BlindableNode `protobuf:"bytes,3,opt,name=data,proto3" json:"data,omitempty"`
}

func (x *MerkleSeqElement) Reset() {
	*x = MerkleSeqElement{}
	mi := &file_com_digitalasset_canton_protocol_v0_merkle_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *MerkleSeqElement) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MerkleSeqElement) ProtoMessage() {}

func (x *MerkleSeqElement) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_merkle_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use MerkleSeqElement.ProtoReflect.Descriptor instead.
func (*MerkleSeqElement) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_merkle_proto_rawDescGZIP(), []int{3}
}

func (x *MerkleSeqElement) GetFirst() *BlindableNode {
	if x != nil {
		return x.First
	}
	return nil
}

func (x *MerkleSeqElement) GetSecond() *BlindableNode {
	if x != nil {
		return x.Second
	}
	return nil
}

func (x *MerkleSeqElement) GetData() *BlindableNode {
	if x != nil {
		return x.Data
	}
	return nil
}

var File_com_digitalasset_canton_protocol_v0_merkle_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_protocol_v0_merkle_proto_rawDesc = []byte{
	0x0a, 0x30, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63,
	0x6f, 0x6c, 0x2f, 0x76, 0x30, 0x2f, 0x6d, 0x65, 0x72, 0x6b, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x12, 0x23, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x22, 0x8a, 0x03, 0x0a, 0x12, 0x47, 0x65, 0x6e, 0x54,
	0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x54, 0x72, 0x65, 0x65, 0x12, 0x61,
	0x0a, 0x12, 0x73, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x74, 0x65, 0x72, 0x5f, 0x6d, 0x65, 0x74, 0x61,
	0x64, 0x61, 0x74, 0x61, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x32, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30,
	0x2e, 0x42, 0x6c, 0x69, 0x6e, 0x64, 0x61, 0x62, 0x6c, 0x65, 0x4e, 0x6f, 0x64, 0x65, 0x52, 0x11,
	0x73, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x74, 0x65, 0x72, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74,
	0x61, 0x12, 0x5b, 0x0a, 0x0f, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x5f, 0x6d, 0x65, 0x74, 0x61,
	0x64, 0x61, 0x74, 0x61, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x32, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30,
	0x2e, 0x42, 0x6c, 0x69, 0x6e, 0x64, 0x61, 0x62, 0x6c, 0x65, 0x4e, 0x6f, 0x64, 0x65, 0x52, 0x0e,
	0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x12, 0x65,
	0x0a, 0x14, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x5f, 0x6d, 0x65,
	0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x32, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e,
	0x76, 0x30, 0x2e, 0x42, 0x6c, 0x69, 0x6e, 0x64, 0x61, 0x62, 0x6c, 0x65, 0x4e, 0x6f, 0x64, 0x65,
	0x52, 0x13, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x4d, 0x65, 0x74,
	0x61, 0x64, 0x61, 0x74, 0x61, 0x12, 0x4d, 0x0a, 0x0a, 0x72, 0x6f, 0x6f, 0x74, 0x5f, 0x76, 0x69,
	0x65, 0x77, 0x73, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2e, 0x2e, 0x63, 0x6f, 0x6d, 0x2e,
	0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e,
	0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e,
	0x4d, 0x65, 0x72, 0x6b, 0x6c, 0x65, 0x53, 0x65, 0x71, 0x52, 0x09, 0x72, 0x6f, 0x6f, 0x74, 0x56,
	0x69, 0x65, 0x77, 0x73, 0x22, 0x66, 0x0a, 0x0d, 0x42, 0x6c, 0x69, 0x6e, 0x64, 0x61, 0x62, 0x6c,
	0x65, 0x4e, 0x6f, 0x64, 0x65, 0x12, 0x1e, 0x0a, 0x09, 0x75, 0x6e, 0x62, 0x6c, 0x69, 0x6e, 0x64,
	0x65, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0c, 0x48, 0x00, 0x52, 0x09, 0x75, 0x6e, 0x62, 0x6c,
	0x69, 0x6e, 0x64, 0x65, 0x64, 0x12, 0x23, 0x0a, 0x0c, 0x62, 0x6c, 0x69, 0x6e, 0x64, 0x65, 0x64,
	0x5f, 0x68, 0x61, 0x73, 0x68, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0c, 0x48, 0x00, 0x52, 0x0b, 0x62,
	0x6c, 0x69, 0x6e, 0x64, 0x65, 0x64, 0x48, 0x61, 0x73, 0x68, 0x42, 0x10, 0x0a, 0x0e, 0x62, 0x6c,
	0x69, 0x6e, 0x64, 0x65, 0x64, 0x5f, 0x6f, 0x72, 0x5f, 0x6e, 0x6f, 0x74, 0x22, 0x63, 0x0a, 0x09,
	0x4d, 0x65, 0x72, 0x6b, 0x6c, 0x65, 0x53, 0x65, 0x71, 0x12, 0x56, 0x0a, 0x0d, 0x72, 0x6f, 0x6f,
	0x74, 0x5f, 0x6f, 0x72, 0x5f, 0x65, 0x6d, 0x70, 0x74, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x32, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73,
	0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x42, 0x6c, 0x69, 0x6e, 0x64, 0x61, 0x62, 0x6c, 0x65,
	0x4e, 0x6f, 0x64, 0x65, 0x52, 0x0b, 0x72, 0x6f, 0x6f, 0x74, 0x4f, 0x72, 0x45, 0x6d, 0x70, 0x74,
	0x79, 0x22, 0xf0, 0x01, 0x0a, 0x10, 0x4d, 0x65, 0x72, 0x6b, 0x6c, 0x65, 0x53, 0x65, 0x71, 0x45,
	0x6c, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x12, 0x48, 0x0a, 0x05, 0x66, 0x69, 0x72, 0x73, 0x74, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x32, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69,
	0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x42, 0x6c, 0x69, 0x6e,
	0x64, 0x61, 0x62, 0x6c, 0x65, 0x4e, 0x6f, 0x64, 0x65, 0x52, 0x05, 0x66, 0x69, 0x72, 0x73, 0x74,
	0x12, 0x4a, 0x0a, 0x06, 0x73, 0x65, 0x63, 0x6f, 0x6e, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x32, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73,
	0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x42, 0x6c, 0x69, 0x6e, 0x64, 0x61, 0x62, 0x6c, 0x65,
	0x4e, 0x6f, 0x64, 0x65, 0x52, 0x06, 0x73, 0x65, 0x63, 0x6f, 0x6e, 0x64, 0x12, 0x46, 0x0a, 0x04,
	0x64, 0x61, 0x74, 0x61, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x32, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30,
	0x2e, 0x42, 0x6c, 0x69, 0x6e, 0x64, 0x61, 0x62, 0x6c, 0x65, 0x4e, 0x6f, 0x64, 0x65, 0x52, 0x04,
	0x64, 0x61, 0x74, 0x61, 0x42, 0x54, 0x5a, 0x52, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63,
	0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f,
	0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74,
	0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x30, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_protocol_v0_merkle_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_protocol_v0_merkle_proto_rawDescData = file_com_digitalasset_canton_protocol_v0_merkle_proto_rawDesc
)

func file_com_digitalasset_canton_protocol_v0_merkle_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_protocol_v0_merkle_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_protocol_v0_merkle_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_protocol_v0_merkle_proto_rawDescData)
	})
	return file_com_digitalasset_canton_protocol_v0_merkle_proto_rawDescData
}

var file_com_digitalasset_canton_protocol_v0_merkle_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_com_digitalasset_canton_protocol_v0_merkle_proto_goTypes = []any{
	(*GenTransactionTree)(nil), // 0: com.digitalasset.canton.protocol.v0.GenTransactionTree
	(*BlindableNode)(nil),      // 1: com.digitalasset.canton.protocol.v0.BlindableNode
	(*MerkleSeq)(nil),          // 2: com.digitalasset.canton.protocol.v0.MerkleSeq
	(*MerkleSeqElement)(nil),   // 3: com.digitalasset.canton.protocol.v0.MerkleSeqElement
}
var file_com_digitalasset_canton_protocol_v0_merkle_proto_depIdxs = []int32{
	1, // 0: com.digitalasset.canton.protocol.v0.GenTransactionTree.submitter_metadata:type_name -> com.digitalasset.canton.protocol.v0.BlindableNode
	1, // 1: com.digitalasset.canton.protocol.v0.GenTransactionTree.common_metadata:type_name -> com.digitalasset.canton.protocol.v0.BlindableNode
	1, // 2: com.digitalasset.canton.protocol.v0.GenTransactionTree.participant_metadata:type_name -> com.digitalasset.canton.protocol.v0.BlindableNode
	2, // 3: com.digitalasset.canton.protocol.v0.GenTransactionTree.root_views:type_name -> com.digitalasset.canton.protocol.v0.MerkleSeq
	1, // 4: com.digitalasset.canton.protocol.v0.MerkleSeq.root_or_empty:type_name -> com.digitalasset.canton.protocol.v0.BlindableNode
	1, // 5: com.digitalasset.canton.protocol.v0.MerkleSeqElement.first:type_name -> com.digitalasset.canton.protocol.v0.BlindableNode
	1, // 6: com.digitalasset.canton.protocol.v0.MerkleSeqElement.second:type_name -> com.digitalasset.canton.protocol.v0.BlindableNode
	1, // 7: com.digitalasset.canton.protocol.v0.MerkleSeqElement.data:type_name -> com.digitalasset.canton.protocol.v0.BlindableNode
	8, // [8:8] is the sub-list for method output_type
	8, // [8:8] is the sub-list for method input_type
	8, // [8:8] is the sub-list for extension type_name
	8, // [8:8] is the sub-list for extension extendee
	0, // [0:8] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_protocol_v0_merkle_proto_init() }
func file_com_digitalasset_canton_protocol_v0_merkle_proto_init() {
	if File_com_digitalasset_canton_protocol_v0_merkle_proto != nil {
		return
	}
	file_com_digitalasset_canton_protocol_v0_merkle_proto_msgTypes[1].OneofWrappers = []any{
		(*BlindableNode_Unblinded)(nil),
		(*BlindableNode_BlindedHash)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_protocol_v0_merkle_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_protocol_v0_merkle_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_protocol_v0_merkle_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_protocol_v0_merkle_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_protocol_v0_merkle_proto = out.File
	file_com_digitalasset_canton_protocol_v0_merkle_proto_rawDesc = nil
	file_com_digitalasset_canton_protocol_v0_merkle_proto_goTypes = nil
	file_com_digitalasset_canton_protocol_v0_merkle_proto_depIdxs = nil
}
