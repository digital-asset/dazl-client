// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/daml/ledger/api/v1/transaction_filter.proto

package v1

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
	unsafe "unsafe"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type TransactionFilter struct {
	state          protoimpl.MessageState `protogen:"open.v1"`
	FiltersByParty map[string]*Filters    `protobuf:"bytes,1,rep,name=filters_by_party,json=filtersByParty,proto3" json:"filters_by_party,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
	unknownFields  protoimpl.UnknownFields
	sizeCache      protoimpl.SizeCache
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
	state         protoimpl.MessageState `protogen:"open.v1"`
	Inclusive     *InclusiveFilters      `protobuf:"bytes,1,opt,name=inclusive,proto3" json:"inclusive,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
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
	state protoimpl.MessageState `protogen:"open.v1"`
	// Deprecated: Marked as deprecated in com/daml/ledger/api/v1/transaction_filter.proto.
	TemplateIds      []*Identifier      `protobuf:"bytes,1,rep,name=template_ids,json=templateIds,proto3" json:"template_ids,omitempty"`
	InterfaceFilters []*InterfaceFilter `protobuf:"bytes,2,rep,name=interface_filters,json=interfaceFilters,proto3" json:"interface_filters,omitempty"`
	TemplateFilters  []*TemplateFilter  `protobuf:"bytes,3,rep,name=template_filters,json=templateFilters,proto3" json:"template_filters,omitempty"`
	unknownFields    protoimpl.UnknownFields
	sizeCache        protoimpl.SizeCache
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
	state                   protoimpl.MessageState `protogen:"open.v1"`
	InterfaceId             *Identifier            `protobuf:"bytes,1,opt,name=interface_id,json=interfaceId,proto3" json:"interface_id,omitempty"`
	IncludeInterfaceView    bool                   `protobuf:"varint,2,opt,name=include_interface_view,json=includeInterfaceView,proto3" json:"include_interface_view,omitempty"`
	IncludeCreatedEventBlob bool                   `protobuf:"varint,4,opt,name=include_created_event_blob,json=includeCreatedEventBlob,proto3" json:"include_created_event_blob,omitempty"`
	unknownFields           protoimpl.UnknownFields
	sizeCache               protoimpl.SizeCache
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
	state                   protoimpl.MessageState `protogen:"open.v1"`
	TemplateId              *Identifier            `protobuf:"bytes,1,opt,name=template_id,json=templateId,proto3" json:"template_id,omitempty"`
	IncludeCreatedEventBlob bool                   `protobuf:"varint,2,opt,name=include_created_event_blob,json=includeCreatedEventBlob,proto3" json:"include_created_event_blob,omitempty"`
	unknownFields           protoimpl.UnknownFields
	sizeCache               protoimpl.SizeCache
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

const file_com_daml_ledger_api_v1_transaction_filter_proto_rawDesc = "" +
	"\n" +
	"/com/daml/ledger/api/v1/transaction_filter.proto\x12\x16com.daml.ledger.api.v1\x1a\"com/daml/ledger/api/v1/value.proto\"\xe0\x01\n" +
	"\x11TransactionFilter\x12g\n" +
	"\x10filters_by_party\x18\x01 \x03(\v2=.com.daml.ledger.api.v1.TransactionFilter.FiltersByPartyEntryR\x0efiltersByParty\x1ab\n" +
	"\x13FiltersByPartyEntry\x12\x10\n" +
	"\x03key\x18\x01 \x01(\tR\x03key\x125\n" +
	"\x05value\x18\x02 \x01(\v2\x1f.com.daml.ledger.api.v1.FiltersR\x05value:\x028\x01\"Q\n" +
	"\aFilters\x12F\n" +
	"\tinclusive\x18\x01 \x01(\v2(.com.daml.ledger.api.v1.InclusiveFiltersR\tinclusive\"\x86\x02\n" +
	"\x10InclusiveFilters\x12I\n" +
	"\ftemplate_ids\x18\x01 \x03(\v2\".com.daml.ledger.api.v1.IdentifierB\x02\x18\x01R\vtemplateIds\x12T\n" +
	"\x11interface_filters\x18\x02 \x03(\v2'.com.daml.ledger.api.v1.InterfaceFilterR\x10interfaceFilters\x12Q\n" +
	"\x10template_filters\x18\x03 \x03(\v2&.com.daml.ledger.api.v1.TemplateFilterR\x0ftemplateFilters\"\xd1\x01\n" +
	"\x0fInterfaceFilter\x12E\n" +
	"\finterface_id\x18\x01 \x01(\v2\".com.daml.ledger.api.v1.IdentifierR\vinterfaceId\x124\n" +
	"\x16include_interface_view\x18\x02 \x01(\bR\x14includeInterfaceView\x12;\n" +
	"\x1ainclude_created_event_blob\x18\x04 \x01(\bR\x17includeCreatedEventBlobJ\x04\b\x03\x10\x04\"\x92\x01\n" +
	"\x0eTemplateFilter\x12C\n" +
	"\vtemplate_id\x18\x01 \x01(\v2\".com.daml.ledger.api.v1.IdentifierR\n" +
	"templateId\x12;\n" +
	"\x1ainclude_created_event_blob\x18\x02 \x01(\bR\x17includeCreatedEventBlobB\x95\x01\n" +
	"\x16com.daml.ledger.api.v1B\x1bTransactionFilterOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v1\xaa\x02\x16Com.Daml.Ledger.Api.V1b\x06proto3"

var (
	file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescData []byte
)

func file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v1_transaction_filter_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_daml_ledger_api_v1_transaction_filter_proto_rawDesc), len(file_com_daml_ledger_api_v1_transaction_filter_proto_rawDesc)))
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
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_daml_ledger_api_v1_transaction_filter_proto_rawDesc), len(file_com_daml_ledger_api_v1_transaction_filter_proto_rawDesc)),
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
	file_com_daml_ledger_api_v1_transaction_filter_proto_goTypes = nil
	file_com_daml_ledger_api_v1_transaction_filter_proto_depIdxs = nil
}
