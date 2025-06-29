// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/admin/participant/v30/pruning_service.proto

package v30

import (
	v30 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/admin/pruning/v30"
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

type PruneRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	PruneUpTo     int64                  `protobuf:"varint,1,opt,name=prune_up_to,json=pruneUpTo,proto3" json:"prune_up_to,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *PruneRequest) Reset() {
	*x = PruneRequest{}
	mi := &file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PruneRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PruneRequest) ProtoMessage() {}

func (x *PruneRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PruneRequest.ProtoReflect.Descriptor instead.
func (*PruneRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_rawDescGZIP(), []int{0}
}

func (x *PruneRequest) GetPruneUpTo() int64 {
	if x != nil {
		return x.PruneUpTo
	}
	return 0
}

type PruneResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *PruneResponse) Reset() {
	*x = PruneResponse{}
	mi := &file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PruneResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PruneResponse) ProtoMessage() {}

func (x *PruneResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PruneResponse.ProtoReflect.Descriptor instead.
func (*PruneResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_rawDescGZIP(), []int{1}
}

type GetSafePruningOffsetRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	BeforeOrAt    *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=before_or_at,json=beforeOrAt,proto3" json:"before_or_at,omitempty"`
	LedgerEnd     int64                  `protobuf:"varint,2,opt,name=ledger_end,json=ledgerEnd,proto3" json:"ledger_end,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetSafePruningOffsetRequest) Reset() {
	*x = GetSafePruningOffsetRequest{}
	mi := &file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetSafePruningOffsetRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetSafePruningOffsetRequest) ProtoMessage() {}

func (x *GetSafePruningOffsetRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetSafePruningOffsetRequest.ProtoReflect.Descriptor instead.
func (*GetSafePruningOffsetRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_rawDescGZIP(), []int{2}
}

func (x *GetSafePruningOffsetRequest) GetBeforeOrAt() *timestamppb.Timestamp {
	if x != nil {
		return x.BeforeOrAt
	}
	return nil
}

func (x *GetSafePruningOffsetRequest) GetLedgerEnd() int64 {
	if x != nil {
		return x.LedgerEnd
	}
	return 0
}

type GetSafePruningOffsetResponse struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// Types that are valid to be assigned to Response:
	//
	//	*GetSafePruningOffsetResponse_SafePruningOffset
	//	*GetSafePruningOffsetResponse_NoSafePruningOffset_
	Response      isGetSafePruningOffsetResponse_Response `protobuf_oneof:"response"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetSafePruningOffsetResponse) Reset() {
	*x = GetSafePruningOffsetResponse{}
	mi := &file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetSafePruningOffsetResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetSafePruningOffsetResponse) ProtoMessage() {}

func (x *GetSafePruningOffsetResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetSafePruningOffsetResponse.ProtoReflect.Descriptor instead.
func (*GetSafePruningOffsetResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_rawDescGZIP(), []int{3}
}

func (x *GetSafePruningOffsetResponse) GetResponse() isGetSafePruningOffsetResponse_Response {
	if x != nil {
		return x.Response
	}
	return nil
}

func (x *GetSafePruningOffsetResponse) GetSafePruningOffset() int64 {
	if x != nil {
		if x, ok := x.Response.(*GetSafePruningOffsetResponse_SafePruningOffset); ok {
			return x.SafePruningOffset
		}
	}
	return 0
}

func (x *GetSafePruningOffsetResponse) GetNoSafePruningOffset() *GetSafePruningOffsetResponse_NoSafePruningOffset {
	if x != nil {
		if x, ok := x.Response.(*GetSafePruningOffsetResponse_NoSafePruningOffset_); ok {
			return x.NoSafePruningOffset
		}
	}
	return nil
}

type isGetSafePruningOffsetResponse_Response interface {
	isGetSafePruningOffsetResponse_Response()
}

type GetSafePruningOffsetResponse_SafePruningOffset struct {
	SafePruningOffset int64 `protobuf:"varint,1,opt,name=safe_pruning_offset,json=safePruningOffset,proto3,oneof"`
}

type GetSafePruningOffsetResponse_NoSafePruningOffset_ struct {
	NoSafePruningOffset *GetSafePruningOffsetResponse_NoSafePruningOffset `protobuf:"bytes,2,opt,name=no_safe_pruning_offset,json=noSafePruningOffset,proto3,oneof"`
}

func (*GetSafePruningOffsetResponse_SafePruningOffset) isGetSafePruningOffsetResponse_Response() {}

func (*GetSafePruningOffsetResponse_NoSafePruningOffset_) isGetSafePruningOffsetResponse_Response() {}

type GetSafePruningOffsetResponse_NoSafePruningOffset struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetSafePruningOffsetResponse_NoSafePruningOffset) Reset() {
	*x = GetSafePruningOffsetResponse_NoSafePruningOffset{}
	mi := &file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetSafePruningOffsetResponse_NoSafePruningOffset) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetSafePruningOffsetResponse_NoSafePruningOffset) ProtoMessage() {}

func (x *GetSafePruningOffsetResponse_NoSafePruningOffset) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetSafePruningOffsetResponse_NoSafePruningOffset.ProtoReflect.Descriptor instead.
func (*GetSafePruningOffsetResponse_NoSafePruningOffset) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_rawDescGZIP(), []int{3, 0}
}

var File_com_digitalasset_canton_admin_participant_v30_pruning_service_proto protoreflect.FileDescriptor

const file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_rawDesc = "" +
	"\n" +
	"Ccom/digitalasset/canton/admin/participant/v30/pruning_service.proto\x12-com.digitalasset.canton.admin.participant.v30\x1a7com/digitalasset/canton/admin/pruning/v30/pruning.proto\x1a\x1fgoogle/protobuf/timestamp.proto\".\n" +
	"\fPruneRequest\x12\x1e\n" +
	"\vprune_up_to\x18\x01 \x01(\x03R\tpruneUpTo\"\x0f\n" +
	"\rPruneResponse\"z\n" +
	"\x1bGetSafePruningOffsetRequest\x12<\n" +
	"\fbefore_or_at\x18\x01 \x01(\v2\x1a.google.protobuf.TimestampR\n" +
	"beforeOrAt\x12\x1d\n" +
	"\n" +
	"ledger_end\x18\x02 \x01(\x03R\tledgerEnd\"\x8c\x02\n" +
	"\x1cGetSafePruningOffsetResponse\x120\n" +
	"\x13safe_pruning_offset\x18\x01 \x01(\x03H\x00R\x11safePruningOffset\x12\x96\x01\n" +
	"\x16no_safe_pruning_offset\x18\x02 \x01(\v2_.com.digitalasset.canton.admin.participant.v30.GetSafePruningOffsetResponse.NoSafePruningOffsetH\x00R\x13noSafePruningOffset\x1a\x15\n" +
	"\x13NoSafePruningOffsetB\n" +
	"\n" +
	"\bresponse2\xaf\x10\n" +
	"\x0ePruningService\x12\x82\x01\n" +
	"\x05Prune\x12;.com.digitalasset.canton.admin.participant.v30.PruneRequest\x1a<.com.digitalasset.canton.admin.participant.v30.PruneResponse\x12\xaf\x01\n" +
	"\x14GetSafePruningOffset\x12J.com.digitalasset.canton.admin.participant.v30.GetSafePruningOffsetRequest\x1aK.com.digitalasset.canton.admin.participant.v30.GetSafePruningOffsetResponse\x12\x8c\x01\n" +
	"\vSetSchedule\x12=.com.digitalasset.canton.admin.pruning.v30.SetScheduleRequest\x1a>.com.digitalasset.canton.admin.pruning.v30.SetScheduleResponse\x12\xad\x01\n" +
	"\x16SetParticipantSchedule\x12H.com.digitalasset.canton.admin.pruning.v30.SetParticipantScheduleRequest\x1aI.com.digitalasset.canton.admin.pruning.v30.SetParticipantScheduleResponse\x12\x80\x01\n" +
	"\aSetCron\x129.com.digitalasset.canton.admin.pruning.v30.SetCronRequest\x1a:.com.digitalasset.canton.admin.pruning.v30.SetCronResponse\x12\x95\x01\n" +
	"\x0eSetMaxDuration\x12@.com.digitalasset.canton.admin.pruning.v30.SetMaxDurationRequest\x1aA.com.digitalasset.canton.admin.pruning.v30.SetMaxDurationResponse\x12\x8f\x01\n" +
	"\fSetRetention\x12>.com.digitalasset.canton.admin.pruning.v30.SetRetentionRequest\x1a?.com.digitalasset.canton.admin.pruning.v30.SetRetentionResponse\x12\x92\x01\n" +
	"\rClearSchedule\x12?.com.digitalasset.canton.admin.pruning.v30.ClearScheduleRequest\x1a@.com.digitalasset.canton.admin.pruning.v30.ClearScheduleResponse\x12\x8c\x01\n" +
	"\vGetSchedule\x12=.com.digitalasset.canton.admin.pruning.v30.GetScheduleRequest\x1a>.com.digitalasset.canton.admin.pruning.v30.GetScheduleResponse\x12\xad\x01\n" +
	"\x16GetParticipantSchedule\x12H.com.digitalasset.canton.admin.pruning.v30.GetParticipantScheduleRequest\x1aI.com.digitalasset.canton.admin.pruning.v30.GetParticipantScheduleResponse\x12\xb3\x01\n" +
	"\x18SetNoWaitCommitmentsFrom\x12J.com.digitalasset.canton.admin.pruning.v30.SetNoWaitCommitmentsFromRequest\x1aK.com.digitalasset.canton.admin.pruning.v30.SetNoWaitCommitmentsFromResponse\x12\xb9\x01\n" +
	"\x1aResetNoWaitCommitmentsFrom\x12L.com.digitalasset.canton.admin.pruning.v30.ResetNoWaitCommitmentsFromRequest\x1aM.com.digitalasset.canton.admin.pruning.v30.ResetNoWaitCommitmentsFromResponse\x12\xb3\x01\n" +
	"\x18GetNoWaitCommitmentsFrom\x12J.com.digitalasset.canton.admin.pruning.v30.GetNoWaitCommitmentsFromRequest\x1aK.com.digitalasset.canton.admin.pruning.v30.GetNoWaitCommitmentsFromResponseB^Z\\github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/admin/participant/v30b\x06proto3"

var (
	file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_rawDescData []byte
)

func file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_rawDesc), len(file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_rawDesc)))
	})
	return file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_rawDescData
}

var file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_msgTypes = make([]protoimpl.MessageInfo, 5)
var file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_goTypes = []any{
	(*PruneRequest)(nil),                                     // 0: com.digitalasset.canton.admin.participant.v30.PruneRequest
	(*PruneResponse)(nil),                                    // 1: com.digitalasset.canton.admin.participant.v30.PruneResponse
	(*GetSafePruningOffsetRequest)(nil),                      // 2: com.digitalasset.canton.admin.participant.v30.GetSafePruningOffsetRequest
	(*GetSafePruningOffsetResponse)(nil),                     // 3: com.digitalasset.canton.admin.participant.v30.GetSafePruningOffsetResponse
	(*GetSafePruningOffsetResponse_NoSafePruningOffset)(nil), // 4: com.digitalasset.canton.admin.participant.v30.GetSafePruningOffsetResponse.NoSafePruningOffset
	(*timestamppb.Timestamp)(nil),                            // 5: google.protobuf.Timestamp
	(*v30.SetScheduleRequest)(nil),                           // 6: com.digitalasset.canton.admin.pruning.v30.SetScheduleRequest
	(*v30.SetParticipantScheduleRequest)(nil),                // 7: com.digitalasset.canton.admin.pruning.v30.SetParticipantScheduleRequest
	(*v30.SetCronRequest)(nil),                               // 8: com.digitalasset.canton.admin.pruning.v30.SetCronRequest
	(*v30.SetMaxDurationRequest)(nil),                        // 9: com.digitalasset.canton.admin.pruning.v30.SetMaxDurationRequest
	(*v30.SetRetentionRequest)(nil),                          // 10: com.digitalasset.canton.admin.pruning.v30.SetRetentionRequest
	(*v30.ClearScheduleRequest)(nil),                         // 11: com.digitalasset.canton.admin.pruning.v30.ClearScheduleRequest
	(*v30.GetScheduleRequest)(nil),                           // 12: com.digitalasset.canton.admin.pruning.v30.GetScheduleRequest
	(*v30.GetParticipantScheduleRequest)(nil),                // 13: com.digitalasset.canton.admin.pruning.v30.GetParticipantScheduleRequest
	(*v30.SetNoWaitCommitmentsFromRequest)(nil),              // 14: com.digitalasset.canton.admin.pruning.v30.SetNoWaitCommitmentsFromRequest
	(*v30.ResetNoWaitCommitmentsFromRequest)(nil),            // 15: com.digitalasset.canton.admin.pruning.v30.ResetNoWaitCommitmentsFromRequest
	(*v30.GetNoWaitCommitmentsFromRequest)(nil),              // 16: com.digitalasset.canton.admin.pruning.v30.GetNoWaitCommitmentsFromRequest
	(*v30.SetScheduleResponse)(nil),                          // 17: com.digitalasset.canton.admin.pruning.v30.SetScheduleResponse
	(*v30.SetParticipantScheduleResponse)(nil),               // 18: com.digitalasset.canton.admin.pruning.v30.SetParticipantScheduleResponse
	(*v30.SetCronResponse)(nil),                              // 19: com.digitalasset.canton.admin.pruning.v30.SetCronResponse
	(*v30.SetMaxDurationResponse)(nil),                       // 20: com.digitalasset.canton.admin.pruning.v30.SetMaxDurationResponse
	(*v30.SetRetentionResponse)(nil),                         // 21: com.digitalasset.canton.admin.pruning.v30.SetRetentionResponse
	(*v30.ClearScheduleResponse)(nil),                        // 22: com.digitalasset.canton.admin.pruning.v30.ClearScheduleResponse
	(*v30.GetScheduleResponse)(nil),                          // 23: com.digitalasset.canton.admin.pruning.v30.GetScheduleResponse
	(*v30.GetParticipantScheduleResponse)(nil),               // 24: com.digitalasset.canton.admin.pruning.v30.GetParticipantScheduleResponse
	(*v30.SetNoWaitCommitmentsFromResponse)(nil),             // 25: com.digitalasset.canton.admin.pruning.v30.SetNoWaitCommitmentsFromResponse
	(*v30.ResetNoWaitCommitmentsFromResponse)(nil),           // 26: com.digitalasset.canton.admin.pruning.v30.ResetNoWaitCommitmentsFromResponse
	(*v30.GetNoWaitCommitmentsFromResponse)(nil),             // 27: com.digitalasset.canton.admin.pruning.v30.GetNoWaitCommitmentsFromResponse
}
var file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_depIdxs = []int32{
	5,  // 0: com.digitalasset.canton.admin.participant.v30.GetSafePruningOffsetRequest.before_or_at:type_name -> google.protobuf.Timestamp
	4,  // 1: com.digitalasset.canton.admin.participant.v30.GetSafePruningOffsetResponse.no_safe_pruning_offset:type_name -> com.digitalasset.canton.admin.participant.v30.GetSafePruningOffsetResponse.NoSafePruningOffset
	0,  // 2: com.digitalasset.canton.admin.participant.v30.PruningService.Prune:input_type -> com.digitalasset.canton.admin.participant.v30.PruneRequest
	2,  // 3: com.digitalasset.canton.admin.participant.v30.PruningService.GetSafePruningOffset:input_type -> com.digitalasset.canton.admin.participant.v30.GetSafePruningOffsetRequest
	6,  // 4: com.digitalasset.canton.admin.participant.v30.PruningService.SetSchedule:input_type -> com.digitalasset.canton.admin.pruning.v30.SetScheduleRequest
	7,  // 5: com.digitalasset.canton.admin.participant.v30.PruningService.SetParticipantSchedule:input_type -> com.digitalasset.canton.admin.pruning.v30.SetParticipantScheduleRequest
	8,  // 6: com.digitalasset.canton.admin.participant.v30.PruningService.SetCron:input_type -> com.digitalasset.canton.admin.pruning.v30.SetCronRequest
	9,  // 7: com.digitalasset.canton.admin.participant.v30.PruningService.SetMaxDuration:input_type -> com.digitalasset.canton.admin.pruning.v30.SetMaxDurationRequest
	10, // 8: com.digitalasset.canton.admin.participant.v30.PruningService.SetRetention:input_type -> com.digitalasset.canton.admin.pruning.v30.SetRetentionRequest
	11, // 9: com.digitalasset.canton.admin.participant.v30.PruningService.ClearSchedule:input_type -> com.digitalasset.canton.admin.pruning.v30.ClearScheduleRequest
	12, // 10: com.digitalasset.canton.admin.participant.v30.PruningService.GetSchedule:input_type -> com.digitalasset.canton.admin.pruning.v30.GetScheduleRequest
	13, // 11: com.digitalasset.canton.admin.participant.v30.PruningService.GetParticipantSchedule:input_type -> com.digitalasset.canton.admin.pruning.v30.GetParticipantScheduleRequest
	14, // 12: com.digitalasset.canton.admin.participant.v30.PruningService.SetNoWaitCommitmentsFrom:input_type -> com.digitalasset.canton.admin.pruning.v30.SetNoWaitCommitmentsFromRequest
	15, // 13: com.digitalasset.canton.admin.participant.v30.PruningService.ResetNoWaitCommitmentsFrom:input_type -> com.digitalasset.canton.admin.pruning.v30.ResetNoWaitCommitmentsFromRequest
	16, // 14: com.digitalasset.canton.admin.participant.v30.PruningService.GetNoWaitCommitmentsFrom:input_type -> com.digitalasset.canton.admin.pruning.v30.GetNoWaitCommitmentsFromRequest
	1,  // 15: com.digitalasset.canton.admin.participant.v30.PruningService.Prune:output_type -> com.digitalasset.canton.admin.participant.v30.PruneResponse
	3,  // 16: com.digitalasset.canton.admin.participant.v30.PruningService.GetSafePruningOffset:output_type -> com.digitalasset.canton.admin.participant.v30.GetSafePruningOffsetResponse
	17, // 17: com.digitalasset.canton.admin.participant.v30.PruningService.SetSchedule:output_type -> com.digitalasset.canton.admin.pruning.v30.SetScheduleResponse
	18, // 18: com.digitalasset.canton.admin.participant.v30.PruningService.SetParticipantSchedule:output_type -> com.digitalasset.canton.admin.pruning.v30.SetParticipantScheduleResponse
	19, // 19: com.digitalasset.canton.admin.participant.v30.PruningService.SetCron:output_type -> com.digitalasset.canton.admin.pruning.v30.SetCronResponse
	20, // 20: com.digitalasset.canton.admin.participant.v30.PruningService.SetMaxDuration:output_type -> com.digitalasset.canton.admin.pruning.v30.SetMaxDurationResponse
	21, // 21: com.digitalasset.canton.admin.participant.v30.PruningService.SetRetention:output_type -> com.digitalasset.canton.admin.pruning.v30.SetRetentionResponse
	22, // 22: com.digitalasset.canton.admin.participant.v30.PruningService.ClearSchedule:output_type -> com.digitalasset.canton.admin.pruning.v30.ClearScheduleResponse
	23, // 23: com.digitalasset.canton.admin.participant.v30.PruningService.GetSchedule:output_type -> com.digitalasset.canton.admin.pruning.v30.GetScheduleResponse
	24, // 24: com.digitalasset.canton.admin.participant.v30.PruningService.GetParticipantSchedule:output_type -> com.digitalasset.canton.admin.pruning.v30.GetParticipantScheduleResponse
	25, // 25: com.digitalasset.canton.admin.participant.v30.PruningService.SetNoWaitCommitmentsFrom:output_type -> com.digitalasset.canton.admin.pruning.v30.SetNoWaitCommitmentsFromResponse
	26, // 26: com.digitalasset.canton.admin.participant.v30.PruningService.ResetNoWaitCommitmentsFrom:output_type -> com.digitalasset.canton.admin.pruning.v30.ResetNoWaitCommitmentsFromResponse
	27, // 27: com.digitalasset.canton.admin.participant.v30.PruningService.GetNoWaitCommitmentsFrom:output_type -> com.digitalasset.canton.admin.pruning.v30.GetNoWaitCommitmentsFromResponse
	15, // [15:28] is the sub-list for method output_type
	2,  // [2:15] is the sub-list for method input_type
	2,  // [2:2] is the sub-list for extension type_name
	2,  // [2:2] is the sub-list for extension extendee
	0,  // [0:2] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_init() }
func file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_init() {
	if File_com_digitalasset_canton_admin_participant_v30_pruning_service_proto != nil {
		return
	}
	file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_msgTypes[3].OneofWrappers = []any{
		(*GetSafePruningOffsetResponse_SafePruningOffset)(nil),
		(*GetSafePruningOffsetResponse_NoSafePruningOffset_)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_rawDesc), len(file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   5,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_admin_participant_v30_pruning_service_proto = out.File
	file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_goTypes = nil
	file_com_digitalasset_canton_admin_participant_v30_pruning_service_proto_depIdxs = nil
}
