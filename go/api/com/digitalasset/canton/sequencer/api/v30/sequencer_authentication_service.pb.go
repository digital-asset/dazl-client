// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/sequencer/api/v30/sequencer_authentication_service.proto

package v30

import (
	v30 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/crypto/v30"
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

type SequencerAuthentication struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SequencerAuthentication) Reset() {
	*x = SequencerAuthentication{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SequencerAuthentication) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerAuthentication) ProtoMessage() {}

func (x *SequencerAuthentication) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SequencerAuthentication.ProtoReflect.Descriptor instead.
func (*SequencerAuthentication) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDescGZIP(), []int{0}
}

type SequencerAuthentication_ChallengeRequest struct {
	state                  protoimpl.MessageState `protogen:"open.v1"`
	Member                 string                 `protobuf:"bytes,1,opt,name=member,proto3" json:"member,omitempty"`
	MemberProtocolVersions []int32                `protobuf:"varint,2,rep,packed,name=member_protocol_versions,json=memberProtocolVersions,proto3" json:"member_protocol_versions,omitempty"`
	unknownFields          protoimpl.UnknownFields
	sizeCache              protoimpl.SizeCache
}

func (x *SequencerAuthentication_ChallengeRequest) Reset() {
	*x = SequencerAuthentication_ChallengeRequest{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SequencerAuthentication_ChallengeRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerAuthentication_ChallengeRequest) ProtoMessage() {}

func (x *SequencerAuthentication_ChallengeRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SequencerAuthentication_ChallengeRequest.ProtoReflect.Descriptor instead.
func (*SequencerAuthentication_ChallengeRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDescGZIP(), []int{0, 0}
}

func (x *SequencerAuthentication_ChallengeRequest) GetMember() string {
	if x != nil {
		return x.Member
	}
	return ""
}

func (x *SequencerAuthentication_ChallengeRequest) GetMemberProtocolVersions() []int32 {
	if x != nil {
		return x.MemberProtocolVersions
	}
	return nil
}

type SequencerAuthentication_ChallengeResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Nonce         []byte                 `protobuf:"bytes,1,opt,name=nonce,proto3" json:"nonce,omitempty"`
	Fingerprints  []string               `protobuf:"bytes,2,rep,name=fingerprints,proto3" json:"fingerprints,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SequencerAuthentication_ChallengeResponse) Reset() {
	*x = SequencerAuthentication_ChallengeResponse{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SequencerAuthentication_ChallengeResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerAuthentication_ChallengeResponse) ProtoMessage() {}

func (x *SequencerAuthentication_ChallengeResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SequencerAuthentication_ChallengeResponse.ProtoReflect.Descriptor instead.
func (*SequencerAuthentication_ChallengeResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDescGZIP(), []int{0, 1}
}

func (x *SequencerAuthentication_ChallengeResponse) GetNonce() []byte {
	if x != nil {
		return x.Nonce
	}
	return nil
}

func (x *SequencerAuthentication_ChallengeResponse) GetFingerprints() []string {
	if x != nil {
		return x.Fingerprints
	}
	return nil
}

type SequencerAuthentication_AuthenticateRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Member        string                 `protobuf:"bytes,1,opt,name=member,proto3" json:"member,omitempty"`
	Signature     *v30.Signature         `protobuf:"bytes,2,opt,name=signature,proto3" json:"signature,omitempty"`
	Nonce         []byte                 `protobuf:"bytes,3,opt,name=nonce,proto3" json:"nonce,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SequencerAuthentication_AuthenticateRequest) Reset() {
	*x = SequencerAuthentication_AuthenticateRequest{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SequencerAuthentication_AuthenticateRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerAuthentication_AuthenticateRequest) ProtoMessage() {}

func (x *SequencerAuthentication_AuthenticateRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SequencerAuthentication_AuthenticateRequest.ProtoReflect.Descriptor instead.
func (*SequencerAuthentication_AuthenticateRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDescGZIP(), []int{0, 2}
}

func (x *SequencerAuthentication_AuthenticateRequest) GetMember() string {
	if x != nil {
		return x.Member
	}
	return ""
}

func (x *SequencerAuthentication_AuthenticateRequest) GetSignature() *v30.Signature {
	if x != nil {
		return x.Signature
	}
	return nil
}

func (x *SequencerAuthentication_AuthenticateRequest) GetNonce() []byte {
	if x != nil {
		return x.Nonce
	}
	return nil
}

type SequencerAuthentication_AuthenticateResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Token         []byte                 `protobuf:"bytes,1,opt,name=token,proto3" json:"token,omitempty"`
	ExpiresAt     *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=expires_at,json=expiresAt,proto3" json:"expires_at,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SequencerAuthentication_AuthenticateResponse) Reset() {
	*x = SequencerAuthentication_AuthenticateResponse{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SequencerAuthentication_AuthenticateResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerAuthentication_AuthenticateResponse) ProtoMessage() {}

func (x *SequencerAuthentication_AuthenticateResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SequencerAuthentication_AuthenticateResponse.ProtoReflect.Descriptor instead.
func (*SequencerAuthentication_AuthenticateResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDescGZIP(), []int{0, 3}
}

func (x *SequencerAuthentication_AuthenticateResponse) GetToken() []byte {
	if x != nil {
		return x.Token
	}
	return nil
}

func (x *SequencerAuthentication_AuthenticateResponse) GetExpiresAt() *timestamppb.Timestamp {
	if x != nil {
		return x.ExpiresAt
	}
	return nil
}

type SequencerAuthentication_LogoutRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Token         []byte                 `protobuf:"bytes,1,opt,name=token,proto3" json:"token,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SequencerAuthentication_LogoutRequest) Reset() {
	*x = SequencerAuthentication_LogoutRequest{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SequencerAuthentication_LogoutRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerAuthentication_LogoutRequest) ProtoMessage() {}

func (x *SequencerAuthentication_LogoutRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_msgTypes[5]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SequencerAuthentication_LogoutRequest.ProtoReflect.Descriptor instead.
func (*SequencerAuthentication_LogoutRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDescGZIP(), []int{0, 4}
}

func (x *SequencerAuthentication_LogoutRequest) GetToken() []byte {
	if x != nil {
		return x.Token
	}
	return nil
}

type SequencerAuthentication_LogoutResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SequencerAuthentication_LogoutResponse) Reset() {
	*x = SequencerAuthentication_LogoutResponse{}
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_msgTypes[6]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SequencerAuthentication_LogoutResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SequencerAuthentication_LogoutResponse) ProtoMessage() {}

func (x *SequencerAuthentication_LogoutResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_msgTypes[6]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SequencerAuthentication_LogoutResponse.ProtoReflect.Descriptor instead.
func (*SequencerAuthentication_LogoutResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDescGZIP(), []int{0, 5}
}

var File_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto protoreflect.FileDescriptor

const file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDesc = "" +
	"\n" +
	"Pcom/digitalasset/canton/sequencer/api/v30/sequencer_authentication_service.proto\x12)com.digitalasset.canton.sequencer.api.v30\x1a/com/digitalasset/canton/crypto/v30/crypto.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x83\x04\n" +
	"\x17SequencerAuthentication\x1ad\n" +
	"\x10ChallengeRequest\x12\x16\n" +
	"\x06member\x18\x01 \x01(\tR\x06member\x128\n" +
	"\x18member_protocol_versions\x18\x02 \x03(\x05R\x16memberProtocolVersions\x1aM\n" +
	"\x11ChallengeResponse\x12\x14\n" +
	"\x05nonce\x18\x01 \x01(\fR\x05nonce\x12\"\n" +
	"\ffingerprints\x18\x02 \x03(\tR\ffingerprints\x1a\x90\x01\n" +
	"\x13AuthenticateRequest\x12\x16\n" +
	"\x06member\x18\x01 \x01(\tR\x06member\x12K\n" +
	"\tsignature\x18\x02 \x01(\v2-.com.digitalasset.canton.crypto.v30.SignatureR\tsignature\x12\x14\n" +
	"\x05nonce\x18\x03 \x01(\fR\x05nonce\x1ag\n" +
	"\x14AuthenticateResponse\x12\x14\n" +
	"\x05token\x18\x01 \x01(\fR\x05token\x129\n" +
	"\n" +
	"expires_at\x18\x02 \x01(\v2\x1a.google.protobuf.TimestampR\texpiresAt\x1a%\n" +
	"\rLogoutRequest\x12\x14\n" +
	"\x05token\x18\x01 \x01(\fR\x05token\x1a\x10\n" +
	"\x0eLogoutResponse2\xd1\x04\n" +
	"\x1eSequencerAuthenticationService\x12\xb8\x01\n" +
	"\tChallenge\x12S.com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.ChallengeRequest\x1aT.com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.ChallengeResponse\"\x00\x12\xc1\x01\n" +
	"\fAuthenticate\x12V.com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.AuthenticateRequest\x1aW.com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.AuthenticateResponse\"\x00\x12\xaf\x01\n" +
	"\x06Logout\x12P.com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.LogoutRequest\x1aQ.com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.LogoutResponse\"\x00BZZXgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/sequencer/api/v30b\x06proto3"

var (
	file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDescData []byte
)

func file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDesc), len(file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDesc)))
	})
	return file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDescData
}

var file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_msgTypes = make([]protoimpl.MessageInfo, 7)
var file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_goTypes = []any{
	(*SequencerAuthentication)(nil),                      // 0: com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication
	(*SequencerAuthentication_ChallengeRequest)(nil),     // 1: com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.ChallengeRequest
	(*SequencerAuthentication_ChallengeResponse)(nil),    // 2: com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.ChallengeResponse
	(*SequencerAuthentication_AuthenticateRequest)(nil),  // 3: com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.AuthenticateRequest
	(*SequencerAuthentication_AuthenticateResponse)(nil), // 4: com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.AuthenticateResponse
	(*SequencerAuthentication_LogoutRequest)(nil),        // 5: com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.LogoutRequest
	(*SequencerAuthentication_LogoutResponse)(nil),       // 6: com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.LogoutResponse
	(*v30.Signature)(nil),                                // 7: com.digitalasset.canton.crypto.v30.Signature
	(*timestamppb.Timestamp)(nil),                        // 8: google.protobuf.Timestamp
}
var file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_depIdxs = []int32{
	7, // 0: com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.AuthenticateRequest.signature:type_name -> com.digitalasset.canton.crypto.v30.Signature
	8, // 1: com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.AuthenticateResponse.expires_at:type_name -> google.protobuf.Timestamp
	1, // 2: com.digitalasset.canton.sequencer.api.v30.SequencerAuthenticationService.Challenge:input_type -> com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.ChallengeRequest
	3, // 3: com.digitalasset.canton.sequencer.api.v30.SequencerAuthenticationService.Authenticate:input_type -> com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.AuthenticateRequest
	5, // 4: com.digitalasset.canton.sequencer.api.v30.SequencerAuthenticationService.Logout:input_type -> com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.LogoutRequest
	2, // 5: com.digitalasset.canton.sequencer.api.v30.SequencerAuthenticationService.Challenge:output_type -> com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.ChallengeResponse
	4, // 6: com.digitalasset.canton.sequencer.api.v30.SequencerAuthenticationService.Authenticate:output_type -> com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.AuthenticateResponse
	6, // 7: com.digitalasset.canton.sequencer.api.v30.SequencerAuthenticationService.Logout:output_type -> com.digitalasset.canton.sequencer.api.v30.SequencerAuthentication.LogoutResponse
	5, // [5:8] is the sub-list for method output_type
	2, // [2:5] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() {
	file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_init()
}
func file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_init() {
	if File_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDesc), len(file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   7,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto = out.File
	file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_goTypes = nil
	file_com_digitalasset_canton_sequencer_api_v30_sequencer_authentication_service_proto_depIdxs = nil
}
