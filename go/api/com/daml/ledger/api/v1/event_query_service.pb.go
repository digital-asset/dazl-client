// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/daml/ledger/api/v1/event_query_service.proto

package v1

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

type GetEventsByContractIdRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ContractId        string   `protobuf:"bytes,1,opt,name=contract_id,json=contractId,proto3" json:"contract_id,omitempty"`
	RequestingParties []string `protobuf:"bytes,2,rep,name=requesting_parties,json=requestingParties,proto3" json:"requesting_parties,omitempty"`
}

func (x *GetEventsByContractIdRequest) Reset() {
	*x = GetEventsByContractIdRequest{}
	mi := &file_com_daml_ledger_api_v1_event_query_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetEventsByContractIdRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetEventsByContractIdRequest) ProtoMessage() {}

func (x *GetEventsByContractIdRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_event_query_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetEventsByContractIdRequest.ProtoReflect.Descriptor instead.
func (*GetEventsByContractIdRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_event_query_service_proto_rawDescGZIP(), []int{0}
}

func (x *GetEventsByContractIdRequest) GetContractId() string {
	if x != nil {
		return x.ContractId
	}
	return ""
}

func (x *GetEventsByContractIdRequest) GetRequestingParties() []string {
	if x != nil {
		return x.RequestingParties
	}
	return nil
}

type GetEventsByContractIdResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	CreateEvent  *CreatedEvent  `protobuf:"bytes,1,opt,name=create_event,json=createEvent,proto3" json:"create_event,omitempty"`
	ArchiveEvent *ArchivedEvent `protobuf:"bytes,2,opt,name=archive_event,json=archiveEvent,proto3" json:"archive_event,omitempty"`
}

func (x *GetEventsByContractIdResponse) Reset() {
	*x = GetEventsByContractIdResponse{}
	mi := &file_com_daml_ledger_api_v1_event_query_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetEventsByContractIdResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetEventsByContractIdResponse) ProtoMessage() {}

func (x *GetEventsByContractIdResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_event_query_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetEventsByContractIdResponse.ProtoReflect.Descriptor instead.
func (*GetEventsByContractIdResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_event_query_service_proto_rawDescGZIP(), []int{1}
}

func (x *GetEventsByContractIdResponse) GetCreateEvent() *CreatedEvent {
	if x != nil {
		return x.CreateEvent
	}
	return nil
}

func (x *GetEventsByContractIdResponse) GetArchiveEvent() *ArchivedEvent {
	if x != nil {
		return x.ArchiveEvent
	}
	return nil
}

type GetEventsByContractKeyRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ContractKey       *Value      `protobuf:"bytes,1,opt,name=contract_key,json=contractKey,proto3" json:"contract_key,omitempty"`
	TemplateId        *Identifier `protobuf:"bytes,2,opt,name=template_id,json=templateId,proto3" json:"template_id,omitempty"`
	RequestingParties []string    `protobuf:"bytes,3,rep,name=requesting_parties,json=requestingParties,proto3" json:"requesting_parties,omitempty"`
	ContinuationToken string      `protobuf:"bytes,4,opt,name=continuation_token,json=continuationToken,proto3" json:"continuation_token,omitempty"`
}

func (x *GetEventsByContractKeyRequest) Reset() {
	*x = GetEventsByContractKeyRequest{}
	mi := &file_com_daml_ledger_api_v1_event_query_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetEventsByContractKeyRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetEventsByContractKeyRequest) ProtoMessage() {}

func (x *GetEventsByContractKeyRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_event_query_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetEventsByContractKeyRequest.ProtoReflect.Descriptor instead.
func (*GetEventsByContractKeyRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_event_query_service_proto_rawDescGZIP(), []int{2}
}

func (x *GetEventsByContractKeyRequest) GetContractKey() *Value {
	if x != nil {
		return x.ContractKey
	}
	return nil
}

func (x *GetEventsByContractKeyRequest) GetTemplateId() *Identifier {
	if x != nil {
		return x.TemplateId
	}
	return nil
}

func (x *GetEventsByContractKeyRequest) GetRequestingParties() []string {
	if x != nil {
		return x.RequestingParties
	}
	return nil
}

func (x *GetEventsByContractKeyRequest) GetContinuationToken() string {
	if x != nil {
		return x.ContinuationToken
	}
	return ""
}

type GetEventsByContractKeyResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	CreateEvent       *CreatedEvent  `protobuf:"bytes,1,opt,name=create_event,json=createEvent,proto3" json:"create_event,omitempty"`
	ArchiveEvent      *ArchivedEvent `protobuf:"bytes,2,opt,name=archive_event,json=archiveEvent,proto3" json:"archive_event,omitempty"`
	ContinuationToken string         `protobuf:"bytes,4,opt,name=continuation_token,json=continuationToken,proto3" json:"continuation_token,omitempty"`
}

func (x *GetEventsByContractKeyResponse) Reset() {
	*x = GetEventsByContractKeyResponse{}
	mi := &file_com_daml_ledger_api_v1_event_query_service_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetEventsByContractKeyResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetEventsByContractKeyResponse) ProtoMessage() {}

func (x *GetEventsByContractKeyResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_event_query_service_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetEventsByContractKeyResponse.ProtoReflect.Descriptor instead.
func (*GetEventsByContractKeyResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_event_query_service_proto_rawDescGZIP(), []int{3}
}

func (x *GetEventsByContractKeyResponse) GetCreateEvent() *CreatedEvent {
	if x != nil {
		return x.CreateEvent
	}
	return nil
}

func (x *GetEventsByContractKeyResponse) GetArchiveEvent() *ArchivedEvent {
	if x != nil {
		return x.ArchiveEvent
	}
	return nil
}

func (x *GetEventsByContractKeyResponse) GetContinuationToken() string {
	if x != nil {
		return x.ContinuationToken
	}
	return ""
}

var File_com_daml_ledger_api_v1_event_query_service_proto protoreflect.FileDescriptor

var file_com_daml_ledger_api_v1_event_query_service_proto_rawDesc = []byte{
	0x0a, 0x30, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x5f, 0x71,
	0x75, 0x65, 0x72, 0x79, 0x5f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x12, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64,
	0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x1a, 0x22, 0x63, 0x6f, 0x6d, 0x2f,
	0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f,
	0x76, 0x31, 0x2f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x22,
	0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f,
	0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x22, 0x6e, 0x0a, 0x1c, 0x47, 0x65, 0x74, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x73, 0x42,
	0x79, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x49, 0x64, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x12, 0x1f, 0x0a, 0x0b, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x5f, 0x69,
	0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63,
	0x74, 0x49, 0x64, 0x12, 0x2d, 0x0a, 0x12, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x69, 0x6e,
	0x67, 0x5f, 0x70, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x18, 0x02, 0x20, 0x03, 0x28, 0x09, 0x52,
	0x11, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x69, 0x6e, 0x67, 0x50, 0x61, 0x72, 0x74, 0x69,
	0x65, 0x73, 0x22, 0xb4, 0x01, 0x0a, 0x1d, 0x47, 0x65, 0x74, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x73,
	0x42, 0x79, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x49, 0x64, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x12, 0x47, 0x0a, 0x0c, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x5f, 0x65,
	0x76, 0x65, 0x6e, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x24, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x76, 0x31, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74,
	0x52, 0x0b, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x12, 0x4a, 0x0a,
	0x0d, 0x61, 0x72, 0x63, 0x68, 0x69, 0x76, 0x65, 0x5f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x18, 0x02,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x25, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e,
	0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x41, 0x72,
	0x63, 0x68, 0x69, 0x76, 0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x52, 0x0c, 0x61, 0x72, 0x63,
	0x68, 0x69, 0x76, 0x65, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x22, 0x84, 0x02, 0x0a, 0x1d, 0x47, 0x65,
	0x74, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x73, 0x42, 0x79, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63,
	0x74, 0x4b, 0x65, 0x79, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x40, 0x0a, 0x0c, 0x63,
	0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x5f, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x0b, 0x32, 0x1d, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64,
	0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x56, 0x61, 0x6c, 0x75, 0x65,
	0x52, 0x0b, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x4b, 0x65, 0x79, 0x12, 0x43, 0x0a,
	0x0b, 0x74, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x0b, 0x32, 0x22, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65,
	0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x49, 0x64, 0x65, 0x6e,
	0x74, 0x69, 0x66, 0x69, 0x65, 0x72, 0x52, 0x0a, 0x74, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65,
	0x49, 0x64, 0x12, 0x2d, 0x0a, 0x12, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x69, 0x6e, 0x67,
	0x5f, 0x70, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x18, 0x03, 0x20, 0x03, 0x28, 0x09, 0x52, 0x11,
	0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x69, 0x6e, 0x67, 0x50, 0x61, 0x72, 0x74, 0x69, 0x65,
	0x73, 0x12, 0x2d, 0x0a, 0x12, 0x63, 0x6f, 0x6e, 0x74, 0x69, 0x6e, 0x75, 0x61, 0x74, 0x69, 0x6f,
	0x6e, 0x5f, 0x74, 0x6f, 0x6b, 0x65, 0x6e, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x11, 0x63,
	0x6f, 0x6e, 0x74, 0x69, 0x6e, 0x75, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x54, 0x6f, 0x6b, 0x65, 0x6e,
	0x22, 0xe4, 0x01, 0x0a, 0x1e, 0x47, 0x65, 0x74, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x73, 0x42, 0x79,
	0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x4b, 0x65, 0x79, 0x52, 0x65, 0x73, 0x70, 0x6f,
	0x6e, 0x73, 0x65, 0x12, 0x47, 0x0a, 0x0c, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x5f, 0x65, 0x76,
	0x65, 0x6e, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x24, 0x2e, 0x63, 0x6f, 0x6d, 0x2e,
	0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e,
	0x76, 0x31, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x52,
	0x0b, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x12, 0x4a, 0x0a, 0x0d,
	0x61, 0x72, 0x63, 0x68, 0x69, 0x76, 0x65, 0x5f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x18, 0x02, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x25, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c,
	0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x41, 0x72, 0x63,
	0x68, 0x69, 0x76, 0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x52, 0x0c, 0x61, 0x72, 0x63, 0x68,
	0x69, 0x76, 0x65, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x12, 0x2d, 0x0a, 0x12, 0x63, 0x6f, 0x6e, 0x74,
	0x69, 0x6e, 0x75, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x74, 0x6f, 0x6b, 0x65, 0x6e, 0x18, 0x04,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x11, 0x63, 0x6f, 0x6e, 0x74, 0x69, 0x6e, 0x75, 0x61, 0x74, 0x69,
	0x6f, 0x6e, 0x54, 0x6f, 0x6b, 0x65, 0x6e, 0x32, 0xa4, 0x02, 0x0a, 0x11, 0x45, 0x76, 0x65, 0x6e,
	0x74, 0x51, 0x75, 0x65, 0x72, 0x79, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x84, 0x01,
	0x0a, 0x15, 0x47, 0x65, 0x74, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x73, 0x42, 0x79, 0x43, 0x6f, 0x6e,
	0x74, 0x72, 0x61, 0x63, 0x74, 0x49, 0x64, 0x12, 0x34, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61,
	0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31,
	0x2e, 0x47, 0x65, 0x74, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x73, 0x42, 0x79, 0x43, 0x6f, 0x6e, 0x74,
	0x72, 0x61, 0x63, 0x74, 0x49, 0x64, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x35, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e,
	0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x47, 0x65, 0x74, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x73,
	0x42, 0x79, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x49, 0x64, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x12, 0x87, 0x01, 0x0a, 0x16, 0x47, 0x65, 0x74, 0x45, 0x76, 0x65, 0x6e,
	0x74, 0x73, 0x42, 0x79, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x4b, 0x65, 0x79, 0x12,
	0x35, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x47, 0x65, 0x74, 0x45, 0x76, 0x65, 0x6e,
	0x74, 0x73, 0x42, 0x79, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x4b, 0x65, 0x79, 0x52,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x36, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d,
	0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e,
	0x47, 0x65, 0x74, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x73, 0x42, 0x79, 0x43, 0x6f, 0x6e, 0x74, 0x72,
	0x61, 0x63, 0x74, 0x4b, 0x65, 0x79, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x42, 0x95,
	0x01, 0x0a, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x42, 0x1b, 0x45, 0x76, 0x65, 0x6e, 0x74,
	0x51, 0x75, 0x65, 0x72, 0x79, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x4f, 0x75, 0x74, 0x65,
	0x72, 0x43, 0x6c, 0x61, 0x73, 0x73, 0x5a, 0x45, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63,
	0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f,
	0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f,
	0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0xaa, 0x02, 0x16,
	0x43, 0x6f, 0x6d, 0x2e, 0x44, 0x61, 0x6d, 0x6c, 0x2e, 0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e,
	0x41, 0x70, 0x69, 0x2e, 0x56, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_daml_ledger_api_v1_event_query_service_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v1_event_query_service_proto_rawDescData = file_com_daml_ledger_api_v1_event_query_service_proto_rawDesc
)

func file_com_daml_ledger_api_v1_event_query_service_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v1_event_query_service_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v1_event_query_service_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_ledger_api_v1_event_query_service_proto_rawDescData)
	})
	return file_com_daml_ledger_api_v1_event_query_service_proto_rawDescData
}

var file_com_daml_ledger_api_v1_event_query_service_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_com_daml_ledger_api_v1_event_query_service_proto_goTypes = []any{
	(*GetEventsByContractIdRequest)(nil),   // 0: com.daml.ledger.api.v1.GetEventsByContractIdRequest
	(*GetEventsByContractIdResponse)(nil),  // 1: com.daml.ledger.api.v1.GetEventsByContractIdResponse
	(*GetEventsByContractKeyRequest)(nil),  // 2: com.daml.ledger.api.v1.GetEventsByContractKeyRequest
	(*GetEventsByContractKeyResponse)(nil), // 3: com.daml.ledger.api.v1.GetEventsByContractKeyResponse
	(*CreatedEvent)(nil),                   // 4: com.daml.ledger.api.v1.CreatedEvent
	(*ArchivedEvent)(nil),                  // 5: com.daml.ledger.api.v1.ArchivedEvent
	(*Value)(nil),                          // 6: com.daml.ledger.api.v1.Value
	(*Identifier)(nil),                     // 7: com.daml.ledger.api.v1.Identifier
}
var file_com_daml_ledger_api_v1_event_query_service_proto_depIdxs = []int32{
	4, // 0: com.daml.ledger.api.v1.GetEventsByContractIdResponse.create_event:type_name -> com.daml.ledger.api.v1.CreatedEvent
	5, // 1: com.daml.ledger.api.v1.GetEventsByContractIdResponse.archive_event:type_name -> com.daml.ledger.api.v1.ArchivedEvent
	6, // 2: com.daml.ledger.api.v1.GetEventsByContractKeyRequest.contract_key:type_name -> com.daml.ledger.api.v1.Value
	7, // 3: com.daml.ledger.api.v1.GetEventsByContractKeyRequest.template_id:type_name -> com.daml.ledger.api.v1.Identifier
	4, // 4: com.daml.ledger.api.v1.GetEventsByContractKeyResponse.create_event:type_name -> com.daml.ledger.api.v1.CreatedEvent
	5, // 5: com.daml.ledger.api.v1.GetEventsByContractKeyResponse.archive_event:type_name -> com.daml.ledger.api.v1.ArchivedEvent
	0, // 6: com.daml.ledger.api.v1.EventQueryService.GetEventsByContractId:input_type -> com.daml.ledger.api.v1.GetEventsByContractIdRequest
	2, // 7: com.daml.ledger.api.v1.EventQueryService.GetEventsByContractKey:input_type -> com.daml.ledger.api.v1.GetEventsByContractKeyRequest
	1, // 8: com.daml.ledger.api.v1.EventQueryService.GetEventsByContractId:output_type -> com.daml.ledger.api.v1.GetEventsByContractIdResponse
	3, // 9: com.daml.ledger.api.v1.EventQueryService.GetEventsByContractKey:output_type -> com.daml.ledger.api.v1.GetEventsByContractKeyResponse
	8, // [8:10] is the sub-list for method output_type
	6, // [6:8] is the sub-list for method input_type
	6, // [6:6] is the sub-list for extension type_name
	6, // [6:6] is the sub-list for extension extendee
	0, // [0:6] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v1_event_query_service_proto_init() }
func file_com_daml_ledger_api_v1_event_query_service_proto_init() {
	if File_com_daml_ledger_api_v1_event_query_service_proto != nil {
		return
	}
	file_com_daml_ledger_api_v1_event_proto_init()
	file_com_daml_ledger_api_v1_value_proto_init()
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_daml_ledger_api_v1_event_query_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_daml_ledger_api_v1_event_query_service_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v1_event_query_service_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v1_event_query_service_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v1_event_query_service_proto = out.File
	file_com_daml_ledger_api_v1_event_query_service_proto_rawDesc = nil
	file_com_daml_ledger_api_v1_event_query_service_proto_goTypes = nil
	file_com_daml_ledger_api_v1_event_query_service_proto_depIdxs = nil
}
