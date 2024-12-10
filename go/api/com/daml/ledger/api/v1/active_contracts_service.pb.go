// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v5.27.2
// source: com/daml/ledger/api/v1/active_contracts_service.proto

package v1

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

type GetActiveContractsRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	LedgerId       string             `protobuf:"bytes,1,opt,name=ledger_id,json=ledgerId,proto3" json:"ledger_id,omitempty"`
	Filter         *TransactionFilter `protobuf:"bytes,2,opt,name=filter,proto3" json:"filter,omitempty"`
	Verbose        bool               `protobuf:"varint,3,opt,name=verbose,proto3" json:"verbose,omitempty"`
	ActiveAtOffset string             `protobuf:"bytes,4,opt,name=active_at_offset,json=activeAtOffset,proto3" json:"active_at_offset,omitempty"`
}

func (x *GetActiveContractsRequest) Reset() {
	*x = GetActiveContractsRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_active_contracts_service_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetActiveContractsRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetActiveContractsRequest) ProtoMessage() {}

func (x *GetActiveContractsRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_active_contracts_service_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetActiveContractsRequest.ProtoReflect.Descriptor instead.
func (*GetActiveContractsRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_active_contracts_service_proto_rawDescGZIP(), []int{0}
}

func (x *GetActiveContractsRequest) GetLedgerId() string {
	if x != nil {
		return x.LedgerId
	}
	return ""
}

func (x *GetActiveContractsRequest) GetFilter() *TransactionFilter {
	if x != nil {
		return x.Filter
	}
	return nil
}

func (x *GetActiveContractsRequest) GetVerbose() bool {
	if x != nil {
		return x.Verbose
	}
	return false
}

func (x *GetActiveContractsRequest) GetActiveAtOffset() string {
	if x != nil {
		return x.ActiveAtOffset
	}
	return ""
}

type GetActiveContractsResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Offset          string          `protobuf:"bytes,1,opt,name=offset,proto3" json:"offset,omitempty"`
	WorkflowId      string          `protobuf:"bytes,2,opt,name=workflow_id,json=workflowId,proto3" json:"workflow_id,omitempty"`
	ActiveContracts []*CreatedEvent `protobuf:"bytes,3,rep,name=active_contracts,json=activeContracts,proto3" json:"active_contracts,omitempty"`
}

func (x *GetActiveContractsResponse) Reset() {
	*x = GetActiveContractsResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_active_contracts_service_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetActiveContractsResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetActiveContractsResponse) ProtoMessage() {}

func (x *GetActiveContractsResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_active_contracts_service_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetActiveContractsResponse.ProtoReflect.Descriptor instead.
func (*GetActiveContractsResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_active_contracts_service_proto_rawDescGZIP(), []int{1}
}

func (x *GetActiveContractsResponse) GetOffset() string {
	if x != nil {
		return x.Offset
	}
	return ""
}

func (x *GetActiveContractsResponse) GetWorkflowId() string {
	if x != nil {
		return x.WorkflowId
	}
	return ""
}

func (x *GetActiveContractsResponse) GetActiveContracts() []*CreatedEvent {
	if x != nil {
		return x.ActiveContracts
	}
	return nil
}

var File_com_daml_ledger_api_v1_active_contracts_service_proto protoreflect.FileDescriptor

var file_com_daml_ledger_api_v1_active_contracts_service_proto_rawDesc = []byte{
	0x0a, 0x35, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x61, 0x63, 0x74, 0x69, 0x76, 0x65, 0x5f,
	0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x73, 0x5f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63,
	0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x16, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d,
	0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x1a,
	0x22, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72,
	0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x65, 0x76, 0x65, 0x6e, 0x74, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x1a, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65,
	0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x74, 0x72, 0x61, 0x6e,
	0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x66, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x22, 0xbf, 0x01, 0x0a, 0x19, 0x47, 0x65, 0x74, 0x41, 0x63, 0x74, 0x69,
	0x76, 0x65, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x12, 0x1b, 0x0a, 0x09, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x5f, 0x69, 0x64, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x49, 0x64, 0x12,
	0x41, 0x0a, 0x06, 0x66, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x29, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63,
	0x74, 0x69, 0x6f, 0x6e, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x52, 0x06, 0x66, 0x69, 0x6c, 0x74,
	0x65, 0x72, 0x12, 0x18, 0x0a, 0x07, 0x76, 0x65, 0x72, 0x62, 0x6f, 0x73, 0x65, 0x18, 0x03, 0x20,
	0x01, 0x28, 0x08, 0x52, 0x07, 0x76, 0x65, 0x72, 0x62, 0x6f, 0x73, 0x65, 0x12, 0x28, 0x0a, 0x10,
	0x61, 0x63, 0x74, 0x69, 0x76, 0x65, 0x5f, 0x61, 0x74, 0x5f, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74,
	0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0e, 0x61, 0x63, 0x74, 0x69, 0x76, 0x65, 0x41, 0x74,
	0x4f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x22, 0xa6, 0x01, 0x0a, 0x1a, 0x47, 0x65, 0x74, 0x41, 0x63,
	0x74, 0x69, 0x76, 0x65, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x73, 0x52, 0x65, 0x73,
	0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x16, 0x0a, 0x06, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x6f, 0x66, 0x66, 0x73, 0x65, 0x74, 0x12, 0x1f, 0x0a,
	0x0b, 0x77, 0x6f, 0x72, 0x6b, 0x66, 0x6c, 0x6f, 0x77, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x0a, 0x77, 0x6f, 0x72, 0x6b, 0x66, 0x6c, 0x6f, 0x77, 0x49, 0x64, 0x12, 0x4f,
	0x0a, 0x10, 0x61, 0x63, 0x74, 0x69, 0x76, 0x65, 0x5f, 0x63, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63,
	0x74, 0x73, 0x18, 0x03, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x24, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64,
	0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76,
	0x31, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x45, 0x76, 0x65, 0x6e, 0x74, 0x52, 0x0f,
	0x61, 0x63, 0x74, 0x69, 0x76, 0x65, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x73, 0x32,
	0x97, 0x01, 0x0a, 0x16, 0x41, 0x63, 0x74, 0x69, 0x76, 0x65, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61,
	0x63, 0x74, 0x73, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x7d, 0x0a, 0x12, 0x47, 0x65,
	0x74, 0x41, 0x63, 0x74, 0x69, 0x76, 0x65, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x73,
	0x12, 0x31, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x47, 0x65, 0x74, 0x41, 0x63, 0x74,
	0x69, 0x76, 0x65, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x73, 0x52, 0x65, 0x71, 0x75,
	0x65, 0x73, 0x74, 0x1a, 0x32, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c,
	0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x47, 0x65, 0x74,
	0x41, 0x63, 0x74, 0x69, 0x76, 0x65, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x61, 0x63, 0x74, 0x73, 0x52,
	0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x30, 0x01, 0x42, 0x9a, 0x01, 0x0a, 0x16, 0x63, 0x6f,
	0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70,
	0x69, 0x2e, 0x76, 0x31, 0x42, 0x20, 0x41, 0x63, 0x74, 0x69, 0x76, 0x65, 0x43, 0x6f, 0x6e, 0x74,
	0x72, 0x61, 0x63, 0x74, 0x73, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x4f, 0x75, 0x74, 0x65,
	0x72, 0x43, 0x6c, 0x61, 0x73, 0x73, 0x5a, 0x45, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63,
	0x6f, 0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74,
	0x2f, 0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x76, 0x38, 0x2f,
	0x67, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f,
	0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0xaa, 0x02, 0x16,
	0x43, 0x6f, 0x6d, 0x2e, 0x44, 0x61, 0x6d, 0x6c, 0x2e, 0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e,
	0x41, 0x70, 0x69, 0x2e, 0x56, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_com_daml_ledger_api_v1_active_contracts_service_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v1_active_contracts_service_proto_rawDescData = file_com_daml_ledger_api_v1_active_contracts_service_proto_rawDesc
)

func file_com_daml_ledger_api_v1_active_contracts_service_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v1_active_contracts_service_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v1_active_contracts_service_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_ledger_api_v1_active_contracts_service_proto_rawDescData)
	})
	return file_com_daml_ledger_api_v1_active_contracts_service_proto_rawDescData
}

var file_com_daml_ledger_api_v1_active_contracts_service_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_com_daml_ledger_api_v1_active_contracts_service_proto_goTypes = []interface{}{
	(*GetActiveContractsRequest)(nil),  // 0: com.daml.ledger.api.v1.GetActiveContractsRequest
	(*GetActiveContractsResponse)(nil), // 1: com.daml.ledger.api.v1.GetActiveContractsResponse
	(*TransactionFilter)(nil),          // 2: com.daml.ledger.api.v1.TransactionFilter
	(*CreatedEvent)(nil),               // 3: com.daml.ledger.api.v1.CreatedEvent
}
var file_com_daml_ledger_api_v1_active_contracts_service_proto_depIdxs = []int32{
	2, // 0: com.daml.ledger.api.v1.GetActiveContractsRequest.filter:type_name -> com.daml.ledger.api.v1.TransactionFilter
	3, // 1: com.daml.ledger.api.v1.GetActiveContractsResponse.active_contracts:type_name -> com.daml.ledger.api.v1.CreatedEvent
	0, // 2: com.daml.ledger.api.v1.ActiveContractsService.GetActiveContracts:input_type -> com.daml.ledger.api.v1.GetActiveContractsRequest
	1, // 3: com.daml.ledger.api.v1.ActiveContractsService.GetActiveContracts:output_type -> com.daml.ledger.api.v1.GetActiveContractsResponse
	3, // [3:4] is the sub-list for method output_type
	2, // [2:3] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v1_active_contracts_service_proto_init() }
func file_com_daml_ledger_api_v1_active_contracts_service_proto_init() {
	if File_com_daml_ledger_api_v1_active_contracts_service_proto != nil {
		return
	}
	file_com_daml_ledger_api_v1_event_proto_init()
	file_com_daml_ledger_api_v1_transaction_filter_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_com_daml_ledger_api_v1_active_contracts_service_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetActiveContractsRequest); i {
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
		file_com_daml_ledger_api_v1_active_contracts_service_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetActiveContractsResponse); i {
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
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_daml_ledger_api_v1_active_contracts_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_daml_ledger_api_v1_active_contracts_service_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v1_active_contracts_service_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v1_active_contracts_service_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v1_active_contracts_service_proto = out.File
	file_com_daml_ledger_api_v1_active_contracts_service_proto_rawDesc = nil
	file_com_daml_ledger_api_v1_active_contracts_service_proto_goTypes = nil
	file_com_daml_ledger_api_v1_active_contracts_service_proto_depIdxs = nil
}
