// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/digitalasset/canton/protocol/v0/common.proto

package v0

import (
	v0 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/crypto/v0"
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

type ViewType int32

const (
	ViewType_MissingViewType     ViewType = 0
	ViewType_TransactionViewType ViewType = 1
	ViewType_TransferOutViewType ViewType = 2
	ViewType_TransferInViewType  ViewType = 3
)

// Enum value maps for ViewType.
var (
	ViewType_name = map[int32]string{
		0: "MissingViewType",
		1: "TransactionViewType",
		2: "TransferOutViewType",
		3: "TransferInViewType",
	}
	ViewType_value = map[string]int32{
		"MissingViewType":     0,
		"TransactionViewType": 1,
		"TransferOutViewType": 2,
		"TransferInViewType":  3,
	}
)

func (x ViewType) Enum() *ViewType {
	p := new(ViewType)
	*p = x
	return p
}

func (x ViewType) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (ViewType) Descriptor() protoreflect.EnumDescriptor {
	return file_com_digitalasset_canton_protocol_v0_common_proto_enumTypes[0].Descriptor()
}

func (ViewType) Type() protoreflect.EnumType {
	return &file_com_digitalasset_canton_protocol_v0_common_proto_enumTypes[0]
}

func (x ViewType) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use ViewType.Descriptor instead.
func (ViewType) EnumDescriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_common_proto_rawDescGZIP(), []int{0}
}

type SerializableContract struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ContractId          string                         `protobuf:"bytes,1,opt,name=contract_id,json=contractId,proto3" json:"contract_id,omitempty"`
	RawContractInstance []byte                         `protobuf:"bytes,2,opt,name=raw_contract_instance,json=rawContractInstance,proto3" json:"raw_contract_instance,omitempty"`
	Metadata            *SerializableContract_Metadata `protobuf:"bytes,3,opt,name=metadata,proto3" json:"metadata,omitempty"`
	LedgerCreateTime    *timestamppb.Timestamp         `protobuf:"bytes,4,opt,name=ledger_create_time,json=ledgerCreateTime,proto3" json:"ledger_create_time,omitempty"`
}

func (x *SerializableContract) Reset() {
	*x = SerializableContract{}
	mi := &file_com_digitalasset_canton_protocol_v0_common_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SerializableContract) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SerializableContract) ProtoMessage() {}

func (x *SerializableContract) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_common_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SerializableContract.ProtoReflect.Descriptor instead.
func (*SerializableContract) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_common_proto_rawDescGZIP(), []int{0}
}

func (x *SerializableContract) GetContractId() string {
	if x != nil {
		return x.ContractId
	}
	return ""
}

func (x *SerializableContract) GetRawContractInstance() []byte {
	if x != nil {
		return x.RawContractInstance
	}
	return nil
}

func (x *SerializableContract) GetMetadata() *SerializableContract_Metadata {
	if x != nil {
		return x.Metadata
	}
	return nil
}

func (x *SerializableContract) GetLedgerCreateTime() *timestamppb.Timestamp {
	if x != nil {
		return x.LedgerCreateTime
	}
	return nil
}

type GlobalKey struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	TemplateId []byte `protobuf:"bytes,1,opt,name=template_id,json=templateId,proto3" json:"template_id,omitempty"`
	Key        []byte `protobuf:"bytes,2,opt,name=key,proto3" json:"key,omitempty"`
}

func (x *GlobalKey) Reset() {
	*x = GlobalKey{}
	mi := &file_com_digitalasset_canton_protocol_v0_common_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GlobalKey) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GlobalKey) ProtoMessage() {}

func (x *GlobalKey) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_common_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GlobalKey.ProtoReflect.Descriptor instead.
func (*GlobalKey) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_common_proto_rawDescGZIP(), []int{1}
}

func (x *GlobalKey) GetTemplateId() []byte {
	if x != nil {
		return x.TemplateId
	}
	return nil
}

func (x *GlobalKey) GetKey() []byte {
	if x != nil {
		return x.Key
	}
	return nil
}

type DriverContractMetadata struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ContractSalt *v0.Salt `protobuf:"bytes,1,opt,name=contract_salt,json=contractSalt,proto3" json:"contract_salt,omitempty"`
}

func (x *DriverContractMetadata) Reset() {
	*x = DriverContractMetadata{}
	mi := &file_com_digitalasset_canton_protocol_v0_common_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *DriverContractMetadata) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DriverContractMetadata) ProtoMessage() {}

func (x *DriverContractMetadata) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_common_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DriverContractMetadata.ProtoReflect.Descriptor instead.
func (*DriverContractMetadata) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_common_proto_rawDescGZIP(), []int{2}
}

func (x *DriverContractMetadata) GetContractSalt() *v0.Salt {
	if x != nil {
		return x.ContractSalt
	}
	return nil
}

type SerializableContract_Metadata struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	NonMaintainerSignatories []string   `protobuf:"bytes,1,rep,name=non_maintainer_signatories,json=nonMaintainerSignatories,proto3" json:"non_maintainer_signatories,omitempty"`
	NonSignatoryStakeholders []string   `protobuf:"bytes,2,rep,name=non_signatory_stakeholders,json=nonSignatoryStakeholders,proto3" json:"non_signatory_stakeholders,omitempty"`
	Key                      *GlobalKey `protobuf:"bytes,3,opt,name=key,proto3" json:"key,omitempty"`
	Maintainers              []string   `protobuf:"bytes,4,rep,name=maintainers,proto3" json:"maintainers,omitempty"`
}

func (x *SerializableContract_Metadata) Reset() {
	*x = SerializableContract_Metadata{}
	mi := &file_com_digitalasset_canton_protocol_v0_common_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SerializableContract_Metadata) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SerializableContract_Metadata) ProtoMessage() {}

func (x *SerializableContract_Metadata) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v0_common_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SerializableContract_Metadata.ProtoReflect.Descriptor instead.
func (*SerializableContract_Metadata) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v0_common_proto_rawDescGZIP(), []int{0, 0}
}

func (x *SerializableContract_Metadata) GetNonMaintainerSignatories() []string {
	if x != nil {
		return x.NonMaintainerSignatories
	}
	return nil
}

func (x *SerializableContract_Metadata) GetNonSignatoryStakeholders() []string {
	if x != nil {
		return x.NonSignatoryStakeholders
	}
	return nil
}

func (x *SerializableContract_Metadata) GetKey() *GlobalKey {
	if x != nil {
		return x.Key
	}
	return nil
}

func (x *SerializableContract_Metadata) GetMaintainers() []string {
	if x != nil {
		return x.Maintainers
	}
	return nil
}

var File_com_digitalasset_canton_protocol_v0_common_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_protocol_v0_common_proto_rawDesc = []byte{
	0x0a, 0x30, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63,
	0x6f, 0x6c, 0x2f, 0x76, 0x30, 0x2f, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x12, 0x23, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x1a, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67,
	0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e,
	0x2f, 0x63, 0x72, 0x79, 0x70, 0x74, 0x6f, 0x2f, 0x76, 0x30, 0x2f, 0x63, 0x72, 0x79, 0x70, 0x74,
	0x6f, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61,
	0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x82, 0x04, 0x0a, 0x14, 0x53, 0x65, 0x72,
	0x69, 0x61, 0x6c, 0x69, 0x7a, 0x61, 0x62, 0x6c, 0x65, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63,
	0x74, 0x12, 0x1f, 0x0a, 0x0b, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x5f, 0x69, 0x64,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74,
	0x49, 0x64, 0x12, 0x32, 0x0a, 0x15, 0x72, 0x61, 0x77, 0x5f, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61,
	0x63, 0x74, 0x5f, 0x69, 0x6e, 0x73, 0x74, 0x61, 0x6e, 0x63, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28,
	0x0c, 0x52, 0x13, 0x72, 0x61, 0x77, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x49, 0x6e,
	0x73, 0x74, 0x61, 0x6e, 0x63, 0x65, 0x12, 0x5e, 0x0a, 0x08, 0x6d, 0x65, 0x74, 0x61, 0x64, 0x61,
	0x74, 0x61, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x42, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74,
	0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x53,
	0x65, 0x72, 0x69, 0x61, 0x6c, 0x69, 0x7a, 0x61, 0x62, 0x6c, 0x65, 0x43, 0x6f, 0x6e, 0x74, 0x72,
	0x61, 0x63, 0x74, 0x2e, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x52, 0x08, 0x6d, 0x65,
	0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x12, 0x48, 0x0a, 0x12, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x5f, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x18, 0x04, 0x20, 0x01,
	0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x10,
	0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x54, 0x69, 0x6d, 0x65,
	0x1a, 0xea, 0x01, 0x0a, 0x08, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x12, 0x3c, 0x0a,
	0x1a, 0x6e, 0x6f, 0x6e, 0x5f, 0x6d, 0x61, 0x69, 0x6e, 0x74, 0x61, 0x69, 0x6e, 0x65, 0x72, 0x5f,
	0x73, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x6f, 0x72, 0x69, 0x65, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28,
	0x09, 0x52, 0x18, 0x6e, 0x6f, 0x6e, 0x4d, 0x61, 0x69, 0x6e, 0x74, 0x61, 0x69, 0x6e, 0x65, 0x72,
	0x53, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x6f, 0x72, 0x69, 0x65, 0x73, 0x12, 0x3c, 0x0a, 0x1a, 0x6e,
	0x6f, 0x6e, 0x5f, 0x73, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x6f, 0x72, 0x79, 0x5f, 0x73, 0x74, 0x61,
	0x6b, 0x65, 0x68, 0x6f, 0x6c, 0x64, 0x65, 0x72, 0x73, 0x18, 0x02, 0x20, 0x03, 0x28, 0x09, 0x52,
	0x18, 0x6e, 0x6f, 0x6e, 0x53, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x6f, 0x72, 0x79, 0x53, 0x74, 0x61,
	0x6b, 0x65, 0x68, 0x6f, 0x6c, 0x64, 0x65, 0x72, 0x73, 0x12, 0x40, 0x0a, 0x03, 0x6b, 0x65, 0x79,
	0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2e, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67,
	0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x47, 0x6c, 0x6f,
	0x62, 0x61, 0x6c, 0x4b, 0x65, 0x79, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x12, 0x20, 0x0a, 0x0b, 0x6d,
	0x61, 0x69, 0x6e, 0x74, 0x61, 0x69, 0x6e, 0x65, 0x72, 0x73, 0x18, 0x04, 0x20, 0x03, 0x28, 0x09,
	0x52, 0x0b, 0x6d, 0x61, 0x69, 0x6e, 0x74, 0x61, 0x69, 0x6e, 0x65, 0x72, 0x73, 0x22, 0x3e, 0x0a,
	0x09, 0x47, 0x6c, 0x6f, 0x62, 0x61, 0x6c, 0x4b, 0x65, 0x79, 0x12, 0x1f, 0x0a, 0x0b, 0x74, 0x65,
	0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0c, 0x52,
	0x0a, 0x74, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x49, 0x64, 0x12, 0x10, 0x0a, 0x03, 0x6b,
	0x65, 0x79, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0c, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x22, 0x66, 0x0a,
	0x16, 0x44, 0x72, 0x69, 0x76, 0x65, 0x72, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x4d,
	0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x12, 0x4c, 0x0a, 0x0d, 0x63, 0x6f, 0x6e, 0x74, 0x72,
	0x61, 0x63, 0x74, 0x5f, 0x73, 0x61, 0x6c, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x27,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65,
	0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x63, 0x72, 0x79, 0x70, 0x74, 0x6f, 0x2e,
	0x76, 0x30, 0x2e, 0x53, 0x61, 0x6c, 0x74, 0x52, 0x0c, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63,
	0x74, 0x53, 0x61, 0x6c, 0x74, 0x2a, 0x69, 0x0a, 0x08, 0x56, 0x69, 0x65, 0x77, 0x54, 0x79, 0x70,
	0x65, 0x12, 0x13, 0x0a, 0x0f, 0x4d, 0x69, 0x73, 0x73, 0x69, 0x6e, 0x67, 0x56, 0x69, 0x65, 0x77,
	0x54, 0x79, 0x70, 0x65, 0x10, 0x00, 0x12, 0x17, 0x0a, 0x13, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61,
	0x63, 0x74, 0x69, 0x6f, 0x6e, 0x56, 0x69, 0x65, 0x77, 0x54, 0x79, 0x70, 0x65, 0x10, 0x01, 0x12,
	0x17, 0x0a, 0x13, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x65, 0x72, 0x4f, 0x75, 0x74, 0x56, 0x69,
	0x65, 0x77, 0x54, 0x79, 0x70, 0x65, 0x10, 0x02, 0x12, 0x16, 0x0a, 0x12, 0x54, 0x72, 0x61, 0x6e,
	0x73, 0x66, 0x65, 0x72, 0x49, 0x6e, 0x56, 0x69, 0x65, 0x77, 0x54, 0x79, 0x70, 0x65, 0x10, 0x03,
	0x42, 0x54, 0x5a, 0x52, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64,
	0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a,
	0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61,
	0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73,
	0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x30, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_protocol_v0_common_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_protocol_v0_common_proto_rawDescData = file_com_digitalasset_canton_protocol_v0_common_proto_rawDesc
)

func file_com_digitalasset_canton_protocol_v0_common_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_protocol_v0_common_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_protocol_v0_common_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_protocol_v0_common_proto_rawDescData)
	})
	return file_com_digitalasset_canton_protocol_v0_common_proto_rawDescData
}

var file_com_digitalasset_canton_protocol_v0_common_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_com_digitalasset_canton_protocol_v0_common_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_com_digitalasset_canton_protocol_v0_common_proto_goTypes = []any{
	(ViewType)(0),                         // 0: com.digitalasset.canton.protocol.v0.ViewType
	(*SerializableContract)(nil),          // 1: com.digitalasset.canton.protocol.v0.SerializableContract
	(*GlobalKey)(nil),                     // 2: com.digitalasset.canton.protocol.v0.GlobalKey
	(*DriverContractMetadata)(nil),        // 3: com.digitalasset.canton.protocol.v0.DriverContractMetadata
	(*SerializableContract_Metadata)(nil), // 4: com.digitalasset.canton.protocol.v0.SerializableContract.Metadata
	(*timestamppb.Timestamp)(nil),         // 5: google.protobuf.Timestamp
	(*v0.Salt)(nil),                       // 6: com.digitalasset.canton.crypto.v0.Salt
}
var file_com_digitalasset_canton_protocol_v0_common_proto_depIdxs = []int32{
	4, // 0: com.digitalasset.canton.protocol.v0.SerializableContract.metadata:type_name -> com.digitalasset.canton.protocol.v0.SerializableContract.Metadata
	5, // 1: com.digitalasset.canton.protocol.v0.SerializableContract.ledger_create_time:type_name -> google.protobuf.Timestamp
	6, // 2: com.digitalasset.canton.protocol.v0.DriverContractMetadata.contract_salt:type_name -> com.digitalasset.canton.crypto.v0.Salt
	2, // 3: com.digitalasset.canton.protocol.v0.SerializableContract.Metadata.key:type_name -> com.digitalasset.canton.protocol.v0.GlobalKey
	4, // [4:4] is the sub-list for method output_type
	4, // [4:4] is the sub-list for method input_type
	4, // [4:4] is the sub-list for extension type_name
	4, // [4:4] is the sub-list for extension extendee
	0, // [0:4] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_protocol_v0_common_proto_init() }
func file_com_digitalasset_canton_protocol_v0_common_proto_init() {
	if File_com_digitalasset_canton_protocol_v0_common_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_protocol_v0_common_proto_rawDesc,
			NumEnums:      1,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_protocol_v0_common_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_protocol_v0_common_proto_depIdxs,
		EnumInfos:         file_com_digitalasset_canton_protocol_v0_common_proto_enumTypes,
		MessageInfos:      file_com_digitalasset_canton_protocol_v0_common_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_protocol_v0_common_proto = out.File
	file_com_digitalasset_canton_protocol_v0_common_proto_rawDesc = nil
	file_com_digitalasset_canton_protocol_v0_common_proto_goTypes = nil
	file_com_digitalasset_canton_protocol_v0_common_proto_depIdxs = nil
}
