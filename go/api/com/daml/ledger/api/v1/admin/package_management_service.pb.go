// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.34.2
// 	protoc        v5.27.2
// source: com/daml/ledger/api/v1/admin/package_management_service.proto

package admin

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

type ListKnownPackagesRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *ListKnownPackagesRequest) Reset() {
	*x = ListKnownPackagesRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ListKnownPackagesRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListKnownPackagesRequest) ProtoMessage() {}

func (x *ListKnownPackagesRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListKnownPackagesRequest.ProtoReflect.Descriptor instead.
func (*ListKnownPackagesRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDescGZIP(), []int{0}
}

type ListKnownPackagesResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	PackageDetails []*PackageDetails `protobuf:"bytes,1,rep,name=package_details,json=packageDetails,proto3" json:"package_details,omitempty"`
}

func (x *ListKnownPackagesResponse) Reset() {
	*x = ListKnownPackagesResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ListKnownPackagesResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListKnownPackagesResponse) ProtoMessage() {}

func (x *ListKnownPackagesResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListKnownPackagesResponse.ProtoReflect.Descriptor instead.
func (*ListKnownPackagesResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDescGZIP(), []int{1}
}

func (x *ListKnownPackagesResponse) GetPackageDetails() []*PackageDetails {
	if x != nil {
		return x.PackageDetails
	}
	return nil
}

type PackageDetails struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	PackageId         string                 `protobuf:"bytes,1,opt,name=package_id,json=packageId,proto3" json:"package_id,omitempty"`
	PackageSize       uint64                 `protobuf:"varint,2,opt,name=package_size,json=packageSize,proto3" json:"package_size,omitempty"`
	KnownSince        *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=known_since,json=knownSince,proto3" json:"known_since,omitempty"`
	SourceDescription string                 `protobuf:"bytes,4,opt,name=source_description,json=sourceDescription,proto3" json:"source_description,omitempty"`
}

func (x *PackageDetails) Reset() {
	*x = PackageDetails{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PackageDetails) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PackageDetails) ProtoMessage() {}

func (x *PackageDetails) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PackageDetails.ProtoReflect.Descriptor instead.
func (*PackageDetails) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDescGZIP(), []int{2}
}

func (x *PackageDetails) GetPackageId() string {
	if x != nil {
		return x.PackageId
	}
	return ""
}

func (x *PackageDetails) GetPackageSize() uint64 {
	if x != nil {
		return x.PackageSize
	}
	return 0
}

func (x *PackageDetails) GetKnownSince() *timestamppb.Timestamp {
	if x != nil {
		return x.KnownSince
	}
	return nil
}

func (x *PackageDetails) GetSourceDescription() string {
	if x != nil {
		return x.SourceDescription
	}
	return ""
}

type UploadDarFileRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	DarFile      []byte `protobuf:"bytes,1,opt,name=dar_file,json=darFile,proto3" json:"dar_file,omitempty"`
	SubmissionId string `protobuf:"bytes,2,opt,name=submission_id,json=submissionId,proto3" json:"submission_id,omitempty"`
}

func (x *UploadDarFileRequest) Reset() {
	*x = UploadDarFileRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *UploadDarFileRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UploadDarFileRequest) ProtoMessage() {}

func (x *UploadDarFileRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UploadDarFileRequest.ProtoReflect.Descriptor instead.
func (*UploadDarFileRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDescGZIP(), []int{3}
}

func (x *UploadDarFileRequest) GetDarFile() []byte {
	if x != nil {
		return x.DarFile
	}
	return nil
}

func (x *UploadDarFileRequest) GetSubmissionId() string {
	if x != nil {
		return x.SubmissionId
	}
	return ""
}

type UploadDarFileResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *UploadDarFileResponse) Reset() {
	*x = UploadDarFileResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *UploadDarFileResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UploadDarFileResponse) ProtoMessage() {}

func (x *UploadDarFileResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UploadDarFileResponse.ProtoReflect.Descriptor instead.
func (*UploadDarFileResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDescGZIP(), []int{4}
}

type ValidateDarFileRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	DarFile      []byte `protobuf:"bytes,1,opt,name=dar_file,json=darFile,proto3" json:"dar_file,omitempty"`
	SubmissionId string `protobuf:"bytes,2,opt,name=submission_id,json=submissionId,proto3" json:"submission_id,omitempty"`
}

func (x *ValidateDarFileRequest) Reset() {
	*x = ValidateDarFileRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ValidateDarFileRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ValidateDarFileRequest) ProtoMessage() {}

func (x *ValidateDarFileRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ValidateDarFileRequest.ProtoReflect.Descriptor instead.
func (*ValidateDarFileRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDescGZIP(), []int{5}
}

func (x *ValidateDarFileRequest) GetDarFile() []byte {
	if x != nil {
		return x.DarFile
	}
	return nil
}

func (x *ValidateDarFileRequest) GetSubmissionId() string {
	if x != nil {
		return x.SubmissionId
	}
	return ""
}

type ValidateDarFileResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *ValidateDarFileResponse) Reset() {
	*x = ValidateDarFileResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ValidateDarFileResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ValidateDarFileResponse) ProtoMessage() {}

func (x *ValidateDarFileResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ValidateDarFileResponse.ProtoReflect.Descriptor instead.
func (*ValidateDarFileResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDescGZIP(), []int{6}
}

var File_com_daml_ledger_api_v1_admin_package_management_service_proto protoreflect.FileDescriptor

var file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDesc = []byte{
	0x0a, 0x3d, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x70,
	0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x5f, 0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e,
	0x74, 0x5f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12,
	0x1c, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x1a, 0x1f, 0x67,
	0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74,
	0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x1a,
	0x0a, 0x18, 0x4c, 0x69, 0x73, 0x74, 0x4b, 0x6e, 0x6f, 0x77, 0x6e, 0x50, 0x61, 0x63, 0x6b, 0x61,
	0x67, 0x65, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x22, 0x72, 0x0a, 0x19, 0x4c, 0x69,
	0x73, 0x74, 0x4b, 0x6e, 0x6f, 0x77, 0x6e, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x73, 0x52,
	0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x55, 0x0a, 0x0f, 0x70, 0x61, 0x63, 0x6b, 0x61,
	0x67, 0x65, 0x5f, 0x64, 0x65, 0x74, 0x61, 0x69, 0x6c, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b,
	0x32, 0x2c, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e,
	0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x44, 0x65, 0x74, 0x61, 0x69, 0x6c, 0x73, 0x52, 0x0e,
	0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x44, 0x65, 0x74, 0x61, 0x69, 0x6c, 0x73, 0x22, 0xbe,
	0x01, 0x0a, 0x0e, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x44, 0x65, 0x74, 0x61, 0x69, 0x6c,
	0x73, 0x12, 0x1d, 0x0a, 0x0a, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x5f, 0x69, 0x64, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x49, 0x64,
	0x12, 0x21, 0x0a, 0x0c, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x5f, 0x73, 0x69, 0x7a, 0x65,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x04, 0x52, 0x0b, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x53,
	0x69, 0x7a, 0x65, 0x12, 0x3b, 0x0a, 0x0b, 0x6b, 0x6e, 0x6f, 0x77, 0x6e, 0x5f, 0x73, 0x69, 0x6e,
	0x63, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c,
	0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73,
	0x74, 0x61, 0x6d, 0x70, 0x52, 0x0a, 0x6b, 0x6e, 0x6f, 0x77, 0x6e, 0x53, 0x69, 0x6e, 0x63, 0x65,
	0x12, 0x2d, 0x0a, 0x12, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x5f, 0x64, 0x65, 0x73, 0x63, 0x72,
	0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x11, 0x73, 0x6f,
	0x75, 0x72, 0x63, 0x65, 0x44, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x22,
	0x56, 0x0a, 0x14, 0x55, 0x70, 0x6c, 0x6f, 0x61, 0x64, 0x44, 0x61, 0x72, 0x46, 0x69, 0x6c, 0x65,
	0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x19, 0x0a, 0x08, 0x64, 0x61, 0x72, 0x5f, 0x66,
	0x69, 0x6c, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0c, 0x52, 0x07, 0x64, 0x61, 0x72, 0x46, 0x69,
	0x6c, 0x65, 0x12, 0x23, 0x0a, 0x0d, 0x73, 0x75, 0x62, 0x6d, 0x69, 0x73, 0x73, 0x69, 0x6f, 0x6e,
	0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0c, 0x73, 0x75, 0x62, 0x6d, 0x69,
	0x73, 0x73, 0x69, 0x6f, 0x6e, 0x49, 0x64, 0x22, 0x17, 0x0a, 0x15, 0x55, 0x70, 0x6c, 0x6f, 0x61,
	0x64, 0x44, 0x61, 0x72, 0x46, 0x69, 0x6c, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65,
	0x22, 0x58, 0x0a, 0x16, 0x56, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x44, 0x61, 0x72, 0x46,
	0x69, 0x6c, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x19, 0x0a, 0x08, 0x64, 0x61,
	0x72, 0x5f, 0x66, 0x69, 0x6c, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0c, 0x52, 0x07, 0x64, 0x61,
	0x72, 0x46, 0x69, 0x6c, 0x65, 0x12, 0x23, 0x0a, 0x0d, 0x73, 0x75, 0x62, 0x6d, 0x69, 0x73, 0x73,
	0x69, 0x6f, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0c, 0x73, 0x75,
	0x62, 0x6d, 0x69, 0x73, 0x73, 0x69, 0x6f, 0x6e, 0x49, 0x64, 0x22, 0x19, 0x0a, 0x17, 0x56, 0x61,
	0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x44, 0x61, 0x72, 0x46, 0x69, 0x6c, 0x65, 0x52, 0x65, 0x73,
	0x70, 0x6f, 0x6e, 0x73, 0x65, 0x32, 0x9b, 0x03, 0x0a, 0x18, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67,
	0x65, 0x4d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x53, 0x65, 0x72, 0x76, 0x69,
	0x63, 0x65, 0x12, 0x84, 0x01, 0x0a, 0x11, 0x4c, 0x69, 0x73, 0x74, 0x4b, 0x6e, 0x6f, 0x77, 0x6e,
	0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x73, 0x12, 0x36, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76,
	0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x4c, 0x69, 0x73, 0x74, 0x4b, 0x6e, 0x6f, 0x77,
	0x6e, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74,
	0x1a, 0x37, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e,
	0x4c, 0x69, 0x73, 0x74, 0x4b, 0x6e, 0x6f, 0x77, 0x6e, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65,
	0x73, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x78, 0x0a, 0x0d, 0x55, 0x70, 0x6c,
	0x6f, 0x61, 0x64, 0x44, 0x61, 0x72, 0x46, 0x69, 0x6c, 0x65, 0x12, 0x32, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x55, 0x70, 0x6c, 0x6f, 0x61, 0x64,
	0x44, 0x61, 0x72, 0x46, 0x69, 0x6c, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x33,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x55, 0x70,
	0x6c, 0x6f, 0x61, 0x64, 0x44, 0x61, 0x72, 0x46, 0x69, 0x6c, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f,
	0x6e, 0x73, 0x65, 0x12, 0x7e, 0x0a, 0x0f, 0x56, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x44,
	0x61, 0x72, 0x46, 0x69, 0x6c, 0x65, 0x12, 0x34, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d,
	0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e,
	0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x56, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x44, 0x61,
	0x72, 0x46, 0x69, 0x6c, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x35, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61,
	0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x56, 0x61, 0x6c, 0x69,
	0x64, 0x61, 0x74, 0x65, 0x44, 0x61, 0x72, 0x46, 0x69, 0x6c, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f,
	0x6e, 0x73, 0x65, 0x42, 0xae, 0x01, 0x0a, 0x1c, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c,
	0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61,
	0x64, 0x6d, 0x69, 0x6e, 0x42, 0x22, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x4d, 0x61, 0x6e,
	0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x4f, 0x75,
	0x74, 0x65, 0x72, 0x43, 0x6c, 0x61, 0x73, 0x73, 0x5a, 0x4b, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62,
	0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76,
	0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d,
	0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f,
	0x61, 0x64, 0x6d, 0x69, 0x6e, 0xaa, 0x02, 0x1c, 0x43, 0x6f, 0x6d, 0x2e, 0x44, 0x61, 0x6d, 0x6c,
	0x2e, 0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x41, 0x70, 0x69, 0x2e, 0x56, 0x31, 0x2e, 0x41,
	0x64, 0x6d, 0x69, 0x6e, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDescData = file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDesc
)

func file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDescData)
	})
	return file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDescData
}

var file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes = make([]protoimpl.MessageInfo, 7)
var file_com_daml_ledger_api_v1_admin_package_management_service_proto_goTypes = []any{
	(*ListKnownPackagesRequest)(nil),  // 0: com.daml.ledger.api.v1.admin.ListKnownPackagesRequest
	(*ListKnownPackagesResponse)(nil), // 1: com.daml.ledger.api.v1.admin.ListKnownPackagesResponse
	(*PackageDetails)(nil),            // 2: com.daml.ledger.api.v1.admin.PackageDetails
	(*UploadDarFileRequest)(nil),      // 3: com.daml.ledger.api.v1.admin.UploadDarFileRequest
	(*UploadDarFileResponse)(nil),     // 4: com.daml.ledger.api.v1.admin.UploadDarFileResponse
	(*ValidateDarFileRequest)(nil),    // 5: com.daml.ledger.api.v1.admin.ValidateDarFileRequest
	(*ValidateDarFileResponse)(nil),   // 6: com.daml.ledger.api.v1.admin.ValidateDarFileResponse
	(*timestamppb.Timestamp)(nil),     // 7: google.protobuf.Timestamp
}
var file_com_daml_ledger_api_v1_admin_package_management_service_proto_depIdxs = []int32{
	2, // 0: com.daml.ledger.api.v1.admin.ListKnownPackagesResponse.package_details:type_name -> com.daml.ledger.api.v1.admin.PackageDetails
	7, // 1: com.daml.ledger.api.v1.admin.PackageDetails.known_since:type_name -> google.protobuf.Timestamp
	0, // 2: com.daml.ledger.api.v1.admin.PackageManagementService.ListKnownPackages:input_type -> com.daml.ledger.api.v1.admin.ListKnownPackagesRequest
	3, // 3: com.daml.ledger.api.v1.admin.PackageManagementService.UploadDarFile:input_type -> com.daml.ledger.api.v1.admin.UploadDarFileRequest
	5, // 4: com.daml.ledger.api.v1.admin.PackageManagementService.ValidateDarFile:input_type -> com.daml.ledger.api.v1.admin.ValidateDarFileRequest
	1, // 5: com.daml.ledger.api.v1.admin.PackageManagementService.ListKnownPackages:output_type -> com.daml.ledger.api.v1.admin.ListKnownPackagesResponse
	4, // 6: com.daml.ledger.api.v1.admin.PackageManagementService.UploadDarFile:output_type -> com.daml.ledger.api.v1.admin.UploadDarFileResponse
	6, // 7: com.daml.ledger.api.v1.admin.PackageManagementService.ValidateDarFile:output_type -> com.daml.ledger.api.v1.admin.ValidateDarFileResponse
	5, // [5:8] is the sub-list for method output_type
	2, // [2:5] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v1_admin_package_management_service_proto_init() }
func file_com_daml_ledger_api_v1_admin_package_management_service_proto_init() {
	if File_com_daml_ledger_api_v1_admin_package_management_service_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[0].Exporter = func(v any, i int) any {
			switch v := v.(*ListKnownPackagesRequest); i {
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
		file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[1].Exporter = func(v any, i int) any {
			switch v := v.(*ListKnownPackagesResponse); i {
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
		file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[2].Exporter = func(v any, i int) any {
			switch v := v.(*PackageDetails); i {
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
		file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[3].Exporter = func(v any, i int) any {
			switch v := v.(*UploadDarFileRequest); i {
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
		file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[4].Exporter = func(v any, i int) any {
			switch v := v.(*UploadDarFileResponse); i {
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
		file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[5].Exporter = func(v any, i int) any {
			switch v := v.(*ValidateDarFileRequest); i {
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
		file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes[6].Exporter = func(v any, i int) any {
			switch v := v.(*ValidateDarFileResponse); i {
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
			RawDescriptor: file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   7,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_daml_ledger_api_v1_admin_package_management_service_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v1_admin_package_management_service_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v1_admin_package_management_service_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v1_admin_package_management_service_proto = out.File
	file_com_daml_ledger_api_v1_admin_package_management_service_proto_rawDesc = nil
	file_com_daml_ledger_api_v1_admin_package_management_service_proto_goTypes = nil
	file_com_daml_ledger_api_v1_admin_package_management_service_proto_depIdxs = nil
}
