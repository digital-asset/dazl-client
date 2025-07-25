// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/domain/admin/v0/domain_manager_status_service.proto

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

type DomainManagerStatusRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *DomainManagerStatusRequest) Reset() {
	*x = DomainManagerStatusRequest{}
	mi := &file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *DomainManagerStatusRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DomainManagerStatusRequest) ProtoMessage() {}

func (x *DomainManagerStatusRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DomainManagerStatusRequest.ProtoReflect.Descriptor instead.
func (*DomainManagerStatusRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_rawDescGZIP(), []int{0}
}

type DomainManagerStatusResponse struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// Types that are valid to be assigned to Kind:
	//
	//	*DomainManagerStatusResponse_Status
	//	*DomainManagerStatusResponse_Unavailable
	//	*DomainManagerStatusResponse_Failure
	Kind          isDomainManagerStatusResponse_Kind `protobuf_oneof:"kind"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *DomainManagerStatusResponse) Reset() {
	*x = DomainManagerStatusResponse{}
	mi := &file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *DomainManagerStatusResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DomainManagerStatusResponse) ProtoMessage() {}

func (x *DomainManagerStatusResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DomainManagerStatusResponse.ProtoReflect.Descriptor instead.
func (*DomainManagerStatusResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_rawDescGZIP(), []int{1}
}

func (x *DomainManagerStatusResponse) GetKind() isDomainManagerStatusResponse_Kind {
	if x != nil {
		return x.Kind
	}
	return nil
}

func (x *DomainManagerStatusResponse) GetStatus() *DomainManagerStatusResponse_DomainManagerStatusResponseStatus {
	if x != nil {
		if x, ok := x.Kind.(*DomainManagerStatusResponse_Status); ok {
			return x.Status
		}
	}
	return nil
}

func (x *DomainManagerStatusResponse) GetUnavailable() *v0.NodeStatus_NotInitialized {
	if x != nil {
		if x, ok := x.Kind.(*DomainManagerStatusResponse_Unavailable); ok {
			return x.Unavailable
		}
	}
	return nil
}

func (x *DomainManagerStatusResponse) GetFailure() *v1.Failure {
	if x != nil {
		if x, ok := x.Kind.(*DomainManagerStatusResponse_Failure); ok {
			return x.Failure
		}
	}
	return nil
}

type isDomainManagerStatusResponse_Kind interface {
	isDomainManagerStatusResponse_Kind()
}

type DomainManagerStatusResponse_Status struct {
	Status *DomainManagerStatusResponse_DomainManagerStatusResponseStatus `protobuf:"bytes,1,opt,name=status,proto3,oneof"`
}

type DomainManagerStatusResponse_Unavailable struct {
	Unavailable *v0.NodeStatus_NotInitialized `protobuf:"bytes,2,opt,name=unavailable,proto3,oneof"`
}

type DomainManagerStatusResponse_Failure struct {
	Failure *v1.Failure `protobuf:"bytes,3,opt,name=failure,proto3,oneof"`
}

func (*DomainManagerStatusResponse_Status) isDomainManagerStatusResponse_Kind() {}

func (*DomainManagerStatusResponse_Unavailable) isDomainManagerStatusResponse_Kind() {}

func (*DomainManagerStatusResponse_Failure) isDomainManagerStatusResponse_Kind() {}

type DomainManagerStatusResponse_DomainManagerStatusResponseStatus struct {
	state           protoimpl.MessageState `protogen:"open.v1"`
	CommonStatus    *v1.Status             `protobuf:"bytes,1,opt,name=common_status,json=commonStatus,proto3" json:"common_status,omitempty"`
	ProtocolVersion int32                  `protobuf:"varint,2,opt,name=protocol_version,json=protocolVersion,proto3" json:"protocol_version,omitempty"`
	unknownFields   protoimpl.UnknownFields
	sizeCache       protoimpl.SizeCache
}

func (x *DomainManagerStatusResponse_DomainManagerStatusResponseStatus) Reset() {
	*x = DomainManagerStatusResponse_DomainManagerStatusResponseStatus{}
	mi := &file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *DomainManagerStatusResponse_DomainManagerStatusResponseStatus) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DomainManagerStatusResponse_DomainManagerStatusResponseStatus) ProtoMessage() {}

func (x *DomainManagerStatusResponse_DomainManagerStatusResponseStatus) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DomainManagerStatusResponse_DomainManagerStatusResponseStatus.ProtoReflect.Descriptor instead.
func (*DomainManagerStatusResponse_DomainManagerStatusResponseStatus) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_rawDescGZIP(), []int{1, 0}
}

func (x *DomainManagerStatusResponse_DomainManagerStatusResponseStatus) GetCommonStatus() *v1.Status {
	if x != nil {
		return x.CommonStatus
	}
	return nil
}

func (x *DomainManagerStatusResponse_DomainManagerStatusResponseStatus) GetProtocolVersion() int32 {
	if x != nil {
		return x.ProtocolVersion
	}
	return 0
}

var File_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto protoreflect.FileDescriptor

const file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_rawDesc = "" +
	"\n" +
	"Kcom/digitalasset/canton/domain/admin/v0/domain_manager_status_service.proto\x12'com.digitalasset.canton.domain.admin.v0\x1a<com/digitalasset/canton/health/admin/v0/status_service.proto\x1a<com/digitalasset/canton/health/admin/v1/status_service.proto\"\x1c\n" +
	"\x1aDomainManagerStatusRequest\"\x85\x04\n" +
	"\x1bDomainManagerStatusResponse\x12\x80\x01\n" +
	"\x06status\x18\x01 \x01(\v2f.com.digitalasset.canton.domain.admin.v0.DomainManagerStatusResponse.DomainManagerStatusResponseStatusH\x00R\x06status\x12f\n" +
	"\vunavailable\x18\x02 \x01(\v2B.com.digitalasset.canton.health.admin.v0.NodeStatus.NotInitializedH\x00R\vunavailable\x12L\n" +
	"\afailure\x18\x03 \x01(\v20.com.digitalasset.canton.health.admin.v1.FailureH\x00R\afailure\x1a\xa4\x01\n" +
	"!DomainManagerStatusResponseStatus\x12T\n" +
	"\rcommon_status\x18\x01 \x01(\v2/.com.digitalasset.canton.health.admin.v1.StatusR\fcommonStatus\x12)\n" +
	"\x10protocol_version\x18\x02 \x01(\x05R\x0fprotocolVersionB\x06\n" +
	"\x04kind2\xbf\x01\n" +
	"\x1aDomainManagerStatusService\x12\xa0\x01\n" +
	"\x13DomainManagerStatus\x12C.com.digitalasset.canton.domain.admin.v0.DomainManagerStatusRequest\x1aD.com.digitalasset.canton.domain.admin.v0.DomainManagerStatusResponseBXZVgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/admin/v0b\x06proto3"

var (
	file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_rawDescData []byte
)

func file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_rawDesc), len(file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_rawDesc)))
	})
	return file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_rawDescData
}

var file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_goTypes = []any{
	(*DomainManagerStatusRequest)(nil),                                    // 0: com.digitalasset.canton.domain.admin.v0.DomainManagerStatusRequest
	(*DomainManagerStatusResponse)(nil),                                   // 1: com.digitalasset.canton.domain.admin.v0.DomainManagerStatusResponse
	(*DomainManagerStatusResponse_DomainManagerStatusResponseStatus)(nil), // 2: com.digitalasset.canton.domain.admin.v0.DomainManagerStatusResponse.DomainManagerStatusResponseStatus
	(*v0.NodeStatus_NotInitialized)(nil),                                  // 3: com.digitalasset.canton.health.admin.v0.NodeStatus.NotInitialized
	(*v1.Failure)(nil),                                                    // 4: com.digitalasset.canton.health.admin.v1.Failure
	(*v1.Status)(nil),                                                     // 5: com.digitalasset.canton.health.admin.v1.Status
}
var file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_depIdxs = []int32{
	2, // 0: com.digitalasset.canton.domain.admin.v0.DomainManagerStatusResponse.status:type_name -> com.digitalasset.canton.domain.admin.v0.DomainManagerStatusResponse.DomainManagerStatusResponseStatus
	3, // 1: com.digitalasset.canton.domain.admin.v0.DomainManagerStatusResponse.unavailable:type_name -> com.digitalasset.canton.health.admin.v0.NodeStatus.NotInitialized
	4, // 2: com.digitalasset.canton.domain.admin.v0.DomainManagerStatusResponse.failure:type_name -> com.digitalasset.canton.health.admin.v1.Failure
	5, // 3: com.digitalasset.canton.domain.admin.v0.DomainManagerStatusResponse.DomainManagerStatusResponseStatus.common_status:type_name -> com.digitalasset.canton.health.admin.v1.Status
	0, // 4: com.digitalasset.canton.domain.admin.v0.DomainManagerStatusService.DomainManagerStatus:input_type -> com.digitalasset.canton.domain.admin.v0.DomainManagerStatusRequest
	1, // 5: com.digitalasset.canton.domain.admin.v0.DomainManagerStatusService.DomainManagerStatus:output_type -> com.digitalasset.canton.domain.admin.v0.DomainManagerStatusResponse
	5, // [5:6] is the sub-list for method output_type
	4, // [4:5] is the sub-list for method input_type
	4, // [4:4] is the sub-list for extension type_name
	4, // [4:4] is the sub-list for extension extendee
	0, // [0:4] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_init() }
func file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_init() {
	if File_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto != nil {
		return
	}
	file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_msgTypes[1].OneofWrappers = []any{
		(*DomainManagerStatusResponse_Status)(nil),
		(*DomainManagerStatusResponse_Unavailable)(nil),
		(*DomainManagerStatusResponse_Failure)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_rawDesc), len(file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto = out.File
	file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_goTypes = nil
	file_com_digitalasset_canton_domain_admin_v0_domain_manager_status_service_proto_depIdxs = nil
}
