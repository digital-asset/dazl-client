// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/participant/admin/v0/participant_status_service.proto

package v0

import (
	v0 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/health/admin/v0"
	v1 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/health/admin/v1"
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

type ParticipantStatusRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ParticipantStatusRequest) Reset() {
	*x = ParticipantStatusRequest{}
	mi := &file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ParticipantStatusRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ParticipantStatusRequest) ProtoMessage() {}

func (x *ParticipantStatusRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ParticipantStatusRequest.ProtoReflect.Descriptor instead.
func (*ParticipantStatusRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_rawDescGZIP(), []int{0}
}

type ConnectedDomain struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	DomainId      string                 `protobuf:"bytes,1,opt,name=domain_id,json=domainId,proto3" json:"domain_id,omitempty"`
	Healthy       bool                   `protobuf:"varint,2,opt,name=healthy,proto3" json:"healthy,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ConnectedDomain) Reset() {
	*x = ConnectedDomain{}
	mi := &file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ConnectedDomain) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ConnectedDomain) ProtoMessage() {}

func (x *ConnectedDomain) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ConnectedDomain.ProtoReflect.Descriptor instead.
func (*ConnectedDomain) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_rawDescGZIP(), []int{1}
}

func (x *ConnectedDomain) GetDomainId() string {
	if x != nil {
		return x.DomainId
	}
	return ""
}

func (x *ConnectedDomain) GetHealthy() bool {
	if x != nil {
		return x.Healthy
	}
	return false
}

type ParticipantStatusResponse struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// Types that are valid to be assigned to Kind:
	//
	//	*ParticipantStatusResponse_Status
	//	*ParticipantStatusResponse_Unavailable
	//	*ParticipantStatusResponse_Failure
	Kind          isParticipantStatusResponse_Kind `protobuf_oneof:"kind"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ParticipantStatusResponse) Reset() {
	*x = ParticipantStatusResponse{}
	mi := &file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ParticipantStatusResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ParticipantStatusResponse) ProtoMessage() {}

func (x *ParticipantStatusResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ParticipantStatusResponse.ProtoReflect.Descriptor instead.
func (*ParticipantStatusResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_rawDescGZIP(), []int{2}
}

func (x *ParticipantStatusResponse) GetKind() isParticipantStatusResponse_Kind {
	if x != nil {
		return x.Kind
	}
	return nil
}

func (x *ParticipantStatusResponse) GetStatus() *ParticipantStatusResponse_ParticipantStatusResponseStatus {
	if x != nil {
		if x, ok := x.Kind.(*ParticipantStatusResponse_Status); ok {
			return x.Status
		}
	}
	return nil
}

func (x *ParticipantStatusResponse) GetUnavailable() *v0.NodeStatus_NotInitialized {
	if x != nil {
		if x, ok := x.Kind.(*ParticipantStatusResponse_Unavailable); ok {
			return x.Unavailable
		}
	}
	return nil
}

func (x *ParticipantStatusResponse) GetFailure() *v1.Failure {
	if x != nil {
		if x, ok := x.Kind.(*ParticipantStatusResponse_Failure); ok {
			return x.Failure
		}
	}
	return nil
}

type isParticipantStatusResponse_Kind interface {
	isParticipantStatusResponse_Kind()
}

type ParticipantStatusResponse_Status struct {
	Status *ParticipantStatusResponse_ParticipantStatusResponseStatus `protobuf:"bytes,1,opt,name=status,proto3,oneof"`
}

type ParticipantStatusResponse_Unavailable struct {
	Unavailable *v0.NodeStatus_NotInitialized `protobuf:"bytes,2,opt,name=unavailable,proto3,oneof"`
}

type ParticipantStatusResponse_Failure struct {
	Failure *v1.Failure `protobuf:"bytes,3,opt,name=failure,proto3,oneof"`
}

func (*ParticipantStatusResponse_Status) isParticipantStatusResponse_Kind() {}

func (*ParticipantStatusResponse_Unavailable) isParticipantStatusResponse_Kind() {}

func (*ParticipantStatusResponse_Failure) isParticipantStatusResponse_Kind() {}

type ParticipantStatusResponse_ParticipantStatusResponseStatus struct {
	state                     protoimpl.MessageState `protogen:"open.v1"`
	CommonStatus              *v1.Status             `protobuf:"bytes,1,opt,name=common_status,json=commonStatus,proto3" json:"common_status,omitempty"`
	ConnectedDomains          []*ConnectedDomain     `protobuf:"bytes,2,rep,name=connected_domains,json=connectedDomains,proto3" json:"connected_domains,omitempty"`
	Active                    bool                   `protobuf:"varint,3,opt,name=active,proto3" json:"active,omitempty"`
	SupportedProtocolVersions []int32                `protobuf:"varint,4,rep,packed,name=supported_protocol_versions,json=supportedProtocolVersions,proto3" json:"supported_protocol_versions,omitempty"`
	unknownFields             protoimpl.UnknownFields
	sizeCache                 protoimpl.SizeCache
}

func (x *ParticipantStatusResponse_ParticipantStatusResponseStatus) Reset() {
	*x = ParticipantStatusResponse_ParticipantStatusResponseStatus{}
	mi := &file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ParticipantStatusResponse_ParticipantStatusResponseStatus) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ParticipantStatusResponse_ParticipantStatusResponseStatus) ProtoMessage() {}

func (x *ParticipantStatusResponse_ParticipantStatusResponseStatus) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ParticipantStatusResponse_ParticipantStatusResponseStatus.ProtoReflect.Descriptor instead.
func (*ParticipantStatusResponse_ParticipantStatusResponseStatus) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_rawDescGZIP(), []int{2, 0}
}

func (x *ParticipantStatusResponse_ParticipantStatusResponseStatus) GetCommonStatus() *v1.Status {
	if x != nil {
		return x.CommonStatus
	}
	return nil
}

func (x *ParticipantStatusResponse_ParticipantStatusResponseStatus) GetConnectedDomains() []*ConnectedDomain {
	if x != nil {
		return x.ConnectedDomains
	}
	return nil
}

func (x *ParticipantStatusResponse_ParticipantStatusResponseStatus) GetActive() bool {
	if x != nil {
		return x.Active
	}
	return false
}

func (x *ParticipantStatusResponse_ParticipantStatusResponseStatus) GetSupportedProtocolVersions() []int32 {
	if x != nil {
		return x.SupportedProtocolVersions
	}
	return nil
}

var File_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto protoreflect.FileDescriptor

const file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_rawDesc = "" +
	"\n" +
	"Mcom/digitalasset/canton/participant/admin/v0/participant_status_service.proto\x12,com.digitalasset.canton.participant.admin.v0\x1a<com/digitalasset/canton/health/admin/v0/status_service.proto\x1a<com/digitalasset/canton/health/admin/v1/status_service.proto\"\x1a\n" +
	"\x18ParticipantStatusRequest\"H\n" +
	"\x0fConnectedDomain\x12\x1b\n" +
	"\tdomain_id\x18\x01 \x01(\tR\bdomainId\x12\x18\n" +
	"\ahealthy\x18\x02 \x01(\bR\ahealthy\"\x9b\x05\n" +
	"\x19ParticipantStatusResponse\x12\x81\x01\n" +
	"\x06status\x18\x01 \x01(\v2g.com.digitalasset.canton.participant.admin.v0.ParticipantStatusResponse.ParticipantStatusResponseStatusH\x00R\x06status\x12f\n" +
	"\vunavailable\x18\x02 \x01(\v2B.com.digitalasset.canton.health.admin.v0.NodeStatus.NotInitializedH\x00R\vunavailable\x12L\n" +
	"\afailure\x18\x03 \x01(\v20.com.digitalasset.canton.health.admin.v1.FailureH\x00R\afailure\x1a\xbb\x02\n" +
	"\x1fParticipantStatusResponseStatus\x12T\n" +
	"\rcommon_status\x18\x01 \x01(\v2/.com.digitalasset.canton.health.admin.v1.StatusR\fcommonStatus\x12j\n" +
	"\x11connected_domains\x18\x02 \x03(\v2=.com.digitalasset.canton.participant.admin.v0.ConnectedDomainR\x10connectedDomains\x12\x16\n" +
	"\x06active\x18\x03 \x01(\bR\x06active\x12>\n" +
	"\x1bsupported_protocol_versions\x18\x04 \x03(\x05R\x19supportedProtocolVersionsB\x06\n" +
	"\x04kind2\xc1\x01\n" +
	"\x18ParticipantStatusService\x12\xa4\x01\n" +
	"\x11ParticipantStatus\x12F.com.digitalasset.canton.participant.admin.v0.ParticipantStatusRequest\x1aG.com.digitalasset.canton.participant.admin.v0.ParticipantStatusResponseB]Z[github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/participant/admin/v0b\x06proto3"

var (
	file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_rawDescData []byte
)

func file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_rawDesc), len(file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_rawDesc)))
	})
	return file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_rawDescData
}

var file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_goTypes = []any{
	(*ParticipantStatusRequest)(nil),                                  // 0: com.digitalasset.canton.participant.admin.v0.ParticipantStatusRequest
	(*ConnectedDomain)(nil),                                           // 1: com.digitalasset.canton.participant.admin.v0.ConnectedDomain
	(*ParticipantStatusResponse)(nil),                                 // 2: com.digitalasset.canton.participant.admin.v0.ParticipantStatusResponse
	(*ParticipantStatusResponse_ParticipantStatusResponseStatus)(nil), // 3: com.digitalasset.canton.participant.admin.v0.ParticipantStatusResponse.ParticipantStatusResponseStatus
	(*v0.NodeStatus_NotInitialized)(nil),                              // 4: com.digitalasset.canton.health.admin.v0.NodeStatus.NotInitialized
	(*v1.Failure)(nil),                                                // 5: com.digitalasset.canton.health.admin.v1.Failure
	(*v1.Status)(nil),                                                 // 6: com.digitalasset.canton.health.admin.v1.Status
}
var file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_depIdxs = []int32{
	3, // 0: com.digitalasset.canton.participant.admin.v0.ParticipantStatusResponse.status:type_name -> com.digitalasset.canton.participant.admin.v0.ParticipantStatusResponse.ParticipantStatusResponseStatus
	4, // 1: com.digitalasset.canton.participant.admin.v0.ParticipantStatusResponse.unavailable:type_name -> com.digitalasset.canton.health.admin.v0.NodeStatus.NotInitialized
	5, // 2: com.digitalasset.canton.participant.admin.v0.ParticipantStatusResponse.failure:type_name -> com.digitalasset.canton.health.admin.v1.Failure
	6, // 3: com.digitalasset.canton.participant.admin.v0.ParticipantStatusResponse.ParticipantStatusResponseStatus.common_status:type_name -> com.digitalasset.canton.health.admin.v1.Status
	1, // 4: com.digitalasset.canton.participant.admin.v0.ParticipantStatusResponse.ParticipantStatusResponseStatus.connected_domains:type_name -> com.digitalasset.canton.participant.admin.v0.ConnectedDomain
	0, // 5: com.digitalasset.canton.participant.admin.v0.ParticipantStatusService.ParticipantStatus:input_type -> com.digitalasset.canton.participant.admin.v0.ParticipantStatusRequest
	2, // 6: com.digitalasset.canton.participant.admin.v0.ParticipantStatusService.ParticipantStatus:output_type -> com.digitalasset.canton.participant.admin.v0.ParticipantStatusResponse
	6, // [6:7] is the sub-list for method output_type
	5, // [5:6] is the sub-list for method input_type
	5, // [5:5] is the sub-list for extension type_name
	5, // [5:5] is the sub-list for extension extendee
	0, // [0:5] is the sub-list for field type_name
}

func init() {
	file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_init()
}
func file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_init() {
	if File_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto != nil {
		return
	}
	file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_msgTypes[2].OneofWrappers = []any{
		(*ParticipantStatusResponse_Status)(nil),
		(*ParticipantStatusResponse_Unavailable)(nil),
		(*ParticipantStatusResponse_Failure)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_rawDesc), len(file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto = out.File
	file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_goTypes = nil
	file_com_digitalasset_canton_participant_admin_v0_participant_status_service_proto_depIdxs = nil
}
