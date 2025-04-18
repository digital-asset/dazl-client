// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/digitalasset/canton/participant/admin/v0/pruning_service.proto

package v0

import (
	v0 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/pruning/admin/v0"
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

type PruneRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	PruneUpTo string `protobuf:"bytes,1,opt,name=prune_up_to,json=pruneUpTo,proto3" json:"prune_up_to,omitempty"`
}

func (x *PruneRequest) Reset() {
	*x = PruneRequest{}
	mi := &file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PruneRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PruneRequest) ProtoMessage() {}

func (x *PruneRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PruneRequest.ProtoReflect.Descriptor instead.
func (*PruneRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_rawDescGZIP(), []int{0}
}

func (x *PruneRequest) GetPruneUpTo() string {
	if x != nil {
		return x.PruneUpTo
	}
	return ""
}

type PruneResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *PruneResponse) Reset() {
	*x = PruneResponse{}
	mi := &file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PruneResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PruneResponse) ProtoMessage() {}

func (x *PruneResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PruneResponse.ProtoReflect.Descriptor instead.
func (*PruneResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_rawDescGZIP(), []int{1}
}

type GetSafePruningOffsetRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	BeforeOrAt *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=before_or_at,json=beforeOrAt,proto3" json:"before_or_at,omitempty"`
	LedgerEnd  string                 `protobuf:"bytes,2,opt,name=ledger_end,json=ledgerEnd,proto3" json:"ledger_end,omitempty"`
}

func (x *GetSafePruningOffsetRequest) Reset() {
	*x = GetSafePruningOffsetRequest{}
	mi := &file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetSafePruningOffsetRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetSafePruningOffsetRequest) ProtoMessage() {}

func (x *GetSafePruningOffsetRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetSafePruningOffsetRequest.ProtoReflect.Descriptor instead.
func (*GetSafePruningOffsetRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_rawDescGZIP(), []int{2}
}

func (x *GetSafePruningOffsetRequest) GetBeforeOrAt() *timestamppb.Timestamp {
	if x != nil {
		return x.BeforeOrAt
	}
	return nil
}

func (x *GetSafePruningOffsetRequest) GetLedgerEnd() string {
	if x != nil {
		return x.LedgerEnd
	}
	return ""
}

type GetSafePruningOffsetResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Response:
	//
	//	*GetSafePruningOffsetResponse_SafePruningOffset
	//	*GetSafePruningOffsetResponse_NoSafePruningOffset_
	Response isGetSafePruningOffsetResponse_Response `protobuf_oneof:"response"`
}

func (x *GetSafePruningOffsetResponse) Reset() {
	*x = GetSafePruningOffsetResponse{}
	mi := &file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetSafePruningOffsetResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetSafePruningOffsetResponse) ProtoMessage() {}

func (x *GetSafePruningOffsetResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetSafePruningOffsetResponse.ProtoReflect.Descriptor instead.
func (*GetSafePruningOffsetResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_rawDescGZIP(), []int{3}
}

func (m *GetSafePruningOffsetResponse) GetResponse() isGetSafePruningOffsetResponse_Response {
	if m != nil {
		return m.Response
	}
	return nil
}

func (x *GetSafePruningOffsetResponse) GetSafePruningOffset() string {
	if x, ok := x.GetResponse().(*GetSafePruningOffsetResponse_SafePruningOffset); ok {
		return x.SafePruningOffset
	}
	return ""
}

func (x *GetSafePruningOffsetResponse) GetNoSafePruningOffset() *GetSafePruningOffsetResponse_NoSafePruningOffset {
	if x, ok := x.GetResponse().(*GetSafePruningOffsetResponse_NoSafePruningOffset_); ok {
		return x.NoSafePruningOffset
	}
	return nil
}

type isGetSafePruningOffsetResponse_Response interface {
	isGetSafePruningOffsetResponse_Response()
}

type GetSafePruningOffsetResponse_SafePruningOffset struct {
	SafePruningOffset string `protobuf:"bytes,1,opt,name=safe_pruning_offset,json=safePruningOffset,proto3,oneof"`
}

type GetSafePruningOffsetResponse_NoSafePruningOffset_ struct {
	NoSafePruningOffset *GetSafePruningOffsetResponse_NoSafePruningOffset `protobuf:"bytes,2,opt,name=no_safe_pruning_offset,json=noSafePruningOffset,proto3,oneof"`
}

func (*GetSafePruningOffsetResponse_SafePruningOffset) isGetSafePruningOffsetResponse_Response() {}

func (*GetSafePruningOffsetResponse_NoSafePruningOffset_) isGetSafePruningOffsetResponse_Response() {}

type GetSafePruningOffsetResponse_NoSafePruningOffset struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *GetSafePruningOffsetResponse_NoSafePruningOffset) Reset() {
	*x = GetSafePruningOffsetResponse_NoSafePruningOffset{}
	mi := &file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetSafePruningOffsetResponse_NoSafePruningOffset) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetSafePruningOffsetResponse_NoSafePruningOffset) ProtoMessage() {}

func (x *GetSafePruningOffsetResponse_NoSafePruningOffset) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetSafePruningOffsetResponse_NoSafePruningOffset.ProtoReflect.Descriptor instead.
func (*GetSafePruningOffsetResponse_NoSafePruningOffset) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_rawDescGZIP(), []int{3, 0}
}

var File_com_digitalasset_canton_participant_admin_v0_pruning_service_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_rawDesc = []byte{
	0x0a, 0x42, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63,
	0x69, 0x70, 0x61, 0x6e, 0x74, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x76, 0x30, 0x2f, 0x70,
	0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x5f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x12, 0x2c, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61,
	0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x61,
	0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e,
	0x76, 0x30, 0x1a, 0x36, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x75, 0x6e,
	0x69, 0x6e, 0x67, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x76, 0x30, 0x2f, 0x70, 0x72, 0x75,
	0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65,
	0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x2e, 0x0a, 0x0c, 0x50,
	0x72, 0x75, 0x6e, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x1e, 0x0a, 0x0b, 0x70,
	0x72, 0x75, 0x6e, 0x65, 0x5f, 0x75, 0x70, 0x5f, 0x74, 0x6f, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x09, 0x70, 0x72, 0x75, 0x6e, 0x65, 0x55, 0x70, 0x54, 0x6f, 0x22, 0x0f, 0x0a, 0x0d, 0x50,
	0x72, 0x75, 0x6e, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x7a, 0x0a, 0x1b,
	0x47, 0x65, 0x74, 0x53, 0x61, 0x66, 0x65, 0x50, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4f, 0x66,
	0x66, 0x73, 0x65, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x3c, 0x0a, 0x0c, 0x62,
	0x65, 0x66, 0x6f, 0x72, 0x65, 0x5f, 0x6f, 0x72, 0x5f, 0x61, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x0a, 0x62,
	0x65, 0x66, 0x6f, 0x72, 0x65, 0x4f, 0x72, 0x41, 0x74, 0x12, 0x1d, 0x0a, 0x0a, 0x6c, 0x65, 0x64,
	0x67, 0x65, 0x72, 0x5f, 0x65, 0x6e, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x6c,
	0x65, 0x64, 0x67, 0x65, 0x72, 0x45, 0x6e, 0x64, 0x22, 0x8b, 0x02, 0x0a, 0x1c, 0x47, 0x65, 0x74,
	0x53, 0x61, 0x66, 0x65, 0x50, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4f, 0x66, 0x66, 0x73, 0x65,
	0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x30, 0x0a, 0x13, 0x73, 0x61, 0x66,
	0x65, 0x5f, 0x70, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x5f, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52, 0x11, 0x73, 0x61, 0x66, 0x65, 0x50, 0x72,
	0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x12, 0x95, 0x01, 0x0a, 0x16,
	0x6e, 0x6f, 0x5f, 0x73, 0x61, 0x66, 0x65, 0x5f, 0x70, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x5f,
	0x6f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x5e, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61,
	0x6e, 0x74, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x47, 0x65, 0x74, 0x53,
	0x61, 0x66, 0x65, 0x50, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4f, 0x66, 0x66, 0x73, 0x65, 0x74,
	0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x2e, 0x4e, 0x6f, 0x53, 0x61, 0x66, 0x65, 0x50,
	0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x48, 0x00, 0x52, 0x13,
	0x6e, 0x6f, 0x53, 0x61, 0x66, 0x65, 0x50, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4f, 0x66, 0x66,
	0x73, 0x65, 0x74, 0x1a, 0x15, 0x0a, 0x13, 0x4e, 0x6f, 0x53, 0x61, 0x66, 0x65, 0x50, 0x72, 0x75,
	0x6e, 0x69, 0x6e, 0x67, 0x4f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x42, 0x0a, 0x0a, 0x08, 0x72, 0x65,
	0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x32, 0x83, 0x0c, 0x0a, 0x0e, 0x50, 0x72, 0x75, 0x6e, 0x69,
	0x6e, 0x67, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x80, 0x01, 0x0a, 0x05, 0x50, 0x72,
	0x75, 0x6e, 0x65, 0x12, 0x3a, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61,
	0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x61,
	0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e,
	0x76, 0x30, 0x2e, 0x50, 0x72, 0x75, 0x6e, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a,
	0x3b, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63,
	0x69, 0x70, 0x61, 0x6e, 0x74, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x50,
	0x72, 0x75, 0x6e, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0xad, 0x01, 0x0a,
	0x14, 0x47, 0x65, 0x74, 0x53, 0x61, 0x66, 0x65, 0x50, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4f,
	0x66, 0x66, 0x73, 0x65, 0x74, 0x12, 0x49, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69,
	0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e,
	0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x2e, 0x61, 0x64, 0x6d, 0x69,
	0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x47, 0x65, 0x74, 0x53, 0x61, 0x66, 0x65, 0x50, 0x72, 0x75, 0x6e,
	0x69, 0x6e, 0x67, 0x4f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74,
	0x1a, 0x4a, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73,
	0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x61, 0x72, 0x74, 0x69,
	0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e,
	0x47, 0x65, 0x74, 0x53, 0x61, 0x66, 0x65, 0x50, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x4f, 0x66,
	0x66, 0x73, 0x65, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x8c, 0x01, 0x0a,
	0x0b, 0x53, 0x65, 0x74, 0x53, 0x63, 0x68, 0x65, 0x64, 0x75, 0x6c, 0x65, 0x12, 0x3d, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x61,
	0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x65, 0x74, 0x53, 0x63, 0x68, 0x65, 0x64,
	0x75, 0x6c, 0x65, 0x2e, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x3e, 0x2e, 0x63, 0x6f,
	0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63,
	0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x61, 0x64,
	0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x65, 0x74, 0x53, 0x63, 0x68, 0x65, 0x64, 0x75,
	0x6c, 0x65, 0x2e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0xad, 0x01, 0x0a, 0x16,
	0x53, 0x65, 0x74, 0x50, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x53, 0x63,
	0x68, 0x65, 0x64, 0x75, 0x6c, 0x65, 0x12, 0x48, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67,
	0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e,
	0x2e, 0x70, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76,
	0x30, 0x2e, 0x53, 0x65, 0x74, 0x50, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74,
	0x53, 0x63, 0x68, 0x65, 0x64, 0x75, 0x6c, 0x65, 0x2e, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74,
	0x1a, 0x49, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73,
	0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x75, 0x6e, 0x69,
	0x6e, 0x67, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x65, 0x74, 0x50,
	0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x53, 0x63, 0x68, 0x65, 0x64, 0x75,
	0x6c, 0x65, 0x2e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x80, 0x01, 0x0a, 0x07,
	0x53, 0x65, 0x74, 0x43, 0x72, 0x6f, 0x6e, 0x12, 0x39, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69,
	0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f,
	0x6e, 0x2e, 0x70, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e,
	0x76, 0x30, 0x2e, 0x53, 0x65, 0x74, 0x43, 0x72, 0x6f, 0x6e, 0x2e, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x1a, 0x3a, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c,
	0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x75,
	0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x65,
	0x74, 0x43, 0x72, 0x6f, 0x6e, 0x2e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x95,
	0x01, 0x0a, 0x0e, 0x53, 0x65, 0x74, 0x4d, 0x61, 0x78, 0x44, 0x75, 0x72, 0x61, 0x74, 0x69, 0x6f,
	0x6e, 0x12, 0x40, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x75, 0x6e,
	0x69, 0x6e, 0x67, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x65, 0x74,
	0x4d, 0x61, 0x78, 0x44, 0x75, 0x72, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x52, 0x65, 0x71, 0x75,
	0x65, 0x73, 0x74, 0x1a, 0x41, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61,
	0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72,
	0x75, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x53,
	0x65, 0x74, 0x4d, 0x61, 0x78, 0x44, 0x75, 0x72, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x52, 0x65,
	0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x8f, 0x01, 0x0a, 0x0c, 0x53, 0x65, 0x74, 0x52, 0x65,
	0x74, 0x65, 0x6e, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x3e, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69,
	0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f,
	0x6e, 0x2e, 0x70, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e,
	0x76, 0x30, 0x2e, 0x53, 0x65, 0x74, 0x52, 0x65, 0x74, 0x65, 0x6e, 0x74, 0x69, 0x6f, 0x6e, 0x2e,
	0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x3f, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69,
	0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f,
	0x6e, 0x2e, 0x70, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e,
	0x76, 0x30, 0x2e, 0x53, 0x65, 0x74, 0x52, 0x65, 0x74, 0x65, 0x6e, 0x74, 0x69, 0x6f, 0x6e, 0x2e,
	0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x92, 0x01, 0x0a, 0x0d, 0x43, 0x6c, 0x65,
	0x61, 0x72, 0x53, 0x63, 0x68, 0x65, 0x64, 0x75, 0x6c, 0x65, 0x12, 0x3f, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x61, 0x64, 0x6d,
	0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x43, 0x6c, 0x65, 0x61, 0x72, 0x53, 0x63, 0x68, 0x65, 0x64,
	0x75, 0x6c, 0x65, 0x2e, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x40, 0x2e, 0x63, 0x6f,
	0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63,
	0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x61, 0x64,
	0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x43, 0x6c, 0x65, 0x61, 0x72, 0x53, 0x63, 0x68, 0x65,
	0x64, 0x75, 0x6c, 0x65, 0x2e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x8c, 0x01,
	0x0a, 0x0b, 0x47, 0x65, 0x74, 0x53, 0x63, 0x68, 0x65, 0x64, 0x75, 0x6c, 0x65, 0x12, 0x3d, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x2e,
	0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x47, 0x65, 0x74, 0x53, 0x63, 0x68, 0x65,
	0x64, 0x75, 0x6c, 0x65, 0x2e, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x3e, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x61,
	0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x47, 0x65, 0x74, 0x53, 0x63, 0x68, 0x65, 0x64,
	0x75, 0x6c, 0x65, 0x2e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0xad, 0x01, 0x0a,
	0x16, 0x47, 0x65, 0x74, 0x50, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x53,
	0x63, 0x68, 0x65, 0x64, 0x75, 0x6c, 0x65, 0x12, 0x48, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69,
	0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f,
	0x6e, 0x2e, 0x70, 0x72, 0x75, 0x6e, 0x69, 0x6e, 0x67, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e,
	0x76, 0x30, 0x2e, 0x47, 0x65, 0x74, 0x50, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e,
	0x74, 0x53, 0x63, 0x68, 0x65, 0x64, 0x75, 0x6c, 0x65, 0x2e, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x1a, 0x49, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x75, 0x6e,
	0x69, 0x6e, 0x67, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x47, 0x65, 0x74,
	0x50, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x53, 0x63, 0x68, 0x65, 0x64,
	0x75, 0x6c, 0x65, 0x2e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x42, 0x5d, 0x5a, 0x5b,
	0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74,
	0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c,
	0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63,
	0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61,
	0x6e, 0x74, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x76, 0x30, 0x62, 0x06, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_rawDescData = file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_rawDesc
)

func file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_rawDescData)
	})
	return file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_rawDescData
}

var file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_msgTypes = make([]protoimpl.MessageInfo, 5)
var file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_goTypes = []any{
	(*PruneRequest)(nil),                                     // 0: com.digitalasset.canton.participant.admin.v0.PruneRequest
	(*PruneResponse)(nil),                                    // 1: com.digitalasset.canton.participant.admin.v0.PruneResponse
	(*GetSafePruningOffsetRequest)(nil),                      // 2: com.digitalasset.canton.participant.admin.v0.GetSafePruningOffsetRequest
	(*GetSafePruningOffsetResponse)(nil),                     // 3: com.digitalasset.canton.participant.admin.v0.GetSafePruningOffsetResponse
	(*GetSafePruningOffsetResponse_NoSafePruningOffset)(nil), // 4: com.digitalasset.canton.participant.admin.v0.GetSafePruningOffsetResponse.NoSafePruningOffset
	(*timestamppb.Timestamp)(nil),                            // 5: google.protobuf.Timestamp
	(*v0.SetSchedule_Request)(nil),                           // 6: com.digitalasset.canton.pruning.admin.v0.SetSchedule.Request
	(*v0.SetParticipantSchedule_Request)(nil),                // 7: com.digitalasset.canton.pruning.admin.v0.SetParticipantSchedule.Request
	(*v0.SetCron_Request)(nil),                               // 8: com.digitalasset.canton.pruning.admin.v0.SetCron.Request
	(*v0.SetMaxDuration_Request)(nil),                        // 9: com.digitalasset.canton.pruning.admin.v0.SetMaxDuration.Request
	(*v0.SetRetention_Request)(nil),                          // 10: com.digitalasset.canton.pruning.admin.v0.SetRetention.Request
	(*v0.ClearSchedule_Request)(nil),                         // 11: com.digitalasset.canton.pruning.admin.v0.ClearSchedule.Request
	(*v0.GetSchedule_Request)(nil),                           // 12: com.digitalasset.canton.pruning.admin.v0.GetSchedule.Request
	(*v0.GetParticipantSchedule_Request)(nil),                // 13: com.digitalasset.canton.pruning.admin.v0.GetParticipantSchedule.Request
	(*v0.SetSchedule_Response)(nil),                          // 14: com.digitalasset.canton.pruning.admin.v0.SetSchedule.Response
	(*v0.SetParticipantSchedule_Response)(nil),               // 15: com.digitalasset.canton.pruning.admin.v0.SetParticipantSchedule.Response
	(*v0.SetCron_Response)(nil),                              // 16: com.digitalasset.canton.pruning.admin.v0.SetCron.Response
	(*v0.SetMaxDuration_Response)(nil),                       // 17: com.digitalasset.canton.pruning.admin.v0.SetMaxDuration.Response
	(*v0.SetRetention_Response)(nil),                         // 18: com.digitalasset.canton.pruning.admin.v0.SetRetention.Response
	(*v0.ClearSchedule_Response)(nil),                        // 19: com.digitalasset.canton.pruning.admin.v0.ClearSchedule.Response
	(*v0.GetSchedule_Response)(nil),                          // 20: com.digitalasset.canton.pruning.admin.v0.GetSchedule.Response
	(*v0.GetParticipantSchedule_Response)(nil),               // 21: com.digitalasset.canton.pruning.admin.v0.GetParticipantSchedule.Response
}
var file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_depIdxs = []int32{
	5,  // 0: com.digitalasset.canton.participant.admin.v0.GetSafePruningOffsetRequest.before_or_at:type_name -> google.protobuf.Timestamp
	4,  // 1: com.digitalasset.canton.participant.admin.v0.GetSafePruningOffsetResponse.no_safe_pruning_offset:type_name -> com.digitalasset.canton.participant.admin.v0.GetSafePruningOffsetResponse.NoSafePruningOffset
	0,  // 2: com.digitalasset.canton.participant.admin.v0.PruningService.Prune:input_type -> com.digitalasset.canton.participant.admin.v0.PruneRequest
	2,  // 3: com.digitalasset.canton.participant.admin.v0.PruningService.GetSafePruningOffset:input_type -> com.digitalasset.canton.participant.admin.v0.GetSafePruningOffsetRequest
	6,  // 4: com.digitalasset.canton.participant.admin.v0.PruningService.SetSchedule:input_type -> com.digitalasset.canton.pruning.admin.v0.SetSchedule.Request
	7,  // 5: com.digitalasset.canton.participant.admin.v0.PruningService.SetParticipantSchedule:input_type -> com.digitalasset.canton.pruning.admin.v0.SetParticipantSchedule.Request
	8,  // 6: com.digitalasset.canton.participant.admin.v0.PruningService.SetCron:input_type -> com.digitalasset.canton.pruning.admin.v0.SetCron.Request
	9,  // 7: com.digitalasset.canton.participant.admin.v0.PruningService.SetMaxDuration:input_type -> com.digitalasset.canton.pruning.admin.v0.SetMaxDuration.Request
	10, // 8: com.digitalasset.canton.participant.admin.v0.PruningService.SetRetention:input_type -> com.digitalasset.canton.pruning.admin.v0.SetRetention.Request
	11, // 9: com.digitalasset.canton.participant.admin.v0.PruningService.ClearSchedule:input_type -> com.digitalasset.canton.pruning.admin.v0.ClearSchedule.Request
	12, // 10: com.digitalasset.canton.participant.admin.v0.PruningService.GetSchedule:input_type -> com.digitalasset.canton.pruning.admin.v0.GetSchedule.Request
	13, // 11: com.digitalasset.canton.participant.admin.v0.PruningService.GetParticipantSchedule:input_type -> com.digitalasset.canton.pruning.admin.v0.GetParticipantSchedule.Request
	1,  // 12: com.digitalasset.canton.participant.admin.v0.PruningService.Prune:output_type -> com.digitalasset.canton.participant.admin.v0.PruneResponse
	3,  // 13: com.digitalasset.canton.participant.admin.v0.PruningService.GetSafePruningOffset:output_type -> com.digitalasset.canton.participant.admin.v0.GetSafePruningOffsetResponse
	14, // 14: com.digitalasset.canton.participant.admin.v0.PruningService.SetSchedule:output_type -> com.digitalasset.canton.pruning.admin.v0.SetSchedule.Response
	15, // 15: com.digitalasset.canton.participant.admin.v0.PruningService.SetParticipantSchedule:output_type -> com.digitalasset.canton.pruning.admin.v0.SetParticipantSchedule.Response
	16, // 16: com.digitalasset.canton.participant.admin.v0.PruningService.SetCron:output_type -> com.digitalasset.canton.pruning.admin.v0.SetCron.Response
	17, // 17: com.digitalasset.canton.participant.admin.v0.PruningService.SetMaxDuration:output_type -> com.digitalasset.canton.pruning.admin.v0.SetMaxDuration.Response
	18, // 18: com.digitalasset.canton.participant.admin.v0.PruningService.SetRetention:output_type -> com.digitalasset.canton.pruning.admin.v0.SetRetention.Response
	19, // 19: com.digitalasset.canton.participant.admin.v0.PruningService.ClearSchedule:output_type -> com.digitalasset.canton.pruning.admin.v0.ClearSchedule.Response
	20, // 20: com.digitalasset.canton.participant.admin.v0.PruningService.GetSchedule:output_type -> com.digitalasset.canton.pruning.admin.v0.GetSchedule.Response
	21, // 21: com.digitalasset.canton.participant.admin.v0.PruningService.GetParticipantSchedule:output_type -> com.digitalasset.canton.pruning.admin.v0.GetParticipantSchedule.Response
	12, // [12:22] is the sub-list for method output_type
	2,  // [2:12] is the sub-list for method input_type
	2,  // [2:2] is the sub-list for extension type_name
	2,  // [2:2] is the sub-list for extension extendee
	0,  // [0:2] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_init() }
func file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_init() {
	if File_com_digitalasset_canton_participant_admin_v0_pruning_service_proto != nil {
		return
	}
	file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_msgTypes[3].OneofWrappers = []any{
		(*GetSafePruningOffsetResponse_SafePruningOffset)(nil),
		(*GetSafePruningOffsetResponse_NoSafePruningOffset_)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   5,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_participant_admin_v0_pruning_service_proto = out.File
	file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_rawDesc = nil
	file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_goTypes = nil
	file_com_digitalasset_canton_participant_admin_v0_pruning_service_proto_depIdxs = nil
}
