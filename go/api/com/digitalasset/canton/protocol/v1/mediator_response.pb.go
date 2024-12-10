// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v5.27.2
// source: com/digitalasset/canton/protocol/v1/mediator_response.proto

package v1

import (
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

type MediatorResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	RequestId         *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
	Sender            string                 `protobuf:"bytes,2,opt,name=sender,proto3" json:"sender,omitempty"`
	ViewHash          []byte                 `protobuf:"bytes,3,opt,name=view_hash,json=viewHash,proto3" json:"view_hash,omitempty"`
	LocalVerdict      *LocalVerdict          `protobuf:"bytes,4,opt,name=local_verdict,json=localVerdict,proto3" json:"local_verdict,omitempty"`
	RootHash          []byte                 `protobuf:"bytes,5,opt,name=root_hash,json=rootHash,proto3" json:"root_hash,omitempty"`
	ConfirmingParties []string               `protobuf:"bytes,6,rep,name=confirming_parties,json=confirmingParties,proto3" json:"confirming_parties,omitempty"`
	DomainId          string                 `protobuf:"bytes,7,opt,name=domain_id,json=domainId,proto3" json:"domain_id,omitempty"`
}

func (x *MediatorResponse) Reset() {
	*x = MediatorResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v1_mediator_response_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *MediatorResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MediatorResponse) ProtoMessage() {}

func (x *MediatorResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v1_mediator_response_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use MediatorResponse.ProtoReflect.Descriptor instead.
func (*MediatorResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v1_mediator_response_proto_rawDescGZIP(), []int{0}
}

func (x *MediatorResponse) GetRequestId() *timestamppb.Timestamp {
	if x != nil {
		return x.RequestId
	}
	return nil
}

func (x *MediatorResponse) GetSender() string {
	if x != nil {
		return x.Sender
	}
	return ""
}

func (x *MediatorResponse) GetViewHash() []byte {
	if x != nil {
		return x.ViewHash
	}
	return nil
}

func (x *MediatorResponse) GetLocalVerdict() *LocalVerdict {
	if x != nil {
		return x.LocalVerdict
	}
	return nil
}

func (x *MediatorResponse) GetRootHash() []byte {
	if x != nil {
		return x.RootHash
	}
	return nil
}

func (x *MediatorResponse) GetConfirmingParties() []string {
	if x != nil {
		return x.ConfirmingParties
	}
	return nil
}

func (x *MediatorResponse) GetDomainId() string {
	if x != nil {
		return x.DomainId
	}
	return ""
}

type LocalVerdict struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to SomeLocalVerdict:
	//
	//	*LocalVerdict_LocalApprove
	//	*LocalVerdict_LocalReject
	SomeLocalVerdict isLocalVerdict_SomeLocalVerdict `protobuf_oneof:"some_local_verdict"`
}

func (x *LocalVerdict) Reset() {
	*x = LocalVerdict{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v1_mediator_response_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *LocalVerdict) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*LocalVerdict) ProtoMessage() {}

func (x *LocalVerdict) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v1_mediator_response_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
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
	return file_com_digitalasset_canton_protocol_v1_mediator_response_proto_rawDescGZIP(), []int{1}
}

func (m *LocalVerdict) GetSomeLocalVerdict() isLocalVerdict_SomeLocalVerdict {
	if m != nil {
		return m.SomeLocalVerdict
	}
	return nil
}

func (x *LocalVerdict) GetLocalApprove() *emptypb.Empty {
	if x, ok := x.GetSomeLocalVerdict().(*LocalVerdict_LocalApprove); ok {
		return x.LocalApprove
	}
	return nil
}

func (x *LocalVerdict) GetLocalReject() *LocalReject {
	if x, ok := x.GetSomeLocalVerdict().(*LocalVerdict_LocalReject); ok {
		return x.LocalReject
	}
	return nil
}

type isLocalVerdict_SomeLocalVerdict interface {
	isLocalVerdict_SomeLocalVerdict()
}

type LocalVerdict_LocalApprove struct {
	LocalApprove *emptypb.Empty `protobuf:"bytes,1,opt,name=local_approve,json=localApprove,proto3,oneof"`
}

type LocalVerdict_LocalReject struct {
	LocalReject *LocalReject `protobuf:"bytes,2,opt,name=local_reject,json=localReject,proto3,oneof"`
}

func (*LocalVerdict_LocalApprove) isLocalVerdict_SomeLocalVerdict() {}

func (*LocalVerdict_LocalReject) isLocalVerdict_SomeLocalVerdict() {}

type LocalReject struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	CausePrefix   string   `protobuf:"bytes,4,opt,name=cause_prefix,json=causePrefix,proto3" json:"cause_prefix,omitempty"`
	Details       string   `protobuf:"bytes,2,opt,name=details,proto3" json:"details,omitempty"`
	Resource      []string `protobuf:"bytes,3,rep,name=resource,proto3" json:"resource,omitempty"`
	ErrorCode     string   `protobuf:"bytes,5,opt,name=error_code,json=errorCode,proto3" json:"error_code,omitempty"`
	ErrorCategory uint32   `protobuf:"varint,6,opt,name=error_category,json=errorCategory,proto3" json:"error_category,omitempty"`
}

func (x *LocalReject) Reset() {
	*x = LocalReject{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_protocol_v1_mediator_response_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *LocalReject) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*LocalReject) ProtoMessage() {}

func (x *LocalReject) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v1_mediator_response_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use LocalReject.ProtoReflect.Descriptor instead.
func (*LocalReject) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v1_mediator_response_proto_rawDescGZIP(), []int{2}
}

func (x *LocalReject) GetCausePrefix() string {
	if x != nil {
		return x.CausePrefix
	}
	return ""
}

func (x *LocalReject) GetDetails() string {
	if x != nil {
		return x.Details
	}
	return ""
}

func (x *LocalReject) GetResource() []string {
	if x != nil {
		return x.Resource
	}
	return nil
}

func (x *LocalReject) GetErrorCode() string {
	if x != nil {
		return x.ErrorCode
	}
	return ""
}

func (x *LocalReject) GetErrorCategory() uint32 {
	if x != nil {
		return x.ErrorCategory
	}
	return 0
}

var File_com_digitalasset_canton_protocol_v1_mediator_response_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_protocol_v1_mediator_response_proto_rawDesc = []byte{
	0x0a, 0x3b, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63,
	0x6f, 0x6c, 0x2f, 0x76, 0x31, 0x2f, 0x6d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x5f, 0x72,
	0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x23, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e,
	0x76, 0x31, 0x1a, 0x1b, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x75, 0x66, 0x2f, 0x65, 0x6d, 0x70, 0x74, 0x79, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a,
	0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66,
	0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x22, 0xc3, 0x02, 0x0a, 0x10, 0x4d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x6f, 0x72, 0x52, 0x65, 0x73,
	0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x39, 0x0a, 0x0a, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74,
	0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65,
	0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x09, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x49, 0x64,
	0x12, 0x16, 0x0a, 0x06, 0x73, 0x65, 0x6e, 0x64, 0x65, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x06, 0x73, 0x65, 0x6e, 0x64, 0x65, 0x72, 0x12, 0x1b, 0x0a, 0x09, 0x76, 0x69, 0x65, 0x77,
	0x5f, 0x68, 0x61, 0x73, 0x68, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0c, 0x52, 0x08, 0x76, 0x69, 0x65,
	0x77, 0x48, 0x61, 0x73, 0x68, 0x12, 0x56, 0x0a, 0x0d, 0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x5f, 0x76,
	0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x31, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e,
	0x76, 0x31, 0x2e, 0x4c, 0x6f, 0x63, 0x61, 0x6c, 0x56, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x52,
	0x0c, 0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x56, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x12, 0x1b, 0x0a,
	0x09, 0x72, 0x6f, 0x6f, 0x74, 0x5f, 0x68, 0x61, 0x73, 0x68, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0c,
	0x52, 0x08, 0x72, 0x6f, 0x6f, 0x74, 0x48, 0x61, 0x73, 0x68, 0x12, 0x2d, 0x0a, 0x12, 0x63, 0x6f,
	0x6e, 0x66, 0x69, 0x72, 0x6d, 0x69, 0x6e, 0x67, 0x5f, 0x70, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73,
	0x18, 0x06, 0x20, 0x03, 0x28, 0x09, 0x52, 0x11, 0x63, 0x6f, 0x6e, 0x66, 0x69, 0x72, 0x6d, 0x69,
	0x6e, 0x67, 0x50, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x12, 0x1b, 0x0a, 0x09, 0x64, 0x6f, 0x6d,
	0x61, 0x69, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x07, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x64, 0x6f,
	0x6d, 0x61, 0x69, 0x6e, 0x49, 0x64, 0x22, 0xba, 0x01, 0x0a, 0x0c, 0x4c, 0x6f, 0x63, 0x61, 0x6c,
	0x56, 0x65, 0x72, 0x64, 0x69, 0x63, 0x74, 0x12, 0x3d, 0x0a, 0x0d, 0x6c, 0x6f, 0x63, 0x61, 0x6c,
	0x5f, 0x61, 0x70, 0x70, 0x72, 0x6f, 0x76, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x16,
	0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66,
	0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x48, 0x00, 0x52, 0x0c, 0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x41,
	0x70, 0x70, 0x72, 0x6f, 0x76, 0x65, 0x12, 0x55, 0x0a, 0x0c, 0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x5f,
	0x72, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x30, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e,
	0x76, 0x31, 0x2e, 0x4c, 0x6f, 0x63, 0x61, 0x6c, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x48, 0x00,
	0x52, 0x0b, 0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x52, 0x65, 0x6a, 0x65, 0x63, 0x74, 0x42, 0x14, 0x0a,
	0x12, 0x73, 0x6f, 0x6d, 0x65, 0x5f, 0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x5f, 0x76, 0x65, 0x72, 0x64,
	0x69, 0x63, 0x74, 0x22, 0xb2, 0x01, 0x0a, 0x0b, 0x4c, 0x6f, 0x63, 0x61, 0x6c, 0x52, 0x65, 0x6a,
	0x65, 0x63, 0x74, 0x12, 0x21, 0x0a, 0x0c, 0x63, 0x61, 0x75, 0x73, 0x65, 0x5f, 0x70, 0x72, 0x65,
	0x66, 0x69, 0x78, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x63, 0x61, 0x75, 0x73, 0x65,
	0x50, 0x72, 0x65, 0x66, 0x69, 0x78, 0x12, 0x18, 0x0a, 0x07, 0x64, 0x65, 0x74, 0x61, 0x69, 0x6c,
	0x73, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x64, 0x65, 0x74, 0x61, 0x69, 0x6c, 0x73,
	0x12, 0x1a, 0x0a, 0x08, 0x72, 0x65, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x18, 0x03, 0x20, 0x03,
	0x28, 0x09, 0x52, 0x08, 0x72, 0x65, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x12, 0x1d, 0x0a, 0x0a,
	0x65, 0x72, 0x72, 0x6f, 0x72, 0x5f, 0x63, 0x6f, 0x64, 0x65, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x09, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x43, 0x6f, 0x64, 0x65, 0x12, 0x25, 0x0a, 0x0e, 0x65,
	0x72, 0x72, 0x6f, 0x72, 0x5f, 0x63, 0x61, 0x74, 0x65, 0x67, 0x6f, 0x72, 0x79, 0x18, 0x06, 0x20,
	0x01, 0x28, 0x0d, 0x52, 0x0d, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x43, 0x61, 0x74, 0x65, 0x67, 0x6f,
	0x72, 0x79, 0x4a, 0x04, 0x08, 0x01, 0x10, 0x02, 0x42, 0x54, 0x5a, 0x52, 0x67, 0x69, 0x74, 0x68,
	0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61,
	0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74,
	0x2f, 0x76, 0x37, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64,
	0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74,
	0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x31, 0x62, 0x06,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_protocol_v1_mediator_response_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_protocol_v1_mediator_response_proto_rawDescData = file_com_digitalasset_canton_protocol_v1_mediator_response_proto_rawDesc
)

func file_com_digitalasset_canton_protocol_v1_mediator_response_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_protocol_v1_mediator_response_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_protocol_v1_mediator_response_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_protocol_v1_mediator_response_proto_rawDescData)
	})
	return file_com_digitalasset_canton_protocol_v1_mediator_response_proto_rawDescData
}

var file_com_digitalasset_canton_protocol_v1_mediator_response_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_com_digitalasset_canton_protocol_v1_mediator_response_proto_goTypes = []interface{}{
	(*MediatorResponse)(nil),      // 0: com.digitalasset.canton.protocol.v1.MediatorResponse
	(*LocalVerdict)(nil),          // 1: com.digitalasset.canton.protocol.v1.LocalVerdict
	(*LocalReject)(nil),           // 2: com.digitalasset.canton.protocol.v1.LocalReject
	(*timestamppb.Timestamp)(nil), // 3: google.protobuf.Timestamp
	(*emptypb.Empty)(nil),         // 4: google.protobuf.Empty
}
var file_com_digitalasset_canton_protocol_v1_mediator_response_proto_depIdxs = []int32{
	3, // 0: com.digitalasset.canton.protocol.v1.MediatorResponse.request_id:type_name -> google.protobuf.Timestamp
	1, // 1: com.digitalasset.canton.protocol.v1.MediatorResponse.local_verdict:type_name -> com.digitalasset.canton.protocol.v1.LocalVerdict
	4, // 2: com.digitalasset.canton.protocol.v1.LocalVerdict.local_approve:type_name -> google.protobuf.Empty
	2, // 3: com.digitalasset.canton.protocol.v1.LocalVerdict.local_reject:type_name -> com.digitalasset.canton.protocol.v1.LocalReject
	4, // [4:4] is the sub-list for method output_type
	4, // [4:4] is the sub-list for method input_type
	4, // [4:4] is the sub-list for extension type_name
	4, // [4:4] is the sub-list for extension extendee
	0, // [0:4] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_protocol_v1_mediator_response_proto_init() }
func file_com_digitalasset_canton_protocol_v1_mediator_response_proto_init() {
	if File_com_digitalasset_canton_protocol_v1_mediator_response_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_com_digitalasset_canton_protocol_v1_mediator_response_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*MediatorResponse); i {
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
		file_com_digitalasset_canton_protocol_v1_mediator_response_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*LocalVerdict); i {
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
		file_com_digitalasset_canton_protocol_v1_mediator_response_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*LocalReject); i {
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
	file_com_digitalasset_canton_protocol_v1_mediator_response_proto_msgTypes[1].OneofWrappers = []interface{}{
		(*LocalVerdict_LocalApprove)(nil),
		(*LocalVerdict_LocalReject)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_protocol_v1_mediator_response_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_protocol_v1_mediator_response_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_protocol_v1_mediator_response_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_protocol_v1_mediator_response_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_protocol_v1_mediator_response_proto = out.File
	file_com_digitalasset_canton_protocol_v1_mediator_response_proto_rawDesc = nil
	file_com_digitalasset_canton_protocol_v1_mediator_response_proto_goTypes = nil
	file_com_digitalasset_canton_protocol_v1_mediator_response_proto_depIdxs = nil
}
