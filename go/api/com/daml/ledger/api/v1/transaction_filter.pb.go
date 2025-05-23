// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/daml/ledger/api/v1/transaction_filter.proto

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

type TransactionFilter struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	FiltersByParty map[string]*Filters `protobuf:"bytes,1,rep,name=filters_by_party,json=filtersByParty,proto3" json:"filters_by_party,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
}

func (x *TransactionFilter) Reset() {
	*x = TransactionFilter{}
	mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TransactionFilter) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransactionFilter) ProtoMessage() {}

func (x *TransactionFilter) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TransactionFilter.ProtoReflect.Descriptor instead.
func (*TransactionFilter) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescGZIP(), []int{0}
}

func (x *TransactionFilter) GetFiltersByParty() map[string]*Filters {
	if x != nil {
		return x.FiltersByParty
	}
	return nil
}

type Filters struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Inclusive *InclusiveFilters `protobuf:"bytes,1,opt,name=inclusive,proto3" json:"inclusive,omitempty"`
}

func (x *Filters) Reset() {
	*x = Filters{}
	mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Filters) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Filters) ProtoMessage() {}

func (x *Filters) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Filters.ProtoReflect.Descriptor instead.
func (*Filters) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescGZIP(), []int{1}
}

func (x *Filters) GetInclusive() *InclusiveFilters {
	if x != nil {
		return x.Inclusive
	}
	return nil
}

type InclusiveFilters struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Deprecated: Marked as deprecated in com/daml/ledger/api/v1/transaction_filter.proto.
	TemplateIds      []*Identifier      `protobuf:"bytes,1,rep,name=template_ids,json=templateIds,proto3" json:"template_ids,omitempty"`
	InterfaceFilters []*InterfaceFilter `protobuf:"bytes,2,rep,name=interface_filters,json=interfaceFilters,proto3" json:"interface_filters,omitempty"`
	TemplateFilters  []*TemplateFilter  `protobuf:"bytes,3,rep,name=template_filters,json=templateFilters,proto3" json:"template_filters,omitempty"`
}

func (x *InclusiveFilters) Reset() {
	*x = InclusiveFilters{}
	mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *InclusiveFilters) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*InclusiveFilters) ProtoMessage() {}

func (x *InclusiveFilters) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use InclusiveFilters.ProtoReflect.Descriptor instead.
func (*InclusiveFilters) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescGZIP(), []int{2}
}

// Deprecated: Marked as deprecated in com/daml/ledger/api/v1/transaction_filter.proto.
func (x *InclusiveFilters) GetTemplateIds() []*Identifier {
	if x != nil {
		return x.TemplateIds
	}
	return nil
}

func (x *InclusiveFilters) GetInterfaceFilters() []*InterfaceFilter {
	if x != nil {
		return x.InterfaceFilters
	}
	return nil
}

func (x *InclusiveFilters) GetTemplateFilters() []*TemplateFilter {
	if x != nil {
		return x.TemplateFilters
	}
	return nil
}

type InterfaceFilter struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	InterfaceId             *Identifier `protobuf:"bytes,1,opt,name=interface_id,json=interfaceId,proto3" json:"interface_id,omitempty"`
	IncludeInterfaceView    bool        `protobuf:"varint,2,opt,name=include_interface_view,json=includeInterfaceView,proto3" json:"include_interface_view,omitempty"`
	IncludeCreatedEventBlob bool        `protobuf:"varint,4,opt,name=include_created_event_blob,json=includeCreatedEventBlob,proto3" json:"include_created_event_blob,omitempty"`
}

func (x *InterfaceFilter) Reset() {
	*x = InterfaceFilter{}
	mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *InterfaceFilter) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*InterfaceFilter) ProtoMessage() {}

func (x *InterfaceFilter) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use InterfaceFilter.ProtoReflect.Descriptor instead.
func (*InterfaceFilter) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescGZIP(), []int{3}
}

func (x *InterfaceFilter) GetInterfaceId() *Identifier {
	if x != nil {
		return x.InterfaceId
	}
	return nil
}

func (x *InterfaceFilter) GetIncludeInterfaceView() bool {
	if x != nil {
		return x.IncludeInterfaceView
	}
	return false
}

func (x *InterfaceFilter) GetIncludeCreatedEventBlob() bool {
	if x != nil {
		return x.IncludeCreatedEventBlob
	}
	return false
}

type TemplateFilter struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	TemplateId              *Identifier `protobuf:"bytes,1,opt,name=template_id,json=templateId,proto3" json:"template_id,omitempty"`
	IncludeCreatedEventBlob bool        `protobuf:"varint,2,opt,name=include_created_event_blob,json=includeCreatedEventBlob,proto3" json:"include_created_event_blob,omitempty"`
}

func (x *TemplateFilter) Reset() {
	*x = TemplateFilter{}
	mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TemplateFilter) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TemplateFilter) ProtoMessage() {}

func (x *TemplateFilter) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TemplateFilter.ProtoReflect.Descriptor instead.
func (*TemplateFilter) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescGZIP(), []int{4}
}

func (x *TemplateFilter) GetTemplateId() *Identifier {
	if x != nil {
		return x.TemplateId
	}
	return nil
}

func (x *TemplateFilter) GetIncludeCreatedEventBlob() bool {
	if x != nil {
		return x.IncludeCreatedEventBlob
	}
	return false
}

var File_com_daml_ledger_api_v1_transaction_filter_proto protoreflect.FileDescriptor

var file_com_daml_ledger_api_v1_transaction_filter_proto_rawDesc = []byte{
	0x0a, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63,
	0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x66, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x12, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x1a, 0x22, 0x63, 0x6f, 0x6d, 0x2f, 0x64,
	0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76,
	0x31, 0x2f, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xe0, 0x01,
	0x0a, 0x11, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x46, 0x69, 0x6c,
	0x74, 0x65, 0x72, 0x12, 0x67, 0x0a, 0x10, 0x66, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x73, 0x5f, 0x62,
	0x79, 0x5f, 0x70, 0x61, 0x72, 0x74, 0x79, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x3d, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e,
	0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69,
	0x6f, 0x6e, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x2e, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x73,
	0x42, 0x79, 0x50, 0x61, 0x72, 0x74, 0x79, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x52, 0x0e, 0x66, 0x69,
	0x6c, 0x74, 0x65, 0x72, 0x73, 0x42, 0x79, 0x50, 0x61, 0x72, 0x74, 0x79, 0x1a, 0x62, 0x0a, 0x13,
	0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x73, 0x42, 0x79, 0x50, 0x61, 0x72, 0x74, 0x79, 0x45, 0x6e,
	0x74, 0x72, 0x79, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x03, 0x6b, 0x65, 0x79, 0x12, 0x35, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x1f, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e,
	0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x46, 0x69,
	0x6c, 0x74, 0x65, 0x72, 0x73, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38, 0x01,
	0x22, 0x51, 0x0a, 0x07, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x73, 0x12, 0x46, 0x0a, 0x09, 0x69,
	0x6e, 0x63, 0x6c, 0x75, 0x73, 0x69, 0x76, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x28,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x49, 0x6e, 0x63, 0x6c, 0x75, 0x73, 0x69, 0x76,
	0x65, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x73, 0x52, 0x09, 0x69, 0x6e, 0x63, 0x6c, 0x75, 0x73,
	0x69, 0x76, 0x65, 0x22, 0x86, 0x02, 0x0a, 0x10, 0x49, 0x6e, 0x63, 0x6c, 0x75, 0x73, 0x69, 0x76,
	0x65, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x73, 0x12, 0x49, 0x0a, 0x0c, 0x74, 0x65, 0x6d, 0x70,
	0x6c, 0x61, 0x74, 0x65, 0x5f, 0x69, 0x64, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x22,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x66, 0x69,
	0x65, 0x72, 0x42, 0x02, 0x18, 0x01, 0x52, 0x0b, 0x74, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65,
	0x49, 0x64, 0x73, 0x12, 0x54, 0x0a, 0x11, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65,
	0x5f, 0x66, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x73, 0x18, 0x02, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x27,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x49, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63,
	0x65, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x52, 0x10, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61,
	0x63, 0x65, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x73, 0x12, 0x51, 0x0a, 0x10, 0x74, 0x65, 0x6d,
	0x70, 0x6c, 0x61, 0x74, 0x65, 0x5f, 0x66, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x73, 0x18, 0x03, 0x20,
	0x03, 0x28, 0x0b, 0x32, 0x26, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c,
	0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x54, 0x65, 0x6d,
	0x70, 0x6c, 0x61, 0x74, 0x65, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x52, 0x0f, 0x74, 0x65, 0x6d,
	0x70, 0x6c, 0x61, 0x74, 0x65, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x73, 0x22, 0xd1, 0x01, 0x0a,
	0x0f, 0x49, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72,
	0x12, 0x45, 0x0a, 0x0c, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x5f, 0x69, 0x64,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x22, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d,
	0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e,
	0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x66, 0x69, 0x65, 0x72, 0x52, 0x0b, 0x69, 0x6e, 0x74, 0x65,
	0x72, 0x66, 0x61, 0x63, 0x65, 0x49, 0x64, 0x12, 0x34, 0x0a, 0x16, 0x69, 0x6e, 0x63, 0x6c, 0x75,
	0x64, 0x65, 0x5f, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x5f, 0x76, 0x69, 0x65,
	0x77, 0x18, 0x02, 0x20, 0x01, 0x28, 0x08, 0x52, 0x14, 0x69, 0x6e, 0x63, 0x6c, 0x75, 0x64, 0x65,
	0x49, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x56, 0x69, 0x65, 0x77, 0x12, 0x3b, 0x0a,
	0x1a, 0x69, 0x6e, 0x63, 0x6c, 0x75, 0x64, 0x65, 0x5f, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64,
	0x5f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x5f, 0x62, 0x6c, 0x6f, 0x62, 0x18, 0x04, 0x20, 0x01, 0x28,
	0x08, 0x52, 0x17, 0x69, 0x6e, 0x63, 0x6c, 0x75, 0x64, 0x65, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65,
	0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x42, 0x6c, 0x6f, 0x62, 0x4a, 0x04, 0x08, 0x03, 0x10, 0x04,
	0x22, 0x92, 0x01, 0x0a, 0x0e, 0x54, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x46, 0x69, 0x6c,
	0x74, 0x65, 0x72, 0x12, 0x43, 0x0a, 0x0b, 0x74, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x5f,
	0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x22, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76,
	0x31, 0x2e, 0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x66, 0x69, 0x65, 0x72, 0x52, 0x0a, 0x74, 0x65,
	0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x49, 0x64, 0x12, 0x3b, 0x0a, 0x1a, 0x69, 0x6e, 0x63, 0x6c,
	0x75, 0x64, 0x65, 0x5f, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x5f, 0x65, 0x76, 0x65, 0x6e,
	0x74, 0x5f, 0x62, 0x6c, 0x6f, 0x62, 0x18, 0x02, 0x20, 0x01, 0x28, 0x08, 0x52, 0x17, 0x69, 0x6e,
	0x63, 0x6c, 0x75, 0x64, 0x65, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x45, 0x76, 0x65, 0x6e,
	0x74, 0x42, 0x6c, 0x6f, 0x62, 0x42, 0x95, 0x01, 0x0a, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61,
	0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31,
	0x42, 0x1b, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x46, 0x69, 0x6c,
	0x74, 0x65, 0x72, 0x4f, 0x75, 0x74, 0x65, 0x72, 0x43, 0x6c, 0x61, 0x73, 0x73, 0x5a, 0x45, 0x67,
	0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61,
	0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69,
	0x65, 0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f,
	0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70,
	0x69, 0x2f, 0x76, 0x31, 0xaa, 0x02, 0x16, 0x43, 0x6f, 0x6d, 0x2e, 0x44, 0x61, 0x6d, 0x6c, 0x2e,
	0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x41, 0x70, 0x69, 0x2e, 0x56, 0x31, 0x62, 0x06, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescData = file_com_daml_ledger_api_v1_transaction_filter_proto_rawDesc
)

func file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescData)
	})
	return file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescData
}

var file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes = make([]protoimpl.MessageInfo, 6)
var file_com_daml_ledger_api_v1_transaction_filter_proto_goTypes = []any{
	(*TransactionFilter)(nil), // 0: com.daml.ledger.api.v1.TransactionFilter
	(*Filters)(nil),           // 1: com.daml.ledger.api.v1.Filters
	(*InclusiveFilters)(nil),  // 2: com.daml.ledger.api.v1.InclusiveFilters
	(*InterfaceFilter)(nil),   // 3: com.daml.ledger.api.v1.InterfaceFilter
	(*TemplateFilter)(nil),    // 4: com.daml.ledger.api.v1.TemplateFilter
	nil,                       // 5: com.daml.ledger.api.v1.TransactionFilter.FiltersByPartyEntry
	(*Identifier)(nil),        // 6: com.daml.ledger.api.v1.Identifier
}
var file_com_daml_ledger_api_v1_transaction_filter_proto_depIdxs = []int32{
	5, // 0: com.daml.ledger.api.v1.TransactionFilter.filters_by_party:type_name -> com.daml.ledger.api.v1.TransactionFilter.FiltersByPartyEntry
	2, // 1: com.daml.ledger.api.v1.Filters.inclusive:type_name -> com.daml.ledger.api.v1.InclusiveFilters
	6, // 2: com.daml.ledger.api.v1.InclusiveFilters.template_ids:type_name -> com.daml.ledger.api.v1.Identifier
	3, // 3: com.daml.ledger.api.v1.InclusiveFilters.interface_filters:type_name -> com.daml.ledger.api.v1.InterfaceFilter
	4, // 4: com.daml.ledger.api.v1.InclusiveFilters.template_filters:type_name -> com.daml.ledger.api.v1.TemplateFilter
	6, // 5: com.daml.ledger.api.v1.InterfaceFilter.interface_id:type_name -> com.daml.ledger.api.v1.Identifier
	6, // 6: com.daml.ledger.api.v1.TemplateFilter.template_id:type_name -> com.daml.ledger.api.v1.Identifier
	1, // 7: com.daml.ledger.api.v1.TransactionFilter.FiltersByPartyEntry.value:type_name -> com.daml.ledger.api.v1.Filters
	8, // [8:8] is the sub-list for method output_type
	8, // [8:8] is the sub-list for method input_type
	8, // [8:8] is the sub-list for extension type_name
	8, // [8:8] is the sub-list for extension extendee
	0, // [0:8] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v1_transaction_filter_proto_init() }
func file_com_daml_ledger_api_v1_transaction_filter_proto_init() {
	if File_com_daml_ledger_api_v1_transaction_filter_proto != nil {
		return
	}
	file_com_daml_ledger_api_v1_value_proto_init()
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_daml_ledger_api_v1_transaction_filter_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   6,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_daml_ledger_api_v1_transaction_filter_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v1_transaction_filter_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v1_transaction_filter_proto = out.File
	file_com_daml_ledger_api_v1_transaction_filter_proto_rawDesc = nil
	file_com_daml_ledger_api_v1_transaction_filter_proto_goTypes = nil
	file_com_daml_ledger_api_v1_transaction_filter_proto_depIdxs = nil
}
