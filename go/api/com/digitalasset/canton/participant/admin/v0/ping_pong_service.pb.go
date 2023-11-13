// Copyright (c) 2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v4.24.3
// source: com/digitalasset/canton/participant/admin/v0/ping_pong_service.proto

package v0

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

type PingRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	TargetParties           []string `protobuf:"bytes,1,rep,name=target_parties,json=targetParties,proto3" json:"target_parties,omitempty"`
	Validators              []string `protobuf:"bytes,2,rep,name=validators,proto3" json:"validators,omitempty"`
	TimeoutMilliseconds     uint64   `protobuf:"varint,3,opt,name=timeout_milliseconds,json=timeoutMilliseconds,proto3" json:"timeout_milliseconds,omitempty"`
	Levels                  uint64   `protobuf:"varint,4,opt,name=levels,proto3" json:"levels,omitempty"`
	GracePeriodMilliseconds uint64   `protobuf:"varint,5,opt,name=grace_period_milliseconds,json=gracePeriodMilliseconds,proto3" json:"grace_period_milliseconds,omitempty"`
	WorkflowId              string   `protobuf:"bytes,6,opt,name=workflow_id,json=workflowId,proto3" json:"workflow_id,omitempty"` // optional
	Id                      string   `protobuf:"bytes,7,opt,name=id,proto3" json:"id,omitempty"`                                   // optional UUID to be used for ping test
}

func (x *PingRequest) Reset() {
	*x = PingRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PingRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PingRequest) ProtoMessage() {}

func (x *PingRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PingRequest.ProtoReflect.Descriptor instead.
func (*PingRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescGZIP(), []int{0}
}

func (x *PingRequest) GetTargetParties() []string {
	if x != nil {
		return x.TargetParties
	}
	return nil
}

func (x *PingRequest) GetValidators() []string {
	if x != nil {
		return x.Validators
	}
	return nil
}

func (x *PingRequest) GetTimeoutMilliseconds() uint64 {
	if x != nil {
		return x.TimeoutMilliseconds
	}
	return 0
}

func (x *PingRequest) GetLevels() uint64 {
	if x != nil {
		return x.Levels
	}
	return 0
}

func (x *PingRequest) GetGracePeriodMilliseconds() uint64 {
	if x != nil {
		return x.GracePeriodMilliseconds
	}
	return 0
}

func (x *PingRequest) GetWorkflowId() string {
	if x != nil {
		return x.WorkflowId
	}
	return ""
}

func (x *PingRequest) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

type PingSuccess struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	PingTime  uint64 `protobuf:"varint,1,opt,name=ping_time,json=pingTime,proto3" json:"ping_time,omitempty"`
	Responder string `protobuf:"bytes,2,opt,name=responder,proto3" json:"responder,omitempty"`
}

func (x *PingSuccess) Reset() {
	*x = PingSuccess{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PingSuccess) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PingSuccess) ProtoMessage() {}

func (x *PingSuccess) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PingSuccess.ProtoReflect.Descriptor instead.
func (*PingSuccess) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescGZIP(), []int{1}
}

func (x *PingSuccess) GetPingTime() uint64 {
	if x != nil {
		return x.PingTime
	}
	return 0
}

func (x *PingSuccess) GetResponder() string {
	if x != nil {
		return x.Responder
	}
	return ""
}

type PingFailure struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *PingFailure) Reset() {
	*x = PingFailure{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PingFailure) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PingFailure) ProtoMessage() {}

func (x *PingFailure) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PingFailure.ProtoReflect.Descriptor instead.
func (*PingFailure) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescGZIP(), []int{2}
}

type PingResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Response:
	//	*PingResponse_Success
	//	*PingResponse_Failure
	Response isPingResponse_Response `protobuf_oneof:"response"`
}

func (x *PingResponse) Reset() {
	*x = PingResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PingResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PingResponse) ProtoMessage() {}

func (x *PingResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PingResponse.ProtoReflect.Descriptor instead.
func (*PingResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescGZIP(), []int{3}
}

func (m *PingResponse) GetResponse() isPingResponse_Response {
	if m != nil {
		return m.Response
	}
	return nil
}

func (x *PingResponse) GetSuccess() *PingSuccess {
	if x, ok := x.GetResponse().(*PingResponse_Success); ok {
		return x.Success
	}
	return nil
}

func (x *PingResponse) GetFailure() *PingFailure {
	if x, ok := x.GetResponse().(*PingResponse_Failure); ok {
		return x.Failure
	}
	return nil
}

type isPingResponse_Response interface {
	isPingResponse_Response()
}

type PingResponse_Success struct {
	Success *PingSuccess `protobuf:"bytes,1,opt,name=success,proto3,oneof"`
}

type PingResponse_Failure struct {
	Failure *PingFailure `protobuf:"bytes,2,opt,name=failure,proto3,oneof"`
}

func (*PingResponse_Success) isPingResponse_Response() {}

func (*PingResponse_Failure) isPingResponse_Response() {}

var File_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDesc = []byte{
	0x0a, 0x44, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63,
	0x69, 0x70, 0x61, 0x6e, 0x74, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x76, 0x30, 0x2f, 0x70,
	0x69, 0x6e, 0x67, 0x5f, 0x70, 0x6f, 0x6e, 0x67, 0x5f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x2c, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69,
	0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e,
	0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x2e, 0x61, 0x64, 0x6d, 0x69,
	0x6e, 0x2e, 0x76, 0x30, 0x22, 0x8c, 0x02, 0x0a, 0x0b, 0x50, 0x69, 0x6e, 0x67, 0x52, 0x65, 0x71,
	0x75, 0x65, 0x73, 0x74, 0x12, 0x25, 0x0a, 0x0e, 0x74, 0x61, 0x72, 0x67, 0x65, 0x74, 0x5f, 0x70,
	0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x09, 0x52, 0x0d, 0x74, 0x61,
	0x72, 0x67, 0x65, 0x74, 0x50, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x12, 0x1e, 0x0a, 0x0a, 0x76,
	0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x6f, 0x72, 0x73, 0x18, 0x02, 0x20, 0x03, 0x28, 0x09, 0x52,
	0x0a, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x6f, 0x72, 0x73, 0x12, 0x31, 0x0a, 0x14, 0x74,
	0x69, 0x6d, 0x65, 0x6f, 0x75, 0x74, 0x5f, 0x6d, 0x69, 0x6c, 0x6c, 0x69, 0x73, 0x65, 0x63, 0x6f,
	0x6e, 0x64, 0x73, 0x18, 0x03, 0x20, 0x01, 0x28, 0x04, 0x52, 0x13, 0x74, 0x69, 0x6d, 0x65, 0x6f,
	0x75, 0x74, 0x4d, 0x69, 0x6c, 0x6c, 0x69, 0x73, 0x65, 0x63, 0x6f, 0x6e, 0x64, 0x73, 0x12, 0x16,
	0x0a, 0x06, 0x6c, 0x65, 0x76, 0x65, 0x6c, 0x73, 0x18, 0x04, 0x20, 0x01, 0x28, 0x04, 0x52, 0x06,
	0x6c, 0x65, 0x76, 0x65, 0x6c, 0x73, 0x12, 0x3a, 0x0a, 0x19, 0x67, 0x72, 0x61, 0x63, 0x65, 0x5f,
	0x70, 0x65, 0x72, 0x69, 0x6f, 0x64, 0x5f, 0x6d, 0x69, 0x6c, 0x6c, 0x69, 0x73, 0x65, 0x63, 0x6f,
	0x6e, 0x64, 0x73, 0x18, 0x05, 0x20, 0x01, 0x28, 0x04, 0x52, 0x17, 0x67, 0x72, 0x61, 0x63, 0x65,
	0x50, 0x65, 0x72, 0x69, 0x6f, 0x64, 0x4d, 0x69, 0x6c, 0x6c, 0x69, 0x73, 0x65, 0x63, 0x6f, 0x6e,
	0x64, 0x73, 0x12, 0x1f, 0x0a, 0x0b, 0x77, 0x6f, 0x72, 0x6b, 0x66, 0x6c, 0x6f, 0x77, 0x5f, 0x69,
	0x64, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x77, 0x6f, 0x72, 0x6b, 0x66, 0x6c, 0x6f,
	0x77, 0x49, 0x64, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x07, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x02, 0x69, 0x64, 0x22, 0x48, 0x0a, 0x0b, 0x50, 0x69, 0x6e, 0x67, 0x53, 0x75, 0x63, 0x63, 0x65,
	0x73, 0x73, 0x12, 0x1b, 0x0a, 0x09, 0x70, 0x69, 0x6e, 0x67, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x04, 0x52, 0x08, 0x70, 0x69, 0x6e, 0x67, 0x54, 0x69, 0x6d, 0x65, 0x12,
	0x1c, 0x0a, 0x09, 0x72, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x64, 0x65, 0x72, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x09, 0x72, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x64, 0x65, 0x72, 0x22, 0x0d, 0x0a,
	0x0b, 0x50, 0x69, 0x6e, 0x67, 0x46, 0x61, 0x69, 0x6c, 0x75, 0x72, 0x65, 0x22, 0xc8, 0x01, 0x0a,
	0x0c, 0x50, 0x69, 0x6e, 0x67, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x55, 0x0a,
	0x07, 0x73, 0x75, 0x63, 0x63, 0x65, 0x73, 0x73, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x39,
	0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65,
	0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69,
	0x70, 0x61, 0x6e, 0x74, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x50, 0x69,
	0x6e, 0x67, 0x53, 0x75, 0x63, 0x63, 0x65, 0x73, 0x73, 0x48, 0x00, 0x52, 0x07, 0x73, 0x75, 0x63,
	0x63, 0x65, 0x73, 0x73, 0x12, 0x55, 0x0a, 0x07, 0x66, 0x61, 0x69, 0x6c, 0x75, 0x72, 0x65, 0x18,
	0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x39, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69,
	0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e,
	0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x2e, 0x61, 0x64, 0x6d, 0x69,
	0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x50, 0x69, 0x6e, 0x67, 0x46, 0x61, 0x69, 0x6c, 0x75, 0x72, 0x65,
	0x48, 0x00, 0x52, 0x07, 0x66, 0x61, 0x69, 0x6c, 0x75, 0x72, 0x65, 0x42, 0x0a, 0x0a, 0x08, 0x72,
	0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x32, 0x8c, 0x01, 0x0a, 0x0b, 0x50, 0x69, 0x6e, 0x67,
	0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x7d, 0x0a, 0x04, 0x70, 0x69, 0x6e, 0x67, 0x12,
	0x39, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63,
	0x69, 0x70, 0x61, 0x6e, 0x74, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x50,
	0x69, 0x6e, 0x67, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x3a, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74,
	0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x50, 0x69, 0x6e, 0x67, 0x52, 0x65,
	0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x42, 0x5d, 0x5a, 0x5b, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62,
	0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76,
	0x37, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67,
	0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e,
	0x2f, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x2f, 0x61, 0x64, 0x6d,
	0x69, 0x6e, 0x2f, 0x76, 0x30, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescData = file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDesc
)

func file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescData)
	})
	return file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescData
}

var file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_goTypes = []interface{}{
	(*PingRequest)(nil),  // 0: com.digitalasset.canton.participant.admin.v0.PingRequest
	(*PingSuccess)(nil),  // 1: com.digitalasset.canton.participant.admin.v0.PingSuccess
	(*PingFailure)(nil),  // 2: com.digitalasset.canton.participant.admin.v0.PingFailure
	(*PingResponse)(nil), // 3: com.digitalasset.canton.participant.admin.v0.PingResponse
}
var file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_depIdxs = []int32{
	1, // 0: com.digitalasset.canton.participant.admin.v0.PingResponse.success:type_name -> com.digitalasset.canton.participant.admin.v0.PingSuccess
	2, // 1: com.digitalasset.canton.participant.admin.v0.PingResponse.failure:type_name -> com.digitalasset.canton.participant.admin.v0.PingFailure
	0, // 2: com.digitalasset.canton.participant.admin.v0.PingService.ping:input_type -> com.digitalasset.canton.participant.admin.v0.PingRequest
	3, // 3: com.digitalasset.canton.participant.admin.v0.PingService.ping:output_type -> com.digitalasset.canton.participant.admin.v0.PingResponse
	3, // [3:4] is the sub-list for method output_type
	2, // [2:3] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_init() }
func file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_init() {
	if File_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*PingRequest); i {
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
		file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*PingSuccess); i {
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
		file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*PingFailure); i {
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
		file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*PingResponse); i {
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
	file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[3].OneofWrappers = []interface{}{
		(*PingResponse_Success)(nil),
		(*PingResponse_Failure)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto = out.File
	file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDesc = nil
	file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_goTypes = nil
	file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_depIdxs = nil
}
