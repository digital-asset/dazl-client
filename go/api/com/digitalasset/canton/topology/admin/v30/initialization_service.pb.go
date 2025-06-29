// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/topology/admin/v30/initialization_service.proto

package v30

import (
	v30 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v30"
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

type InitIdRequest struct {
	state                protoimpl.MessageState           `protogen:"open.v1"`
	Identifier           string                           `protobuf:"bytes,1,opt,name=identifier,proto3" json:"identifier,omitempty"`
	Namespace            string                           `protobuf:"bytes,2,opt,name=namespace,proto3" json:"namespace,omitempty"`
	NamespaceDelegations []*v30.SignedTopologyTransaction `protobuf:"bytes,3,rep,name=namespace_delegations,json=namespaceDelegations,proto3" json:"namespace_delegations,omitempty"`
	unknownFields        protoimpl.UnknownFields
	sizeCache            protoimpl.SizeCache
}

func (x *InitIdRequest) Reset() {
	*x = InitIdRequest{}
	mi := &file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *InitIdRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*InitIdRequest) ProtoMessage() {}

func (x *InitIdRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use InitIdRequest.ProtoReflect.Descriptor instead.
func (*InitIdRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDescGZIP(), []int{0}
}

func (x *InitIdRequest) GetIdentifier() string {
	if x != nil {
		return x.Identifier
	}
	return ""
}

func (x *InitIdRequest) GetNamespace() string {
	if x != nil {
		return x.Namespace
	}
	return ""
}

func (x *InitIdRequest) GetNamespaceDelegations() []*v30.SignedTopologyTransaction {
	if x != nil {
		return x.NamespaceDelegations
	}
	return nil
}

type InitIdResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *InitIdResponse) Reset() {
	*x = InitIdResponse{}
	mi := &file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *InitIdResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*InitIdResponse) ProtoMessage() {}

func (x *InitIdResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use InitIdResponse.ProtoReflect.Descriptor instead.
func (*InitIdResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDescGZIP(), []int{1}
}

type GetIdResponse struct {
	state            protoimpl.MessageState `protogen:"open.v1"`
	Initialized      bool                   `protobuf:"varint,1,opt,name=initialized,proto3" json:"initialized,omitempty"`
	UniqueIdentifier string                 `protobuf:"bytes,2,opt,name=unique_identifier,json=uniqueIdentifier,proto3" json:"unique_identifier,omitempty"`
	unknownFields    protoimpl.UnknownFields
	sizeCache        protoimpl.SizeCache
}

func (x *GetIdResponse) Reset() {
	*x = GetIdResponse{}
	mi := &file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetIdResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetIdResponse) ProtoMessage() {}

func (x *GetIdResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetIdResponse.ProtoReflect.Descriptor instead.
func (*GetIdResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDescGZIP(), []int{2}
}

func (x *GetIdResponse) GetInitialized() bool {
	if x != nil {
		return x.Initialized
	}
	return false
}

func (x *GetIdResponse) GetUniqueIdentifier() string {
	if x != nil {
		return x.UniqueIdentifier
	}
	return ""
}

type GetOnboardingTransactionsRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetOnboardingTransactionsRequest) Reset() {
	*x = GetOnboardingTransactionsRequest{}
	mi := &file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetOnboardingTransactionsRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetOnboardingTransactionsRequest) ProtoMessage() {}

func (x *GetOnboardingTransactionsRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetOnboardingTransactionsRequest.ProtoReflect.Descriptor instead.
func (*GetOnboardingTransactionsRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDescGZIP(), []int{3}
}

type GetOnboardingTransactionsResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Transactions  *TopologyTransactions  `protobuf:"bytes,1,opt,name=transactions,proto3" json:"transactions,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetOnboardingTransactionsResponse) Reset() {
	*x = GetOnboardingTransactionsResponse{}
	mi := &file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetOnboardingTransactionsResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetOnboardingTransactionsResponse) ProtoMessage() {}

func (x *GetOnboardingTransactionsResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetOnboardingTransactionsResponse.ProtoReflect.Descriptor instead.
func (*GetOnboardingTransactionsResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDescGZIP(), []int{4}
}

func (x *GetOnboardingTransactionsResponse) GetTransactions() *TopologyTransactions {
	if x != nil {
		return x.Transactions
	}
	return nil
}

type GetIdRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetIdRequest) Reset() {
	*x = GetIdRequest{}
	mi := &file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetIdRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetIdRequest) ProtoMessage() {}

func (x *GetIdRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes[5]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetIdRequest.ProtoReflect.Descriptor instead.
func (*GetIdRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDescGZIP(), []int{5}
}

type CurrentTimeRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CurrentTimeRequest) Reset() {
	*x = CurrentTimeRequest{}
	mi := &file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes[6]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CurrentTimeRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CurrentTimeRequest) ProtoMessage() {}

func (x *CurrentTimeRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes[6]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CurrentTimeRequest.ProtoReflect.Descriptor instead.
func (*CurrentTimeRequest) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDescGZIP(), []int{6}
}

type CurrentTimeResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	CurrentTime   int64                  `protobuf:"varint,1,opt,name=current_time,json=currentTime,proto3" json:"current_time,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CurrentTimeResponse) Reset() {
	*x = CurrentTimeResponse{}
	mi := &file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes[7]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CurrentTimeResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CurrentTimeResponse) ProtoMessage() {}

func (x *CurrentTimeResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes[7]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CurrentTimeResponse.ProtoReflect.Descriptor instead.
func (*CurrentTimeResponse) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDescGZIP(), []int{7}
}

func (x *CurrentTimeResponse) GetCurrentTime() int64 {
	if x != nil {
		return x.CurrentTime
	}
	return 0
}

var File_com_digitalasset_canton_topology_admin_v30_initialization_service_proto protoreflect.FileDescriptor

const file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDesc = "" +
	"\n" +
	"Gcom/digitalasset/canton/topology/admin/v30/initialization_service.proto\x12*com.digitalasset.canton.topology.admin.v30\x1a3com/digitalasset/canton/protocol/v30/topology.proto\x1a7com/digitalasset/canton/topology/admin/v30/common.proto\"\xc3\x01\n" +
	"\rInitIdRequest\x12\x1e\n" +
	"\n" +
	"identifier\x18\x01 \x01(\tR\n" +
	"identifier\x12\x1c\n" +
	"\tnamespace\x18\x02 \x01(\tR\tnamespace\x12t\n" +
	"\x15namespace_delegations\x18\x03 \x03(\v2?.com.digitalasset.canton.protocol.v30.SignedTopologyTransactionR\x14namespaceDelegations\"\x10\n" +
	"\x0eInitIdResponse\"^\n" +
	"\rGetIdResponse\x12 \n" +
	"\vinitialized\x18\x01 \x01(\bR\vinitialized\x12+\n" +
	"\x11unique_identifier\x18\x02 \x01(\tR\x10uniqueIdentifier\"\"\n" +
	" GetOnboardingTransactionsRequest\"\x89\x01\n" +
	"!GetOnboardingTransactionsResponse\x12d\n" +
	"\ftransactions\x18\x01 \x01(\v2@.com.digitalasset.canton.topology.admin.v30.TopologyTransactionsR\ftransactions\"\x0e\n" +
	"\fGetIdRequest\"\x14\n" +
	"\x12CurrentTimeRequest\"8\n" +
	"\x13CurrentTimeResponse\x12!\n" +
	"\fcurrent_time\x18\x01 \x01(\x03R\vcurrentTime2\xaf\x03\n" +
	"\x1dIdentityInitializationService\x12\x7f\n" +
	"\x06InitId\x129.com.digitalasset.canton.topology.admin.v30.InitIdRequest\x1a:.com.digitalasset.canton.topology.admin.v30.InitIdResponse\x12|\n" +
	"\x05GetId\x128.com.digitalasset.canton.topology.admin.v30.GetIdRequest\x1a9.com.digitalasset.canton.topology.admin.v30.GetIdResponse\x12\x8e\x01\n" +
	"\vCurrentTime\x12>.com.digitalasset.canton.topology.admin.v30.CurrentTimeRequest\x1a?.com.digitalasset.canton.topology.admin.v30.CurrentTimeResponseB[ZYgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/topology/admin/v30b\x06proto3"

var (
	file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDescData []byte
)

func file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDesc), len(file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDesc)))
	})
	return file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDescData
}

var file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes = make([]protoimpl.MessageInfo, 8)
var file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_goTypes = []any{
	(*InitIdRequest)(nil),                     // 0: com.digitalasset.canton.topology.admin.v30.InitIdRequest
	(*InitIdResponse)(nil),                    // 1: com.digitalasset.canton.topology.admin.v30.InitIdResponse
	(*GetIdResponse)(nil),                     // 2: com.digitalasset.canton.topology.admin.v30.GetIdResponse
	(*GetOnboardingTransactionsRequest)(nil),  // 3: com.digitalasset.canton.topology.admin.v30.GetOnboardingTransactionsRequest
	(*GetOnboardingTransactionsResponse)(nil), // 4: com.digitalasset.canton.topology.admin.v30.GetOnboardingTransactionsResponse
	(*GetIdRequest)(nil),                      // 5: com.digitalasset.canton.topology.admin.v30.GetIdRequest
	(*CurrentTimeRequest)(nil),                // 6: com.digitalasset.canton.topology.admin.v30.CurrentTimeRequest
	(*CurrentTimeResponse)(nil),               // 7: com.digitalasset.canton.topology.admin.v30.CurrentTimeResponse
	(*v30.SignedTopologyTransaction)(nil),     // 8: com.digitalasset.canton.protocol.v30.SignedTopologyTransaction
	(*TopologyTransactions)(nil),              // 9: com.digitalasset.canton.topology.admin.v30.TopologyTransactions
}
var file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_depIdxs = []int32{
	8, // 0: com.digitalasset.canton.topology.admin.v30.InitIdRequest.namespace_delegations:type_name -> com.digitalasset.canton.protocol.v30.SignedTopologyTransaction
	9, // 1: com.digitalasset.canton.topology.admin.v30.GetOnboardingTransactionsResponse.transactions:type_name -> com.digitalasset.canton.topology.admin.v30.TopologyTransactions
	0, // 2: com.digitalasset.canton.topology.admin.v30.IdentityInitializationService.InitId:input_type -> com.digitalasset.canton.topology.admin.v30.InitIdRequest
	5, // 3: com.digitalasset.canton.topology.admin.v30.IdentityInitializationService.GetId:input_type -> com.digitalasset.canton.topology.admin.v30.GetIdRequest
	6, // 4: com.digitalasset.canton.topology.admin.v30.IdentityInitializationService.CurrentTime:input_type -> com.digitalasset.canton.topology.admin.v30.CurrentTimeRequest
	1, // 5: com.digitalasset.canton.topology.admin.v30.IdentityInitializationService.InitId:output_type -> com.digitalasset.canton.topology.admin.v30.InitIdResponse
	2, // 6: com.digitalasset.canton.topology.admin.v30.IdentityInitializationService.GetId:output_type -> com.digitalasset.canton.topology.admin.v30.GetIdResponse
	7, // 7: com.digitalasset.canton.topology.admin.v30.IdentityInitializationService.CurrentTime:output_type -> com.digitalasset.canton.topology.admin.v30.CurrentTimeResponse
	5, // [5:8] is the sub-list for method output_type
	2, // [2:5] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_init() }
func file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_init() {
	if File_com_digitalasset_canton_topology_admin_v30_initialization_service_proto != nil {
		return
	}
	file_com_digitalasset_canton_topology_admin_v30_common_proto_init()
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDesc), len(file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   8,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_topology_admin_v30_initialization_service_proto = out.File
	file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_goTypes = nil
	file_com_digitalasset_canton_topology_admin_v30_initialization_service_proto_depIdxs = nil
}
