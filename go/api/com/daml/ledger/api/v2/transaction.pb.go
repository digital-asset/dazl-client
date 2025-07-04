// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/daml/ledger/api/v2/transaction.proto

package v2

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	timestamppb "google.golang.org/protobuf/types/known/timestamppb"
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

type TreeEvent struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// Types that are valid to be assigned to Kind:
	//
	//	*TreeEvent_Created
	//	*TreeEvent_Exercised
	Kind          isTreeEvent_Kind `protobuf_oneof:"kind"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *TreeEvent) Reset() {
	*x = TreeEvent{}
	mi := &file_com_daml_ledger_api_v2_transaction_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TreeEvent) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TreeEvent) ProtoMessage() {}

func (x *TreeEvent) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_transaction_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TreeEvent.ProtoReflect.Descriptor instead.
func (*TreeEvent) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_transaction_proto_rawDescGZIP(), []int{0}
}

func (x *TreeEvent) GetKind() isTreeEvent_Kind {
	if x != nil {
		return x.Kind
	}
	return nil
}

func (x *TreeEvent) GetCreated() *CreatedEvent {
	if x != nil {
		if x, ok := x.Kind.(*TreeEvent_Created); ok {
			return x.Created
		}
	}
	return nil
}

func (x *TreeEvent) GetExercised() *ExercisedEvent {
	if x != nil {
		if x, ok := x.Kind.(*TreeEvent_Exercised); ok {
			return x.Exercised
		}
	}
	return nil
}

type isTreeEvent_Kind interface {
	isTreeEvent_Kind()
}

type TreeEvent_Created struct {
	Created *CreatedEvent `protobuf:"bytes,1,opt,name=created,proto3,oneof"`
}

type TreeEvent_Exercised struct {
	Exercised *ExercisedEvent `protobuf:"bytes,2,opt,name=exercised,proto3,oneof"`
}

func (*TreeEvent_Created) isTreeEvent_Kind() {}

func (*TreeEvent_Exercised) isTreeEvent_Kind() {}

type TransactionTree struct {
	state          protoimpl.MessageState `protogen:"open.v1"`
	UpdateId       string                 `protobuf:"bytes,1,opt,name=update_id,json=updateId,proto3" json:"update_id,omitempty"`
	CommandId      string                 `protobuf:"bytes,2,opt,name=command_id,json=commandId,proto3" json:"command_id,omitempty"`
	WorkflowId     string                 `protobuf:"bytes,3,opt,name=workflow_id,json=workflowId,proto3" json:"workflow_id,omitempty"`
	EffectiveAt    *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=effective_at,json=effectiveAt,proto3" json:"effective_at,omitempty"`
	Offset         int64                  `protobuf:"varint,5,opt,name=offset,proto3" json:"offset,omitempty"`
	EventsById     map[int32]*TreeEvent   `protobuf:"bytes,6,rep,name=events_by_id,json=eventsById,proto3" json:"events_by_id,omitempty" protobuf_key:"varint,1,opt,name=key" protobuf_val:"bytes,2,opt,name=value"`
	SynchronizerId string                 `protobuf:"bytes,7,opt,name=synchronizer_id,json=synchronizerId,proto3" json:"synchronizer_id,omitempty"`
	TraceContext   *TraceContext          `protobuf:"bytes,8,opt,name=trace_context,json=traceContext,proto3" json:"trace_context,omitempty"`
	RecordTime     *timestamppb.Timestamp `protobuf:"bytes,9,opt,name=record_time,json=recordTime,proto3" json:"record_time,omitempty"`
	unknownFields  protoimpl.UnknownFields
	sizeCache      protoimpl.SizeCache
}

func (x *TransactionTree) Reset() {
	*x = TransactionTree{}
	mi := &file_com_daml_ledger_api_v2_transaction_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TransactionTree) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TransactionTree) ProtoMessage() {}

func (x *TransactionTree) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_transaction_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TransactionTree.ProtoReflect.Descriptor instead.
func (*TransactionTree) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_transaction_proto_rawDescGZIP(), []int{1}
}

func (x *TransactionTree) GetUpdateId() string {
	if x != nil {
		return x.UpdateId
	}
	return ""
}

func (x *TransactionTree) GetCommandId() string {
	if x != nil {
		return x.CommandId
	}
	return ""
}

func (x *TransactionTree) GetWorkflowId() string {
	if x != nil {
		return x.WorkflowId
	}
	return ""
}

func (x *TransactionTree) GetEffectiveAt() *timestamppb.Timestamp {
	if x != nil {
		return x.EffectiveAt
	}
	return nil
}

func (x *TransactionTree) GetOffset() int64 {
	if x != nil {
		return x.Offset
	}
	return 0
}

func (x *TransactionTree) GetEventsById() map[int32]*TreeEvent {
	if x != nil {
		return x.EventsById
	}
	return nil
}

func (x *TransactionTree) GetSynchronizerId() string {
	if x != nil {
		return x.SynchronizerId
	}
	return ""
}

func (x *TransactionTree) GetTraceContext() *TraceContext {
	if x != nil {
		return x.TraceContext
	}
	return nil
}

func (x *TransactionTree) GetRecordTime() *timestamppb.Timestamp {
	if x != nil {
		return x.RecordTime
	}
	return nil
}

type Transaction struct {
	state          protoimpl.MessageState `protogen:"open.v1"`
	UpdateId       string                 `protobuf:"bytes,1,opt,name=update_id,json=updateId,proto3" json:"update_id,omitempty"`
	CommandId      string                 `protobuf:"bytes,2,opt,name=command_id,json=commandId,proto3" json:"command_id,omitempty"`
	WorkflowId     string                 `protobuf:"bytes,3,opt,name=workflow_id,json=workflowId,proto3" json:"workflow_id,omitempty"`
	EffectiveAt    *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=effective_at,json=effectiveAt,proto3" json:"effective_at,omitempty"`
	Events         []*Event               `protobuf:"bytes,5,rep,name=events,proto3" json:"events,omitempty"`
	Offset         int64                  `protobuf:"varint,6,opt,name=offset,proto3" json:"offset,omitempty"`
	SynchronizerId string                 `protobuf:"bytes,7,opt,name=synchronizer_id,json=synchronizerId,proto3" json:"synchronizer_id,omitempty"`
	TraceContext   *TraceContext          `protobuf:"bytes,8,opt,name=trace_context,json=traceContext,proto3" json:"trace_context,omitempty"`
	RecordTime     *timestamppb.Timestamp `protobuf:"bytes,9,opt,name=record_time,json=recordTime,proto3" json:"record_time,omitempty"`
	unknownFields  protoimpl.UnknownFields
	sizeCache      protoimpl.SizeCache
}

func (x *Transaction) Reset() {
	*x = Transaction{}
	mi := &file_com_daml_ledger_api_v2_transaction_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Transaction) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Transaction) ProtoMessage() {}

func (x *Transaction) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_transaction_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Transaction.ProtoReflect.Descriptor instead.
func (*Transaction) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_transaction_proto_rawDescGZIP(), []int{2}
}

func (x *Transaction) GetUpdateId() string {
	if x != nil {
		return x.UpdateId
	}
	return ""
}

func (x *Transaction) GetCommandId() string {
	if x != nil {
		return x.CommandId
	}
	return ""
}

func (x *Transaction) GetWorkflowId() string {
	if x != nil {
		return x.WorkflowId
	}
	return ""
}

func (x *Transaction) GetEffectiveAt() *timestamppb.Timestamp {
	if x != nil {
		return x.EffectiveAt
	}
	return nil
}

func (x *Transaction) GetEvents() []*Event {
	if x != nil {
		return x.Events
	}
	return nil
}

func (x *Transaction) GetOffset() int64 {
	if x != nil {
		return x.Offset
	}
	return 0
}

func (x *Transaction) GetSynchronizerId() string {
	if x != nil {
		return x.SynchronizerId
	}
	return ""
}

func (x *Transaction) GetTraceContext() *TraceContext {
	if x != nil {
		return x.TraceContext
	}
	return nil
}

func (x *Transaction) GetRecordTime() *timestamppb.Timestamp {
	if x != nil {
		return x.RecordTime
	}
	return nil
}

var File_com_daml_ledger_api_v2_transaction_proto protoreflect.FileDescriptor

const file_com_daml_ledger_api_v2_transaction_proto_rawDesc = "" +
	"\n" +
	"(com/daml/ledger/api/v2/transaction.proto\x12\x16com.daml.ledger.api.v2\x1a\"com/daml/ledger/api/v2/event.proto\x1a*com/daml/ledger/api/v2/trace_context.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9d\x01\n" +
	"\tTreeEvent\x12@\n" +
	"\acreated\x18\x01 \x01(\v2$.com.daml.ledger.api.v2.CreatedEventH\x00R\acreated\x12F\n" +
	"\texercised\x18\x02 \x01(\v2&.com.daml.ledger.api.v2.ExercisedEventH\x00R\texercisedB\x06\n" +
	"\x04kind\"\xb3\x04\n" +
	"\x0fTransactionTree\x12\x1b\n" +
	"\tupdate_id\x18\x01 \x01(\tR\bupdateId\x12\x1d\n" +
	"\n" +
	"command_id\x18\x02 \x01(\tR\tcommandId\x12\x1f\n" +
	"\vworkflow_id\x18\x03 \x01(\tR\n" +
	"workflowId\x12=\n" +
	"\feffective_at\x18\x04 \x01(\v2\x1a.google.protobuf.TimestampR\veffectiveAt\x12\x16\n" +
	"\x06offset\x18\x05 \x01(\x03R\x06offset\x12Y\n" +
	"\fevents_by_id\x18\x06 \x03(\v27.com.daml.ledger.api.v2.TransactionTree.EventsByIdEntryR\n" +
	"eventsById\x12'\n" +
	"\x0fsynchronizer_id\x18\a \x01(\tR\x0esynchronizerId\x12I\n" +
	"\rtrace_context\x18\b \x01(\v2$.com.daml.ledger.api.v2.TraceContextR\ftraceContext\x12;\n" +
	"\vrecord_time\x18\t \x01(\v2\x1a.google.protobuf.TimestampR\n" +
	"recordTime\x1a`\n" +
	"\x0fEventsByIdEntry\x12\x10\n" +
	"\x03key\x18\x01 \x01(\x05R\x03key\x127\n" +
	"\x05value\x18\x02 \x01(\v2!.com.daml.ledger.api.v2.TreeEventR\x05value:\x028\x01\"\xa9\x03\n" +
	"\vTransaction\x12\x1b\n" +
	"\tupdate_id\x18\x01 \x01(\tR\bupdateId\x12\x1d\n" +
	"\n" +
	"command_id\x18\x02 \x01(\tR\tcommandId\x12\x1f\n" +
	"\vworkflow_id\x18\x03 \x01(\tR\n" +
	"workflowId\x12=\n" +
	"\feffective_at\x18\x04 \x01(\v2\x1a.google.protobuf.TimestampR\veffectiveAt\x125\n" +
	"\x06events\x18\x05 \x03(\v2\x1d.com.daml.ledger.api.v2.EventR\x06events\x12\x16\n" +
	"\x06offset\x18\x06 \x01(\x03R\x06offset\x12'\n" +
	"\x0fsynchronizer_id\x18\a \x01(\tR\x0esynchronizerId\x12I\n" +
	"\rtrace_context\x18\b \x01(\v2$.com.daml.ledger.api.v2.TraceContextR\ftraceContext\x12;\n" +
	"\vrecord_time\x18\t \x01(\v2\x1a.google.protobuf.TimestampR\n" +
	"recordTimeB\x8f\x01\n" +
	"\x16com.daml.ledger.api.v2B\x15TransactionOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\xaa\x02\x16Com.Daml.Ledger.Api.V2b\x06proto3"

var (
	file_com_daml_ledger_api_v2_transaction_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v2_transaction_proto_rawDescData []byte
)

func file_com_daml_ledger_api_v2_transaction_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v2_transaction_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v2_transaction_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_daml_ledger_api_v2_transaction_proto_rawDesc), len(file_com_daml_ledger_api_v2_transaction_proto_rawDesc)))
	})
	return file_com_daml_ledger_api_v2_transaction_proto_rawDescData
}

var file_com_daml_ledger_api_v2_transaction_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_com_daml_ledger_api_v2_transaction_proto_goTypes = []any{
	(*TreeEvent)(nil),             // 0: com.daml.ledger.api.v2.TreeEvent
	(*TransactionTree)(nil),       // 1: com.daml.ledger.api.v2.TransactionTree
	(*Transaction)(nil),           // 2: com.daml.ledger.api.v2.Transaction
	nil,                           // 3: com.daml.ledger.api.v2.TransactionTree.EventsByIdEntry
	(*CreatedEvent)(nil),          // 4: com.daml.ledger.api.v2.CreatedEvent
	(*ExercisedEvent)(nil),        // 5: com.daml.ledger.api.v2.ExercisedEvent
	(*timestamppb.Timestamp)(nil), // 6: google.protobuf.Timestamp
	(*TraceContext)(nil),          // 7: com.daml.ledger.api.v2.TraceContext
	(*Event)(nil),                 // 8: com.daml.ledger.api.v2.Event
}
var file_com_daml_ledger_api_v2_transaction_proto_depIdxs = []int32{
	4,  // 0: com.daml.ledger.api.v2.TreeEvent.created:type_name -> com.daml.ledger.api.v2.CreatedEvent
	5,  // 1: com.daml.ledger.api.v2.TreeEvent.exercised:type_name -> com.daml.ledger.api.v2.ExercisedEvent
	6,  // 2: com.daml.ledger.api.v2.TransactionTree.effective_at:type_name -> google.protobuf.Timestamp
	3,  // 3: com.daml.ledger.api.v2.TransactionTree.events_by_id:type_name -> com.daml.ledger.api.v2.TransactionTree.EventsByIdEntry
	7,  // 4: com.daml.ledger.api.v2.TransactionTree.trace_context:type_name -> com.daml.ledger.api.v2.TraceContext
	6,  // 5: com.daml.ledger.api.v2.TransactionTree.record_time:type_name -> google.protobuf.Timestamp
	6,  // 6: com.daml.ledger.api.v2.Transaction.effective_at:type_name -> google.protobuf.Timestamp
	8,  // 7: com.daml.ledger.api.v2.Transaction.events:type_name -> com.daml.ledger.api.v2.Event
	7,  // 8: com.daml.ledger.api.v2.Transaction.trace_context:type_name -> com.daml.ledger.api.v2.TraceContext
	6,  // 9: com.daml.ledger.api.v2.Transaction.record_time:type_name -> google.protobuf.Timestamp
	0,  // 10: com.daml.ledger.api.v2.TransactionTree.EventsByIdEntry.value:type_name -> com.daml.ledger.api.v2.TreeEvent
	11, // [11:11] is the sub-list for method output_type
	11, // [11:11] is the sub-list for method input_type
	11, // [11:11] is the sub-list for extension type_name
	11, // [11:11] is the sub-list for extension extendee
	0,  // [0:11] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v2_transaction_proto_init() }
func file_com_daml_ledger_api_v2_transaction_proto_init() {
	if File_com_daml_ledger_api_v2_transaction_proto != nil {
		return
	}
	file_com_daml_ledger_api_v2_event_proto_init()
	file_com_daml_ledger_api_v2_trace_context_proto_init()
	file_com_daml_ledger_api_v2_transaction_proto_msgTypes[0].OneofWrappers = []any{
		(*TreeEvent_Created)(nil),
		(*TreeEvent_Exercised)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_daml_ledger_api_v2_transaction_proto_rawDesc), len(file_com_daml_ledger_api_v2_transaction_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_daml_ledger_api_v2_transaction_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v2_transaction_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v2_transaction_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v2_transaction_proto = out.File
	file_com_daml_ledger_api_v2_transaction_proto_goTypes = nil
	file_com_daml_ledger_api_v2_transaction_proto_depIdxs = nil
}
