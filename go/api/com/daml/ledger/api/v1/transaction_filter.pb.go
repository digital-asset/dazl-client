// Copyright (c) 2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.21.6
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

// A filter both for filtering create and archive events as well as for
// filtering transaction trees.
type TransactionFilter struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Each key must be a valid PartyIdString (as described in “value.proto“).
	// The interpretation of the filter depends on the stream being filtered:
	// (1) For **transaction tree streams** only party filters with wildcards are allowed, and all subtrees
	//
	//	whose root has one of the listed parties as an informee are returned.
	//
	// (2) For **transaction and active-contract-set streams** create and archive events are returned for all contracts whose
	//
	//	stakeholders include at least one of the listed parties and match the
	//	per-party filter.
	//
	// Required
	FiltersByParty map[string]*Filters `protobuf:"bytes,1,rep,name=filters_by_party,json=filtersByParty,proto3" json:"filters_by_party,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
}

func (x *TransactionFilter) Reset() {
	*x = TransactionFilter{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TransactionFilter) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransactionFilter) ProtoMessage() {}

func (x *TransactionFilter) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
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

// The union of a set of contract filters, or a wildcard.
type Filters struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// If set, then contracts matching any of the “InclusiveFilters“ match
	// this filter.
	// If not set, or if “InclusiveFilters“ has empty “template_ids“ and empty “interface_filters“:
	// any contract matches this filter.
	// Optional
	Inclusive *InclusiveFilters `protobuf:"bytes,1,opt,name=inclusive,proto3" json:"inclusive,omitempty"`
}

func (x *Filters) Reset() {
	*x = Filters{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Filters) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Filters) ProtoMessage() {}

func (x *Filters) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
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

// A filter that matches all contracts that are either an instance of one of
// the “template_ids“ or that match one of the “interface_filters“.
type InclusiveFilters struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// A collection of templates for which the payload will be included in the
	// “create_arguments“ of a matching “CreatedEvent“.
	// SHOULD NOT contain duplicates.
	// All “template_ids“ needs to be valid: corresponding template should be defined in one of
	// the available packages at the time of the query.
	// Optional
	TemplateIds []*Identifier `protobuf:"bytes,1,rep,name=template_ids,json=templateIds,proto3" json:"template_ids,omitempty"`
	// Include an “InterfaceView“ for every “InterfaceFilter“ matching a contract.
	// The “InterfaceFilter“s MUST use unique “interface_id“s.
	// All “interface_id“ needs to be valid: corresponding interface should be defined in one of
	// the available packages at the time of the query.
	// Optional
	InterfaceFilters []*InterfaceFilter `protobuf:"bytes,2,rep,name=interface_filters,json=interfaceFilters,proto3" json:"interface_filters,omitempty"`
}

func (x *InclusiveFilters) Reset() {
	*x = InclusiveFilters{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *InclusiveFilters) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*InclusiveFilters) ProtoMessage() {}

func (x *InclusiveFilters) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
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

// This filter matches contracts that implement a specific interface.
type InterfaceFilter struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// The interface that a matching contract must implement.
	// Required
	InterfaceId *Identifier `protobuf:"bytes,1,opt,name=interface_id,json=interfaceId,proto3" json:"interface_id,omitempty"`
	// Whether to include the interface view on the contract in the returned “CreateEvent“.
	// Use this to access contract data in a uniform manner in your API client.
	// Optional
	IncludeInterfaceView bool `protobuf:"varint,2,opt,name=include_interface_view,json=includeInterfaceView,proto3" json:"include_interface_view,omitempty"`
	// Whether to include a “create_arguments_blob“ in the returned
	// “CreateEvent“.
	// Use this to access the complete contract data in your API client
	// for submitting it as a disclosed contract with future commands.
	// Optional
	IncludeCreateArgumentsBlob bool `protobuf:"varint,3,opt,name=include_create_arguments_blob,json=includeCreateArgumentsBlob,proto3" json:"include_create_arguments_blob,omitempty"`
}

func (x *InterfaceFilter) Reset() {
	*x = InterfaceFilter{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *InterfaceFilter) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*InterfaceFilter) ProtoMessage() {}

func (x *InterfaceFilter) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
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

func (x *InterfaceFilter) GetIncludeCreateArgumentsBlob() bool {
	if x != nil {
		return x.IncludeCreateArgumentsBlob
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
	0x69, 0x76, 0x65, 0x22, 0xaf, 0x01, 0x0a, 0x10, 0x49, 0x6e, 0x63, 0x6c, 0x75, 0x73, 0x69, 0x76,
	0x65, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x73, 0x12, 0x45, 0x0a, 0x0c, 0x74, 0x65, 0x6d, 0x70,
	0x6c, 0x61, 0x74, 0x65, 0x5f, 0x69, 0x64, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x22,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x66, 0x69,
	0x65, 0x72, 0x52, 0x0b, 0x74, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x49, 0x64, 0x73, 0x12,
	0x54, 0x0a, 0x11, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x5f, 0x66, 0x69, 0x6c,
	0x74, 0x65, 0x72, 0x73, 0x18, 0x02, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x27, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x76, 0x31, 0x2e, 0x49, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x46, 0x69, 0x6c,
	0x74, 0x65, 0x72, 0x52, 0x10, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x46, 0x69,
	0x6c, 0x74, 0x65, 0x72, 0x73, 0x22, 0xd1, 0x01, 0x0a, 0x0f, 0x49, 0x6e, 0x74, 0x65, 0x72, 0x66,
	0x61, 0x63, 0x65, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x12, 0x45, 0x0a, 0x0c, 0x69, 0x6e, 0x74,
	0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x22, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x66,
	0x69, 0x65, 0x72, 0x52, 0x0b, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x49, 0x64,
	0x12, 0x34, 0x0a, 0x16, 0x69, 0x6e, 0x63, 0x6c, 0x75, 0x64, 0x65, 0x5f, 0x69, 0x6e, 0x74, 0x65,
	0x72, 0x66, 0x61, 0x63, 0x65, 0x5f, 0x76, 0x69, 0x65, 0x77, 0x18, 0x02, 0x20, 0x01, 0x28, 0x08,
	0x52, 0x14, 0x69, 0x6e, 0x63, 0x6c, 0x75, 0x64, 0x65, 0x49, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61,
	0x63, 0x65, 0x56, 0x69, 0x65, 0x77, 0x12, 0x41, 0x0a, 0x1d, 0x69, 0x6e, 0x63, 0x6c, 0x75, 0x64,
	0x65, 0x5f, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x5f, 0x61, 0x72, 0x67, 0x75, 0x6d, 0x65, 0x6e,
	0x74, 0x73, 0x5f, 0x62, 0x6c, 0x6f, 0x62, 0x18, 0x03, 0x20, 0x01, 0x28, 0x08, 0x52, 0x1a, 0x69,
	0x6e, 0x63, 0x6c, 0x75, 0x64, 0x65, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x41, 0x72, 0x67, 0x75,
	0x6d, 0x65, 0x6e, 0x74, 0x73, 0x42, 0x6c, 0x6f, 0x62, 0x42, 0x95, 0x01, 0x0a, 0x16, 0x63, 0x6f,
	0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70,
	0x69, 0x2e, 0x76, 0x31, 0x42, 0x1b, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f,
	0x6e, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x4f, 0x75, 0x74, 0x65, 0x72, 0x43, 0x6c, 0x61, 0x73,
	0x73, 0x5a, 0x45, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69,
	0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c,
	0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x37, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70,
	0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0xaa, 0x02, 0x16, 0x43, 0x6f, 0x6d, 0x2e, 0x44,
	0x61, 0x6d, 0x6c, 0x2e, 0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x41, 0x70, 0x69, 0x2e, 0x56,
	0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
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

var file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes = make([]protoimpl.MessageInfo, 5)
var file_com_daml_ledger_api_v1_transaction_filter_proto_goTypes = []interface{}{
	(*TransactionFilter)(nil), // 0: com.daml.ledger.api.v1.TransactionFilter
	(*Filters)(nil),           // 1: com.daml.ledger.api.v1.Filters
	(*InclusiveFilters)(nil),  // 2: com.daml.ledger.api.v1.InclusiveFilters
	(*InterfaceFilter)(nil),   // 3: com.daml.ledger.api.v1.InterfaceFilter
	nil,                       // 4: com.daml.ledger.api.v1.TransactionFilter.FiltersByPartyEntry
	(*Identifier)(nil),        // 5: com.daml.ledger.api.v1.Identifier
}
var file_com_daml_ledger_api_v1_transaction_filter_proto_depIdxs = []int32{
	4, // 0: com.daml.ledger.api.v1.TransactionFilter.filters_by_party:type_name -> com.daml.ledger.api.v1.TransactionFilter.FiltersByPartyEntry
	2, // 1: com.daml.ledger.api.v1.Filters.inclusive:type_name -> com.daml.ledger.api.v1.InclusiveFilters
	5, // 2: com.daml.ledger.api.v1.InclusiveFilters.template_ids:type_name -> com.daml.ledger.api.v1.Identifier
	3, // 3: com.daml.ledger.api.v1.InclusiveFilters.interface_filters:type_name -> com.daml.ledger.api.v1.InterfaceFilter
	5, // 4: com.daml.ledger.api.v1.InterfaceFilter.interface_id:type_name -> com.daml.ledger.api.v1.Identifier
	1, // 5: com.daml.ledger.api.v1.TransactionFilter.FiltersByPartyEntry.value:type_name -> com.daml.ledger.api.v1.Filters
	6, // [6:6] is the sub-list for method output_type
	6, // [6:6] is the sub-list for method input_type
	6, // [6:6] is the sub-list for extension type_name
	6, // [6:6] is the sub-list for extension extendee
	0, // [0:6] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v1_transaction_filter_proto_init() }
func file_com_daml_ledger_api_v1_transaction_filter_proto_init() {
	if File_com_daml_ledger_api_v1_transaction_filter_proto != nil {
		return
	}
	file_com_daml_ledger_api_v1_value_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TransactionFilter); i {
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
		file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Filters); i {
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
		file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*InclusiveFilters); i {
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
		file_com_daml_ledger_api_v1_transaction_filter_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*InterfaceFilter); i {
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
			RawDescriptor: file_com_daml_ledger_api_v1_transaction_filter_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   5,
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
