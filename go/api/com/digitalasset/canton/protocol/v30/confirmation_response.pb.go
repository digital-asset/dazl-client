// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/protocol/v30/confirmation_response.proto

package v30

import (
	status "google.golang.org/genproto/googleapis/rpc/status"
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

type LocalVerdict_VerdictCode int32

const (
	LocalVerdict_VERDICT_CODE_UNSPECIFIED     LocalVerdict_VerdictCode = 0
	LocalVerdict_VERDICT_CODE_LOCAL_APPROVE   LocalVerdict_VerdictCode = 1
	LocalVerdict_VERDICT_CODE_LOCAL_REJECT    LocalVerdict_VerdictCode = 2
	LocalVerdict_VERDICT_CODE_LOCAL_MALFORMED LocalVerdict_VerdictCode = 3
)

// Enum value maps for LocalVerdict_VerdictCode.
var (
	LocalVerdict_VerdictCode_name = map[int32]string{
		0: "VERDICT_CODE_UNSPECIFIED",
		1: "VERDICT_CODE_LOCAL_APPROVE",
		2: "VERDICT_CODE_LOCAL_REJECT",
		3: "VERDICT_CODE_LOCAL_MALFORMED",
	}
	LocalVerdict_VerdictCode_value = map[string]int32{
		"VERDICT_CODE_UNSPECIFIED":     0,
		"VERDICT_CODE_LOCAL_APPROVE":   1,
		"VERDICT_CODE_LOCAL_REJECT":    2,
		"VERDICT_CODE_LOCAL_MALFORMED": 3,
	}
)

func (x LocalVerdict_VerdictCode) Enum() *LocalVerdict_VerdictCode {
	p := new(LocalVerdict_VerdictCode)
	*p = x
	return p
}

func (x LocalVerdict_VerdictCode) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (LocalVerdict_VerdictCode) Descriptor() protoreflect.EnumDescriptor {
	return file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_enumTypes[0].Descriptor()
}

func (LocalVerdict_VerdictCode) Type() protoreflect.EnumType {
	return &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_enumTypes[0]
}

func (x LocalVerdict_VerdictCode) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use LocalVerdict_VerdictCode.Descriptor instead.
func (LocalVerdict_VerdictCode) EnumDescriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescGZIP(), []int{0, 0}
}

type LocalVerdict struct {
	state         protoimpl.MessageState   `protogen:"open.v1"`
	Code          LocalVerdict_VerdictCode `protobuf:"varint,1,opt,name=code,proto3,enum=com.digitalasset.canton.protocol.v30.LocalVerdict_VerdictCode" json:"code,omitempty"`
	Reason        *status.Status           `protobuf:"bytes,2,opt,name=reason,proto3" json:"reason,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *LocalVerdict) Reset() {
	*x = LocalVerdict{}
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *LocalVerdict) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*LocalVerdict) ProtoMessage() {}

func (x *LocalVerdict) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use LocalVerdict.ProtoReflect.Descriptor instead.
func (*LocalVerdict) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescGZIP(), []int{0}
}

func (x *LocalVerdict) GetCode() LocalVerdict_VerdictCode {
	if x != nil {
		return x.Code
	}
	return LocalVerdict_VERDICT_CODE_UNSPECIFIED
}

func (x *LocalVerdict) GetReason() *status.Status {
	if x != nil {
		return x.Reason
	}
	return nil
}

type ConfirmationResponse struct {
	state             protoimpl.MessageState `protogen:"open.v1"`
	LocalVerdict      *LocalVerdict          `protobuf:"bytes,1,opt,name=local_verdict,json=localVerdict,proto3" json:"local_verdict,omitempty"`
	ConfirmingParties []string               `protobuf:"bytes,2,rep,name=confirming_parties,json=confirmingParties,proto3" json:"confirming_parties,omitempty"`
	ViewPosition      *ViewPosition          `protobuf:"bytes,3,opt,name=view_position,json=viewPosition,proto3" json:"view_position,omitempty"`
	unknownFields     protoimpl.UnknownFields
	sizeCache         protoimpl.SizeCache
}

func (x *ConfirmationResponse) Reset() {
	*x = ConfirmationResponse{}
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ConfirmationResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ConfirmationResponse) ProtoMessage() {}

func (x *ConfirmationResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ConfirmationResponse.ProtoReflect.Descriptor instead.
func (*ConfirmationResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescGZIP(), []int{1}
}

func (x *ConfirmationResponse) GetLocalVerdict() *LocalVerdict {
	if x != nil {
		return x.LocalVerdict
	}
	return nil
}

func (x *ConfirmationResponse) GetConfirmingParties() []string {
	if x != nil {
		return x.ConfirmingParties
	}
	return nil
}

func (x *ConfirmationResponse) GetViewPosition() *ViewPosition {
	if x != nil {
		return x.ViewPosition
	}
	return nil
}

type ConfirmationResponses struct {
	state          protoimpl.MessageState  `protogen:"open.v1"`
	RequestId      int64                   `protobuf:"varint,1,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
	RootHash       []byte                  `protobuf:"bytes,2,opt,name=root_hash,json=rootHash,proto3" json:"root_hash,omitempty"`
	SynchronizerId string                  `protobuf:"bytes,3,opt,name=synchronizer_id,json=synchronizerId,proto3" json:"synchronizer_id,omitempty"`
	Sender         string                  `protobuf:"bytes,4,opt,name=sender,proto3" json:"sender,omitempty"`
	Responses      []*ConfirmationResponse `protobuf:"bytes,5,rep,name=responses,proto3" json:"responses,omitempty"`
	unknownFields  protoimpl.UnknownFields
	sizeCache      protoimpl.SizeCache
}

func (x *ConfirmationResponses) Reset() {
	*x = ConfirmationResponses{}
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ConfirmationResponses) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ConfirmationResponses) ProtoMessage() {}

func (x *ConfirmationResponses) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ConfirmationResponses.ProtoReflect.Descriptor instead.
func (*ConfirmationResponses) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescGZIP(), []int{2}
}

func (x *ConfirmationResponses) GetRequestId() int64 {
	if x != nil {
		return x.RequestId
	}
	return 0
}

func (x *ConfirmationResponses) GetRootHash() []byte {
	if x != nil {
		return x.RootHash
	}
	return nil
}

func (x *ConfirmationResponses) GetSynchronizerId() string {
	if x != nil {
		return x.SynchronizerId
	}
	return ""
}

func (x *ConfirmationResponses) GetSender() string {
	if x != nil {
		return x.Sender
	}
	return ""
}

func (x *ConfirmationResponses) GetResponses() []*ConfirmationResponse {
	if x != nil {
		return x.Responses
	}
	return nil
}

type ViewPosition struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Position      []*MerkleSeqIndex      `protobuf:"bytes,1,rep,name=position,proto3" json:"position,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ViewPosition) Reset() {
	*x = ViewPosition{}
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ViewPosition) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ViewPosition) ProtoMessage() {}

func (x *ViewPosition) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ViewPosition.ProtoReflect.Descriptor instead.
func (*ViewPosition) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescGZIP(), []int{3}
}

func (x *ViewPosition) GetPosition() []*MerkleSeqIndex {
	if x != nil {
		return x.Position
	}
	return nil
}

type MerkleSeqIndex struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	IsRight       []bool                 `protobuf:"varint,1,rep,packed,name=is_right,json=isRight,proto3" json:"is_right,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *MerkleSeqIndex) Reset() {
	*x = MerkleSeqIndex{}
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *MerkleSeqIndex) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MerkleSeqIndex) ProtoMessage() {}

func (x *MerkleSeqIndex) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use MerkleSeqIndex.ProtoReflect.Descriptor instead.
func (*MerkleSeqIndex) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescGZIP(), []int{4}
}

func (x *MerkleSeqIndex) GetIsRight() []bool {
	if x != nil {
		return x.IsRight
	}
	return nil
}

var File_com_digitalasset_canton_protocol_v30_confirmation_response_proto protoreflect.FileDescriptor

const file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDesc = "" +
	"\n" +
	"@com/digitalasset/canton/protocol/v30/confirmation_response.proto\x12$com.digitalasset.canton.protocol.v30\x1a\x17google/rpc/status.proto\"\x9d\x02\n" +
	"\fLocalVerdict\x12R\n" +
	"\x04code\x18\x01 \x01(\x0e2>.com.digitalasset.canton.protocol.v30.LocalVerdict.VerdictCodeR\x04code\x12*\n" +
	"\x06reason\x18\x02 \x01(\v2\x12.google.rpc.StatusR\x06reason\"\x8c\x01\n" +
	"\vVerdictCode\x12\x1c\n" +
	"\x18VERDICT_CODE_UNSPECIFIED\x10\x00\x12\x1e\n" +
	"\x1aVERDICT_CODE_LOCAL_APPROVE\x10\x01\x12\x1d\n" +
	"\x19VERDICT_CODE_LOCAL_REJECT\x10\x02\x12 \n" +
	"\x1cVERDICT_CODE_LOCAL_MALFORMED\x10\x03\"\xf7\x01\n" +
	"\x14ConfirmationResponse\x12W\n" +
	"\rlocal_verdict\x18\x01 \x01(\v22.com.digitalasset.canton.protocol.v30.LocalVerdictR\flocalVerdict\x12-\n" +
	"\x12confirming_parties\x18\x02 \x03(\tR\x11confirmingParties\x12W\n" +
	"\rview_position\x18\x03 \x01(\v22.com.digitalasset.canton.protocol.v30.ViewPositionR\fviewPosition\"\xee\x01\n" +
	"\x15ConfirmationResponses\x12\x1d\n" +
	"\n" +
	"request_id\x18\x01 \x01(\x03R\trequestId\x12\x1b\n" +
	"\troot_hash\x18\x02 \x01(\fR\brootHash\x12'\n" +
	"\x0fsynchronizer_id\x18\x03 \x01(\tR\x0esynchronizerId\x12\x16\n" +
	"\x06sender\x18\x04 \x01(\tR\x06sender\x12X\n" +
	"\tresponses\x18\x05 \x03(\v2:.com.digitalasset.canton.protocol.v30.ConfirmationResponseR\tresponses\"`\n" +
	"\fViewPosition\x12P\n" +
	"\bposition\x18\x01 \x03(\v24.com.digitalasset.canton.protocol.v30.MerkleSeqIndexR\bposition\"+\n" +
	"\x0eMerkleSeqIndex\x12\x19\n" +
	"\bis_right\x18\x01 \x03(\bR\aisRightBUZSgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v30b\x06proto3"

var (
	file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescData []byte
)

func file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDesc), len(file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDesc)))
	})
	return file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDescData
}

var file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes = make([]protoimpl.MessageInfo, 5)
var file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_goTypes = []any{
	(LocalVerdict_VerdictCode)(0), // 0: com.digitalasset.canton.protocol.v30.LocalVerdict.VerdictCode
	(*LocalVerdict)(nil),          // 1: com.digitalasset.canton.protocol.v30.LocalVerdict
	(*ConfirmationResponse)(nil),  // 2: com.digitalasset.canton.protocol.v30.ConfirmationResponse
	(*ConfirmationResponses)(nil), // 3: com.digitalasset.canton.protocol.v30.ConfirmationResponses
	(*ViewPosition)(nil),          // 4: com.digitalasset.canton.protocol.v30.ViewPosition
	(*MerkleSeqIndex)(nil),        // 5: com.digitalasset.canton.protocol.v30.MerkleSeqIndex
	(*status.Status)(nil),         // 6: google.rpc.Status
}
var file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_depIdxs = []int32{
	0, // 0: com.digitalasset.canton.protocol.v30.LocalVerdict.code:type_name -> com.digitalasset.canton.protocol.v30.LocalVerdict.VerdictCode
	6, // 1: com.digitalasset.canton.protocol.v30.LocalVerdict.reason:type_name -> google.rpc.Status
	1, // 2: com.digitalasset.canton.protocol.v30.ConfirmationResponse.local_verdict:type_name -> com.digitalasset.canton.protocol.v30.LocalVerdict
	4, // 3: com.digitalasset.canton.protocol.v30.ConfirmationResponse.view_position:type_name -> com.digitalasset.canton.protocol.v30.ViewPosition
	2, // 4: com.digitalasset.canton.protocol.v30.ConfirmationResponses.responses:type_name -> com.digitalasset.canton.protocol.v30.ConfirmationResponse
	5, // 5: com.digitalasset.canton.protocol.v30.ViewPosition.position:type_name -> com.digitalasset.canton.protocol.v30.MerkleSeqIndex
	6, // [6:6] is the sub-list for method output_type
	6, // [6:6] is the sub-list for method input_type
	6, // [6:6] is the sub-list for extension type_name
	6, // [6:6] is the sub-list for extension extendee
	0, // [0:6] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_init() }
func file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_init() {
	if File_com_digitalasset_canton_protocol_v30_confirmation_response_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDesc), len(file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_rawDesc)),
			NumEnums:      1,
			NumMessages:   5,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_depIdxs,
		EnumInfos:         file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_enumTypes,
		MessageInfos:      file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_protocol_v30_confirmation_response_proto = out.File
	file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_goTypes = nil
	file_com_digitalasset_canton_protocol_v30_confirmation_response_proto_depIdxs = nil
}
