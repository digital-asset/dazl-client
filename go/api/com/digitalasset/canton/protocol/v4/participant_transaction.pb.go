// Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v6.30.0
// source: com/digitalasset/canton/protocol/v4/participant_transaction.proto

package v4

import (
	v0 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/crypto/v0"
	v01 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v0"
	v1 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v1"
	v2 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v2"
	v3 "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v3"
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

type ViewParticipantData struct {
	state                          protoimpl.MessageState                   `protogen:"open.v1"`
	Salt                           *v0.Salt                                 `protobuf:"bytes,1,opt,name=salt,proto3" json:"salt,omitempty"`
	CoreInputs                     []*v2.InputContract                      `protobuf:"bytes,2,rep,name=core_inputs,json=coreInputs,proto3" json:"core_inputs,omitempty"`
	CreatedCore                    []*v2.CreatedContract                    `protobuf:"bytes,3,rep,name=created_core,json=createdCore,proto3" json:"created_core,omitempty"`
	CreatedInSubviewArchivedInCore []string                                 `protobuf:"bytes,4,rep,name=created_in_subview_archived_in_core,json=createdInSubviewArchivedInCore,proto3" json:"created_in_subview_archived_in_core,omitempty"`
	ResolvedKeys                   []*v1.ResolvedKey                        `protobuf:"bytes,5,rep,name=resolved_keys,json=resolvedKeys,proto3" json:"resolved_keys,omitempty"`
	ActionDescription              *v3.ActionDescription                    `protobuf:"bytes,6,opt,name=action_description,json=actionDescription,proto3" json:"action_description,omitempty"`
	RollbackContext                *v01.ViewParticipantData_RollbackContext `protobuf:"bytes,7,opt,name=rollback_context,json=rollbackContext,proto3" json:"rollback_context,omitempty"`
	unknownFields                  protoimpl.UnknownFields
	sizeCache                      protoimpl.SizeCache
}

func (x *ViewParticipantData) Reset() {
	*x = ViewParticipantData{}
	mi := &file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ViewParticipantData) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ViewParticipantData) ProtoMessage() {}

func (x *ViewParticipantData) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ViewParticipantData.ProtoReflect.Descriptor instead.
func (*ViewParticipantData) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_rawDescGZIP(), []int{0}
}

func (x *ViewParticipantData) GetSalt() *v0.Salt {
	if x != nil {
		return x.Salt
	}
	return nil
}

func (x *ViewParticipantData) GetCoreInputs() []*v2.InputContract {
	if x != nil {
		return x.CoreInputs
	}
	return nil
}

func (x *ViewParticipantData) GetCreatedCore() []*v2.CreatedContract {
	if x != nil {
		return x.CreatedCore
	}
	return nil
}

func (x *ViewParticipantData) GetCreatedInSubviewArchivedInCore() []string {
	if x != nil {
		return x.CreatedInSubviewArchivedInCore
	}
	return nil
}

func (x *ViewParticipantData) GetResolvedKeys() []*v1.ResolvedKey {
	if x != nil {
		return x.ResolvedKeys
	}
	return nil
}

func (x *ViewParticipantData) GetActionDescription() *v3.ActionDescription {
	if x != nil {
		return x.ActionDescription
	}
	return nil
}

func (x *ViewParticipantData) GetRollbackContext() *v01.ViewParticipantData_RollbackContext {
	if x != nil {
		return x.RollbackContext
	}
	return nil
}

type ActionDescription struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// Types that are valid to be assigned to Description:
	//
	//	*ActionDescription_Create
	//	*ActionDescription_Exercise
	//	*ActionDescription_Fetch
	//	*ActionDescription_LookupByKey
	Description   isActionDescription_Description `protobuf_oneof:"description"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ActionDescription) Reset() {
	*x = ActionDescription{}
	mi := &file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ActionDescription) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ActionDescription) ProtoMessage() {}

func (x *ActionDescription) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ActionDescription.ProtoReflect.Descriptor instead.
func (*ActionDescription) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_rawDescGZIP(), []int{1}
}

func (x *ActionDescription) GetDescription() isActionDescription_Description {
	if x != nil {
		return x.Description
	}
	return nil
}

func (x *ActionDescription) GetCreate() *v01.ActionDescription_CreateActionDescription {
	if x != nil {
		if x, ok := x.Description.(*ActionDescription_Create); ok {
			return x.Create
		}
	}
	return nil
}

func (x *ActionDescription) GetExercise() *v3.ActionDescription_ExerciseActionDescription {
	if x != nil {
		if x, ok := x.Description.(*ActionDescription_Exercise); ok {
			return x.Exercise
		}
	}
	return nil
}

func (x *ActionDescription) GetFetch() *ActionDescription_FetchActionDescription {
	if x != nil {
		if x, ok := x.Description.(*ActionDescription_Fetch); ok {
			return x.Fetch
		}
	}
	return nil
}

func (x *ActionDescription) GetLookupByKey() *v1.ActionDescription_LookupByKeyActionDescription {
	if x != nil {
		if x, ok := x.Description.(*ActionDescription_LookupByKey); ok {
			return x.LookupByKey
		}
	}
	return nil
}

type isActionDescription_Description interface {
	isActionDescription_Description()
}

type ActionDescription_Create struct {
	Create *v01.ActionDescription_CreateActionDescription `protobuf:"bytes,1,opt,name=create,proto3,oneof"`
}

type ActionDescription_Exercise struct {
	Exercise *v3.ActionDescription_ExerciseActionDescription `protobuf:"bytes,2,opt,name=exercise,proto3,oneof"`
}

type ActionDescription_Fetch struct {
	Fetch *ActionDescription_FetchActionDescription `protobuf:"bytes,3,opt,name=fetch,proto3,oneof"`
}

type ActionDescription_LookupByKey struct {
	LookupByKey *v1.ActionDescription_LookupByKeyActionDescription `protobuf:"bytes,4,opt,name=lookup_by_key,json=lookupByKey,proto3,oneof"`
}

func (*ActionDescription_Create) isActionDescription_Description() {}

func (*ActionDescription_Exercise) isActionDescription_Description() {}

func (*ActionDescription_Fetch) isActionDescription_Description() {}

func (*ActionDescription_LookupByKey) isActionDescription_Description() {}

type ActionDescription_FetchActionDescription struct {
	state           protoimpl.MessageState `protogen:"open.v1"`
	InputContractId string                 `protobuf:"bytes,1,opt,name=input_contract_id,json=inputContractId,proto3" json:"input_contract_id,omitempty"`
	Actors          []string               `protobuf:"bytes,2,rep,name=actors,proto3" json:"actors,omitempty"`
	ByKey           bool                   `protobuf:"varint,3,opt,name=by_key,json=byKey,proto3" json:"by_key,omitempty"`
	Version         string                 `protobuf:"bytes,4,opt,name=version,proto3" json:"version,omitempty"`
	TemplateId      *string                `protobuf:"bytes,5,opt,name=template_id,json=templateId,proto3,oneof" json:"template_id,omitempty"`
	InterfaceId     *string                `protobuf:"bytes,6,opt,name=interface_id,json=interfaceId,proto3,oneof" json:"interface_id,omitempty"`
	unknownFields   protoimpl.UnknownFields
	sizeCache       protoimpl.SizeCache
}

func (x *ActionDescription_FetchActionDescription) Reset() {
	*x = ActionDescription_FetchActionDescription{}
	mi := &file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ActionDescription_FetchActionDescription) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ActionDescription_FetchActionDescription) ProtoMessage() {}

func (x *ActionDescription_FetchActionDescription) ProtoReflect() protoreflect.Message {
	mi := &file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ActionDescription_FetchActionDescription.ProtoReflect.Descriptor instead.
func (*ActionDescription_FetchActionDescription) Descriptor() ([]byte, []int) {
	return file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_rawDescGZIP(), []int{1, 0}
}

func (x *ActionDescription_FetchActionDescription) GetInputContractId() string {
	if x != nil {
		return x.InputContractId
	}
	return ""
}

func (x *ActionDescription_FetchActionDescription) GetActors() []string {
	if x != nil {
		return x.Actors
	}
	return nil
}

func (x *ActionDescription_FetchActionDescription) GetByKey() bool {
	if x != nil {
		return x.ByKey
	}
	return false
}

func (x *ActionDescription_FetchActionDescription) GetVersion() string {
	if x != nil {
		return x.Version
	}
	return ""
}

func (x *ActionDescription_FetchActionDescription) GetTemplateId() string {
	if x != nil && x.TemplateId != nil {
		return *x.TemplateId
	}
	return ""
}

func (x *ActionDescription_FetchActionDescription) GetInterfaceId() string {
	if x != nil && x.InterfaceId != nil {
		return *x.InterfaceId
	}
	return ""
}

var File_com_digitalasset_canton_protocol_v4_participant_transaction_proto protoreflect.FileDescriptor

const file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_rawDesc = "" +
	"\n" +
	"Acom/digitalasset/canton/protocol/v4/participant_transaction.proto\x12#com.digitalasset.canton.protocol.v4\x1a.com/digitalasset/canton/crypto/v0/crypto.proto\x1aAcom/digitalasset/canton/protocol/v0/participant_transaction.proto\x1aAcom/digitalasset/canton/protocol/v1/participant_transaction.proto\x1aAcom/digitalasset/canton/protocol/v2/participant_transaction.proto\x1aAcom/digitalasset/canton/protocol/v3/participant_transaction.proto\"\x80\x05\n" +
	"\x13ViewParticipantData\x12;\n" +
	"\x04salt\x18\x01 \x01(\v2'.com.digitalasset.canton.crypto.v0.SaltR\x04salt\x12S\n" +
	"\vcore_inputs\x18\x02 \x03(\v22.com.digitalasset.canton.protocol.v2.InputContractR\n" +
	"coreInputs\x12W\n" +
	"\fcreated_core\x18\x03 \x03(\v24.com.digitalasset.canton.protocol.v2.CreatedContractR\vcreatedCore\x12K\n" +
	"#created_in_subview_archived_in_core\x18\x04 \x03(\tR\x1ecreatedInSubviewArchivedInCore\x12U\n" +
	"\rresolved_keys\x18\x05 \x03(\v20.com.digitalasset.canton.protocol.v1.ResolvedKeyR\fresolvedKeys\x12e\n" +
	"\x12action_description\x18\x06 \x01(\v26.com.digitalasset.canton.protocol.v3.ActionDescriptionR\x11actionDescription\x12s\n" +
	"\x10rollback_context\x18\a \x01(\v2H.com.digitalasset.canton.protocol.v0.ViewParticipantData.RollbackContextR\x0frollbackContext\"\xdd\x05\n" +
	"\x11ActionDescription\x12h\n" +
	"\x06create\x18\x01 \x01(\v2N.com.digitalasset.canton.protocol.v0.ActionDescription.CreateActionDescriptionH\x00R\x06create\x12n\n" +
	"\bexercise\x18\x02 \x01(\v2P.com.digitalasset.canton.protocol.v3.ActionDescription.ExerciseActionDescriptionH\x00R\bexercise\x12e\n" +
	"\x05fetch\x18\x03 \x01(\v2M.com.digitalasset.canton.protocol.v4.ActionDescription.FetchActionDescriptionH\x00R\x05fetch\x12y\n" +
	"\rlookup_by_key\x18\x04 \x01(\v2S.com.digitalasset.canton.protocol.v1.ActionDescription.LookupByKeyActionDescriptionH\x00R\vlookupByKey\x1a\xfc\x01\n" +
	"\x16FetchActionDescription\x12*\n" +
	"\x11input_contract_id\x18\x01 \x01(\tR\x0finputContractId\x12\x16\n" +
	"\x06actors\x18\x02 \x03(\tR\x06actors\x12\x15\n" +
	"\x06by_key\x18\x03 \x01(\bR\x05byKey\x12\x18\n" +
	"\aversion\x18\x04 \x01(\tR\aversion\x12$\n" +
	"\vtemplate_id\x18\x05 \x01(\tH\x00R\n" +
	"templateId\x88\x01\x01\x12&\n" +
	"\finterface_id\x18\x06 \x01(\tH\x01R\vinterfaceId\x88\x01\x01B\x0e\n" +
	"\f_template_idB\x0f\n" +
	"\r_interface_idB\r\n" +
	"\vdescriptionBTZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v4b\x06proto3"

var (
	file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_rawDescOnce sync.Once
	file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_rawDescData []byte
)

func file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_rawDescGZIP() []byte {
	file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_rawDescOnce.Do(func() {
		file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_rawDesc), len(file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_rawDesc)))
	})
	return file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_rawDescData
}

var file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_goTypes = []any{
	(*ViewParticipantData)(nil),                               // 0: com.digitalasset.canton.protocol.v4.ViewParticipantData
	(*ActionDescription)(nil),                                 // 1: com.digitalasset.canton.protocol.v4.ActionDescription
	(*ActionDescription_FetchActionDescription)(nil),          // 2: com.digitalasset.canton.protocol.v4.ActionDescription.FetchActionDescription
	(*v0.Salt)(nil),                                           // 3: com.digitalasset.canton.crypto.v0.Salt
	(*v2.InputContract)(nil),                                  // 4: com.digitalasset.canton.protocol.v2.InputContract
	(*v2.CreatedContract)(nil),                                // 5: com.digitalasset.canton.protocol.v2.CreatedContract
	(*v1.ResolvedKey)(nil),                                    // 6: com.digitalasset.canton.protocol.v1.ResolvedKey
	(*v3.ActionDescription)(nil),                              // 7: com.digitalasset.canton.protocol.v3.ActionDescription
	(*v01.ViewParticipantData_RollbackContext)(nil),           // 8: com.digitalasset.canton.protocol.v0.ViewParticipantData.RollbackContext
	(*v01.ActionDescription_CreateActionDescription)(nil),     // 9: com.digitalasset.canton.protocol.v0.ActionDescription.CreateActionDescription
	(*v3.ActionDescription_ExerciseActionDescription)(nil),    // 10: com.digitalasset.canton.protocol.v3.ActionDescription.ExerciseActionDescription
	(*v1.ActionDescription_LookupByKeyActionDescription)(nil), // 11: com.digitalasset.canton.protocol.v1.ActionDescription.LookupByKeyActionDescription
}
var file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_depIdxs = []int32{
	3,  // 0: com.digitalasset.canton.protocol.v4.ViewParticipantData.salt:type_name -> com.digitalasset.canton.crypto.v0.Salt
	4,  // 1: com.digitalasset.canton.protocol.v4.ViewParticipantData.core_inputs:type_name -> com.digitalasset.canton.protocol.v2.InputContract
	5,  // 2: com.digitalasset.canton.protocol.v4.ViewParticipantData.created_core:type_name -> com.digitalasset.canton.protocol.v2.CreatedContract
	6,  // 3: com.digitalasset.canton.protocol.v4.ViewParticipantData.resolved_keys:type_name -> com.digitalasset.canton.protocol.v1.ResolvedKey
	7,  // 4: com.digitalasset.canton.protocol.v4.ViewParticipantData.action_description:type_name -> com.digitalasset.canton.protocol.v3.ActionDescription
	8,  // 5: com.digitalasset.canton.protocol.v4.ViewParticipantData.rollback_context:type_name -> com.digitalasset.canton.protocol.v0.ViewParticipantData.RollbackContext
	9,  // 6: com.digitalasset.canton.protocol.v4.ActionDescription.create:type_name -> com.digitalasset.canton.protocol.v0.ActionDescription.CreateActionDescription
	10, // 7: com.digitalasset.canton.protocol.v4.ActionDescription.exercise:type_name -> com.digitalasset.canton.protocol.v3.ActionDescription.ExerciseActionDescription
	2,  // 8: com.digitalasset.canton.protocol.v4.ActionDescription.fetch:type_name -> com.digitalasset.canton.protocol.v4.ActionDescription.FetchActionDescription
	11, // 9: com.digitalasset.canton.protocol.v4.ActionDescription.lookup_by_key:type_name -> com.digitalasset.canton.protocol.v1.ActionDescription.LookupByKeyActionDescription
	10, // [10:10] is the sub-list for method output_type
	10, // [10:10] is the sub-list for method input_type
	10, // [10:10] is the sub-list for extension type_name
	10, // [10:10] is the sub-list for extension extendee
	0,  // [0:10] is the sub-list for field type_name
}

func init() { file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_init() }
func file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_init() {
	if File_com_digitalasset_canton_protocol_v4_participant_transaction_proto != nil {
		return
	}
	file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_msgTypes[1].OneofWrappers = []any{
		(*ActionDescription_Create)(nil),
		(*ActionDescription_Exercise)(nil),
		(*ActionDescription_Fetch)(nil),
		(*ActionDescription_LookupByKey)(nil),
	}
	file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_msgTypes[2].OneofWrappers = []any{}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_rawDesc), len(file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_goTypes,
		DependencyIndexes: file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_depIdxs,
		MessageInfos:      file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_msgTypes,
	}.Build()
	File_com_digitalasset_canton_protocol_v4_participant_transaction_proto = out.File
	file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_goTypes = nil
	file_com_digitalasset_canton_protocol_v4_participant_transaction_proto_depIdxs = nil
}
