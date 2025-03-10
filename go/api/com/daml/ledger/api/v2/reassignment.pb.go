// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/daml/ledger/api/v2/reassignment.proto

package v2

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

type Reassignment struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	UpdateId   string `protobuf:"bytes,1,opt,name=update_id,json=updateId,proto3" json:"update_id,omitempty"`
	CommandId  string `protobuf:"bytes,2,opt,name=command_id,json=commandId,proto3" json:"command_id,omitempty"`
	WorkflowId string `protobuf:"bytes,3,opt,name=workflow_id,json=workflowId,proto3" json:"workflow_id,omitempty"`
	Offset     int64  `protobuf:"varint,4,opt,name=offset,proto3" json:"offset,omitempty"`
	// Types that are assignable to Event:
	//
	//	*Reassignment_UnassignedEvent
	//	*Reassignment_AssignedEvent
	Event        isReassignment_Event   `protobuf_oneof:"event"`
	TraceContext *TraceContext          `protobuf:"bytes,7,opt,name=trace_context,json=traceContext,proto3" json:"trace_context,omitempty"`
	RecordTime   *timestamppb.Timestamp `protobuf:"bytes,8,opt,name=record_time,json=recordTime,proto3" json:"record_time,omitempty"`
}

func (x *Reassignment) Reset() {
	*x = Reassignment{}
	mi := &file_com_daml_ledger_api_v2_reassignment_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Reassignment) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Reassignment) ProtoMessage() {}

func (x *Reassignment) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_reassignment_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Reassignment.ProtoReflect.Descriptor instead.
func (*Reassignment) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_reassignment_proto_rawDescGZIP(), []int{0}
}

func (x *Reassignment) GetUpdateId() string {
	if x != nil {
		return x.UpdateId
	}
	return ""
}

func (x *Reassignment) GetCommandId() string {
	if x != nil {
		return x.CommandId
	}
	return ""
}

func (x *Reassignment) GetWorkflowId() string {
	if x != nil {
		return x.WorkflowId
	}
	return ""
}

func (x *Reassignment) GetOffset() int64 {
	if x != nil {
		return x.Offset
	}
	return 0
}

func (m *Reassignment) GetEvent() isReassignment_Event {
	if m != nil {
		return m.Event
	}
	return nil
}

func (x *Reassignment) GetUnassignedEvent() *UnassignedEvent {
	if x, ok := x.GetEvent().(*Reassignment_UnassignedEvent); ok {
		return x.UnassignedEvent
	}
	return nil
}

func (x *Reassignment) GetAssignedEvent() *AssignedEvent {
	if x, ok := x.GetEvent().(*Reassignment_AssignedEvent); ok {
		return x.AssignedEvent
	}
	return nil
}

func (x *Reassignment) GetTraceContext() *TraceContext {
	if x != nil {
		return x.TraceContext
	}
	return nil
}

func (x *Reassignment) GetRecordTime() *timestamppb.Timestamp {
	if x != nil {
		return x.RecordTime
	}
	return nil
}

type isReassignment_Event interface {
	isReassignment_Event()
}

type Reassignment_UnassignedEvent struct {
	UnassignedEvent *UnassignedEvent `protobuf:"bytes,5,opt,name=unassigned_event,json=unassignedEvent,proto3,oneof"`
}

type Reassignment_AssignedEvent struct {
	AssignedEvent *AssignedEvent `protobuf:"bytes,6,opt,name=assigned_event,json=assignedEvent,proto3,oneof"`
}

func (*Reassignment_UnassignedEvent) isReassignment_Event() {}

func (*Reassignment_AssignedEvent) isReassignment_Event() {}

type UnassignedEvent struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	UnassignId            string                 `protobuf:"bytes,1,opt,name=unassign_id,json=unassignId,proto3" json:"unassign_id,omitempty"`
	ContractId            string                 `protobuf:"bytes,2,opt,name=contract_id,json=contractId,proto3" json:"contract_id,omitempty"`
	TemplateId            *Identifier            `protobuf:"bytes,3,opt,name=template_id,json=templateId,proto3" json:"template_id,omitempty"`
	Source                string                 `protobuf:"bytes,4,opt,name=source,proto3" json:"source,omitempty"`
	Target                string                 `protobuf:"bytes,5,opt,name=target,proto3" json:"target,omitempty"`
	Submitter             string                 `protobuf:"bytes,6,opt,name=submitter,proto3" json:"submitter,omitempty"`
	ReassignmentCounter   uint64                 `protobuf:"varint,7,opt,name=reassignment_counter,json=reassignmentCounter,proto3" json:"reassignment_counter,omitempty"`
	AssignmentExclusivity *timestamppb.Timestamp `protobuf:"bytes,8,opt,name=assignment_exclusivity,json=assignmentExclusivity,proto3" json:"assignment_exclusivity,omitempty"`
	WitnessParties        []string               `protobuf:"bytes,9,rep,name=witness_parties,json=witnessParties,proto3" json:"witness_parties,omitempty"`
	PackageName           string                 `protobuf:"bytes,10,opt,name=package_name,json=packageName,proto3" json:"package_name,omitempty"`
}

func (x *UnassignedEvent) Reset() {
	*x = UnassignedEvent{}
	mi := &file_com_daml_ledger_api_v2_reassignment_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *UnassignedEvent) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UnassignedEvent) ProtoMessage() {}

func (x *UnassignedEvent) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_reassignment_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UnassignedEvent.ProtoReflect.Descriptor instead.
func (*UnassignedEvent) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_reassignment_proto_rawDescGZIP(), []int{1}
}

func (x *UnassignedEvent) GetUnassignId() string {
	if x != nil {
		return x.UnassignId
	}
	return ""
}

func (x *UnassignedEvent) GetContractId() string {
	if x != nil {
		return x.ContractId
	}
	return ""
}

func (x *UnassignedEvent) GetTemplateId() *Identifier {
	if x != nil {
		return x.TemplateId
	}
	return nil
}

func (x *UnassignedEvent) GetSource() string {
	if x != nil {
		return x.Source
	}
	return ""
}

func (x *UnassignedEvent) GetTarget() string {
	if x != nil {
		return x.Target
	}
	return ""
}

func (x *UnassignedEvent) GetSubmitter() string {
	if x != nil {
		return x.Submitter
	}
	return ""
}

func (x *UnassignedEvent) GetReassignmentCounter() uint64 {
	if x != nil {
		return x.ReassignmentCounter
	}
	return 0
}

func (x *UnassignedEvent) GetAssignmentExclusivity() *timestamppb.Timestamp {
	if x != nil {
		return x.AssignmentExclusivity
	}
	return nil
}

func (x *UnassignedEvent) GetWitnessParties() []string {
	if x != nil {
		return x.WitnessParties
	}
	return nil
}

func (x *UnassignedEvent) GetPackageName() string {
	if x != nil {
		return x.PackageName
	}
	return ""
}

type AssignedEvent struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Source              string        `protobuf:"bytes,1,opt,name=source,proto3" json:"source,omitempty"`
	Target              string        `protobuf:"bytes,2,opt,name=target,proto3" json:"target,omitempty"`
	UnassignId          string        `protobuf:"bytes,3,opt,name=unassign_id,json=unassignId,proto3" json:"unassign_id,omitempty"`
	Submitter           string        `protobuf:"bytes,4,opt,name=submitter,proto3" json:"submitter,omitempty"`
	ReassignmentCounter uint64        `protobuf:"varint,5,opt,name=reassignment_counter,json=reassignmentCounter,proto3" json:"reassignment_counter,omitempty"`
	CreatedEvent        *CreatedEvent `protobuf:"bytes,6,opt,name=created_event,json=createdEvent,proto3" json:"created_event,omitempty"`
}

func (x *AssignedEvent) Reset() {
	*x = AssignedEvent{}
	mi := &file_com_daml_ledger_api_v2_reassignment_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *AssignedEvent) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*AssignedEvent) ProtoMessage() {}

func (x *AssignedEvent) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_reassignment_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use AssignedEvent.ProtoReflect.Descriptor instead.
func (*AssignedEvent) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_reassignment_proto_rawDescGZIP(), []int{2}
}

func (x *AssignedEvent) GetSource() string {
	if x != nil {
		return x.Source
	}
	return ""
}

func (x *AssignedEvent) GetTarget() string {
	if x != nil {
		return x.Target
	}
	return ""
}

func (x *AssignedEvent) GetUnassignId() string {
	if x != nil {
		return x.UnassignId
	}
	return ""
}

func (x *AssignedEvent) GetSubmitter() string {
	if x != nil {
		return x.Submitter
	}
	return ""
}

func (x *AssignedEvent) GetReassignmentCounter() uint64 {
	if x != nil {
		return x.ReassignmentCounter
	}
	return 0
}

func (x *AssignedEvent) GetCreatedEvent() *CreatedEvent {
	if x != nil {
		return x.CreatedEvent
	}
	return nil
}

var File_com_daml_ledger_api_v2_reassignment_proto protoreflect.FileDescriptor

var file_com_daml_ledger_api_v2_reassignment_proto_rawDesc = []byte{
	0x0a, 0x29, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x32, 0x2f, 0x72, 0x65, 0x61, 0x73, 0x73, 0x69, 0x67,
	0x6e, 0x6d, 0x65, 0x6e, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x16, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x76, 0x32, 0x1a, 0x22, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65,
	0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x32, 0x2f, 0x65, 0x76, 0x65, 0x6e,
	0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x2a, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d,
	0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x32, 0x2f,
	0x74, 0x72, 0x61, 0x63, 0x65, 0x5f, 0x63, 0x6f, 0x6e, 0x74, 0x65, 0x78, 0x74, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x1a, 0x22, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65,
	0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x32, 0x2f, 0x76, 0x61, 0x6c, 0x75,
	0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61,
	0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xba, 0x03, 0x0a, 0x0c, 0x52, 0x65, 0x61,
	0x73, 0x73, 0x69, 0x67, 0x6e, 0x6d, 0x65, 0x6e, 0x74, 0x12, 0x1b, 0x0a, 0x09, 0x75, 0x70, 0x64,
	0x61, 0x74, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x75, 0x70,
	0x64, 0x61, 0x74, 0x65, 0x49, 0x64, 0x12, 0x1d, 0x0a, 0x0a, 0x63, 0x6f, 0x6d, 0x6d, 0x61, 0x6e,
	0x64, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x63, 0x6f, 0x6d, 0x6d,
	0x61, 0x6e, 0x64, 0x49, 0x64, 0x12, 0x1f, 0x0a, 0x0b, 0x77, 0x6f, 0x72, 0x6b, 0x66, 0x6c, 0x6f,
	0x77, 0x5f, 0x69, 0x64, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x77, 0x6f, 0x72, 0x6b,
	0x66, 0x6c, 0x6f, 0x77, 0x49, 0x64, 0x12, 0x16, 0x0a, 0x06, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74,
	0x18, 0x04, 0x20, 0x01, 0x28, 0x03, 0x52, 0x06, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x12, 0x54,
	0x0a, 0x10, 0x75, 0x6e, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x65, 0x64, 0x5f, 0x65, 0x76, 0x65,
	0x6e, 0x74, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x27, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76,
	0x32, 0x2e, 0x55, 0x6e, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x65, 0x64, 0x45, 0x76, 0x65, 0x6e,
	0x74, 0x48, 0x00, 0x52, 0x0f, 0x75, 0x6e, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x65, 0x64, 0x45,
	0x76, 0x65, 0x6e, 0x74, 0x12, 0x4e, 0x0a, 0x0e, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x65, 0x64,
	0x5f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x18, 0x06, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x25, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61,
	0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x41, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x65, 0x64, 0x45, 0x76,
	0x65, 0x6e, 0x74, 0x48, 0x00, 0x52, 0x0d, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x65, 0x64, 0x45,
	0x76, 0x65, 0x6e, 0x74, 0x12, 0x49, 0x0a, 0x0d, 0x74, 0x72, 0x61, 0x63, 0x65, 0x5f, 0x63, 0x6f,
	0x6e, 0x74, 0x65, 0x78, 0x74, 0x18, 0x07, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x24, 0x2e, 0x63, 0x6f,
	0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70,
	0x69, 0x2e, 0x76, 0x32, 0x2e, 0x54, 0x72, 0x61, 0x63, 0x65, 0x43, 0x6f, 0x6e, 0x74, 0x65, 0x78,
	0x74, 0x52, 0x0c, 0x74, 0x72, 0x61, 0x63, 0x65, 0x43, 0x6f, 0x6e, 0x74, 0x65, 0x78, 0x74, 0x12,
	0x3b, 0x0a, 0x0b, 0x72, 0x65, 0x63, 0x6f, 0x72, 0x64, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x18, 0x08,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70,
	0x52, 0x0a, 0x72, 0x65, 0x63, 0x6f, 0x72, 0x64, 0x54, 0x69, 0x6d, 0x65, 0x42, 0x07, 0x0a, 0x05,
	0x65, 0x76, 0x65, 0x6e, 0x74, 0x22, 0xb8, 0x03, 0x0a, 0x0f, 0x55, 0x6e, 0x61, 0x73, 0x73, 0x69,
	0x67, 0x6e, 0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x12, 0x1f, 0x0a, 0x0b, 0x75, 0x6e, 0x61,
	0x73, 0x73, 0x69, 0x67, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a,
	0x75, 0x6e, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x49, 0x64, 0x12, 0x1f, 0x0a, 0x0b, 0x63, 0x6f,
	0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x0a, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x49, 0x64, 0x12, 0x43, 0x0a, 0x0b, 0x74,
	0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x22, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x2e, 0x49, 0x64, 0x65, 0x6e, 0x74, 0x69,
	0x66, 0x69, 0x65, 0x72, 0x52, 0x0a, 0x74, 0x65, 0x6d, 0x70, 0x6c, 0x61, 0x74, 0x65, 0x49, 0x64,
	0x12, 0x16, 0x0a, 0x06, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x06, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x12, 0x16, 0x0a, 0x06, 0x74, 0x61, 0x72, 0x67,
	0x65, 0x74, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x74, 0x61, 0x72, 0x67, 0x65, 0x74,
	0x12, 0x1c, 0x0a, 0x09, 0x73, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x74, 0x65, 0x72, 0x18, 0x06, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x09, 0x73, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x74, 0x65, 0x72, 0x12, 0x31,
	0x0a, 0x14, 0x72, 0x65, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x6d, 0x65, 0x6e, 0x74, 0x5f, 0x63,
	0x6f, 0x75, 0x6e, 0x74, 0x65, 0x72, 0x18, 0x07, 0x20, 0x01, 0x28, 0x04, 0x52, 0x13, 0x72, 0x65,
	0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x6d, 0x65, 0x6e, 0x74, 0x43, 0x6f, 0x75, 0x6e, 0x74, 0x65,
	0x72, 0x12, 0x51, 0x0a, 0x16, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x6d, 0x65, 0x6e, 0x74, 0x5f,
	0x65, 0x78, 0x63, 0x6c, 0x75, 0x73, 0x69, 0x76, 0x69, 0x74, 0x79, 0x18, 0x08, 0x20, 0x01, 0x28,
	0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x15, 0x61,
	0x73, 0x73, 0x69, 0x67, 0x6e, 0x6d, 0x65, 0x6e, 0x74, 0x45, 0x78, 0x63, 0x6c, 0x75, 0x73, 0x69,
	0x76, 0x69, 0x74, 0x79, 0x12, 0x27, 0x0a, 0x0f, 0x77, 0x69, 0x74, 0x6e, 0x65, 0x73, 0x73, 0x5f,
	0x70, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x18, 0x09, 0x20, 0x03, 0x28, 0x09, 0x52, 0x0e, 0x77,
	0x69, 0x74, 0x6e, 0x65, 0x73, 0x73, 0x50, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x12, 0x21, 0x0a,
	0x0c, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x0a, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x0b, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x4e, 0x61, 0x6d, 0x65,
	0x22, 0xfc, 0x01, 0x0a, 0x0d, 0x41, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x65, 0x64, 0x45, 0x76, 0x65,
	0x6e, 0x74, 0x12, 0x16, 0x0a, 0x06, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x06, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x12, 0x16, 0x0a, 0x06, 0x74, 0x61,
	0x72, 0x67, 0x65, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x74, 0x61, 0x72, 0x67,
	0x65, 0x74, 0x12, 0x1f, 0x0a, 0x0b, 0x75, 0x6e, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x5f, 0x69,
	0x64, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x75, 0x6e, 0x61, 0x73, 0x73, 0x69, 0x67,
	0x6e, 0x49, 0x64, 0x12, 0x1c, 0x0a, 0x09, 0x73, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x74, 0x65, 0x72,
	0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x73, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x74, 0x65,
	0x72, 0x12, 0x31, 0x0a, 0x14, 0x72, 0x65, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x6d, 0x65, 0x6e,
	0x74, 0x5f, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x65, 0x72, 0x18, 0x05, 0x20, 0x01, 0x28, 0x04, 0x52,
	0x13, 0x72, 0x65, 0x61, 0x73, 0x73, 0x69, 0x67, 0x6e, 0x6d, 0x65, 0x6e, 0x74, 0x43, 0x6f, 0x75,
	0x6e, 0x74, 0x65, 0x72, 0x12, 0x49, 0x0a, 0x0d, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x5f,
	0x65, 0x76, 0x65, 0x6e, 0x74, 0x18, 0x06, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x24, 0x2e, 0x63, 0x6f,
	0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70,
	0x69, 0x2e, 0x76, 0x32, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x45, 0x76, 0x65, 0x6e,
	0x74, 0x52, 0x0c, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x42,
	0x90, 0x01, 0x0a, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64,
	0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x32, 0x42, 0x16, 0x52, 0x65, 0x61, 0x73,
	0x73, 0x69, 0x67, 0x6e, 0x6d, 0x65, 0x6e, 0x74, 0x4f, 0x75, 0x74, 0x65, 0x72, 0x43, 0x6c, 0x61,
	0x73, 0x73, 0x5a, 0x45, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64,
	0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a,
	0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61,
	0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x32, 0xaa, 0x02, 0x16, 0x43, 0x6f, 0x6d, 0x2e,
	0x44, 0x61, 0x6d, 0x6c, 0x2e, 0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x41, 0x70, 0x69, 0x2e,
	0x56, 0x32, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_daml_ledger_api_v2_reassignment_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v2_reassignment_proto_rawDescData = file_com_daml_ledger_api_v2_reassignment_proto_rawDesc
)

func file_com_daml_ledger_api_v2_reassignment_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v2_reassignment_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v2_reassignment_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_ledger_api_v2_reassignment_proto_rawDescData)
	})
	return file_com_daml_ledger_api_v2_reassignment_proto_rawDescData
}

var file_com_daml_ledger_api_v2_reassignment_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_com_daml_ledger_api_v2_reassignment_proto_goTypes = []any{
	(*Reassignment)(nil),          // 0: com.daml.ledger.api.v2.Reassignment
	(*UnassignedEvent)(nil),       // 1: com.daml.ledger.api.v2.UnassignedEvent
	(*AssignedEvent)(nil),         // 2: com.daml.ledger.api.v2.AssignedEvent
	(*TraceContext)(nil),          // 3: com.daml.ledger.api.v2.TraceContext
	(*timestamppb.Timestamp)(nil), // 4: google.protobuf.Timestamp
	(*Identifier)(nil),            // 5: com.daml.ledger.api.v2.Identifier
	(*CreatedEvent)(nil),          // 6: com.daml.ledger.api.v2.CreatedEvent
}
var file_com_daml_ledger_api_v2_reassignment_proto_depIdxs = []int32{
	1, // 0: com.daml.ledger.api.v2.Reassignment.unassigned_event:type_name -> com.daml.ledger.api.v2.UnassignedEvent
	2, // 1: com.daml.ledger.api.v2.Reassignment.assigned_event:type_name -> com.daml.ledger.api.v2.AssignedEvent
	3, // 2: com.daml.ledger.api.v2.Reassignment.trace_context:type_name -> com.daml.ledger.api.v2.TraceContext
	4, // 3: com.daml.ledger.api.v2.Reassignment.record_time:type_name -> google.protobuf.Timestamp
	5, // 4: com.daml.ledger.api.v2.UnassignedEvent.template_id:type_name -> com.daml.ledger.api.v2.Identifier
	4, // 5: com.daml.ledger.api.v2.UnassignedEvent.assignment_exclusivity:type_name -> google.protobuf.Timestamp
	6, // 6: com.daml.ledger.api.v2.AssignedEvent.created_event:type_name -> com.daml.ledger.api.v2.CreatedEvent
	7, // [7:7] is the sub-list for method output_type
	7, // [7:7] is the sub-list for method input_type
	7, // [7:7] is the sub-list for extension type_name
	7, // [7:7] is the sub-list for extension extendee
	0, // [0:7] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v2_reassignment_proto_init() }
func file_com_daml_ledger_api_v2_reassignment_proto_init() {
	if File_com_daml_ledger_api_v2_reassignment_proto != nil {
		return
	}
	file_com_daml_ledger_api_v2_event_proto_init()
	file_com_daml_ledger_api_v2_trace_context_proto_init()
	file_com_daml_ledger_api_v2_value_proto_init()
	file_com_daml_ledger_api_v2_reassignment_proto_msgTypes[0].OneofWrappers = []any{
		(*Reassignment_UnassignedEvent)(nil),
		(*Reassignment_AssignedEvent)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_daml_ledger_api_v2_reassignment_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_daml_ledger_api_v2_reassignment_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v2_reassignment_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v2_reassignment_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v2_reassignment_proto = out.File
	file_com_daml_ledger_api_v2_reassignment_proto_rawDesc = nil
	file_com_daml_ledger_api_v2_reassignment_proto_goTypes = nil
	file_com_daml_ledger_api_v2_reassignment_proto_depIdxs = nil
}
