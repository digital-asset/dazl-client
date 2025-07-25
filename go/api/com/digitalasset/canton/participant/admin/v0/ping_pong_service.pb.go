// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/participant/admin/v0/ping_pong_service.proto

package v0

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

type PingRequest struct {
	state                   protoimpl.MessageState `protogen:"open.v1"`
	TargetParties           []string               `protobuf:"bytes,1,rep,name=target_parties,json=targetParties,proto3" json:"target_parties,omitempty"`
	Validators              []string               `protobuf:"bytes,2,rep,name=validators,proto3" json:"validators,omitempty"`
	TimeoutMilliseconds     uint64                 `protobuf:"varint,3,opt,name=timeout_milliseconds,json=timeoutMilliseconds,proto3" json:"timeout_milliseconds,omitempty"`
	Levels                  uint64                 `protobuf:"varint,4,opt,name=levels,proto3" json:"levels,omitempty"`
	GracePeriodMilliseconds uint64                 `protobuf:"varint,5,opt,name=grace_period_milliseconds,json=gracePeriodMilliseconds,proto3" json:"grace_period_milliseconds,omitempty"`
	WorkflowId              string                 `protobuf:"bytes,6,opt,name=workflow_id,json=workflowId,proto3" json:"workflow_id,omitempty"`
	Id                      string                 `protobuf:"bytes,7,opt,name=id,proto3" json:"id,omitempty"`
	unknownFields           protoimpl.UnknownFields
	sizeCache               protoimpl.SizeCache
}

func (x *PingRequest) Reset() {
	*x = PingRequest{}
	mi := &file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PingRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PingRequest) ProtoMessage() {}

func (x *PingRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[0]
	if x != nil {
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
	state         protoimpl.MessageState `protogen:"open.v1"`
	PingTime      uint64                 `protobuf:"varint,1,opt,name=ping_time,json=pingTime,proto3" json:"ping_time,omitempty"`
	Responder     string                 `protobuf:"bytes,2,opt,name=responder,proto3" json:"responder,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *PingSuccess) Reset() {
	*x = PingSuccess{}
	mi := &file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PingSuccess) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PingSuccess) ProtoMessage() {}

func (x *PingSuccess) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[1]
	if x != nil {
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
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *PingFailure) Reset() {
	*x = PingFailure{}
	mi := &file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PingFailure) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PingFailure) ProtoMessage() {}

func (x *PingFailure) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[2]
	if x != nil {
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
	state protoimpl.MessageState `protogen:"open.v1"`
	// Types that are valid to be assigned to Response:
	//
	//	*PingResponse_Success
	//	*PingResponse_Failure
	Response      isPingResponse_Response `protobuf_oneof:"response"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *PingResponse) Reset() {
	*x = PingResponse{}
	mi := &file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PingResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PingResponse) ProtoMessage() {}

func (x *PingResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[3]
	if x != nil {
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

func (x *PingResponse) GetResponse() isPingResponse_Response {
	if x != nil {
		return x.Response
	}
	return nil
}

func (x *PingResponse) GetSuccess() *PingSuccess {
	if x != nil {
		if x, ok := x.Response.(*PingResponse_Success); ok {
			return x.Success
		}
	}
	return nil
}

func (x *PingResponse) GetFailure() *PingFailure {
	if x != nil {
		if x, ok := x.Response.(*PingResponse_Failure); ok {
			return x.Failure
		}
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

const file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDesc = "" +
	"\n" +
	"Dcom/digitalasset/canton/participant/admin/v0/ping_pong_service.proto\x12,com.digitalasset.canton.participant.admin.v0\"\x8c\x02\n" +
	"\vPingRequest\x12%\n" +
	"\x0etarget_parties\x18\x01 \x03(\tR\rtargetParties\x12\x1e\n" +
	"\n" +
	"validators\x18\x02 \x03(\tR\n" +
	"validators\x121\n" +
	"\x14timeout_milliseconds\x18\x03 \x01(\x04R\x13timeoutMilliseconds\x12\x16\n" +
	"\x06levels\x18\x04 \x01(\x04R\x06levels\x12:\n" +
	"\x19grace_period_milliseconds\x18\x05 \x01(\x04R\x17gracePeriodMilliseconds\x12\x1f\n" +
	"\vworkflow_id\x18\x06 \x01(\tR\n" +
	"workflowId\x12\x0e\n" +
	"\x02id\x18\a \x01(\tR\x02id\"H\n" +
	"\vPingSuccess\x12\x1b\n" +
	"\tping_time\x18\x01 \x01(\x04R\bpingTime\x12\x1c\n" +
	"\tresponder\x18\x02 \x01(\tR\tresponder\"\r\n" +
	"\vPingFailure\"\xc8\x01\n" +
	"\fPingResponse\x12U\n" +
	"\asuccess\x18\x01 \x01(\v29.com.digitalasset.canton.participant.admin.v0.PingSuccessH\x00R\asuccess\x12U\n" +
	"\afailure\x18\x02 \x01(\v29.com.digitalasset.canton.participant.admin.v0.PingFailureH\x00R\afailureB\n" +
	"\n" +
	"\bresponse2\x8c\x01\n" +
	"\vPingService\x12}\n" +
	"\x04ping\x129.com.digitalasset.canton.participant.admin.v0.PingRequest\x1a:.com.digitalasset.canton.participant.admin.v0.PingResponseB]Z[github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/participant/admin/v0b\x06proto3"

var (
	file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescData []byte
)

func file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDesc), len(file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDesc)))
	})
	return file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDescData
}

var file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_goTypes = []any{
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
	file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_msgTypes[3].OneofWrappers = []any{
		(*PingResponse_Success)(nil),
		(*PingResponse_Failure)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDesc), len(file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_rawDesc)),
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
	file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_goTypes = nil
	file_com_digitalasset_canton_participant_admin_v0_ping_pong_service_proto_depIdxs = nil
}
