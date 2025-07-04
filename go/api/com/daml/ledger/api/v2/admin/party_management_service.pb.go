// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/daml/ledger/api/v2/admin/party_management_service.proto

package admin

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	fieldmaskpb "google.golang.org/protobuf/types/known/fieldmaskpb"
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

type GetParticipantIdRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetParticipantIdRequest) Reset() {
	*x = GetParticipantIdRequest{}
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetParticipantIdRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetParticipantIdRequest) ProtoMessage() {}

func (x *GetParticipantIdRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetParticipantIdRequest.ProtoReflect.Descriptor instead.
func (*GetParticipantIdRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescGZIP(), []int{0}
}

type GetParticipantIdResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	ParticipantId string                 `protobuf:"bytes,1,opt,name=participant_id,json=participantId,proto3" json:"participant_id,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetParticipantIdResponse) Reset() {
	*x = GetParticipantIdResponse{}
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetParticipantIdResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetParticipantIdResponse) ProtoMessage() {}

func (x *GetParticipantIdResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetParticipantIdResponse.ProtoReflect.Descriptor instead.
func (*GetParticipantIdResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescGZIP(), []int{1}
}

func (x *GetParticipantIdResponse) GetParticipantId() string {
	if x != nil {
		return x.ParticipantId
	}
	return ""
}

type GetPartiesRequest struct {
	state              protoimpl.MessageState `protogen:"open.v1"`
	Parties            []string               `protobuf:"bytes,1,rep,name=parties,proto3" json:"parties,omitempty"`
	IdentityProviderId string                 `protobuf:"bytes,2,opt,name=identity_provider_id,json=identityProviderId,proto3" json:"identity_provider_id,omitempty"`
	unknownFields      protoimpl.UnknownFields
	sizeCache          protoimpl.SizeCache
}

func (x *GetPartiesRequest) Reset() {
	*x = GetPartiesRequest{}
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetPartiesRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetPartiesRequest) ProtoMessage() {}

func (x *GetPartiesRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetPartiesRequest.ProtoReflect.Descriptor instead.
func (*GetPartiesRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescGZIP(), []int{2}
}

func (x *GetPartiesRequest) GetParties() []string {
	if x != nil {
		return x.Parties
	}
	return nil
}

func (x *GetPartiesRequest) GetIdentityProviderId() string {
	if x != nil {
		return x.IdentityProviderId
	}
	return ""
}

type GetPartiesResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	PartyDetails  []*PartyDetails        `protobuf:"bytes,1,rep,name=party_details,json=partyDetails,proto3" json:"party_details,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetPartiesResponse) Reset() {
	*x = GetPartiesResponse{}
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetPartiesResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetPartiesResponse) ProtoMessage() {}

func (x *GetPartiesResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetPartiesResponse.ProtoReflect.Descriptor instead.
func (*GetPartiesResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescGZIP(), []int{3}
}

func (x *GetPartiesResponse) GetPartyDetails() []*PartyDetails {
	if x != nil {
		return x.PartyDetails
	}
	return nil
}

type ListKnownPartiesRequest struct {
	state              protoimpl.MessageState `protogen:"open.v1"`
	PageToken          string                 `protobuf:"bytes,2,opt,name=page_token,json=pageToken,proto3" json:"page_token,omitempty"`
	PageSize           int32                  `protobuf:"varint,3,opt,name=page_size,json=pageSize,proto3" json:"page_size,omitempty"`
	IdentityProviderId string                 `protobuf:"bytes,1,opt,name=identity_provider_id,json=identityProviderId,proto3" json:"identity_provider_id,omitempty"`
	unknownFields      protoimpl.UnknownFields
	sizeCache          protoimpl.SizeCache
}

func (x *ListKnownPartiesRequest) Reset() {
	*x = ListKnownPartiesRequest{}
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListKnownPartiesRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListKnownPartiesRequest) ProtoMessage() {}

func (x *ListKnownPartiesRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListKnownPartiesRequest.ProtoReflect.Descriptor instead.
func (*ListKnownPartiesRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescGZIP(), []int{4}
}

func (x *ListKnownPartiesRequest) GetPageToken() string {
	if x != nil {
		return x.PageToken
	}
	return ""
}

func (x *ListKnownPartiesRequest) GetPageSize() int32 {
	if x != nil {
		return x.PageSize
	}
	return 0
}

func (x *ListKnownPartiesRequest) GetIdentityProviderId() string {
	if x != nil {
		return x.IdentityProviderId
	}
	return ""
}

type ListKnownPartiesResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	PartyDetails  []*PartyDetails        `protobuf:"bytes,1,rep,name=party_details,json=partyDetails,proto3" json:"party_details,omitempty"`
	NextPageToken string                 `protobuf:"bytes,2,opt,name=next_page_token,json=nextPageToken,proto3" json:"next_page_token,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ListKnownPartiesResponse) Reset() {
	*x = ListKnownPartiesResponse{}
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ListKnownPartiesResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListKnownPartiesResponse) ProtoMessage() {}

func (x *ListKnownPartiesResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[5]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListKnownPartiesResponse.ProtoReflect.Descriptor instead.
func (*ListKnownPartiesResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescGZIP(), []int{5}
}

func (x *ListKnownPartiesResponse) GetPartyDetails() []*PartyDetails {
	if x != nil {
		return x.PartyDetails
	}
	return nil
}

func (x *ListKnownPartiesResponse) GetNextPageToken() string {
	if x != nil {
		return x.NextPageToken
	}
	return ""
}

type AllocatePartyRequest struct {
	state              protoimpl.MessageState `protogen:"open.v1"`
	PartyIdHint        string                 `protobuf:"bytes,1,opt,name=party_id_hint,json=partyIdHint,proto3" json:"party_id_hint,omitempty"`
	LocalMetadata      *ObjectMeta            `protobuf:"bytes,3,opt,name=local_metadata,json=localMetadata,proto3" json:"local_metadata,omitempty"`
	IdentityProviderId string                 `protobuf:"bytes,4,opt,name=identity_provider_id,json=identityProviderId,proto3" json:"identity_provider_id,omitempty"`
	unknownFields      protoimpl.UnknownFields
	sizeCache          protoimpl.SizeCache
}

func (x *AllocatePartyRequest) Reset() {
	*x = AllocatePartyRequest{}
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[6]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *AllocatePartyRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*AllocatePartyRequest) ProtoMessage() {}

func (x *AllocatePartyRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[6]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use AllocatePartyRequest.ProtoReflect.Descriptor instead.
func (*AllocatePartyRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescGZIP(), []int{6}
}

func (x *AllocatePartyRequest) GetPartyIdHint() string {
	if x != nil {
		return x.PartyIdHint
	}
	return ""
}

func (x *AllocatePartyRequest) GetLocalMetadata() *ObjectMeta {
	if x != nil {
		return x.LocalMetadata
	}
	return nil
}

func (x *AllocatePartyRequest) GetIdentityProviderId() string {
	if x != nil {
		return x.IdentityProviderId
	}
	return ""
}

type AllocatePartyResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	PartyDetails  *PartyDetails          `protobuf:"bytes,1,opt,name=party_details,json=partyDetails,proto3" json:"party_details,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *AllocatePartyResponse) Reset() {
	*x = AllocatePartyResponse{}
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[7]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *AllocatePartyResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*AllocatePartyResponse) ProtoMessage() {}

func (x *AllocatePartyResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[7]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use AllocatePartyResponse.ProtoReflect.Descriptor instead.
func (*AllocatePartyResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescGZIP(), []int{7}
}

func (x *AllocatePartyResponse) GetPartyDetails() *PartyDetails {
	if x != nil {
		return x.PartyDetails
	}
	return nil
}

type UpdatePartyDetailsRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	PartyDetails  *PartyDetails          `protobuf:"bytes,1,opt,name=party_details,json=partyDetails,proto3" json:"party_details,omitempty"`
	UpdateMask    *fieldmaskpb.FieldMask `protobuf:"bytes,2,opt,name=update_mask,json=updateMask,proto3" json:"update_mask,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *UpdatePartyDetailsRequest) Reset() {
	*x = UpdatePartyDetailsRequest{}
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[8]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *UpdatePartyDetailsRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpdatePartyDetailsRequest) ProtoMessage() {}

func (x *UpdatePartyDetailsRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[8]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpdatePartyDetailsRequest.ProtoReflect.Descriptor instead.
func (*UpdatePartyDetailsRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescGZIP(), []int{8}
}

func (x *UpdatePartyDetailsRequest) GetPartyDetails() *PartyDetails {
	if x != nil {
		return x.PartyDetails
	}
	return nil
}

func (x *UpdatePartyDetailsRequest) GetUpdateMask() *fieldmaskpb.FieldMask {
	if x != nil {
		return x.UpdateMask
	}
	return nil
}

type UpdatePartyDetailsResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	PartyDetails  *PartyDetails          `protobuf:"bytes,1,opt,name=party_details,json=partyDetails,proto3" json:"party_details,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *UpdatePartyDetailsResponse) Reset() {
	*x = UpdatePartyDetailsResponse{}
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[9]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *UpdatePartyDetailsResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpdatePartyDetailsResponse) ProtoMessage() {}

func (x *UpdatePartyDetailsResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[9]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpdatePartyDetailsResponse.ProtoReflect.Descriptor instead.
func (*UpdatePartyDetailsResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescGZIP(), []int{9}
}

func (x *UpdatePartyDetailsResponse) GetPartyDetails() *PartyDetails {
	if x != nil {
		return x.PartyDetails
	}
	return nil
}

type PartyDetails struct {
	state              protoimpl.MessageState `protogen:"open.v1"`
	Party              string                 `protobuf:"bytes,1,opt,name=party,proto3" json:"party,omitempty"`
	IsLocal            bool                   `protobuf:"varint,3,opt,name=is_local,json=isLocal,proto3" json:"is_local,omitempty"`
	LocalMetadata      *ObjectMeta            `protobuf:"bytes,4,opt,name=local_metadata,json=localMetadata,proto3" json:"local_metadata,omitempty"`
	IdentityProviderId string                 `protobuf:"bytes,5,opt,name=identity_provider_id,json=identityProviderId,proto3" json:"identity_provider_id,omitempty"`
	unknownFields      protoimpl.UnknownFields
	sizeCache          protoimpl.SizeCache
}

func (x *PartyDetails) Reset() {
	*x = PartyDetails{}
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[10]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PartyDetails) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PartyDetails) ProtoMessage() {}

func (x *PartyDetails) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[10]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PartyDetails.ProtoReflect.Descriptor instead.
func (*PartyDetails) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescGZIP(), []int{10}
}

func (x *PartyDetails) GetParty() string {
	if x != nil {
		return x.Party
	}
	return ""
}

func (x *PartyDetails) GetIsLocal() bool {
	if x != nil {
		return x.IsLocal
	}
	return false
}

func (x *PartyDetails) GetLocalMetadata() *ObjectMeta {
	if x != nil {
		return x.LocalMetadata
	}
	return nil
}

func (x *PartyDetails) GetIdentityProviderId() string {
	if x != nil {
		return x.IdentityProviderId
	}
	return ""
}

type UpdatePartyIdentityProviderIdRequest struct {
	state                    protoimpl.MessageState `protogen:"open.v1"`
	Party                    string                 `protobuf:"bytes,1,opt,name=party,proto3" json:"party,omitempty"`
	SourceIdentityProviderId string                 `protobuf:"bytes,2,opt,name=source_identity_provider_id,json=sourceIdentityProviderId,proto3" json:"source_identity_provider_id,omitempty"`
	TargetIdentityProviderId string                 `protobuf:"bytes,3,opt,name=target_identity_provider_id,json=targetIdentityProviderId,proto3" json:"target_identity_provider_id,omitempty"`
	unknownFields            protoimpl.UnknownFields
	sizeCache                protoimpl.SizeCache
}

func (x *UpdatePartyIdentityProviderIdRequest) Reset() {
	*x = UpdatePartyIdentityProviderIdRequest{}
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[11]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *UpdatePartyIdentityProviderIdRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpdatePartyIdentityProviderIdRequest) ProtoMessage() {}

func (x *UpdatePartyIdentityProviderIdRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[11]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpdatePartyIdentityProviderIdRequest.ProtoReflect.Descriptor instead.
func (*UpdatePartyIdentityProviderIdRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescGZIP(), []int{11}
}

func (x *UpdatePartyIdentityProviderIdRequest) GetParty() string {
	if x != nil {
		return x.Party
	}
	return ""
}

func (x *UpdatePartyIdentityProviderIdRequest) GetSourceIdentityProviderId() string {
	if x != nil {
		return x.SourceIdentityProviderId
	}
	return ""
}

func (x *UpdatePartyIdentityProviderIdRequest) GetTargetIdentityProviderId() string {
	if x != nil {
		return x.TargetIdentityProviderId
	}
	return ""
}

type UpdatePartyIdentityProviderIdResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *UpdatePartyIdentityProviderIdResponse) Reset() {
	*x = UpdatePartyIdentityProviderIdResponse{}
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[12]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *UpdatePartyIdentityProviderIdResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpdatePartyIdentityProviderIdResponse) ProtoMessage() {}

func (x *UpdatePartyIdentityProviderIdResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes[12]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpdatePartyIdentityProviderIdResponse.ProtoReflect.Descriptor instead.
func (*UpdatePartyIdentityProviderIdResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescGZIP(), []int{12}
}

var File_com_daml_ledger_api_v2_admin_party_management_service_proto protoreflect.FileDescriptor

const file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDesc = "" +
	"\n" +
	";com/daml/ledger/api/v2/admin/party_management_service.proto\x12\x1ccom.daml.ledger.api.v2.admin\x1a.com/daml/ledger/api/v2/admin/object_meta.proto\x1a google/protobuf/field_mask.proto\"\x19\n" +
	"\x17GetParticipantIdRequest\"A\n" +
	"\x18GetParticipantIdResponse\x12%\n" +
	"\x0eparticipant_id\x18\x01 \x01(\tR\rparticipantId\"_\n" +
	"\x11GetPartiesRequest\x12\x18\n" +
	"\aparties\x18\x01 \x03(\tR\aparties\x120\n" +
	"\x14identity_provider_id\x18\x02 \x01(\tR\x12identityProviderId\"e\n" +
	"\x12GetPartiesResponse\x12O\n" +
	"\rparty_details\x18\x01 \x03(\v2*.com.daml.ledger.api.v2.admin.PartyDetailsR\fpartyDetails\"\x87\x01\n" +
	"\x17ListKnownPartiesRequest\x12\x1d\n" +
	"\n" +
	"page_token\x18\x02 \x01(\tR\tpageToken\x12\x1b\n" +
	"\tpage_size\x18\x03 \x01(\x05R\bpageSize\x120\n" +
	"\x14identity_provider_id\x18\x01 \x01(\tR\x12identityProviderId\"\x93\x01\n" +
	"\x18ListKnownPartiesResponse\x12O\n" +
	"\rparty_details\x18\x01 \x03(\v2*.com.daml.ledger.api.v2.admin.PartyDetailsR\fpartyDetails\x12&\n" +
	"\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\xc3\x01\n" +
	"\x14AllocatePartyRequest\x12\"\n" +
	"\rparty_id_hint\x18\x01 \x01(\tR\vpartyIdHint\x12O\n" +
	"\x0elocal_metadata\x18\x03 \x01(\v2(.com.daml.ledger.api.v2.admin.ObjectMetaR\rlocalMetadata\x120\n" +
	"\x14identity_provider_id\x18\x04 \x01(\tR\x12identityProviderIdJ\x04\b\x02\x10\x03\"h\n" +
	"\x15AllocatePartyResponse\x12O\n" +
	"\rparty_details\x18\x01 \x01(\v2*.com.daml.ledger.api.v2.admin.PartyDetailsR\fpartyDetails\"\xa9\x01\n" +
	"\x19UpdatePartyDetailsRequest\x12O\n" +
	"\rparty_details\x18\x01 \x01(\v2*.com.daml.ledger.api.v2.admin.PartyDetailsR\fpartyDetails\x12;\n" +
	"\vupdate_mask\x18\x02 \x01(\v2\x1a.google.protobuf.FieldMaskR\n" +
	"updateMask\"m\n" +
	"\x1aUpdatePartyDetailsResponse\x12O\n" +
	"\rparty_details\x18\x01 \x01(\v2*.com.daml.ledger.api.v2.admin.PartyDetailsR\fpartyDetails\"\xc2\x01\n" +
	"\fPartyDetails\x12\x14\n" +
	"\x05party\x18\x01 \x01(\tR\x05party\x12\x19\n" +
	"\bis_local\x18\x03 \x01(\bR\aisLocal\x12O\n" +
	"\x0elocal_metadata\x18\x04 \x01(\v2(.com.daml.ledger.api.v2.admin.ObjectMetaR\rlocalMetadata\x120\n" +
	"\x14identity_provider_id\x18\x05 \x01(\tR\x12identityProviderId\"\xba\x01\n" +
	"$UpdatePartyIdentityProviderIdRequest\x12\x14\n" +
	"\x05party\x18\x01 \x01(\tR\x05party\x12=\n" +
	"\x1bsource_identity_provider_id\x18\x02 \x01(\tR\x18sourceIdentityProviderId\x12=\n" +
	"\x1btarget_identity_provider_id\x18\x03 \x01(\tR\x18targetIdentityProviderId\"'\n" +
	"%UpdatePartyIdentityProviderIdResponse2\xc0\x06\n" +
	"\x16PartyManagementService\x12\x81\x01\n" +
	"\x10GetParticipantId\x125.com.daml.ledger.api.v2.admin.GetParticipantIdRequest\x1a6.com.daml.ledger.api.v2.admin.GetParticipantIdResponse\x12o\n" +
	"\n" +
	"GetParties\x12/.com.daml.ledger.api.v2.admin.GetPartiesRequest\x1a0.com.daml.ledger.api.v2.admin.GetPartiesResponse\x12\x81\x01\n" +
	"\x10ListKnownParties\x125.com.daml.ledger.api.v2.admin.ListKnownPartiesRequest\x1a6.com.daml.ledger.api.v2.admin.ListKnownPartiesResponse\x12x\n" +
	"\rAllocateParty\x122.com.daml.ledger.api.v2.admin.AllocatePartyRequest\x1a3.com.daml.ledger.api.v2.admin.AllocatePartyResponse\x12\x87\x01\n" +
	"\x12UpdatePartyDetails\x127.com.daml.ledger.api.v2.admin.UpdatePartyDetailsRequest\x1a8.com.daml.ledger.api.v2.admin.UpdatePartyDetailsResponse\x12\xa8\x01\n" +
	"\x1dUpdatePartyIdentityProviderId\x12B.com.daml.ledger.api.v2.admin.UpdatePartyIdentityProviderIdRequest\x1aC.com.daml.ledger.api.v2.admin.UpdatePartyIdentityProviderIdResponseB\xac\x01\n" +
	"\x1ccom.daml.ledger.api.v2.adminB PartyManagementServiceOuterClassZKgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2/admin\xaa\x02\x1cCom.Daml.Ledger.Api.V2.Adminb\x06proto3"

var (
	file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescData []byte
)

func file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDesc), len(file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDesc)))
	})
	return file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDescData
}

var file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes = make([]protoimpl.MessageInfo, 13)
var file_com_daml_ledger_api_v2_admin_party_management_service_proto_goTypes = []any{
	(*GetParticipantIdRequest)(nil),               // 0: com.daml.ledger.api.v2.admin.GetParticipantIdRequest
	(*GetParticipantIdResponse)(nil),              // 1: com.daml.ledger.api.v2.admin.GetParticipantIdResponse
	(*GetPartiesRequest)(nil),                     // 2: com.daml.ledger.api.v2.admin.GetPartiesRequest
	(*GetPartiesResponse)(nil),                    // 3: com.daml.ledger.api.v2.admin.GetPartiesResponse
	(*ListKnownPartiesRequest)(nil),               // 4: com.daml.ledger.api.v2.admin.ListKnownPartiesRequest
	(*ListKnownPartiesResponse)(nil),              // 5: com.daml.ledger.api.v2.admin.ListKnownPartiesResponse
	(*AllocatePartyRequest)(nil),                  // 6: com.daml.ledger.api.v2.admin.AllocatePartyRequest
	(*AllocatePartyResponse)(nil),                 // 7: com.daml.ledger.api.v2.admin.AllocatePartyResponse
	(*UpdatePartyDetailsRequest)(nil),             // 8: com.daml.ledger.api.v2.admin.UpdatePartyDetailsRequest
	(*UpdatePartyDetailsResponse)(nil),            // 9: com.daml.ledger.api.v2.admin.UpdatePartyDetailsResponse
	(*PartyDetails)(nil),                          // 10: com.daml.ledger.api.v2.admin.PartyDetails
	(*UpdatePartyIdentityProviderIdRequest)(nil),  // 11: com.daml.ledger.api.v2.admin.UpdatePartyIdentityProviderIdRequest
	(*UpdatePartyIdentityProviderIdResponse)(nil), // 12: com.daml.ledger.api.v2.admin.UpdatePartyIdentityProviderIdResponse
	(*ObjectMeta)(nil),                            // 13: com.daml.ledger.api.v2.admin.ObjectMeta
	(*fieldmaskpb.FieldMask)(nil),                 // 14: google.protobuf.FieldMask
}
var file_com_daml_ledger_api_v2_admin_party_management_service_proto_depIdxs = []int32{
	10, // 0: com.daml.ledger.api.v2.admin.GetPartiesResponse.party_details:type_name -> com.daml.ledger.api.v2.admin.PartyDetails
	10, // 1: com.daml.ledger.api.v2.admin.ListKnownPartiesResponse.party_details:type_name -> com.daml.ledger.api.v2.admin.PartyDetails
	13, // 2: com.daml.ledger.api.v2.admin.AllocatePartyRequest.local_metadata:type_name -> com.daml.ledger.api.v2.admin.ObjectMeta
	10, // 3: com.daml.ledger.api.v2.admin.AllocatePartyResponse.party_details:type_name -> com.daml.ledger.api.v2.admin.PartyDetails
	10, // 4: com.daml.ledger.api.v2.admin.UpdatePartyDetailsRequest.party_details:type_name -> com.daml.ledger.api.v2.admin.PartyDetails
	14, // 5: com.daml.ledger.api.v2.admin.UpdatePartyDetailsRequest.update_mask:type_name -> google.protobuf.FieldMask
	10, // 6: com.daml.ledger.api.v2.admin.UpdatePartyDetailsResponse.party_details:type_name -> com.daml.ledger.api.v2.admin.PartyDetails
	13, // 7: com.daml.ledger.api.v2.admin.PartyDetails.local_metadata:type_name -> com.daml.ledger.api.v2.admin.ObjectMeta
	0,  // 8: com.daml.ledger.api.v2.admin.PartyManagementService.GetParticipantId:input_type -> com.daml.ledger.api.v2.admin.GetParticipantIdRequest
	2,  // 9: com.daml.ledger.api.v2.admin.PartyManagementService.GetParties:input_type -> com.daml.ledger.api.v2.admin.GetPartiesRequest
	4,  // 10: com.daml.ledger.api.v2.admin.PartyManagementService.ListKnownParties:input_type -> com.daml.ledger.api.v2.admin.ListKnownPartiesRequest
	6,  // 11: com.daml.ledger.api.v2.admin.PartyManagementService.AllocateParty:input_type -> com.daml.ledger.api.v2.admin.AllocatePartyRequest
	8,  // 12: com.daml.ledger.api.v2.admin.PartyManagementService.UpdatePartyDetails:input_type -> com.daml.ledger.api.v2.admin.UpdatePartyDetailsRequest
	11, // 13: com.daml.ledger.api.v2.admin.PartyManagementService.UpdatePartyIdentityProviderId:input_type -> com.daml.ledger.api.v2.admin.UpdatePartyIdentityProviderIdRequest
	1,  // 14: com.daml.ledger.api.v2.admin.PartyManagementService.GetParticipantId:output_type -> com.daml.ledger.api.v2.admin.GetParticipantIdResponse
	3,  // 15: com.daml.ledger.api.v2.admin.PartyManagementService.GetParties:output_type -> com.daml.ledger.api.v2.admin.GetPartiesResponse
	5,  // 16: com.daml.ledger.api.v2.admin.PartyManagementService.ListKnownParties:output_type -> com.daml.ledger.api.v2.admin.ListKnownPartiesResponse
	7,  // 17: com.daml.ledger.api.v2.admin.PartyManagementService.AllocateParty:output_type -> com.daml.ledger.api.v2.admin.AllocatePartyResponse
	9,  // 18: com.daml.ledger.api.v2.admin.PartyManagementService.UpdatePartyDetails:output_type -> com.daml.ledger.api.v2.admin.UpdatePartyDetailsResponse
	12, // 19: com.daml.ledger.api.v2.admin.PartyManagementService.UpdatePartyIdentityProviderId:output_type -> com.daml.ledger.api.v2.admin.UpdatePartyIdentityProviderIdResponse
	14, // [14:20] is the sub-list for method output_type
	8,  // [8:14] is the sub-list for method input_type
	8,  // [8:8] is the sub-list for extension type_name
	8,  // [8:8] is the sub-list for extension extendee
	0,  // [0:8] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v2_admin_party_management_service_proto_init() }
func file_com_daml_ledger_api_v2_admin_party_management_service_proto_init() {
	if File_com_daml_ledger_api_v2_admin_party_management_service_proto != nil {
		return
	}
	file_com_daml_ledger_api_v2_admin_object_meta_proto_init()
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDesc), len(file_com_daml_ledger_api_v2_admin_party_management_service_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   13,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_daml_ledger_api_v2_admin_party_management_service_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v2_admin_party_management_service_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v2_admin_party_management_service_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v2_admin_party_management_service_proto = out.File
	file_com_daml_ledger_api_v2_admin_party_management_service_proto_goTypes = nil
	file_com_daml_ledger_api_v2_admin_party_management_service_proto_depIdxs = nil
}
