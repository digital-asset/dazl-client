// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.2
// 	protoc        v5.27.2
// source: com/digitalasset/canton/domain/admin/v0/domain_service.proto

package v0

import (
	v0 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/crypto/v0"
	v01 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v0"
	v1 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v1"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
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

type GetDomainParameters struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *GetDomainParameters) Reset() {
	*x = GetDomainParameters{}
	mi := &file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetDomainParameters) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetDomainParameters) ProtoMessage() {}

func (x *GetDomainParameters) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetDomainParameters.ProtoReflect.Descriptor instead.
func (*GetDomainParameters) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_rawDescGZIP(), []int{0}
}

type ServiceAgreementAcceptances struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Acceptances []*ServiceAgreementAcceptance `protobuf:"bytes,1,rep,name=acceptances,proto3" json:"acceptances,omitempty"`
}

func (x *ServiceAgreementAcceptances) Reset() {
	*x = ServiceAgreementAcceptances{}
	mi := &file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ServiceAgreementAcceptances) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ServiceAgreementAcceptances) ProtoMessage() {}

func (x *ServiceAgreementAcceptances) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ServiceAgreementAcceptances.ProtoReflect.Descriptor instead.
func (*ServiceAgreementAcceptances) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_rawDescGZIP(), []int{1}
}

func (x *ServiceAgreementAcceptances) GetAcceptances() []*ServiceAgreementAcceptance {
	if x != nil {
		return x.Acceptances
	}
	return nil
}

type ServiceAgreementAcceptance struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	AgreementId   string                 `protobuf:"bytes,1,opt,name=agreement_id,json=agreementId,proto3" json:"agreement_id,omitempty"`
	ParticipantId string                 `protobuf:"bytes,2,opt,name=participant_id,json=participantId,proto3" json:"participant_id,omitempty"`
	Signature     *v0.Signature          `protobuf:"bytes,3,opt,name=signature,proto3" json:"signature,omitempty"`
	Timestamp     *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=timestamp,proto3" json:"timestamp,omitempty"`
}

func (x *ServiceAgreementAcceptance) Reset() {
	*x = ServiceAgreementAcceptance{}
	mi := &file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ServiceAgreementAcceptance) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ServiceAgreementAcceptance) ProtoMessage() {}

func (x *ServiceAgreementAcceptance) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ServiceAgreementAcceptance.ProtoReflect.Descriptor instead.
func (*ServiceAgreementAcceptance) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_rawDescGZIP(), []int{2}
}

func (x *ServiceAgreementAcceptance) GetAgreementId() string {
	if x != nil {
		return x.AgreementId
	}
	return ""
}

func (x *ServiceAgreementAcceptance) GetParticipantId() string {
	if x != nil {
		return x.ParticipantId
	}
	return ""
}

func (x *ServiceAgreementAcceptance) GetSignature() *v0.Signature {
	if x != nil {
		return x.Signature
	}
	return nil
}

func (x *ServiceAgreementAcceptance) GetTimestamp() *timestamppb.Timestamp {
	if x != nil {
		return x.Timestamp
	}
	return nil
}

type GetDomainParameters_Request struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *GetDomainParameters_Request) Reset() {
	*x = GetDomainParameters_Request{}
	mi := &file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetDomainParameters_Request) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetDomainParameters_Request) ProtoMessage() {}

func (x *GetDomainParameters_Request) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetDomainParameters_Request.ProtoReflect.Descriptor instead.
func (*GetDomainParameters_Request) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_rawDescGZIP(), []int{0, 0}
}

type GetDomainParameters_Response struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Parameters:
	//
	//	*GetDomainParameters_Response_ParametersV0
	//	*GetDomainParameters_Response_ParametersV1
	Parameters isGetDomainParameters_Response_Parameters `protobuf_oneof:"parameters"`
}

func (x *GetDomainParameters_Response) Reset() {
	*x = GetDomainParameters_Response{}
	mi := &file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetDomainParameters_Response) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetDomainParameters_Response) ProtoMessage() {}

func (x *GetDomainParameters_Response) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetDomainParameters_Response.ProtoReflect.Descriptor instead.
func (*GetDomainParameters_Response) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_rawDescGZIP(), []int{0, 1}
}

func (m *GetDomainParameters_Response) GetParameters() isGetDomainParameters_Response_Parameters {
	if m != nil {
		return m.Parameters
	}
	return nil
}

func (x *GetDomainParameters_Response) GetParametersV0() *v01.StaticDomainParameters {
	if x, ok := x.GetParameters().(*GetDomainParameters_Response_ParametersV0); ok {
		return x.ParametersV0
	}
	return nil
}

func (x *GetDomainParameters_Response) GetParametersV1() *v1.StaticDomainParameters {
	if x, ok := x.GetParameters().(*GetDomainParameters_Response_ParametersV1); ok {
		return x.ParametersV1
	}
	return nil
}

type isGetDomainParameters_Response_Parameters interface {
	isGetDomainParameters_Response_Parameters()
}

type GetDomainParameters_Response_ParametersV0 struct {
	ParametersV0 *v01.StaticDomainParameters `protobuf:"bytes,1,opt,name=parameters_v0,json=parametersV0,proto3,oneof"`
}

type GetDomainParameters_Response_ParametersV1 struct {
	ParametersV1 *v1.StaticDomainParameters `protobuf:"bytes,2,opt,name=parameters_v1,json=parametersV1,proto3,oneof"`
}

func (*GetDomainParameters_Response_ParametersV0) isGetDomainParameters_Response_Parameters() {}

func (*GetDomainParameters_Response_ParametersV1) isGetDomainParameters_Response_Parameters() {}

var File_com_digitalasset_canton_domain_admin_v0_domain_service_proto protoreflect.FileDescriptor

var file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_rawDesc = []byte{
	0x0a, 0x3c, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e,
	0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x76, 0x30, 0x2f, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e,
	0x5f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x27,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2e, 0x61,
	0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x1a, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67,
	0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e,
	0x2f, 0x63, 0x72, 0x79, 0x70, 0x74, 0x6f, 0x2f, 0x76, 0x30, 0x2f, 0x63, 0x72, 0x79, 0x70, 0x74,
	0x6f, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x34, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67,
	0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e,
	0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f, 0x76, 0x30, 0x2f, 0x73, 0x65, 0x71,
	0x75, 0x65, 0x6e, 0x63, 0x69, 0x6e, 0x67, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x34, 0x63,
	0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2f,
	0x76, 0x31, 0x2f, 0x73, 0x65, 0x71, 0x75, 0x65, 0x6e, 0x63, 0x69, 0x6e, 0x67, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x1a, 0x1b, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x62, 0x75, 0x66, 0x2f, 0x65, 0x6d, 0x70, 0x74, 0x79, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75,
	0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x22, 0x83, 0x02, 0x0a, 0x13, 0x47, 0x65, 0x74, 0x44, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x50,
	0x61, 0x72, 0x61, 0x6d, 0x65, 0x74, 0x65, 0x72, 0x73, 0x1a, 0x09, 0x0a, 0x07, 0x52, 0x65, 0x71,
	0x75, 0x65, 0x73, 0x74, 0x1a, 0xe0, 0x01, 0x0a, 0x08, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73,
	0x65, 0x12, 0x62, 0x0a, 0x0d, 0x70, 0x61, 0x72, 0x61, 0x6d, 0x65, 0x74, 0x65, 0x72, 0x73, 0x5f,
	0x76, 0x30, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x3b, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74,
	0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x53,
	0x74, 0x61, 0x74, 0x69, 0x63, 0x44, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x50, 0x61, 0x72, 0x61, 0x6d,
	0x65, 0x74, 0x65, 0x72, 0x73, 0x48, 0x00, 0x52, 0x0c, 0x70, 0x61, 0x72, 0x61, 0x6d, 0x65, 0x74,
	0x65, 0x72, 0x73, 0x56, 0x30, 0x12, 0x62, 0x0a, 0x0d, 0x70, 0x61, 0x72, 0x61, 0x6d, 0x65, 0x74,
	0x65, 0x72, 0x73, 0x5f, 0x76, 0x31, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x3b, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63, 0x6f, 0x6c, 0x2e,
	0x76, 0x31, 0x2e, 0x53, 0x74, 0x61, 0x74, 0x69, 0x63, 0x44, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x50,
	0x61, 0x72, 0x61, 0x6d, 0x65, 0x74, 0x65, 0x72, 0x73, 0x48, 0x00, 0x52, 0x0c, 0x70, 0x61, 0x72,
	0x61, 0x6d, 0x65, 0x74, 0x65, 0x72, 0x73, 0x56, 0x31, 0x42, 0x0c, 0x0a, 0x0a, 0x70, 0x61, 0x72,
	0x61, 0x6d, 0x65, 0x74, 0x65, 0x72, 0x73, 0x22, 0x84, 0x01, 0x0a, 0x1b, 0x53, 0x65, 0x72, 0x76,
	0x69, 0x63, 0x65, 0x41, 0x67, 0x72, 0x65, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x41, 0x63, 0x63, 0x65,
	0x70, 0x74, 0x61, 0x6e, 0x63, 0x65, 0x73, 0x12, 0x65, 0x0a, 0x0b, 0x61, 0x63, 0x63, 0x65, 0x70,
	0x74, 0x61, 0x6e, 0x63, 0x65, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x43, 0x2e, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e,
	0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2e, 0x61, 0x64,
	0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x41, 0x67,
	0x72, 0x65, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x41, 0x63, 0x63, 0x65, 0x70, 0x74, 0x61, 0x6e, 0x63,
	0x65, 0x52, 0x0b, 0x61, 0x63, 0x63, 0x65, 0x70, 0x74, 0x61, 0x6e, 0x63, 0x65, 0x73, 0x22, 0xec,
	0x01, 0x0a, 0x1a, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x41, 0x67, 0x72, 0x65, 0x65, 0x6d,
	0x65, 0x6e, 0x74, 0x41, 0x63, 0x63, 0x65, 0x70, 0x74, 0x61, 0x6e, 0x63, 0x65, 0x12, 0x21, 0x0a,
	0x0c, 0x61, 0x67, 0x72, 0x65, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x0b, 0x61, 0x67, 0x72, 0x65, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x49, 0x64,
	0x12, 0x25, 0x0a, 0x0e, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x5f,
	0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0d, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63,
	0x69, 0x70, 0x61, 0x6e, 0x74, 0x49, 0x64, 0x12, 0x4a, 0x0a, 0x09, 0x73, 0x69, 0x67, 0x6e, 0x61,
	0x74, 0x75, 0x72, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2c, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x63, 0x72, 0x79, 0x70, 0x74, 0x6f, 0x2e, 0x76, 0x30, 0x2e, 0x53,
	0x69, 0x67, 0x6e, 0x61, 0x74, 0x75, 0x72, 0x65, 0x52, 0x09, 0x73, 0x69, 0x67, 0x6e, 0x61, 0x74,
	0x75, 0x72, 0x65, 0x12, 0x38, 0x0a, 0x09, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70,
	0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61,
	0x6d, 0x70, 0x52, 0x09, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x32, 0xaa, 0x03,
	0x0a, 0x0d, 0x44, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12,
	0x7f, 0x0a, 0x1f, 0x4c, 0x69, 0x73, 0x74, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x41, 0x67,
	0x72, 0x65, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x41, 0x63, 0x63, 0x65, 0x70, 0x74, 0x61, 0x6e, 0x63,
	0x65, 0x73, 0x12, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x1a, 0x44, 0x2e, 0x63, 0x6f, 0x6d,
	0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2e, 0x61, 0x64, 0x6d, 0x69,
	0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x41, 0x67, 0x72, 0x65,
	0x65, 0x6d, 0x65, 0x6e, 0x74, 0x41, 0x63, 0x63, 0x65, 0x70, 0x74, 0x61, 0x6e, 0x63, 0x65, 0x73,
	0x12, 0x6a, 0x0a, 0x13, 0x47, 0x65, 0x74, 0x44, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x50, 0x61, 0x72,
	0x61, 0x6d, 0x65, 0x74, 0x65, 0x72, 0x73, 0x12, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x1a,
	0x3b, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73,
	0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x63,
	0x6f, 0x6c, 0x2e, 0x76, 0x30, 0x2e, 0x53, 0x74, 0x61, 0x74, 0x69, 0x63, 0x44, 0x6f, 0x6d, 0x61,
	0x69, 0x6e, 0x50, 0x61, 0x72, 0x61, 0x6d, 0x65, 0x74, 0x65, 0x72, 0x73, 0x12, 0xab, 0x01, 0x0a,
	0x1c, 0x47, 0x65, 0x74, 0x44, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x50, 0x61, 0x72, 0x61, 0x6d, 0x65,
	0x74, 0x65, 0x72, 0x73, 0x56, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x65, 0x64, 0x12, 0x44, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2e, 0x61,
	0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x47, 0x65, 0x74, 0x44, 0x6f, 0x6d, 0x61, 0x69,
	0x6e, 0x50, 0x61, 0x72, 0x61, 0x6d, 0x65, 0x74, 0x65, 0x72, 0x73, 0x2e, 0x52, 0x65, 0x71, 0x75,
	0x65, 0x73, 0x74, 0x1a, 0x45, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61,
	0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2e, 0x63, 0x61, 0x6e, 0x74, 0x6f, 0x6e, 0x2e, 0x64, 0x6f,
	0x6d, 0x61, 0x69, 0x6e, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x76, 0x30, 0x2e, 0x47, 0x65,
	0x74, 0x44, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x50, 0x61, 0x72, 0x61, 0x6d, 0x65, 0x74, 0x65, 0x72,
	0x73, 0x2e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x42, 0x58, 0x5a, 0x56, 0x67, 0x69,
	0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c,
	0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65,
	0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d,
	0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f, 0x63, 0x61,
	0x6e, 0x74, 0x6f, 0x6e, 0x2f, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x2f, 0x61, 0x64, 0x6d, 0x69,
	0x6e, 0x2f, 0x76, 0x30, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_rawDescData = file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_rawDesc
)

func file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_rawDescData)
	})
	return file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_rawDescData
}

var file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_msgTypes = make([]protoimpl.MessageInfo, 5)
var file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_goTypes = []any{
	(*GetDomainParameters)(nil),          // 0: com.digitalasset.canton.domain.admin.v0.GetDomainParameters
	(*ServiceAgreementAcceptances)(nil),  // 1: com.digitalasset.canton.domain.admin.v0.ServiceAgreementAcceptances
	(*ServiceAgreementAcceptance)(nil),   // 2: com.digitalasset.canton.domain.admin.v0.ServiceAgreementAcceptance
	(*GetDomainParameters_Request)(nil),  // 3: com.digitalasset.canton.domain.admin.v0.GetDomainParameters.Request
	(*GetDomainParameters_Response)(nil), // 4: com.digitalasset.canton.domain.admin.v0.GetDomainParameters.Response
	(*v0.Signature)(nil),                 // 5: com.digitalasset.canton.crypto.v0.Signature
	(*timestamppb.Timestamp)(nil),        // 6: google.protobuf.Timestamp
	(*v01.StaticDomainParameters)(nil),   // 7: com.digitalasset.canton.protocol.v0.StaticDomainParameters
	(*v1.StaticDomainParameters)(nil),    // 8: com.digitalasset.canton.protocol.v1.StaticDomainParameters
	(*emptypb.Empty)(nil),                // 9: google.protobuf.Empty
}
var file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_depIdxs = []int32{
	2, // 0: com.digitalasset.canton.domain.admin.v0.ServiceAgreementAcceptances.acceptances:type_name -> com.digitalasset.canton.domain.admin.v0.ServiceAgreementAcceptance
	5, // 1: com.digitalasset.canton.domain.admin.v0.ServiceAgreementAcceptance.signature:type_name -> com.digitalasset.canton.crypto.v0.Signature
	6, // 2: com.digitalasset.canton.domain.admin.v0.ServiceAgreementAcceptance.timestamp:type_name -> google.protobuf.Timestamp
	7, // 3: com.digitalasset.canton.domain.admin.v0.GetDomainParameters.Response.parameters_v0:type_name -> com.digitalasset.canton.protocol.v0.StaticDomainParameters
	8, // 4: com.digitalasset.canton.domain.admin.v0.GetDomainParameters.Response.parameters_v1:type_name -> com.digitalasset.canton.protocol.v1.StaticDomainParameters
	9, // 5: com.digitalasset.canton.domain.admin.v0.DomainService.ListServiceAgreementAcceptances:input_type -> google.protobuf.Empty
	9, // 6: com.digitalasset.canton.domain.admin.v0.DomainService.GetDomainParameters:input_type -> google.protobuf.Empty
	3, // 7: com.digitalasset.canton.domain.admin.v0.DomainService.GetDomainParametersVersioned:input_type -> com.digitalasset.canton.domain.admin.v0.GetDomainParameters.Request
	1, // 8: com.digitalasset.canton.domain.admin.v0.DomainService.ListServiceAgreementAcceptances:output_type -> com.digitalasset.canton.domain.admin.v0.ServiceAgreementAcceptances
	7, // 9: com.digitalasset.canton.domain.admin.v0.DomainService.GetDomainParameters:output_type -> com.digitalasset.canton.protocol.v0.StaticDomainParameters
	4, // 10: com.digitalasset.canton.domain.admin.v0.DomainService.GetDomainParametersVersioned:output_type -> com.digitalasset.canton.domain.admin.v0.GetDomainParameters.Response
	8, // [8:11] is the sub-list for method output_type
	5, // [5:8] is the sub-list for method input_type
	5, // [5:5] is the sub-list for extension type_name
	5, // [5:5] is the sub-list for extension extendee
	0, // [0:5] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_init() }
func file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_init() {
	if File_com_digitalasset_canton_domain_admin_v0_domain_service_proto != nil {
		return
	}
	file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_msgTypes[4].OneofWrappers = []any{
		(*GetDomainParameters_Response_ParametersV0)(nil),
		(*GetDomainParameters_Response_ParametersV1)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   5,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_domain_admin_v0_domain_service_proto = out.File
	file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_rawDesc = nil
	file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_goTypes = nil
	file_com_digitalasset_canton_domain_admin_v0_domain_service_proto_depIdxs = nil
}
