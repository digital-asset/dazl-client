// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/daml/ledger/api/v2/package_service.proto

package v2

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

type PackageStatus int32

const (
	PackageStatus_PACKAGE_STATUS_UNSPECIFIED PackageStatus = 0
	PackageStatus_PACKAGE_STATUS_REGISTERED  PackageStatus = 1
)

// Enum value maps for PackageStatus.
var (
	PackageStatus_name = map[int32]string{
		0: "PACKAGE_STATUS_UNSPECIFIED",
		1: "PACKAGE_STATUS_REGISTERED",
	}
	PackageStatus_value = map[string]int32{
		"PACKAGE_STATUS_UNSPECIFIED": 0,
		"PACKAGE_STATUS_REGISTERED":  1,
	}
)

func (x PackageStatus) Enum() *PackageStatus {
	p := new(PackageStatus)
	*p = x
	return p
}

func (x PackageStatus) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (PackageStatus) Descriptor() protoreflect.EnumDescriptor {
	return file_com_daml_ledger_api_v2_package_service_proto_enumTypes[0].Descriptor()
}

func (PackageStatus) Type() protoreflect.EnumType {
	return &file_com_daml_ledger_api_v2_package_service_proto_enumTypes[0]
}

func (x PackageStatus) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use PackageStatus.Descriptor instead.
func (PackageStatus) EnumDescriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_package_service_proto_rawDescGZIP(), []int{0}
}

type HashFunction int32

const (
	HashFunction_HASH_FUNCTION_SHA256 HashFunction = 0
)

// Enum value maps for HashFunction.
var (
	HashFunction_name = map[int32]string{
		0: "HASH_FUNCTION_SHA256",
	}
	HashFunction_value = map[string]int32{
		"HASH_FUNCTION_SHA256": 0,
	}
)

func (x HashFunction) Enum() *HashFunction {
	p := new(HashFunction)
	*p = x
	return p
}

func (x HashFunction) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (HashFunction) Descriptor() protoreflect.EnumDescriptor {
	return file_com_daml_ledger_api_v2_package_service_proto_enumTypes[1].Descriptor()
}

func (HashFunction) Type() protoreflect.EnumType {
	return &file_com_daml_ledger_api_v2_package_service_proto_enumTypes[1]
}

func (x HashFunction) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use HashFunction.Descriptor instead.
func (HashFunction) EnumDescriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_package_service_proto_rawDescGZIP(), []int{1}
}

type ListPackagesResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	PackageIds []string `protobuf:"bytes,1,rep,name=package_ids,json=packageIds,proto3" json:"package_ids,omitempty"`
}

func (x *ListPackagesResponse) Reset() {
	*x = ListPackagesResponse{}
	mi := &file_com_daml_ledger_api_v2_package_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListPackagesResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListPackagesResponse) ProtoMessage() {}

func (x *ListPackagesResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_package_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListPackagesResponse.ProtoReflect.Descriptor instead.
func (*ListPackagesResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_package_service_proto_rawDescGZIP(), []int{0}
}

func (x *ListPackagesResponse) GetPackageIds() []string {
	if x != nil {
		return x.PackageIds
	}
	return nil
}

type GetPackageResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	HashFunction   HashFunction `protobuf:"varint,1,opt,name=hash_function,json=hashFunction,proto3,enum=com.daml.ledger.api.v2.HashFunction" json:"hash_function,omitempty"`
	ArchivePayload []byte       `protobuf:"bytes,2,opt,name=archive_payload,json=archivePayload,proto3" json:"archive_payload,omitempty"`
	Hash           string       `protobuf:"bytes,3,opt,name=hash,proto3" json:"hash,omitempty"`
}

func (x *GetPackageResponse) Reset() {
	*x = GetPackageResponse{}
	mi := &file_com_daml_ledger_api_v2_package_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetPackageResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetPackageResponse) ProtoMessage() {}

func (x *GetPackageResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_package_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetPackageResponse.ProtoReflect.Descriptor instead.
func (*GetPackageResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_package_service_proto_rawDescGZIP(), []int{1}
}

func (x *GetPackageResponse) GetHashFunction() HashFunction {
	if x != nil {
		return x.HashFunction
	}
	return HashFunction_HASH_FUNCTION_SHA256
}

func (x *GetPackageResponse) GetArchivePayload() []byte {
	if x != nil {
		return x.ArchivePayload
	}
	return nil
}

func (x *GetPackageResponse) GetHash() string {
	if x != nil {
		return x.Hash
	}
	return ""
}

type GetPackageStatusResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	PackageStatus PackageStatus `protobuf:"varint,1,opt,name=package_status,json=packageStatus,proto3,enum=com.daml.ledger.api.v2.PackageStatus" json:"package_status,omitempty"`
}

func (x *GetPackageStatusResponse) Reset() {
	*x = GetPackageStatusResponse{}
	mi := &file_com_daml_ledger_api_v2_package_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetPackageStatusResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetPackageStatusResponse) ProtoMessage() {}

func (x *GetPackageStatusResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_package_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetPackageStatusResponse.ProtoReflect.Descriptor instead.
func (*GetPackageStatusResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_package_service_proto_rawDescGZIP(), []int{2}
}

func (x *GetPackageStatusResponse) GetPackageStatus() PackageStatus {
	if x != nil {
		return x.PackageStatus
	}
	return PackageStatus_PACKAGE_STATUS_UNSPECIFIED
}

type ListPackagesRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *ListPackagesRequest) Reset() {
	*x = ListPackagesRequest{}
	mi := &file_com_daml_ledger_api_v2_package_service_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListPackagesRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListPackagesRequest) ProtoMessage() {}

func (x *ListPackagesRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_package_service_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListPackagesRequest.ProtoReflect.Descriptor instead.
func (*ListPackagesRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_package_service_proto_rawDescGZIP(), []int{3}
}

type GetPackageRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	PackageId string `protobuf:"bytes,1,opt,name=package_id,json=packageId,proto3" json:"package_id,omitempty"`
}

func (x *GetPackageRequest) Reset() {
	*x = GetPackageRequest{}
	mi := &file_com_daml_ledger_api_v2_package_service_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetPackageRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetPackageRequest) ProtoMessage() {}

func (x *GetPackageRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_package_service_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetPackageRequest.ProtoReflect.Descriptor instead.
func (*GetPackageRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_package_service_proto_rawDescGZIP(), []int{4}
}

func (x *GetPackageRequest) GetPackageId() string {
	if x != nil {
		return x.PackageId
	}
	return ""
}

type GetPackageStatusRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	PackageId string `protobuf:"bytes,1,opt,name=package_id,json=packageId,proto3" json:"package_id,omitempty"`
}

func (x *GetPackageStatusRequest) Reset() {
	*x = GetPackageStatusRequest{}
	mi := &file_com_daml_ledger_api_v2_package_service_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetPackageStatusRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetPackageStatusRequest) ProtoMessage() {}

func (x *GetPackageStatusRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_package_service_proto_msgTypes[5]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetPackageStatusRequest.ProtoReflect.Descriptor instead.
func (*GetPackageStatusRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_package_service_proto_rawDescGZIP(), []int{5}
}

func (x *GetPackageStatusRequest) GetPackageId() string {
	if x != nil {
		return x.PackageId
	}
	return ""
}

var File_com_daml_ledger_api_v2_package_service_proto protoreflect.FileDescriptor

var file_com_daml_ledger_api_v2_package_service_proto_rawDesc = []byte{
	0x0a, 0x2c, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x32, 0x2f, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65,
	0x5f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x16,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e,
	0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x22, 0x37, 0x0a, 0x14, 0x4c, 0x69, 0x73, 0x74, 0x50, 0x61,
	0x63, 0x6b, 0x61, 0x67, 0x65, 0x73, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x1f,
	0x0a, 0x0b, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x5f, 0x69, 0x64, 0x73, 0x18, 0x01, 0x20,
	0x03, 0x28, 0x09, 0x52, 0x0a, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x49, 0x64, 0x73, 0x22,
	0x9c, 0x01, 0x0a, 0x12, 0x47, 0x65, 0x74, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65,
	0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x49, 0x0a, 0x0d, 0x68, 0x61, 0x73, 0x68, 0x5f, 0x66,
	0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x24, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e,
	0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x48, 0x61, 0x73, 0x68, 0x46, 0x75, 0x6e, 0x63, 0x74,
	0x69, 0x6f, 0x6e, 0x52, 0x0c, 0x68, 0x61, 0x73, 0x68, 0x46, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f,
	0x6e, 0x12, 0x27, 0x0a, 0x0f, 0x61, 0x72, 0x63, 0x68, 0x69, 0x76, 0x65, 0x5f, 0x70, 0x61, 0x79,
	0x6c, 0x6f, 0x61, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0c, 0x52, 0x0e, 0x61, 0x72, 0x63, 0x68,
	0x69, 0x76, 0x65, 0x50, 0x61, 0x79, 0x6c, 0x6f, 0x61, 0x64, 0x12, 0x12, 0x0a, 0x04, 0x68, 0x61,
	0x73, 0x68, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x68, 0x61, 0x73, 0x68, 0x22, 0x68,
	0x0a, 0x18, 0x47, 0x65, 0x74, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x53, 0x74, 0x61, 0x74,
	0x75, 0x73, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x4c, 0x0a, 0x0e, 0x70, 0x61,
	0x63, 0x6b, 0x61, 0x67, 0x65, 0x5f, 0x73, 0x74, 0x61, 0x74, 0x75, 0x73, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x0e, 0x32, 0x25, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65,
	0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x50, 0x61, 0x63, 0x6b,
	0x61, 0x67, 0x65, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x52, 0x0d, 0x70, 0x61, 0x63, 0x6b, 0x61,
	0x67, 0x65, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x22, 0x15, 0x0a, 0x13, 0x4c, 0x69, 0x73, 0x74,
	0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x22,
	0x32, 0x0a, 0x11, 0x47, 0x65, 0x74, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65, 0x71,
	0x75, 0x65, 0x73, 0x74, 0x12, 0x1d, 0x0a, 0x0a, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x5f,
	0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67,
	0x65, 0x49, 0x64, 0x22, 0x38, 0x0a, 0x17, 0x47, 0x65, 0x74, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67,
	0x65, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x1d,
	0x0a, 0x0a, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x09, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x49, 0x64, 0x2a, 0x4e, 0x0a,
	0x0d, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x12, 0x1e,
	0x0a, 0x1a, 0x50, 0x41, 0x43, 0x4b, 0x41, 0x47, 0x45, 0x5f, 0x53, 0x54, 0x41, 0x54, 0x55, 0x53,
	0x5f, 0x55, 0x4e, 0x53, 0x50, 0x45, 0x43, 0x49, 0x46, 0x49, 0x45, 0x44, 0x10, 0x00, 0x12, 0x1d,
	0x0a, 0x19, 0x50, 0x41, 0x43, 0x4b, 0x41, 0x47, 0x45, 0x5f, 0x53, 0x54, 0x41, 0x54, 0x55, 0x53,
	0x5f, 0x52, 0x45, 0x47, 0x49, 0x53, 0x54, 0x45, 0x52, 0x45, 0x44, 0x10, 0x01, 0x2a, 0x28, 0x0a,
	0x0c, 0x48, 0x61, 0x73, 0x68, 0x46, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x18, 0x0a,
	0x14, 0x48, 0x41, 0x53, 0x48, 0x5f, 0x46, 0x55, 0x4e, 0x43, 0x54, 0x49, 0x4f, 0x4e, 0x5f, 0x53,
	0x48, 0x41, 0x32, 0x35, 0x36, 0x10, 0x00, 0x32, 0xd7, 0x02, 0x0a, 0x0e, 0x50, 0x61, 0x63, 0x6b,
	0x61, 0x67, 0x65, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x69, 0x0a, 0x0c, 0x4c, 0x69,
	0x73, 0x74, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x73, 0x12, 0x2b, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x76, 0x32, 0x2e, 0x4c, 0x69, 0x73, 0x74, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x73,
	0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x2c, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61,
	0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32,
	0x2e, 0x4c, 0x69, 0x73, 0x74, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x73, 0x52, 0x65, 0x73,
	0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x63, 0x0a, 0x0a, 0x47, 0x65, 0x74, 0x50, 0x61, 0x63, 0x6b,
	0x61, 0x67, 0x65, 0x12, 0x29, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c,
	0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x47, 0x65, 0x74,
	0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x2a,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x47, 0x65, 0x74, 0x50, 0x61, 0x63, 0x6b, 0x61,
	0x67, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x75, 0x0a, 0x10, 0x47, 0x65,
	0x74, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x12, 0x2f,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x47, 0x65, 0x74, 0x50, 0x61, 0x63, 0x6b, 0x61,
	0x67, 0x65, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a,
	0x30, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x47, 0x65, 0x74, 0x50, 0x61, 0x63, 0x6b,
	0x61, 0x67, 0x65, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73,
	0x65, 0x42, 0x92, 0x01, 0x0a, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c,
	0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x42, 0x18, 0x50, 0x61,
	0x63, 0x6b, 0x61, 0x67, 0x65, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x4f, 0x75, 0x74, 0x65,
	0x72, 0x43, 0x6c, 0x61, 0x73, 0x73, 0x5a, 0x45, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63,
	0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f,
	0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f,
	0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x32, 0xaa, 0x02, 0x16,
	0x43, 0x6f, 0x6d, 0x2e, 0x44, 0x61, 0x6d, 0x6c, 0x2e, 0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e,
	0x41, 0x70, 0x69, 0x2e, 0x56, 0x32, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_daml_ledger_api_v2_package_service_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v2_package_service_proto_rawDescData = file_com_daml_ledger_api_v2_package_service_proto_rawDesc
)

func file_com_daml_ledger_api_v2_package_service_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v2_package_service_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v2_package_service_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_ledger_api_v2_package_service_proto_rawDescData)
	})
	return file_com_daml_ledger_api_v2_package_service_proto_rawDescData
}

var file_com_daml_ledger_api_v2_package_service_proto_enumTypes = make([]protoimpl.EnumInfo, 2)
var file_com_daml_ledger_api_v2_package_service_proto_msgTypes = make([]protoimpl.MessageInfo, 6)
var file_com_daml_ledger_api_v2_package_service_proto_goTypes = []any{
	(PackageStatus)(0),               // 0: com.daml.ledger.api.v2.PackageStatus
	(HashFunction)(0),                // 1: com.daml.ledger.api.v2.HashFunction
	(*ListPackagesResponse)(nil),     // 2: com.daml.ledger.api.v2.ListPackagesResponse
	(*GetPackageResponse)(nil),       // 3: com.daml.ledger.api.v2.GetPackageResponse
	(*GetPackageStatusResponse)(nil), // 4: com.daml.ledger.api.v2.GetPackageStatusResponse
	(*ListPackagesRequest)(nil),      // 5: com.daml.ledger.api.v2.ListPackagesRequest
	(*GetPackageRequest)(nil),        // 6: com.daml.ledger.api.v2.GetPackageRequest
	(*GetPackageStatusRequest)(nil),  // 7: com.daml.ledger.api.v2.GetPackageStatusRequest
}
var file_com_daml_ledger_api_v2_package_service_proto_depIdxs = []int32{
	1, // 0: com.daml.ledger.api.v2.GetPackageResponse.hash_function:type_name -> com.daml.ledger.api.v2.HashFunction
	0, // 1: com.daml.ledger.api.v2.GetPackageStatusResponse.package_status:type_name -> com.daml.ledger.api.v2.PackageStatus
	5, // 2: com.daml.ledger.api.v2.PackageService.ListPackages:input_type -> com.daml.ledger.api.v2.ListPackagesRequest
	6, // 3: com.daml.ledger.api.v2.PackageService.GetPackage:input_type -> com.daml.ledger.api.v2.GetPackageRequest
	7, // 4: com.daml.ledger.api.v2.PackageService.GetPackageStatus:input_type -> com.daml.ledger.api.v2.GetPackageStatusRequest
	2, // 5: com.daml.ledger.api.v2.PackageService.ListPackages:output_type -> com.daml.ledger.api.v2.ListPackagesResponse
	3, // 6: com.daml.ledger.api.v2.PackageService.GetPackage:output_type -> com.daml.ledger.api.v2.GetPackageResponse
	4, // 7: com.daml.ledger.api.v2.PackageService.GetPackageStatus:output_type -> com.daml.ledger.api.v2.GetPackageStatusResponse
	5, // [5:8] is the sub-list for method output_type
	2, // [2:5] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v2_package_service_proto_init() }
func file_com_daml_ledger_api_v2_package_service_proto_init() {
	if File_com_daml_ledger_api_v2_package_service_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_daml_ledger_api_v2_package_service_proto_rawDesc,
			NumEnums:      2,
			NumMessages:   6,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_daml_ledger_api_v2_package_service_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v2_package_service_proto_depIdxs,
		EnumInfos:         file_com_daml_ledger_api_v2_package_service_proto_enumTypes,
		MessageInfos:      file_com_daml_ledger_api_v2_package_service_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v2_package_service_proto = out.File
	file_com_daml_ledger_api_v2_package_service_proto_rawDesc = nil
	file_com_daml_ledger_api_v2_package_service_proto_goTypes = nil
	file_com_daml_ledger_api_v2_package_service_proto_depIdxs = nil
}
