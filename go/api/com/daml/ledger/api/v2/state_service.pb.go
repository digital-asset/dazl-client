// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/daml/ledger/api/v2/state_service.proto

package v2

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

type ParticipantPermission int32

const (
	ParticipantPermission_PARTICIPANT_PERMISSION_UNSPECIFIED  ParticipantPermission = 0
	ParticipantPermission_PARTICIPANT_PERMISSION_SUBMISSION   ParticipantPermission = 1
	ParticipantPermission_PARTICIPANT_PERMISSION_CONFIRMATION ParticipantPermission = 2
	ParticipantPermission_PARTICIPANT_PERMISSION_OBSERVATION  ParticipantPermission = 3
)

// Enum value maps for ParticipantPermission.
var (
	ParticipantPermission_name = map[int32]string{
		0: "PARTICIPANT_PERMISSION_UNSPECIFIED",
		1: "PARTICIPANT_PERMISSION_SUBMISSION",
		2: "PARTICIPANT_PERMISSION_CONFIRMATION",
		3: "PARTICIPANT_PERMISSION_OBSERVATION",
	}
	ParticipantPermission_value = map[string]int32{
		"PARTICIPANT_PERMISSION_UNSPECIFIED":  0,
		"PARTICIPANT_PERMISSION_SUBMISSION":   1,
		"PARTICIPANT_PERMISSION_CONFIRMATION": 2,
		"PARTICIPANT_PERMISSION_OBSERVATION":  3,
	}
)

func (x ParticipantPermission) Enum() *ParticipantPermission {
	p := new(ParticipantPermission)
	*p = x
	return p
}

func (x ParticipantPermission) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (ParticipantPermission) Descriptor() protoreflect.EnumDescriptor {
	return file_com_daml_ledger_api_v2_state_service_proto_enumTypes[0].Descriptor()
}

func (ParticipantPermission) Type() protoreflect.EnumType {
	return &file_com_daml_ledger_api_v2_state_service_proto_enumTypes[0]
}

func (x ParticipantPermission) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use ParticipantPermission.Descriptor instead.
func (ParticipantPermission) EnumDescriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_state_service_proto_rawDescGZIP(), []int{0}
}

type GetActiveContractsRequest struct {
	state          protoimpl.MessageState `protogen:"open.v1"`
	Filter         *TransactionFilter     `protobuf:"bytes,1,opt,name=filter,proto3" json:"filter,omitempty"`
	Verbose        bool                   `protobuf:"varint,2,opt,name=verbose,proto3" json:"verbose,omitempty"`
	ActiveAtOffset int64                  `protobuf:"varint,3,opt,name=active_at_offset,json=activeAtOffset,proto3" json:"active_at_offset,omitempty"`
	EventFormat    *EventFormat           `protobuf:"bytes,4,opt,name=event_format,json=eventFormat,proto3" json:"event_format,omitempty"`
	unknownFields  protoimpl.UnknownFields
	sizeCache      protoimpl.SizeCache
}

func (x *GetActiveContractsRequest) Reset() {
	*x = GetActiveContractsRequest{}
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetActiveContractsRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetActiveContractsRequest) ProtoMessage() {}

func (x *GetActiveContractsRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetActiveContractsRequest.ProtoReflect.Descriptor instead.
func (*GetActiveContractsRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_state_service_proto_rawDescGZIP(), []int{0}
}

func (x *GetActiveContractsRequest) GetFilter() *TransactionFilter {
	if x != nil {
		return x.Filter
	}
	return nil
}

func (x *GetActiveContractsRequest) GetVerbose() bool {
	if x != nil {
		return x.Verbose
	}
	return false
}

func (x *GetActiveContractsRequest) GetActiveAtOffset() int64 {
	if x != nil {
		return x.ActiveAtOffset
	}
	return 0
}

func (x *GetActiveContractsRequest) GetEventFormat() *EventFormat {
	if x != nil {
		return x.EventFormat
	}
	return nil
}

type GetActiveContractsResponse struct {
	state      protoimpl.MessageState `protogen:"open.v1"`
	WorkflowId string                 `protobuf:"bytes,1,opt,name=workflow_id,json=workflowId,proto3" json:"workflow_id,omitempty"`
	// Types that are valid to be assigned to ContractEntry:
	//
	//	*GetActiveContractsResponse_ActiveContract
	//	*GetActiveContractsResponse_IncompleteUnassigned
	//	*GetActiveContractsResponse_IncompleteAssigned
	ContractEntry isGetActiveContractsResponse_ContractEntry `protobuf_oneof:"contract_entry"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetActiveContractsResponse) Reset() {
	*x = GetActiveContractsResponse{}
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetActiveContractsResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetActiveContractsResponse) ProtoMessage() {}

func (x *GetActiveContractsResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetActiveContractsResponse.ProtoReflect.Descriptor instead.
func (*GetActiveContractsResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_state_service_proto_rawDescGZIP(), []int{1}
}

func (x *GetActiveContractsResponse) GetWorkflowId() string {
	if x != nil {
		return x.WorkflowId
	}
	return ""
}

func (x *GetActiveContractsResponse) GetContractEntry() isGetActiveContractsResponse_ContractEntry {
	if x != nil {
		return x.ContractEntry
	}
	return nil
}

func (x *GetActiveContractsResponse) GetActiveContract() *ActiveContract {
	if x != nil {
		if x, ok := x.ContractEntry.(*GetActiveContractsResponse_ActiveContract); ok {
			return x.ActiveContract
		}
	}
	return nil
}

func (x *GetActiveContractsResponse) GetIncompleteUnassigned() *IncompleteUnassigned {
	if x != nil {
		if x, ok := x.ContractEntry.(*GetActiveContractsResponse_IncompleteUnassigned); ok {
			return x.IncompleteUnassigned
		}
	}
	return nil
}

func (x *GetActiveContractsResponse) GetIncompleteAssigned() *IncompleteAssigned {
	if x != nil {
		if x, ok := x.ContractEntry.(*GetActiveContractsResponse_IncompleteAssigned); ok {
			return x.IncompleteAssigned
		}
	}
	return nil
}

type isGetActiveContractsResponse_ContractEntry interface {
	isGetActiveContractsResponse_ContractEntry()
}

type GetActiveContractsResponse_ActiveContract struct {
	ActiveContract *ActiveContract `protobuf:"bytes,2,opt,name=active_contract,json=activeContract,proto3,oneof"`
}

type GetActiveContractsResponse_IncompleteUnassigned struct {
	IncompleteUnassigned *IncompleteUnassigned `protobuf:"bytes,3,opt,name=incomplete_unassigned,json=incompleteUnassigned,proto3,oneof"`
}

type GetActiveContractsResponse_IncompleteAssigned struct {
	IncompleteAssigned *IncompleteAssigned `protobuf:"bytes,4,opt,name=incomplete_assigned,json=incompleteAssigned,proto3,oneof"`
}

func (*GetActiveContractsResponse_ActiveContract) isGetActiveContractsResponse_ContractEntry() {}

func (*GetActiveContractsResponse_IncompleteUnassigned) isGetActiveContractsResponse_ContractEntry() {
}

func (*GetActiveContractsResponse_IncompleteAssigned) isGetActiveContractsResponse_ContractEntry() {}

type ActiveContract struct {
	state               protoimpl.MessageState `protogen:"open.v1"`
	CreatedEvent        *CreatedEvent          `protobuf:"bytes,1,opt,name=created_event,json=createdEvent,proto3" json:"created_event,omitempty"`
	SynchronizerId      string                 `protobuf:"bytes,2,opt,name=synchronizer_id,json=synchronizerId,proto3" json:"synchronizer_id,omitempty"`
	ReassignmentCounter uint64                 `protobuf:"varint,3,opt,name=reassignment_counter,json=reassignmentCounter,proto3" json:"reassignment_counter,omitempty"`
	unknownFields       protoimpl.UnknownFields
	sizeCache           protoimpl.SizeCache
}

func (x *ActiveContract) Reset() {
	*x = ActiveContract{}
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ActiveContract) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ActiveContract) ProtoMessage() {}

func (x *ActiveContract) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ActiveContract.ProtoReflect.Descriptor instead.
func (*ActiveContract) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_state_service_proto_rawDescGZIP(), []int{2}
}

func (x *ActiveContract) GetCreatedEvent() *CreatedEvent {
	if x != nil {
		return x.CreatedEvent
	}
	return nil
}

func (x *ActiveContract) GetSynchronizerId() string {
	if x != nil {
		return x.SynchronizerId
	}
	return ""
}

func (x *ActiveContract) GetReassignmentCounter() uint64 {
	if x != nil {
		return x.ReassignmentCounter
	}
	return 0
}

type IncompleteUnassigned struct {
	state           protoimpl.MessageState `protogen:"open.v1"`
	CreatedEvent    *CreatedEvent          `protobuf:"bytes,1,opt,name=created_event,json=createdEvent,proto3" json:"created_event,omitempty"`
	UnassignedEvent *UnassignedEvent       `protobuf:"bytes,2,opt,name=unassigned_event,json=unassignedEvent,proto3" json:"unassigned_event,omitempty"`
	unknownFields   protoimpl.UnknownFields
	sizeCache       protoimpl.SizeCache
}

func (x *IncompleteUnassigned) Reset() {
	*x = IncompleteUnassigned{}
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *IncompleteUnassigned) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*IncompleteUnassigned) ProtoMessage() {}

func (x *IncompleteUnassigned) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use IncompleteUnassigned.ProtoReflect.Descriptor instead.
func (*IncompleteUnassigned) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_state_service_proto_rawDescGZIP(), []int{3}
}

func (x *IncompleteUnassigned) GetCreatedEvent() *CreatedEvent {
	if x != nil {
		return x.CreatedEvent
	}
	return nil
}

func (x *IncompleteUnassigned) GetUnassignedEvent() *UnassignedEvent {
	if x != nil {
		return x.UnassignedEvent
	}
	return nil
}

type IncompleteAssigned struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	AssignedEvent *AssignedEvent         `protobuf:"bytes,1,opt,name=assigned_event,json=assignedEvent,proto3" json:"assigned_event,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *IncompleteAssigned) Reset() {
	*x = IncompleteAssigned{}
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *IncompleteAssigned) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*IncompleteAssigned) ProtoMessage() {}

func (x *IncompleteAssigned) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use IncompleteAssigned.ProtoReflect.Descriptor instead.
func (*IncompleteAssigned) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_state_service_proto_rawDescGZIP(), []int{4}
}

func (x *IncompleteAssigned) GetAssignedEvent() *AssignedEvent {
	if x != nil {
		return x.AssignedEvent
	}
	return nil
}

type GetConnectedSynchronizersRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Party         string                 `protobuf:"bytes,1,opt,name=party,proto3" json:"party,omitempty"`
	ParticipantId string                 `protobuf:"bytes,2,opt,name=participant_id,json=participantId,proto3" json:"participant_id,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetConnectedSynchronizersRequest) Reset() {
	*x = GetConnectedSynchronizersRequest{}
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetConnectedSynchronizersRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetConnectedSynchronizersRequest) ProtoMessage() {}

func (x *GetConnectedSynchronizersRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[5]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetConnectedSynchronizersRequest.ProtoReflect.Descriptor instead.
func (*GetConnectedSynchronizersRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_state_service_proto_rawDescGZIP(), []int{5}
}

func (x *GetConnectedSynchronizersRequest) GetParty() string {
	if x != nil {
		return x.Party
	}
	return ""
}

func (x *GetConnectedSynchronizersRequest) GetParticipantId() string {
	if x != nil {
		return x.ParticipantId
	}
	return ""
}

type GetConnectedSynchronizersResponse struct {
	state                  protoimpl.MessageState                                     `protogen:"open.v1"`
	ConnectedSynchronizers []*GetConnectedSynchronizersResponse_ConnectedSynchronizer `protobuf:"bytes,1,rep,name=connected_synchronizers,json=connectedSynchronizers,proto3" json:"connected_synchronizers,omitempty"`
	unknownFields          protoimpl.UnknownFields
	sizeCache              protoimpl.SizeCache
}

func (x *GetConnectedSynchronizersResponse) Reset() {
	*x = GetConnectedSynchronizersResponse{}
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[6]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetConnectedSynchronizersResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetConnectedSynchronizersResponse) ProtoMessage() {}

func (x *GetConnectedSynchronizersResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[6]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetConnectedSynchronizersResponse.ProtoReflect.Descriptor instead.
func (*GetConnectedSynchronizersResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_state_service_proto_rawDescGZIP(), []int{6}
}

func (x *GetConnectedSynchronizersResponse) GetConnectedSynchronizers() []*GetConnectedSynchronizersResponse_ConnectedSynchronizer {
	if x != nil {
		return x.ConnectedSynchronizers
	}
	return nil
}

type GetLedgerEndRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetLedgerEndRequest) Reset() {
	*x = GetLedgerEndRequest{}
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[7]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetLedgerEndRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetLedgerEndRequest) ProtoMessage() {}

func (x *GetLedgerEndRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[7]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetLedgerEndRequest.ProtoReflect.Descriptor instead.
func (*GetLedgerEndRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_state_service_proto_rawDescGZIP(), []int{7}
}

type GetLedgerEndResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Offset        int64                  `protobuf:"varint,1,opt,name=offset,proto3" json:"offset,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetLedgerEndResponse) Reset() {
	*x = GetLedgerEndResponse{}
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[8]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetLedgerEndResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetLedgerEndResponse) ProtoMessage() {}

func (x *GetLedgerEndResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[8]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetLedgerEndResponse.ProtoReflect.Descriptor instead.
func (*GetLedgerEndResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_state_service_proto_rawDescGZIP(), []int{8}
}

func (x *GetLedgerEndResponse) GetOffset() int64 {
	if x != nil {
		return x.Offset
	}
	return 0
}

type GetLatestPrunedOffsetsRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetLatestPrunedOffsetsRequest) Reset() {
	*x = GetLatestPrunedOffsetsRequest{}
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[9]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetLatestPrunedOffsetsRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetLatestPrunedOffsetsRequest) ProtoMessage() {}

func (x *GetLatestPrunedOffsetsRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[9]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetLatestPrunedOffsetsRequest.ProtoReflect.Descriptor instead.
func (*GetLatestPrunedOffsetsRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_state_service_proto_rawDescGZIP(), []int{9}
}

type GetLatestPrunedOffsetsResponse struct {
	state                                   protoimpl.MessageState `protogen:"open.v1"`
	ParticipantPrunedUpToInclusive          int64                  `protobuf:"varint,1,opt,name=participant_pruned_up_to_inclusive,json=participantPrunedUpToInclusive,proto3" json:"participant_pruned_up_to_inclusive,omitempty"`
	AllDivulgedContractsPrunedUpToInclusive int64                  `protobuf:"varint,2,opt,name=all_divulged_contracts_pruned_up_to_inclusive,json=allDivulgedContractsPrunedUpToInclusive,proto3" json:"all_divulged_contracts_pruned_up_to_inclusive,omitempty"`
	unknownFields                           protoimpl.UnknownFields
	sizeCache                               protoimpl.SizeCache
}

func (x *GetLatestPrunedOffsetsResponse) Reset() {
	*x = GetLatestPrunedOffsetsResponse{}
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[10]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetLatestPrunedOffsetsResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetLatestPrunedOffsetsResponse) ProtoMessage() {}

func (x *GetLatestPrunedOffsetsResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[10]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetLatestPrunedOffsetsResponse.ProtoReflect.Descriptor instead.
func (*GetLatestPrunedOffsetsResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_state_service_proto_rawDescGZIP(), []int{10}
}

func (x *GetLatestPrunedOffsetsResponse) GetParticipantPrunedUpToInclusive() int64 {
	if x != nil {
		return x.ParticipantPrunedUpToInclusive
	}
	return 0
}

func (x *GetLatestPrunedOffsetsResponse) GetAllDivulgedContractsPrunedUpToInclusive() int64 {
	if x != nil {
		return x.AllDivulgedContractsPrunedUpToInclusive
	}
	return 0
}

type GetConnectedSynchronizersResponse_ConnectedSynchronizer struct {
	state             protoimpl.MessageState `protogen:"open.v1"`
	SynchronizerAlias string                 `protobuf:"bytes,1,opt,name=synchronizer_alias,json=synchronizerAlias,proto3" json:"synchronizer_alias,omitempty"`
	SynchronizerId    string                 `protobuf:"bytes,2,opt,name=synchronizer_id,json=synchronizerId,proto3" json:"synchronizer_id,omitempty"`
	Permission        ParticipantPermission  `protobuf:"varint,3,opt,name=permission,proto3,enum=com.daml.ledger.api.v2.ParticipantPermission" json:"permission,omitempty"`
	unknownFields     protoimpl.UnknownFields
	sizeCache         protoimpl.SizeCache
}

func (x *GetConnectedSynchronizersResponse_ConnectedSynchronizer) Reset() {
	*x = GetConnectedSynchronizersResponse_ConnectedSynchronizer{}
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[11]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetConnectedSynchronizersResponse_ConnectedSynchronizer) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetConnectedSynchronizersResponse_ConnectedSynchronizer) ProtoMessage() {}

func (x *GetConnectedSynchronizersResponse_ConnectedSynchronizer) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_state_service_proto_msgTypes[11]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetConnectedSynchronizersResponse_ConnectedSynchronizer.ProtoReflect.Descriptor instead.
func (*GetConnectedSynchronizersResponse_ConnectedSynchronizer) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_state_service_proto_rawDescGZIP(), []int{6, 0}
}

func (x *GetConnectedSynchronizersResponse_ConnectedSynchronizer) GetSynchronizerAlias() string {
	if x != nil {
		return x.SynchronizerAlias
	}
	return ""
}

func (x *GetConnectedSynchronizersResponse_ConnectedSynchronizer) GetSynchronizerId() string {
	if x != nil {
		return x.SynchronizerId
	}
	return ""
}

func (x *GetConnectedSynchronizersResponse_ConnectedSynchronizer) GetPermission() ParticipantPermission {
	if x != nil {
		return x.Permission
	}
	return ParticipantPermission_PARTICIPANT_PERMISSION_UNSPECIFIED
}

var File_com_daml_ledger_api_v2_state_service_proto protoreflect.FileDescriptor

const file_com_daml_ledger_api_v2_state_service_proto_rawDesc = "" +
	"\n" +
	"*com/daml/ledger/api/v2/state_service.proto\x12\x16com.daml.ledger.api.v2\x1a\"com/daml/ledger/api/v2/event.proto\x1a)com/daml/ledger/api/v2/reassignment.proto\x1a/com/daml/ledger/api/v2/transaction_filter.proto\"\xea\x01\n" +
	"\x19GetActiveContractsRequest\x12A\n" +
	"\x06filter\x18\x01 \x01(\v2).com.daml.ledger.api.v2.TransactionFilterR\x06filter\x12\x18\n" +
	"\averbose\x18\x02 \x01(\bR\averbose\x12(\n" +
	"\x10active_at_offset\x18\x03 \x01(\x03R\x0eactiveAtOffset\x12F\n" +
	"\fevent_format\x18\x04 \x01(\v2#.com.daml.ledger.api.v2.EventFormatR\veventFormat\"\xe6\x02\n" +
	"\x1aGetActiveContractsResponse\x12\x1f\n" +
	"\vworkflow_id\x18\x01 \x01(\tR\n" +
	"workflowId\x12Q\n" +
	"\x0factive_contract\x18\x02 \x01(\v2&.com.daml.ledger.api.v2.ActiveContractH\x00R\x0eactiveContract\x12c\n" +
	"\x15incomplete_unassigned\x18\x03 \x01(\v2,.com.daml.ledger.api.v2.IncompleteUnassignedH\x00R\x14incompleteUnassigned\x12]\n" +
	"\x13incomplete_assigned\x18\x04 \x01(\v2*.com.daml.ledger.api.v2.IncompleteAssignedH\x00R\x12incompleteAssignedB\x10\n" +
	"\x0econtract_entry\"\xb7\x01\n" +
	"\x0eActiveContract\x12I\n" +
	"\rcreated_event\x18\x01 \x01(\v2$.com.daml.ledger.api.v2.CreatedEventR\fcreatedEvent\x12'\n" +
	"\x0fsynchronizer_id\x18\x02 \x01(\tR\x0esynchronizerId\x121\n" +
	"\x14reassignment_counter\x18\x03 \x01(\x04R\x13reassignmentCounter\"\xb5\x01\n" +
	"\x14IncompleteUnassigned\x12I\n" +
	"\rcreated_event\x18\x01 \x01(\v2$.com.daml.ledger.api.v2.CreatedEventR\fcreatedEvent\x12R\n" +
	"\x10unassigned_event\x18\x02 \x01(\v2'.com.daml.ledger.api.v2.UnassignedEventR\x0funassignedEvent\"b\n" +
	"\x12IncompleteAssigned\x12L\n" +
	"\x0eassigned_event\x18\x01 \x01(\v2%.com.daml.ledger.api.v2.AssignedEventR\rassignedEvent\"_\n" +
	" GetConnectedSynchronizersRequest\x12\x14\n" +
	"\x05party\x18\x01 \x01(\tR\x05party\x12%\n" +
	"\x0eparticipant_id\x18\x02 \x01(\tR\rparticipantId\"\xef\x02\n" +
	"!GetConnectedSynchronizersResponse\x12\x88\x01\n" +
	"\x17connected_synchronizers\x18\x01 \x03(\v2O.com.daml.ledger.api.v2.GetConnectedSynchronizersResponse.ConnectedSynchronizerR\x16connectedSynchronizers\x1a\xbe\x01\n" +
	"\x15ConnectedSynchronizer\x12-\n" +
	"\x12synchronizer_alias\x18\x01 \x01(\tR\x11synchronizerAlias\x12'\n" +
	"\x0fsynchronizer_id\x18\x02 \x01(\tR\x0esynchronizerId\x12M\n" +
	"\n" +
	"permission\x18\x03 \x01(\x0e2-.com.daml.ledger.api.v2.ParticipantPermissionR\n" +
	"permission\"\x15\n" +
	"\x13GetLedgerEndRequest\".\n" +
	"\x14GetLedgerEndResponse\x12\x16\n" +
	"\x06offset\x18\x01 \x01(\x03R\x06offset\"\x1f\n" +
	"\x1dGetLatestPrunedOffsetsRequest\"\xcc\x01\n" +
	"\x1eGetLatestPrunedOffsetsResponse\x12J\n" +
	"\"participant_pruned_up_to_inclusive\x18\x01 \x01(\x03R\x1eparticipantPrunedUpToInclusive\x12^\n" +
	"-all_divulged_contracts_pruned_up_to_inclusive\x18\x02 \x01(\x03R'allDivulgedContractsPrunedUpToInclusive*\xb7\x01\n" +
	"\x15ParticipantPermission\x12&\n" +
	"\"PARTICIPANT_PERMISSION_UNSPECIFIED\x10\x00\x12%\n" +
	"!PARTICIPANT_PERMISSION_SUBMISSION\x10\x01\x12'\n" +
	"#PARTICIPANT_PERMISSION_CONFIRMATION\x10\x02\x12&\n" +
	"\"PARTICIPANT_PERMISSION_OBSERVATION\x10\x032\x95\x04\n" +
	"\fStateService\x12}\n" +
	"\x12GetActiveContracts\x121.com.daml.ledger.api.v2.GetActiveContractsRequest\x1a2.com.daml.ledger.api.v2.GetActiveContractsResponse0\x01\x12\x90\x01\n" +
	"\x19GetConnectedSynchronizers\x128.com.daml.ledger.api.v2.GetConnectedSynchronizersRequest\x1a9.com.daml.ledger.api.v2.GetConnectedSynchronizersResponse\x12i\n" +
	"\fGetLedgerEnd\x12+.com.daml.ledger.api.v2.GetLedgerEndRequest\x1a,.com.daml.ledger.api.v2.GetLedgerEndResponse\x12\x87\x01\n" +
	"\x16GetLatestPrunedOffsets\x125.com.daml.ledger.api.v2.GetLatestPrunedOffsetsRequest\x1a6.com.daml.ledger.api.v2.GetLatestPrunedOffsetsResponseB\x90\x01\n" +
	"\x16com.daml.ledger.api.v2B\x16StateServiceOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\xaa\x02\x16Com.Daml.Ledger.Api.V2b\x06proto3"

var (
	file_com_daml_ledger_api_v2_state_service_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v2_state_service_proto_rawDescData []byte
)

func file_com_daml_ledger_api_v2_state_service_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v2_state_service_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v2_state_service_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_daml_ledger_api_v2_state_service_proto_rawDesc), len(file_com_daml_ledger_api_v2_state_service_proto_rawDesc)))
	})
	return file_com_daml_ledger_api_v2_state_service_proto_rawDescData
}

var file_com_daml_ledger_api_v2_state_service_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_com_daml_ledger_api_v2_state_service_proto_msgTypes = make([]protoimpl.MessageInfo, 12)
var file_com_daml_ledger_api_v2_state_service_proto_goTypes = []any{
	(ParticipantPermission)(0),                                      // 0: com.daml.ledger.api.v2.ParticipantPermission
	(*GetActiveContractsRequest)(nil),                               // 1: com.daml.ledger.api.v2.GetActiveContractsRequest
	(*GetActiveContractsResponse)(nil),                              // 2: com.daml.ledger.api.v2.GetActiveContractsResponse
	(*ActiveContract)(nil),                                          // 3: com.daml.ledger.api.v2.ActiveContract
	(*IncompleteUnassigned)(nil),                                    // 4: com.daml.ledger.api.v2.IncompleteUnassigned
	(*IncompleteAssigned)(nil),                                      // 5: com.daml.ledger.api.v2.IncompleteAssigned
	(*GetConnectedSynchronizersRequest)(nil),                        // 6: com.daml.ledger.api.v2.GetConnectedSynchronizersRequest
	(*GetConnectedSynchronizersResponse)(nil),                       // 7: com.daml.ledger.api.v2.GetConnectedSynchronizersResponse
	(*GetLedgerEndRequest)(nil),                                     // 8: com.daml.ledger.api.v2.GetLedgerEndRequest
	(*GetLedgerEndResponse)(nil),                                    // 9: com.daml.ledger.api.v2.GetLedgerEndResponse
	(*GetLatestPrunedOffsetsRequest)(nil),                           // 10: com.daml.ledger.api.v2.GetLatestPrunedOffsetsRequest
	(*GetLatestPrunedOffsetsResponse)(nil),                          // 11: com.daml.ledger.api.v2.GetLatestPrunedOffsetsResponse
	(*GetConnectedSynchronizersResponse_ConnectedSynchronizer)(nil), // 12: com.daml.ledger.api.v2.GetConnectedSynchronizersResponse.ConnectedSynchronizer
	(*TransactionFilter)(nil),                                       // 13: com.daml.ledger.api.v2.TransactionFilter
	(*EventFormat)(nil),                                             // 14: com.daml.ledger.api.v2.EventFormat
	(*CreatedEvent)(nil),                                            // 15: com.daml.ledger.api.v2.CreatedEvent
	(*UnassignedEvent)(nil),                                         // 16: com.daml.ledger.api.v2.UnassignedEvent
	(*AssignedEvent)(nil),                                           // 17: com.daml.ledger.api.v2.AssignedEvent
}
var file_com_daml_ledger_api_v2_state_service_proto_depIdxs = []int32{
	13, // 0: com.daml.ledger.api.v2.GetActiveContractsRequest.filter:type_name -> com.daml.ledger.api.v2.TransactionFilter
	14, // 1: com.daml.ledger.api.v2.GetActiveContractsRequest.event_format:type_name -> com.daml.ledger.api.v2.EventFormat
	3,  // 2: com.daml.ledger.api.v2.GetActiveContractsResponse.active_contract:type_name -> com.daml.ledger.api.v2.ActiveContract
	4,  // 3: com.daml.ledger.api.v2.GetActiveContractsResponse.incomplete_unassigned:type_name -> com.daml.ledger.api.v2.IncompleteUnassigned
	5,  // 4: com.daml.ledger.api.v2.GetActiveContractsResponse.incomplete_assigned:type_name -> com.daml.ledger.api.v2.IncompleteAssigned
	15, // 5: com.daml.ledger.api.v2.ActiveContract.created_event:type_name -> com.daml.ledger.api.v2.CreatedEvent
	15, // 6: com.daml.ledger.api.v2.IncompleteUnassigned.created_event:type_name -> com.daml.ledger.api.v2.CreatedEvent
	16, // 7: com.daml.ledger.api.v2.IncompleteUnassigned.unassigned_event:type_name -> com.daml.ledger.api.v2.UnassignedEvent
	17, // 8: com.daml.ledger.api.v2.IncompleteAssigned.assigned_event:type_name -> com.daml.ledger.api.v2.AssignedEvent
	12, // 9: com.daml.ledger.api.v2.GetConnectedSynchronizersResponse.connected_synchronizers:type_name -> com.daml.ledger.api.v2.GetConnectedSynchronizersResponse.ConnectedSynchronizer
	0,  // 10: com.daml.ledger.api.v2.GetConnectedSynchronizersResponse.ConnectedSynchronizer.permission:type_name -> com.daml.ledger.api.v2.ParticipantPermission
	1,  // 11: com.daml.ledger.api.v2.StateService.GetActiveContracts:input_type -> com.daml.ledger.api.v2.GetActiveContractsRequest
	6,  // 12: com.daml.ledger.api.v2.StateService.GetConnectedSynchronizers:input_type -> com.daml.ledger.api.v2.GetConnectedSynchronizersRequest
	8,  // 13: com.daml.ledger.api.v2.StateService.GetLedgerEnd:input_type -> com.daml.ledger.api.v2.GetLedgerEndRequest
	10, // 14: com.daml.ledger.api.v2.StateService.GetLatestPrunedOffsets:input_type -> com.daml.ledger.api.v2.GetLatestPrunedOffsetsRequest
	2,  // 15: com.daml.ledger.api.v2.StateService.GetActiveContracts:output_type -> com.daml.ledger.api.v2.GetActiveContractsResponse
	7,  // 16: com.daml.ledger.api.v2.StateService.GetConnectedSynchronizers:output_type -> com.daml.ledger.api.v2.GetConnectedSynchronizersResponse
	9,  // 17: com.daml.ledger.api.v2.StateService.GetLedgerEnd:output_type -> com.daml.ledger.api.v2.GetLedgerEndResponse
	11, // 18: com.daml.ledger.api.v2.StateService.GetLatestPrunedOffsets:output_type -> com.daml.ledger.api.v2.GetLatestPrunedOffsetsResponse
	15, // [15:19] is the sub-list for method output_type
	11, // [11:15] is the sub-list for method input_type
	11, // [11:11] is the sub-list for extension type_name
	11, // [11:11] is the sub-list for extension extendee
	0,  // [0:11] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v2_state_service_proto_init() }
func file_com_daml_ledger_api_v2_state_service_proto_init() {
	if File_com_daml_ledger_api_v2_state_service_proto != nil {
		return
	}
	file_com_daml_ledger_api_v2_event_proto_init()
	file_com_daml_ledger_api_v2_reassignment_proto_init()
	file_com_daml_ledger_api_v2_transaction_filter_proto_init()
	file_com_daml_ledger_api_v2_state_service_proto_msgTypes[1].OneofWrappers = []any{
		(*GetActiveContractsResponse_ActiveContract)(nil),
		(*GetActiveContractsResponse_IncompleteUnassigned)(nil),
		(*GetActiveContractsResponse_IncompleteAssigned)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_daml_ledger_api_v2_state_service_proto_rawDesc), len(file_com_daml_ledger_api_v2_state_service_proto_rawDesc)),
			NumEnums:      1,
			NumMessages:   12,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_daml_ledger_api_v2_state_service_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v2_state_service_proto_depIdxs,
		EnumInfos:         file_com_daml_ledger_api_v2_state_service_proto_enumTypes,
		MessageInfos:      file_com_daml_ledger_api_v2_state_service_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v2_state_service_proto = out.File
	file_com_daml_ledger_api_v2_state_service_proto_goTypes = nil
	file_com_daml_ledger_api_v2_state_service_proto_depIdxs = nil
}
