// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/daml/ledger/api/v2/event.proto

package v2

import (
	status "google.golang.org/genproto/googleapis/rpc/status"
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

type Event struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Event:
	//
	//	*Event_Created
	//	*Event_Archived
	Event isEvent_Event `protobuf_oneof:"event"`
}

func (x *Event) Reset() {
	*x = Event{}
	mi := &file_com_daml_ledger_api_v2_event_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Event) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Event) ProtoMessage() {}

func (x *Event) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_event_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Event.ProtoReflect.Descriptor instead.
func (*Event) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_event_proto_rawDescGZIP(), []int{0}
}

func (m *Event) GetEvent() isEvent_Event {
	if m != nil {
		return m.Event
	}
	return nil
}

func (x *Event) GetCreated() *CreatedEvent {
	if x, ok := x.GetEvent().(*Event_Created); ok {
		return x.Created
	}
	return nil
}

func (x *Event) GetArchived() *ArchivedEvent {
	if x, ok := x.GetEvent().(*Event_Archived); ok {
		return x.Archived
	}
	return nil
}

type isEvent_Event interface {
	isEvent_Event()
}

type Event_Created struct {
	Created *CreatedEvent `protobuf:"bytes,1,opt,name=created,proto3,oneof"`
}

type Event_Archived struct {
	Archived *ArchivedEvent `protobuf:"bytes,2,opt,name=archived,proto3,oneof"`
}

func (*Event_Created) isEvent_Event() {}

func (*Event_Archived) isEvent_Event() {}

type CreatedEvent struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	EventId          string                 `protobuf:"bytes,1,opt,name=event_id,json=eventId,proto3" json:"event_id,omitempty"`
	ContractId       string                 `protobuf:"bytes,2,opt,name=contract_id,json=contractId,proto3" json:"contract_id,omitempty"`
	TemplateId       *Identifier            `protobuf:"bytes,3,opt,name=template_id,json=templateId,proto3" json:"template_id,omitempty"`
	ContractKey      *Value                 `protobuf:"bytes,4,opt,name=contract_key,json=contractKey,proto3" json:"contract_key,omitempty"`
	CreateArguments  *Record                `protobuf:"bytes,5,opt,name=create_arguments,json=createArguments,proto3" json:"create_arguments,omitempty"`
	CreatedEventBlob []byte                 `protobuf:"bytes,6,opt,name=created_event_blob,json=createdEventBlob,proto3" json:"created_event_blob,omitempty"`
	InterfaceViews   []*InterfaceView       `protobuf:"bytes,7,rep,name=interface_views,json=interfaceViews,proto3" json:"interface_views,omitempty"`
	WitnessParties   []string               `protobuf:"bytes,8,rep,name=witness_parties,json=witnessParties,proto3" json:"witness_parties,omitempty"`
	Signatories      []string               `protobuf:"bytes,9,rep,name=signatories,proto3" json:"signatories,omitempty"`
	Observers        []string               `protobuf:"bytes,10,rep,name=observers,proto3" json:"observers,omitempty"`
	CreatedAt        *timestamppb.Timestamp `protobuf:"bytes,11,opt,name=created_at,json=createdAt,proto3" json:"created_at,omitempty"`
	PackageName      string                 `protobuf:"bytes,12,opt,name=package_name,json=packageName,proto3" json:"package_name,omitempty"`
}

func (x *CreatedEvent) Reset() {
	*x = CreatedEvent{}
	mi := &file_com_daml_ledger_api_v2_event_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CreatedEvent) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CreatedEvent) ProtoMessage() {}

func (x *CreatedEvent) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_event_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CreatedEvent.ProtoReflect.Descriptor instead.
func (*CreatedEvent) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_event_proto_rawDescGZIP(), []int{1}
}

func (x *CreatedEvent) GetEventId() string {
	if x != nil {
		return x.EventId
	}
	return ""
}

func (x *CreatedEvent) GetContractId() string {
	if x != nil {
		return x.ContractId
	}
	return ""
}

func (x *CreatedEvent) GetTemplateId() *Identifier {
	if x != nil {
		return x.TemplateId
	}
	return nil
}

func (x *CreatedEvent) GetContractKey() *Value {
	if x != nil {
		return x.ContractKey
	}
	return nil
}

func (x *CreatedEvent) GetCreateArguments() *Record {
	if x != nil {
		return x.CreateArguments
	}
	return nil
}

func (x *CreatedEvent) GetCreatedEventBlob() []byte {
	if x != nil {
		return x.CreatedEventBlob
	}
	return nil
}

func (x *CreatedEvent) GetInterfaceViews() []*InterfaceView {
	if x != nil {
		return x.InterfaceViews
	}
	return nil
}

func (x *CreatedEvent) GetWitnessParties() []string {
	if x != nil {
		return x.WitnessParties
	}
	return nil
}

func (x *CreatedEvent) GetSignatories() []string {
	if x != nil {
		return x.Signatories
	}
	return nil
}

func (x *CreatedEvent) GetObservers() []string {
	if x != nil {
		return x.Observers
	}
	return nil
}

func (x *CreatedEvent) GetCreatedAt() *timestamppb.Timestamp {
	if x != nil {
		return x.CreatedAt
	}
	return nil
}

func (x *CreatedEvent) GetPackageName() string {
	if x != nil {
		return x.PackageName
	}
	return ""
}

type InterfaceView struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	InterfaceId *Identifier    `protobuf:"bytes,1,opt,name=interface_id,json=interfaceId,proto3" json:"interface_id,omitempty"`
	ViewStatus  *status.Status `protobuf:"bytes,2,opt,name=view_status,json=viewStatus,proto3" json:"view_status,omitempty"`
	ViewValue   *Record        `protobuf:"bytes,3,opt,name=view_value,json=viewValue,proto3" json:"view_value,omitempty"`
}

func (x *InterfaceView) Reset() {
	*x = InterfaceView{}
	mi := &file_com_daml_ledger_api_v2_event_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *InterfaceView) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*InterfaceView) ProtoMessage() {}

func (x *InterfaceView) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_event_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use InterfaceView.ProtoReflect.Descriptor instead.
func (*InterfaceView) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_event_proto_rawDescGZIP(), []int{2}
}

func (x *InterfaceView) GetInterfaceId() *Identifier {
	if x != nil {
		return x.InterfaceId
	}
	return nil
}

func (x *InterfaceView) GetViewStatus() *status.Status {
	if x != nil {
		return x.ViewStatus
	}
	return nil
}

func (x *InterfaceView) GetViewValue() *Record {
	if x != nil {
		return x.ViewValue
	}
	return nil
}

type ArchivedEvent struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	EventId        string      `protobuf:"bytes,1,opt,name=event_id,json=eventId,proto3" json:"event_id,omitempty"`
	ContractId     string      `protobuf:"bytes,2,opt,name=contract_id,json=contractId,proto3" json:"contract_id,omitempty"`
	TemplateId     *Identifier `protobuf:"bytes,3,opt,name=template_id,json=templateId,proto3" json:"template_id,omitempty"`
	WitnessParties []string    `protobuf:"bytes,4,rep,name=witness_parties,json=witnessParties,proto3" json:"witness_parties,omitempty"`
	PackageName    string      `protobuf:"bytes,5,opt,name=package_name,json=packageName,proto3" json:"package_name,omitempty"`
}

func (x *ArchivedEvent) Reset() {
	*x = ArchivedEvent{}
	mi := &file_com_daml_ledger_api_v2_event_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ArchivedEvent) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ArchivedEvent) ProtoMessage() {}

func (x *ArchivedEvent) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_event_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ArchivedEvent.ProtoReflect.Descriptor instead.
func (*ArchivedEvent) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_event_proto_rawDescGZIP(), []int{3}
}

func (x *ArchivedEvent) GetEventId() string {
	if x != nil {
		return x.EventId
	}
	return ""
}

func (x *ArchivedEvent) GetContractId() string {
	if x != nil {
		return x.ContractId
	}
	return ""
}

func (x *ArchivedEvent) GetTemplateId() *Identifier {
	if x != nil {
		return x.TemplateId
	}
	return nil
}

func (x *ArchivedEvent) GetWitnessParties() []string {
	if x != nil {
		return x.WitnessParties
	}
	return nil
}

func (x *ArchivedEvent) GetPackageName() string {
	if x != nil {
		return x.PackageName
	}
	return ""
}

type ExercisedEvent struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	EventId        string      `protobuf:"bytes,1,opt,name=event_id,json=eventId,proto3" json:"event_id,omitempty"`
	ContractId     string      `protobuf:"bytes,2,opt,name=contract_id,json=contractId,proto3" json:"contract_id,omitempty"`
	TemplateId     *Identifier `protobuf:"bytes,3,opt,name=template_id,json=templateId,proto3" json:"template_id,omitempty"`
	InterfaceId    *Identifier `protobuf:"bytes,4,opt,name=interface_id,json=interfaceId,proto3" json:"interface_id,omitempty"`
	Choice         string      `protobuf:"bytes,5,opt,name=choice,proto3" json:"choice,omitempty"`
	ChoiceArgument *Value      `protobuf:"bytes,6,opt,name=choice_argument,json=choiceArgument,proto3" json:"choice_argument,omitempty"`
	ActingParties  []string    `protobuf:"bytes,7,rep,name=acting_parties,json=actingParties,proto3" json:"acting_parties,omitempty"`
	Consuming      bool        `protobuf:"varint,8,opt,name=consuming,proto3" json:"consuming,omitempty"`
	WitnessParties []string    `protobuf:"bytes,9,rep,name=witness_parties,json=witnessParties,proto3" json:"witness_parties,omitempty"`
	ChildEventIds  []string    `protobuf:"bytes,10,rep,name=child_event_ids,json=childEventIds,proto3" json:"child_event_ids,omitempty"`
	ExerciseResult *Value      `protobuf:"bytes,11,opt,name=exercise_result,json=exerciseResult,proto3" json:"exercise_result,omitempty"`
	PackageName    string      `protobuf:"bytes,12,opt,name=package_name,json=packageName,proto3" json:"package_name,omitempty"`
}

func (x *ExercisedEvent) Reset() {
	*x = ExercisedEvent{}
	mi := &file_com_daml_ledger_api_v2_event_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ExercisedEvent) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ExercisedEvent) ProtoMessage() {}

func (x *ExercisedEvent) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_event_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ExercisedEvent.ProtoReflect.Descriptor instead.
func (*ExercisedEvent) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_event_proto_rawDescGZIP(), []int{4}
}

func (x *ExercisedEvent) GetEventId() string {
	if x != nil {
		return x.EventId
	}
	return ""
}

func (x *ExercisedEvent) GetContractId() string {
	if x != nil {
		return x.ContractId
	}
	return ""
}

func (x *ExercisedEvent) GetTemplateId() *Identifier {
	if x != nil {
		return x.TemplateId
	}
	return nil
}

func (x *ExercisedEvent) GetInterfaceId() *Identifier {
	if x != nil {
		return x.InterfaceId
	}
	return nil
}

func (x *ExercisedEvent) GetChoice() string {
	if x != nil {
		return x.Choice
	}
	return ""
}

func (x *ExercisedEvent) GetChoiceArgument() *Value {
	if x != nil {
		return x.ChoiceArgument
	}
	return nil
}

func (x *ExercisedEvent) GetActingParties() []string {
	if x != nil {
		return x.ActingParties
	}
	return nil
}

func (x *ExercisedEvent) GetConsuming() bool {
	if x != nil {
		return x.Consuming
	}
	return false
}

func (x *ExercisedEvent) GetWitnessParties() []string {
	if x != nil {
		return x.WitnessParties
	}
	return nil
}

func (x *ExercisedEvent) GetChildEventIds() []string {
	if x != nil {
		return x.ChildEventIds
	}
	return nil
}

func (x *ExercisedEvent) GetExerciseResult() *Value {
	if x != nil {
		return x.ExerciseResult
	}
	return nil
}

func (x *ExercisedEvent) GetPackageName() string {
	if x != nil {
		return x.PackageName
	}
	return ""
}

var File_com_daml_ledger_api_v2_event_proto protoreflect.FileDescriptor

var file_com_daml_ledger_api_v2_event_proto_rawDesc = []byte{
	0x0a, 0x22, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x32, 0x2f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x12, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c,
	0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x1a, 0x22, 0x63, 0x6f,
	0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70,
	0x69, 0x2f, 0x76, 0x32, 0x2f, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75,
	0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x1a, 0x17, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x72, 0x70, 0x63, 0x2f, 0x73, 0x74,
	0x61, 0x74, 0x75, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x97, 0x01, 0x0a, 0x05, 0x45,
	0x76, 0x65, 0x6e, 0x74, 0x12, 0x40, 0x0a, 0x07, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x24, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c,
	0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x43,
	0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x48, 0x00, 0x52, 0x07, 0x63,
	0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x12, 0x43, 0x0a, 0x08, 0x61, 0x72, 0x63, 0x68, 0x69, 0x76,
	0x65, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x25, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76,
	0x32, 0x2e, 0x41, 0x72, 0x63, 0x68, 0x69, 0x76, 0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x48,
	0x00, 0x52, 0x08, 0x61, 0x72, 0x63, 0x68, 0x69, 0x76, 0x65, 0x64, 0x42, 0x07, 0x0a, 0x05, 0x65,
	0x76, 0x65, 0x6e, 0x74, 0x22, 0xe1, 0x04, 0x0a, 0x0c, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64,
	0x45, 0x76, 0x65, 0x6e, 0x74, 0x12, 0x19, 0x0a, 0x08, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x5f, 0x69,
	0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x49, 0x64,
	0x12, 0x1f, 0x0a, 0x0b, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x5f, 0x69, 0x64, 0x18,
	0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x49,
	0x64, 0x12, 0x43, 0x0a, 0x0b, 0x74, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x5f, 0x69, 0x64,
	0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x22, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d,
	0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e,
	0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x66, 0x69, 0x65, 0x72, 0x52, 0x0a, 0x74, 0x65, 0x6d, 0x70,
	0x6c, 0x61, 0x74, 0x65, 0x49, 0x64, 0x12, 0x40, 0x0a, 0x0c, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61,
	0x63, 0x74, 0x5f, 0x6b, 0x65, 0x79, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1d, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61,
	0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x0b, 0x63, 0x6f, 0x6e,
	0x74, 0x72, 0x61, 0x63, 0x74, 0x4b, 0x65, 0x79, 0x12, 0x49, 0x0a, 0x10, 0x63, 0x72, 0x65, 0x61,
	0x74, 0x65, 0x5f, 0x61, 0x72, 0x67, 0x75, 0x6d, 0x65, 0x6e, 0x74, 0x73, 0x18, 0x05, 0x20, 0x01,
	0x28, 0x0b, 0x32, 0x1e, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65,
	0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x52, 0x65, 0x63, 0x6f,
	0x72, 0x64, 0x52, 0x0f, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x41, 0x72, 0x67, 0x75, 0x6d, 0x65,
	0x6e, 0x74, 0x73, 0x12, 0x2c, 0x0a, 0x12, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x5f, 0x65,
	0x76, 0x65, 0x6e, 0x74, 0x5f, 0x62, 0x6c, 0x6f, 0x62, 0x18, 0x06, 0x20, 0x01, 0x28, 0x0c, 0x52,
	0x10, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x42, 0x6c, 0x6f,
	0x62, 0x12, 0x4e, 0x0a, 0x0f, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x5f, 0x76,
	0x69, 0x65, 0x77, 0x73, 0x18, 0x07, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x25, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x76, 0x32, 0x2e, 0x49, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x56, 0x69, 0x65,
	0x77, 0x52, 0x0e, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x56, 0x69, 0x65, 0x77,
	0x73, 0x12, 0x27, 0x0a, 0x0f, 0x77, 0x69, 0x74, 0x6e, 0x65, 0x73, 0x73, 0x5f, 0x70, 0x61, 0x72,
	0x74, 0x69, 0x65, 0x73, 0x18, 0x08, 0x20, 0x03, 0x28, 0x09, 0x52, 0x0e, 0x77, 0x69, 0x74, 0x6e,
	0x65, 0x73, 0x73, 0x50, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x12, 0x20, 0x0a, 0x0b, 0x73, 0x69,
	0x67, 0x6e, 0x61, 0x74, 0x6f, 0x72, 0x69, 0x65, 0x73, 0x18, 0x09, 0x20, 0x03, 0x28, 0x09, 0x52,
	0x0b, 0x73, 0x69, 0x67, 0x6e, 0x61, 0x74, 0x6f, 0x72, 0x69, 0x65, 0x73, 0x12, 0x1c, 0x0a, 0x09,
	0x6f, 0x62, 0x73, 0x65, 0x72, 0x76, 0x65, 0x72, 0x73, 0x18, 0x0a, 0x20, 0x03, 0x28, 0x09, 0x52,
	0x09, 0x6f, 0x62, 0x73, 0x65, 0x72, 0x76, 0x65, 0x72, 0x73, 0x12, 0x39, 0x0a, 0x0a, 0x63, 0x72,
	0x65, 0x61, 0x74, 0x65, 0x64, 0x5f, 0x61, 0x74, 0x18, 0x0b, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a,
	0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66,
	0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x09, 0x63, 0x72, 0x65, 0x61,
	0x74, 0x65, 0x64, 0x41, 0x74, 0x12, 0x21, 0x0a, 0x0c, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65,
	0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x0c, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x70, 0x61, 0x63,
	0x6b, 0x61, 0x67, 0x65, 0x4e, 0x61, 0x6d, 0x65, 0x22, 0xca, 0x01, 0x0a, 0x0d, 0x49, 0x6e, 0x74,
	0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x56, 0x69, 0x65, 0x77, 0x12, 0x45, 0x0a, 0x0c, 0x69, 0x6e,
	0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x22, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x49, 0x64, 0x65, 0x6e, 0x74, 0x69,
	0x66, 0x69, 0x65, 0x72, 0x52, 0x0b, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x49,
	0x64, 0x12, 0x33, 0x0a, 0x0b, 0x76, 0x69, 0x65, 0x77, 0x5f, 0x73, 0x74, 0x61, 0x74, 0x75, 0x73,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x12, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e,
	0x72, 0x70, 0x63, 0x2e, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x52, 0x0a, 0x76, 0x69, 0x65, 0x77,
	0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x12, 0x3d, 0x0a, 0x0a, 0x76, 0x69, 0x65, 0x77, 0x5f, 0x76,
	0x61, 0x6c, 0x75, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1e, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x76, 0x32, 0x2e, 0x52, 0x65, 0x63, 0x6f, 0x72, 0x64, 0x52, 0x09, 0x76, 0x69, 0x65, 0x77,
	0x56, 0x61, 0x6c, 0x75, 0x65, 0x22, 0xdc, 0x01, 0x0a, 0x0d, 0x41, 0x72, 0x63, 0x68, 0x69, 0x76,
	0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x12, 0x19, 0x0a, 0x08, 0x65, 0x76, 0x65, 0x6e, 0x74,
	0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x65, 0x76, 0x65, 0x6e, 0x74,
	0x49, 0x64, 0x12, 0x1f, 0x0a, 0x0b, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x5f, 0x69,
	0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63,
	0x74, 0x49, 0x64, 0x12, 0x43, 0x0a, 0x0b, 0x74, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x5f,
	0x69, 0x64, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x22, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76,
	0x32, 0x2e, 0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x66, 0x69, 0x65, 0x72, 0x52, 0x0a, 0x74, 0x65,
	0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x49, 0x64, 0x12, 0x27, 0x0a, 0x0f, 0x77, 0x69, 0x74, 0x6e,
	0x65, 0x73, 0x73, 0x5f, 0x70, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x18, 0x04, 0x20, 0x03, 0x28,
	0x09, 0x52, 0x0e, 0x77, 0x69, 0x74, 0x6e, 0x65, 0x73, 0x73, 0x50, 0x61, 0x72, 0x74, 0x69, 0x65,
	0x73, 0x12, 0x21, 0x0a, 0x0c, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x5f, 0x6e, 0x61, 0x6d,
	0x65, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65,
	0x4e, 0x61, 0x6d, 0x65, 0x22, 0xb9, 0x04, 0x0a, 0x0e, 0x45, 0x78, 0x65, 0x72, 0x63, 0x69, 0x73,
	0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x12, 0x19, 0x0a, 0x08, 0x65, 0x76, 0x65, 0x6e, 0x74,
	0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x65, 0x76, 0x65, 0x6e, 0x74,
	0x49, 0x64, 0x12, 0x1f, 0x0a, 0x0b, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x5f, 0x69,
	0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63,
	0x74, 0x49, 0x64, 0x12, 0x43, 0x0a, 0x0b, 0x74, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x5f,
	0x69, 0x64, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x22, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76,
	0x32, 0x2e, 0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x66, 0x69, 0x65, 0x72, 0x52, 0x0a, 0x74, 0x65,
	0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x49, 0x64, 0x12, 0x45, 0x0a, 0x0c, 0x69, 0x6e, 0x74, 0x65,
	0x72, 0x66, 0x61, 0x63, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x22,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x49, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x66, 0x69,
	0x65, 0x72, 0x52, 0x0b, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x49, 0x64, 0x12,
	0x16, 0x0a, 0x06, 0x63, 0x68, 0x6f, 0x69, 0x63, 0x65, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x06, 0x63, 0x68, 0x6f, 0x69, 0x63, 0x65, 0x12, 0x46, 0x0a, 0x0f, 0x63, 0x68, 0x6f, 0x69, 0x63,
	0x65, 0x5f, 0x61, 0x72, 0x67, 0x75, 0x6d, 0x65, 0x6e, 0x74, 0x18, 0x06, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x1d, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x52,
	0x0e, 0x63, 0x68, 0x6f, 0x69, 0x63, 0x65, 0x41, 0x72, 0x67, 0x75, 0x6d, 0x65, 0x6e, 0x74, 0x12,
	0x25, 0x0a, 0x0e, 0x61, 0x63, 0x74, 0x69, 0x6e, 0x67, 0x5f, 0x70, 0x61, 0x72, 0x74, 0x69, 0x65,
	0x73, 0x18, 0x07, 0x20, 0x03, 0x28, 0x09, 0x52, 0x0d, 0x61, 0x63, 0x74, 0x69, 0x6e, 0x67, 0x50,
	0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x12, 0x1c, 0x0a, 0x09, 0x63, 0x6f, 0x6e, 0x73, 0x75, 0x6d,
	0x69, 0x6e, 0x67, 0x18, 0x08, 0x20, 0x01, 0x28, 0x08, 0x52, 0x09, 0x63, 0x6f, 0x6e, 0x73, 0x75,
	0x6d, 0x69, 0x6e, 0x67, 0x12, 0x27, 0x0a, 0x0f, 0x77, 0x69, 0x74, 0x6e, 0x65, 0x73, 0x73, 0x5f,
	0x70, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x18, 0x09, 0x20, 0x03, 0x28, 0x09, 0x52, 0x0e, 0x77,
	0x69, 0x74, 0x6e, 0x65, 0x73, 0x73, 0x50, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x12, 0x26, 0x0a,
	0x0f, 0x63, 0x68, 0x69, 0x6c, 0x64, 0x5f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x5f, 0x69, 0x64, 0x73,
	0x18, 0x0a, 0x20, 0x03, 0x28, 0x09, 0x52, 0x0d, 0x63, 0x68, 0x69, 0x6c, 0x64, 0x45, 0x76, 0x65,
	0x6e, 0x74, 0x49, 0x64, 0x73, 0x12, 0x46, 0x0a, 0x0f, 0x65, 0x78, 0x65, 0x72, 0x63, 0x69, 0x73,
	0x65, 0x5f, 0x72, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x18, 0x0b, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1d,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x0e, 0x65,
	0x78, 0x65, 0x72, 0x63, 0x69, 0x73, 0x65, 0x52, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x12, 0x21, 0x0a,
	0x0c, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x0c, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x0b, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x4e, 0x61, 0x6d, 0x65,
	0x42, 0x89, 0x01, 0x0a, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65,
	0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x42, 0x0f, 0x45, 0x76, 0x65,
	0x6e, 0x74, 0x4f, 0x75, 0x74, 0x65, 0x72, 0x43, 0x6c, 0x61, 0x73, 0x73, 0x5a, 0x45, 0x67, 0x69,
	0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c,
	0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65,
	0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d,
	0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69,
	0x2f, 0x76, 0x32, 0xaa, 0x02, 0x16, 0x43, 0x6f, 0x6d, 0x2e, 0x44, 0x61, 0x6d, 0x6c, 0x2e, 0x4c,
	0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x41, 0x70, 0x69, 0x2e, 0x56, 0x32, 0x62, 0x06, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_daml_ledger_api_v2_event_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v2_event_proto_rawDescData = file_com_daml_ledger_api_v2_event_proto_rawDesc
)

func file_com_daml_ledger_api_v2_event_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v2_event_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v2_event_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_ledger_api_v2_event_proto_rawDescData)
	})
	return file_com_daml_ledger_api_v2_event_proto_rawDescData
}

var file_com_daml_ledger_api_v2_event_proto_msgTypes = make([]protoimpl.MessageInfo, 5)
var file_com_daml_ledger_api_v2_event_proto_goTypes = []any{
	(*Event)(nil),                 // 0: com.daml.ledger.api.v2.Event
	(*CreatedEvent)(nil),          // 1: com.daml.ledger.api.v2.CreatedEvent
	(*InterfaceView)(nil),         // 2: com.daml.ledger.api.v2.InterfaceView
	(*ArchivedEvent)(nil),         // 3: com.daml.ledger.api.v2.ArchivedEvent
	(*ExercisedEvent)(nil),        // 4: com.daml.ledger.api.v2.ExercisedEvent
	(*Identifier)(nil),            // 5: com.daml.ledger.api.v2.Identifier
	(*Value)(nil),                 // 6: com.daml.ledger.api.v2.Value
	(*Record)(nil),                // 7: com.daml.ledger.api.v2.Record
	(*timestamppb.Timestamp)(nil), // 8: google.protobuf.Timestamp
	(*status.Status)(nil),         // 9: google.rpc.Status
}
var file_com_daml_ledger_api_v2_event_proto_depIdxs = []int32{
	1,  // 0: com.daml.ledger.api.v2.Event.created:type_name -> com.daml.ledger.api.v2.CreatedEvent
	3,  // 1: com.daml.ledger.api.v2.Event.archived:type_name -> com.daml.ledger.api.v2.ArchivedEvent
	5,  // 2: com.daml.ledger.api.v2.CreatedEvent.template_id:type_name -> com.daml.ledger.api.v2.Identifier
	6,  // 3: com.daml.ledger.api.v2.CreatedEvent.contract_key:type_name -> com.daml.ledger.api.v2.Value
	7,  // 4: com.daml.ledger.api.v2.CreatedEvent.create_arguments:type_name -> com.daml.ledger.api.v2.Record
	2,  // 5: com.daml.ledger.api.v2.CreatedEvent.interface_views:type_name -> com.daml.ledger.api.v2.InterfaceView
	8,  // 6: com.daml.ledger.api.v2.CreatedEvent.created_at:type_name -> google.protobuf.Timestamp
	5,  // 7: com.daml.ledger.api.v2.InterfaceView.interface_id:type_name -> com.daml.ledger.api.v2.Identifier
	9,  // 8: com.daml.ledger.api.v2.InterfaceView.view_status:type_name -> google.rpc.Status
	7,  // 9: com.daml.ledger.api.v2.InterfaceView.view_value:type_name -> com.daml.ledger.api.v2.Record
	5,  // 10: com.daml.ledger.api.v2.ArchivedEvent.template_id:type_name -> com.daml.ledger.api.v2.Identifier
	5,  // 11: com.daml.ledger.api.v2.ExercisedEvent.template_id:type_name -> com.daml.ledger.api.v2.Identifier
	5,  // 12: com.daml.ledger.api.v2.ExercisedEvent.interface_id:type_name -> com.daml.ledger.api.v2.Identifier
	6,  // 13: com.daml.ledger.api.v2.ExercisedEvent.choice_argument:type_name -> com.daml.ledger.api.v2.Value
	6,  // 14: com.daml.ledger.api.v2.ExercisedEvent.exercise_result:type_name -> com.daml.ledger.api.v2.Value
	15, // [15:15] is the sub-list for method output_type
	15, // [15:15] is the sub-list for method input_type
	15, // [15:15] is the sub-list for extension type_name
	15, // [15:15] is the sub-list for extension extendee
	0,  // [0:15] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v2_event_proto_init() }
func file_com_daml_ledger_api_v2_event_proto_init() {
	if File_com_daml_ledger_api_v2_event_proto != nil {
		return
	}
	file_com_daml_ledger_api_v2_value_proto_init()
	file_com_daml_ledger_api_v2_event_proto_msgTypes[0].OneofWrappers = []any{
		(*Event_Created)(nil),
		(*Event_Archived)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_daml_ledger_api_v2_event_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   5,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_daml_ledger_api_v2_event_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v2_event_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v2_event_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v2_event_proto = out.File
	file_com_daml_ledger_api_v2_event_proto_rawDesc = nil
	file_com_daml_ledger_api_v2_event_proto_goTypes = nil
	file_com_daml_ledger_api_v2_event_proto_depIdxs = nil
}
