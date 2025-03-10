// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/daml/ledger/api/v2/value.proto

package v2

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type Value struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Sum:
	//
	//	*Value_Unit
	//	*Value_Bool
	//	*Value_Int64
	//	*Value_Date
	//	*Value_Timestamp
	//	*Value_Numeric
	//	*Value_Party
	//	*Value_Text
	//	*Value_ContractId
	//	*Value_Optional
	//	*Value_List
	//	*Value_TextMap
	//	*Value_GenMap
	//	*Value_Record
	//	*Value_Variant
	//	*Value_Enum
	Sum isValue_Sum `protobuf_oneof:"sum"`
}

func (x *Value) Reset() {
	*x = Value{}
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Value) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Value) ProtoMessage() {}

func (x *Value) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Value.ProtoReflect.Descriptor instead.
func (*Value) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_value_proto_rawDescGZIP(), []int{0}
}

func (m *Value) GetSum() isValue_Sum {
	if m != nil {
		return m.Sum
	}
	return nil
}

func (x *Value) GetUnit() *emptypb.Empty {
	if x, ok := x.GetSum().(*Value_Unit); ok {
		return x.Unit
	}
	return nil
}

func (x *Value) GetBool() bool {
	if x, ok := x.GetSum().(*Value_Bool); ok {
		return x.Bool
	}
	return false
}

func (x *Value) GetInt64() int64 {
	if x, ok := x.GetSum().(*Value_Int64); ok {
		return x.Int64
	}
	return 0
}

func (x *Value) GetDate() int32 {
	if x, ok := x.GetSum().(*Value_Date); ok {
		return x.Date
	}
	return 0
}

func (x *Value) GetTimestamp() int64 {
	if x, ok := x.GetSum().(*Value_Timestamp); ok {
		return x.Timestamp
	}
	return 0
}

func (x *Value) GetNumeric() string {
	if x, ok := x.GetSum().(*Value_Numeric); ok {
		return x.Numeric
	}
	return ""
}

func (x *Value) GetParty() string {
	if x, ok := x.GetSum().(*Value_Party); ok {
		return x.Party
	}
	return ""
}

func (x *Value) GetText() string {
	if x, ok := x.GetSum().(*Value_Text); ok {
		return x.Text
	}
	return ""
}

func (x *Value) GetContractId() string {
	if x, ok := x.GetSum().(*Value_ContractId); ok {
		return x.ContractId
	}
	return ""
}

func (x *Value) GetOptional() *Optional {
	if x, ok := x.GetSum().(*Value_Optional); ok {
		return x.Optional
	}
	return nil
}

func (x *Value) GetList() *List {
	if x, ok := x.GetSum().(*Value_List); ok {
		return x.List
	}
	return nil
}

func (x *Value) GetTextMap() *TextMap {
	if x, ok := x.GetSum().(*Value_TextMap); ok {
		return x.TextMap
	}
	return nil
}

func (x *Value) GetGenMap() *GenMap {
	if x, ok := x.GetSum().(*Value_GenMap); ok {
		return x.GenMap
	}
	return nil
}

func (x *Value) GetRecord() *Record {
	if x, ok := x.GetSum().(*Value_Record); ok {
		return x.Record
	}
	return nil
}

func (x *Value) GetVariant() *Variant {
	if x, ok := x.GetSum().(*Value_Variant); ok {
		return x.Variant
	}
	return nil
}

func (x *Value) GetEnum() *Enum {
	if x, ok := x.GetSum().(*Value_Enum); ok {
		return x.Enum
	}
	return nil
}

type isValue_Sum interface {
	isValue_Sum()
}

type Value_Unit struct {
	Unit *emptypb.Empty `protobuf:"bytes,1,opt,name=unit,proto3,oneof"`
}

type Value_Bool struct {
	Bool bool `protobuf:"varint,2,opt,name=bool,proto3,oneof"`
}

type Value_Int64 struct {
	Int64 int64 `protobuf:"zigzag64,3,opt,name=int64,proto3,oneof"`
}

type Value_Date struct {
	Date int32 `protobuf:"varint,4,opt,name=date,proto3,oneof"`
}

type Value_Timestamp struct {
	Timestamp int64 `protobuf:"fixed64,5,opt,name=timestamp,proto3,oneof"`
}

type Value_Numeric struct {
	Numeric string `protobuf:"bytes,6,opt,name=numeric,proto3,oneof"`
}

type Value_Party struct {
	Party string `protobuf:"bytes,7,opt,name=party,proto3,oneof"`
}

type Value_Text struct {
	Text string `protobuf:"bytes,8,opt,name=text,proto3,oneof"`
}

type Value_ContractId struct {
	ContractId string `protobuf:"bytes,9,opt,name=contract_id,json=contractId,proto3,oneof"`
}

type Value_Optional struct {
	Optional *Optional `protobuf:"bytes,10,opt,name=optional,proto3,oneof"`
}

type Value_List struct {
	List *List `protobuf:"bytes,11,opt,name=list,proto3,oneof"`
}

type Value_TextMap struct {
	TextMap *TextMap `protobuf:"bytes,12,opt,name=text_map,json=textMap,proto3,oneof"`
}

type Value_GenMap struct {
	GenMap *GenMap `protobuf:"bytes,13,opt,name=gen_map,json=genMap,proto3,oneof"`
}

type Value_Record struct {
	Record *Record `protobuf:"bytes,14,opt,name=record,proto3,oneof"`
}

type Value_Variant struct {
	Variant *Variant `protobuf:"bytes,15,opt,name=variant,proto3,oneof"`
}

type Value_Enum struct {
	Enum *Enum `protobuf:"bytes,16,opt,name=enum,proto3,oneof"`
}

func (*Value_Unit) isValue_Sum() {}

func (*Value_Bool) isValue_Sum() {}

func (*Value_Int64) isValue_Sum() {}

func (*Value_Date) isValue_Sum() {}

func (*Value_Timestamp) isValue_Sum() {}

func (*Value_Numeric) isValue_Sum() {}

func (*Value_Party) isValue_Sum() {}

func (*Value_Text) isValue_Sum() {}

func (*Value_ContractId) isValue_Sum() {}

func (*Value_Optional) isValue_Sum() {}

func (*Value_List) isValue_Sum() {}

func (*Value_TextMap) isValue_Sum() {}

func (*Value_GenMap) isValue_Sum() {}

func (*Value_Record) isValue_Sum() {}

func (*Value_Variant) isValue_Sum() {}

func (*Value_Enum) isValue_Sum() {}

type Record struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	RecordId *Identifier    `protobuf:"bytes,1,opt,name=record_id,json=recordId,proto3" json:"record_id,omitempty"`
	Fields   []*RecordField `protobuf:"bytes,2,rep,name=fields,proto3" json:"fields,omitempty"`
}

func (x *Record) Reset() {
	*x = Record{}
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Record) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Record) ProtoMessage() {}

func (x *Record) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Record.ProtoReflect.Descriptor instead.
func (*Record) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_value_proto_rawDescGZIP(), []int{1}
}

func (x *Record) GetRecordId() *Identifier {
	if x != nil {
		return x.RecordId
	}
	return nil
}

func (x *Record) GetFields() []*RecordField {
	if x != nil {
		return x.Fields
	}
	return nil
}

type RecordField struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Label string `protobuf:"bytes,1,opt,name=label,proto3" json:"label,omitempty"`
	Value *Value `protobuf:"bytes,2,opt,name=value,proto3" json:"value,omitempty"`
}

func (x *RecordField) Reset() {
	*x = RecordField{}
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *RecordField) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RecordField) ProtoMessage() {}

func (x *RecordField) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RecordField.ProtoReflect.Descriptor instead.
func (*RecordField) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_value_proto_rawDescGZIP(), []int{2}
}

func (x *RecordField) GetLabel() string {
	if x != nil {
		return x.Label
	}
	return ""
}

func (x *RecordField) GetValue() *Value {
	if x != nil {
		return x.Value
	}
	return nil
}

type Identifier struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	PackageId  string `protobuf:"bytes,1,opt,name=package_id,json=packageId,proto3" json:"package_id,omitempty"`
	ModuleName string `protobuf:"bytes,2,opt,name=module_name,json=moduleName,proto3" json:"module_name,omitempty"`
	EntityName string `protobuf:"bytes,3,opt,name=entity_name,json=entityName,proto3" json:"entity_name,omitempty"`
}

func (x *Identifier) Reset() {
	*x = Identifier{}
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Identifier) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Identifier) ProtoMessage() {}

func (x *Identifier) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Identifier.ProtoReflect.Descriptor instead.
func (*Identifier) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_value_proto_rawDescGZIP(), []int{3}
}

func (x *Identifier) GetPackageId() string {
	if x != nil {
		return x.PackageId
	}
	return ""
}

func (x *Identifier) GetModuleName() string {
	if x != nil {
		return x.ModuleName
	}
	return ""
}

func (x *Identifier) GetEntityName() string {
	if x != nil {
		return x.EntityName
	}
	return ""
}

type Variant struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	VariantId   *Identifier `protobuf:"bytes,1,opt,name=variant_id,json=variantId,proto3" json:"variant_id,omitempty"`
	Constructor string      `protobuf:"bytes,2,opt,name=constructor,proto3" json:"constructor,omitempty"`
	Value       *Value      `protobuf:"bytes,3,opt,name=value,proto3" json:"value,omitempty"`
}

func (x *Variant) Reset() {
	*x = Variant{}
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Variant) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Variant) ProtoMessage() {}

func (x *Variant) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Variant.ProtoReflect.Descriptor instead.
func (*Variant) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_value_proto_rawDescGZIP(), []int{4}
}

func (x *Variant) GetVariantId() *Identifier {
	if x != nil {
		return x.VariantId
	}
	return nil
}

func (x *Variant) GetConstructor() string {
	if x != nil {
		return x.Constructor
	}
	return ""
}

func (x *Variant) GetValue() *Value {
	if x != nil {
		return x.Value
	}
	return nil
}

type Enum struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	EnumId      *Identifier `protobuf:"bytes,1,opt,name=enum_id,json=enumId,proto3" json:"enum_id,omitempty"`
	Constructor string      `protobuf:"bytes,2,opt,name=constructor,proto3" json:"constructor,omitempty"`
}

func (x *Enum) Reset() {
	*x = Enum{}
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Enum) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Enum) ProtoMessage() {}

func (x *Enum) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[5]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Enum.ProtoReflect.Descriptor instead.
func (*Enum) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_value_proto_rawDescGZIP(), []int{5}
}

func (x *Enum) GetEnumId() *Identifier {
	if x != nil {
		return x.EnumId
	}
	return nil
}

func (x *Enum) GetConstructor() string {
	if x != nil {
		return x.Constructor
	}
	return ""
}

type List struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Elements []*Value `protobuf:"bytes,1,rep,name=elements,proto3" json:"elements,omitempty"`
}

func (x *List) Reset() {
	*x = List{}
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[6]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *List) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*List) ProtoMessage() {}

func (x *List) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[6]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use List.ProtoReflect.Descriptor instead.
func (*List) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_value_proto_rawDescGZIP(), []int{6}
}

func (x *List) GetElements() []*Value {
	if x != nil {
		return x.Elements
	}
	return nil
}

type Optional struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Value *Value `protobuf:"bytes,1,opt,name=value,proto3" json:"value,omitempty"`
}

func (x *Optional) Reset() {
	*x = Optional{}
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[7]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Optional) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Optional) ProtoMessage() {}

func (x *Optional) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[7]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Optional.ProtoReflect.Descriptor instead.
func (*Optional) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_value_proto_rawDescGZIP(), []int{7}
}

func (x *Optional) GetValue() *Value {
	if x != nil {
		return x.Value
	}
	return nil
}

type TextMap struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Entries []*TextMap_Entry `protobuf:"bytes,1,rep,name=entries,proto3" json:"entries,omitempty"`
}

func (x *TextMap) Reset() {
	*x = TextMap{}
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[8]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TextMap) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TextMap) ProtoMessage() {}

func (x *TextMap) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[8]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TextMap.ProtoReflect.Descriptor instead.
func (*TextMap) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_value_proto_rawDescGZIP(), []int{8}
}

func (x *TextMap) GetEntries() []*TextMap_Entry {
	if x != nil {
		return x.Entries
	}
	return nil
}

type GenMap struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Entries []*GenMap_Entry `protobuf:"bytes,1,rep,name=entries,proto3" json:"entries,omitempty"`
}

func (x *GenMap) Reset() {
	*x = GenMap{}
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[9]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GenMap) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GenMap) ProtoMessage() {}

func (x *GenMap) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[9]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GenMap.ProtoReflect.Descriptor instead.
func (*GenMap) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_value_proto_rawDescGZIP(), []int{9}
}

func (x *GenMap) GetEntries() []*GenMap_Entry {
	if x != nil {
		return x.Entries
	}
	return nil
}

type TextMap_Entry struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Key   string `protobuf:"bytes,1,opt,name=key,proto3" json:"key,omitempty"`
	Value *Value `protobuf:"bytes,2,opt,name=value,proto3" json:"value,omitempty"`
}

func (x *TextMap_Entry) Reset() {
	*x = TextMap_Entry{}
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[10]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TextMap_Entry) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TextMap_Entry) ProtoMessage() {}

func (x *TextMap_Entry) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[10]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TextMap_Entry.ProtoReflect.Descriptor instead.
func (*TextMap_Entry) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_value_proto_rawDescGZIP(), []int{8, 0}
}

func (x *TextMap_Entry) GetKey() string {
	if x != nil {
		return x.Key
	}
	return ""
}

func (x *TextMap_Entry) GetValue() *Value {
	if x != nil {
		return x.Value
	}
	return nil
}

type GenMap_Entry struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Key   *Value `protobuf:"bytes,1,opt,name=key,proto3" json:"key,omitempty"`
	Value *Value `protobuf:"bytes,2,opt,name=value,proto3" json:"value,omitempty"`
}

func (x *GenMap_Entry) Reset() {
	*x = GenMap_Entry{}
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[11]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GenMap_Entry) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GenMap_Entry) ProtoMessage() {}

func (x *GenMap_Entry) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_value_proto_msgTypes[11]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GenMap_Entry.ProtoReflect.Descriptor instead.
func (*GenMap_Entry) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_value_proto_rawDescGZIP(), []int{9, 0}
}

func (x *GenMap_Entry) GetKey() *Value {
	if x != nil {
		return x.Key
	}
	return nil
}

func (x *GenMap_Entry) GetValue() *Value {
	if x != nil {
		return x.Value
	}
	return nil
}

var File_com_daml_ledger_api_v2_value_proto protoreflect.FileDescriptor

var file_com_daml_ledger_api_v2_value_proto_rawDesc = []byte{
	0x0a, 0x22, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x32, 0x2f, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x12, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c,
	0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x1a, 0x1b, 0x67, 0x6f,
	0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x65, 0x6d,
	0x70, 0x74, 0x79, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xad, 0x05, 0x0a, 0x05, 0x56, 0x61,
	0x6c, 0x75, 0x65, 0x12, 0x2c, 0x0a, 0x04, 0x75, 0x6e, 0x69, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x0b, 0x32, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x48, 0x00, 0x52, 0x04, 0x75, 0x6e, 0x69,
	0x74, 0x12, 0x14, 0x0a, 0x04, 0x62, 0x6f, 0x6f, 0x6c, 0x18, 0x02, 0x20, 0x01, 0x28, 0x08, 0x48,
	0x00, 0x52, 0x04, 0x62, 0x6f, 0x6f, 0x6c, 0x12, 0x1a, 0x0a, 0x05, 0x69, 0x6e, 0x74, 0x36, 0x34,
	0x18, 0x03, 0x20, 0x01, 0x28, 0x12, 0x42, 0x02, 0x30, 0x01, 0x48, 0x00, 0x52, 0x05, 0x69, 0x6e,
	0x74, 0x36, 0x34, 0x12, 0x14, 0x0a, 0x04, 0x64, 0x61, 0x74, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28,
	0x05, 0x48, 0x00, 0x52, 0x04, 0x64, 0x61, 0x74, 0x65, 0x12, 0x22, 0x0a, 0x09, 0x74, 0x69, 0x6d,
	0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x18, 0x05, 0x20, 0x01, 0x28, 0x10, 0x42, 0x02, 0x30, 0x01,
	0x48, 0x00, 0x52, 0x09, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x12, 0x1a, 0x0a,
	0x07, 0x6e, 0x75, 0x6d, 0x65, 0x72, 0x69, 0x63, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00,
	0x52, 0x07, 0x6e, 0x75, 0x6d, 0x65, 0x72, 0x69, 0x63, 0x12, 0x16, 0x0a, 0x05, 0x70, 0x61, 0x72,
	0x74, 0x79, 0x18, 0x07, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52, 0x05, 0x70, 0x61, 0x72, 0x74,
	0x79, 0x12, 0x14, 0x0a, 0x04, 0x74, 0x65, 0x78, 0x74, 0x18, 0x08, 0x20, 0x01, 0x28, 0x09, 0x48,
	0x00, 0x52, 0x04, 0x74, 0x65, 0x78, 0x74, 0x12, 0x21, 0x0a, 0x0b, 0x63, 0x6f, 0x6e, 0x74, 0x72,
	0x61, 0x63, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x09, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52, 0x0a,
	0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x49, 0x64, 0x12, 0x3e, 0x0a, 0x08, 0x6f, 0x70,
	0x74, 0x69, 0x6f, 0x6e, 0x61, 0x6c, 0x18, 0x0a, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x20, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61,
	0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x4f, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x61, 0x6c, 0x48, 0x00,
	0x52, 0x08, 0x6f, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x61, 0x6c, 0x12, 0x32, 0x0a, 0x04, 0x6c, 0x69,
	0x73, 0x74, 0x18, 0x0b, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1c, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76,
	0x32, 0x2e, 0x4c, 0x69, 0x73, 0x74, 0x48, 0x00, 0x52, 0x04, 0x6c, 0x69, 0x73, 0x74, 0x12, 0x3c,
	0x0a, 0x08, 0x74, 0x65, 0x78, 0x74, 0x5f, 0x6d, 0x61, 0x70, 0x18, 0x0c, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x1f, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x54, 0x65, 0x78, 0x74, 0x4d, 0x61,
	0x70, 0x48, 0x00, 0x52, 0x07, 0x74, 0x65, 0x78, 0x74, 0x4d, 0x61, 0x70, 0x12, 0x39, 0x0a, 0x07,
	0x67, 0x65, 0x6e, 0x5f, 0x6d, 0x61, 0x70, 0x18, 0x0d, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1e, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e,
	0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x47, 0x65, 0x6e, 0x4d, 0x61, 0x70, 0x48, 0x00, 0x52,
	0x06, 0x67, 0x65, 0x6e, 0x4d, 0x61, 0x70, 0x12, 0x38, 0x0a, 0x06, 0x72, 0x65, 0x63, 0x6f, 0x72,
	0x64, 0x18, 0x0e, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1e, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61,
	0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32,
	0x2e, 0x52, 0x65, 0x63, 0x6f, 0x72, 0x64, 0x48, 0x00, 0x52, 0x06, 0x72, 0x65, 0x63, 0x6f, 0x72,
	0x64, 0x12, 0x3b, 0x0a, 0x07, 0x76, 0x61, 0x72, 0x69, 0x61, 0x6e, 0x74, 0x18, 0x0f, 0x20, 0x01,
	0x28, 0x0b, 0x32, 0x1f, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65,
	0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x56, 0x61, 0x72, 0x69,
	0x61, 0x6e, 0x74, 0x48, 0x00, 0x52, 0x07, 0x76, 0x61, 0x72, 0x69, 0x61, 0x6e, 0x74, 0x12, 0x32,
	0x0a, 0x04, 0x65, 0x6e, 0x75, 0x6d, 0x18, 0x10, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1c, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61,
	0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x45, 0x6e, 0x75, 0x6d, 0x48, 0x00, 0x52, 0x04, 0x65, 0x6e,
	0x75, 0x6d, 0x42, 0x05, 0x0a, 0x03, 0x73, 0x75, 0x6d, 0x22, 0x86, 0x01, 0x0a, 0x06, 0x52, 0x65,
	0x63, 0x6f, 0x72, 0x64, 0x12, 0x3f, 0x0a, 0x09, 0x72, 0x65, 0x63, 0x6f, 0x72, 0x64, 0x5f, 0x69,
	0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x22, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61,
	0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32,
	0x2e, 0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x66, 0x69, 0x65, 0x72, 0x52, 0x08, 0x72, 0x65, 0x63,
	0x6f, 0x72, 0x64, 0x49, 0x64, 0x12, 0x3b, 0x0a, 0x06, 0x66, 0x69, 0x65, 0x6c, 0x64, 0x73, 0x18,
	0x02, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x23, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c,
	0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x52,
	0x65, 0x63, 0x6f, 0x72, 0x64, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x52, 0x06, 0x66, 0x69, 0x65, 0x6c,
	0x64, 0x73, 0x22, 0x58, 0x0a, 0x0b, 0x52, 0x65, 0x63, 0x6f, 0x72, 0x64, 0x46, 0x69, 0x65, 0x6c,
	0x64, 0x12, 0x14, 0x0a, 0x05, 0x6c, 0x61, 0x62, 0x65, 0x6c, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x05, 0x6c, 0x61, 0x62, 0x65, 0x6c, 0x12, 0x33, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1d, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d,
	0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e,
	0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x22, 0x6d, 0x0a, 0x0a,
	0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x66, 0x69, 0x65, 0x72, 0x12, 0x1d, 0x0a, 0x0a, 0x70, 0x61,
	0x63, 0x6b, 0x61, 0x67, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09,
	0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x49, 0x64, 0x12, 0x1f, 0x0a, 0x0b, 0x6d, 0x6f, 0x64,
	0x75, 0x6c, 0x65, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a,
	0x6d, 0x6f, 0x64, 0x75, 0x6c, 0x65, 0x4e, 0x61, 0x6d, 0x65, 0x12, 0x1f, 0x0a, 0x0b, 0x65, 0x6e,
	0x74, 0x69, 0x74, 0x79, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x0a, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x4e, 0x61, 0x6d, 0x65, 0x22, 0xa3, 0x01, 0x0a, 0x07,
	0x56, 0x61, 0x72, 0x69, 0x61, 0x6e, 0x74, 0x12, 0x41, 0x0a, 0x0a, 0x76, 0x61, 0x72, 0x69, 0x61,
	0x6e, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x22, 0x2e, 0x63, 0x6f,
	0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70,
	0x69, 0x2e, 0x76, 0x32, 0x2e, 0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x66, 0x69, 0x65, 0x72, 0x52,
	0x09, 0x76, 0x61, 0x72, 0x69, 0x61, 0x6e, 0x74, 0x49, 0x64, 0x12, 0x20, 0x0a, 0x0b, 0x63, 0x6f,
	0x6e, 0x73, 0x74, 0x72, 0x75, 0x63, 0x74, 0x6f, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x0b, 0x63, 0x6f, 0x6e, 0x73, 0x74, 0x72, 0x75, 0x63, 0x74, 0x6f, 0x72, 0x12, 0x33, 0x0a, 0x05,
	0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1d, 0x2e, 0x63, 0x6f,
	0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70,
	0x69, 0x2e, 0x76, 0x32, 0x2e, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75,
	0x65, 0x22, 0x65, 0x0a, 0x04, 0x45, 0x6e, 0x75, 0x6d, 0x12, 0x3b, 0x0a, 0x07, 0x65, 0x6e, 0x75,
	0x6d, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x22, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x76, 0x32, 0x2e, 0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x66, 0x69, 0x65, 0x72, 0x52, 0x06,
	0x65, 0x6e, 0x75, 0x6d, 0x49, 0x64, 0x12, 0x20, 0x0a, 0x0b, 0x63, 0x6f, 0x6e, 0x73, 0x74, 0x72,
	0x75, 0x63, 0x74, 0x6f, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x63, 0x6f, 0x6e,
	0x73, 0x74, 0x72, 0x75, 0x63, 0x74, 0x6f, 0x72, 0x22, 0x41, 0x0a, 0x04, 0x4c, 0x69, 0x73, 0x74,
	0x12, 0x39, 0x0a, 0x08, 0x65, 0x6c, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x73, 0x18, 0x01, 0x20, 0x03,
	0x28, 0x0b, 0x32, 0x1d, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65,
	0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x56, 0x61, 0x6c, 0x75,
	0x65, 0x52, 0x08, 0x65, 0x6c, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x73, 0x22, 0x3f, 0x0a, 0x08, 0x4f,
	0x70, 0x74, 0x69, 0x6f, 0x6e, 0x61, 0x6c, 0x12, 0x33, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1d, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d,
	0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e,
	0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x22, 0x9a, 0x01, 0x0a,
	0x07, 0x54, 0x65, 0x78, 0x74, 0x4d, 0x61, 0x70, 0x12, 0x3f, 0x0a, 0x07, 0x65, 0x6e, 0x74, 0x72,
	0x69, 0x65, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x25, 0x2e, 0x63, 0x6f, 0x6d, 0x2e,
	0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e,
	0x76, 0x32, 0x2e, 0x54, 0x65, 0x78, 0x74, 0x4d, 0x61, 0x70, 0x2e, 0x45, 0x6e, 0x74, 0x72, 0x79,
	0x52, 0x07, 0x65, 0x6e, 0x74, 0x72, 0x69, 0x65, 0x73, 0x1a, 0x4e, 0x0a, 0x05, 0x45, 0x6e, 0x74,
	0x72, 0x79, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x03, 0x6b, 0x65, 0x79, 0x12, 0x33, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x1d, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c,
	0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x56, 0x61, 0x6c,
	0x75, 0x65, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x22, 0xb7, 0x01, 0x0a, 0x06, 0x47, 0x65,
	0x6e, 0x4d, 0x61, 0x70, 0x12, 0x3e, 0x0a, 0x07, 0x65, 0x6e, 0x74, 0x72, 0x69, 0x65, 0x73, 0x18,
	0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x24, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c,
	0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x47,
	0x65, 0x6e, 0x4d, 0x61, 0x70, 0x2e, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x52, 0x07, 0x65, 0x6e, 0x74,
	0x72, 0x69, 0x65, 0x73, 0x1a, 0x6d, 0x0a, 0x05, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x12, 0x2f, 0x0a,
	0x03, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1d, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x76, 0x32, 0x2e, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x12, 0x33,
	0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1d, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e,
	0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x05, 0x76, 0x61,
	0x6c, 0x75, 0x65, 0x42, 0x89, 0x01, 0x0a, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c,
	0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x42, 0x0f,
	0x56, 0x61, 0x6c, 0x75, 0x65, 0x4f, 0x75, 0x74, 0x65, 0x72, 0x43, 0x6c, 0x61, 0x73, 0x73, 0x5a,
	0x45, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69,
	0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63,
	0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f,
	0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f,
	0x61, 0x70, 0x69, 0x2f, 0x76, 0x32, 0xaa, 0x02, 0x16, 0x43, 0x6f, 0x6d, 0x2e, 0x44, 0x61, 0x6d,
	0x6c, 0x2e, 0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x41, 0x70, 0x69, 0x2e, 0x56, 0x32, 0x62,
	0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_daml_ledger_api_v2_value_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v2_value_proto_rawDescData = file_com_daml_ledger_api_v2_value_proto_rawDesc
)

func file_com_daml_ledger_api_v2_value_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v2_value_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v2_value_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_ledger_api_v2_value_proto_rawDescData)
	})
	return file_com_daml_ledger_api_v2_value_proto_rawDescData
}

var file_com_daml_ledger_api_v2_value_proto_msgTypes = make([]protoimpl.MessageInfo, 12)
var file_com_daml_ledger_api_v2_value_proto_goTypes = []any{
	(*Value)(nil),         // 0: com.daml.ledger.api.v2.Value
	(*Record)(nil),        // 1: com.daml.ledger.api.v2.Record
	(*RecordField)(nil),   // 2: com.daml.ledger.api.v2.RecordField
	(*Identifier)(nil),    // 3: com.daml.ledger.api.v2.Identifier
	(*Variant)(nil),       // 4: com.daml.ledger.api.v2.Variant
	(*Enum)(nil),          // 5: com.daml.ledger.api.v2.Enum
	(*List)(nil),          // 6: com.daml.ledger.api.v2.List
	(*Optional)(nil),      // 7: com.daml.ledger.api.v2.Optional
	(*TextMap)(nil),       // 8: com.daml.ledger.api.v2.TextMap
	(*GenMap)(nil),        // 9: com.daml.ledger.api.v2.GenMap
	(*TextMap_Entry)(nil), // 10: com.daml.ledger.api.v2.TextMap.Entry
	(*GenMap_Entry)(nil),  // 11: com.daml.ledger.api.v2.GenMap.Entry
	(*emptypb.Empty)(nil), // 12: google.protobuf.Empty
}
var file_com_daml_ledger_api_v2_value_proto_depIdxs = []int32{
	12, // 0: com.daml.ledger.api.v2.Value.unit:type_name -> google.protobuf.Empty
	7,  // 1: com.daml.ledger.api.v2.Value.optional:type_name -> com.daml.ledger.api.v2.Optional
	6,  // 2: com.daml.ledger.api.v2.Value.list:type_name -> com.daml.ledger.api.v2.List
	8,  // 3: com.daml.ledger.api.v2.Value.text_map:type_name -> com.daml.ledger.api.v2.TextMap
	9,  // 4: com.daml.ledger.api.v2.Value.gen_map:type_name -> com.daml.ledger.api.v2.GenMap
	1,  // 5: com.daml.ledger.api.v2.Value.record:type_name -> com.daml.ledger.api.v2.Record
	4,  // 6: com.daml.ledger.api.v2.Value.variant:type_name -> com.daml.ledger.api.v2.Variant
	5,  // 7: com.daml.ledger.api.v2.Value.enum:type_name -> com.daml.ledger.api.v2.Enum
	3,  // 8: com.daml.ledger.api.v2.Record.record_id:type_name -> com.daml.ledger.api.v2.Identifier
	2,  // 9: com.daml.ledger.api.v2.Record.fields:type_name -> com.daml.ledger.api.v2.RecordField
	0,  // 10: com.daml.ledger.api.v2.RecordField.value:type_name -> com.daml.ledger.api.v2.Value
	3,  // 11: com.daml.ledger.api.v2.Variant.variant_id:type_name -> com.daml.ledger.api.v2.Identifier
	0,  // 12: com.daml.ledger.api.v2.Variant.value:type_name -> com.daml.ledger.api.v2.Value
	3,  // 13: com.daml.ledger.api.v2.Enum.enum_id:type_name -> com.daml.ledger.api.v2.Identifier
	0,  // 14: com.daml.ledger.api.v2.List.elements:type_name -> com.daml.ledger.api.v2.Value
	0,  // 15: com.daml.ledger.api.v2.Optional.value:type_name -> com.daml.ledger.api.v2.Value
	10, // 16: com.daml.ledger.api.v2.TextMap.entries:type_name -> com.daml.ledger.api.v2.TextMap.Entry
	11, // 17: com.daml.ledger.api.v2.GenMap.entries:type_name -> com.daml.ledger.api.v2.GenMap.Entry
	0,  // 18: com.daml.ledger.api.v2.TextMap.Entry.value:type_name -> com.daml.ledger.api.v2.Value
	0,  // 19: com.daml.ledger.api.v2.GenMap.Entry.key:type_name -> com.daml.ledger.api.v2.Value
	0,  // 20: com.daml.ledger.api.v2.GenMap.Entry.value:type_name -> com.daml.ledger.api.v2.Value
	21, // [21:21] is the sub-list for method output_type
	21, // [21:21] is the sub-list for method input_type
	21, // [21:21] is the sub-list for extension type_name
	21, // [21:21] is the sub-list for extension extendee
	0,  // [0:21] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v2_value_proto_init() }
func file_com_daml_ledger_api_v2_value_proto_init() {
	if File_com_daml_ledger_api_v2_value_proto != nil {
		return
	}
	file_com_daml_ledger_api_v2_value_proto_msgTypes[0].OneofWrappers = []any{
		(*Value_Unit)(nil),
		(*Value_Bool)(nil),
		(*Value_Int64)(nil),
		(*Value_Date)(nil),
		(*Value_Timestamp)(nil),
		(*Value_Numeric)(nil),
		(*Value_Party)(nil),
		(*Value_Text)(nil),
		(*Value_ContractId)(nil),
		(*Value_Optional)(nil),
		(*Value_List)(nil),
		(*Value_TextMap)(nil),
		(*Value_GenMap)(nil),
		(*Value_Record)(nil),
		(*Value_Variant)(nil),
		(*Value_Enum)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_daml_ledger_api_v2_value_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   12,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_daml_ledger_api_v2_value_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v2_value_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v2_value_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v2_value_proto = out.File
	file_com_daml_ledger_api_v2_value_proto_rawDesc = nil
	file_com_daml_ledger_api_v2_value_proto_goTypes = nil
	file_com_daml_ledger_api_v2_value_proto_depIdxs = nil
}
