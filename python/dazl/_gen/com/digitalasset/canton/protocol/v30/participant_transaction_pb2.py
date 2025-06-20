# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/protocol/v30/participant_transaction.proto
# Protobuf Python Version: 6.30.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    0,
    '',
    'com/digitalasset/canton/protocol/v30/participant_transaction.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...crypto.v30 import crypto_pb2 as com_dot_digitalasset_dot_canton_dot_crypto_dot_v30_dot_crypto__pb2
from . import common_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v30_dot_common__pb2
from . import common_stable_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v30_dot_common__stable__pb2
from . import merkle_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v30_dot_merkle__pb2
from . import quorum_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v30_dot_quorum__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBcom/digitalasset/canton/protocol/v30/participant_transaction.proto\x12$com.digitalasset.canton.protocol.v30\x1a/com/digitalasset/canton/crypto/v30/crypto.proto\x1a\x31\x63om/digitalasset/canton/protocol/v30/common.proto\x1a\x38\x63om/digitalasset/canton/protocol/v30/common_stable.proto\x1a\x31\x63om/digitalasset/canton/protocol/v30/merkle.proto\x1a\x31\x63om/digitalasset/canton/protocol/v30/quorum.proto\x1a\x1egoogle/protobuf/duration.proto\"r\n\x13\x44\x65\x64uplicationPeriod\x12\x37\n\x08\x64uration\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00R\x08\x64uration\x12\x18\n\x06offset\x18\x02 \x01(\x03H\x00R\x06offsetB\x08\n\x06period\"\xc0\x01\n\x13ParticipantMetadata\x12<\n\x04salt\x18\x01 \x01(\x0b\x32(.com.digitalasset.canton.crypto.v30.SaltR\x04salt\x12\x1f\n\x0bledger_time\x18\x02 \x01(\x03R\nledgerTime\x12)\n\x10preparation_time\x18\x03 \x01(\x03R\x0fpreparationTime\x12\x1f\n\x0bworkflow_id\x18\x04 \x01(\tR\nworkflowId\"\xf8\x01\n\x0fRootHashMessage\x12\x1b\n\troot_hash\x18\x01 \x01(\x0cR\x08rootHash\x12\'\n\x0fsynchronizer_id\x18\x02 \x01(\tR\x0esynchronizerId\x12K\n\tview_type\x18\x03 \x01(\x0e\x32..com.digitalasset.canton.protocol.v30.ViewTypeR\x08viewType\x12\x38\n\x18submission_topology_time\x18\x04 \x01(\x03R\x16submissionTopologyTime\x12\x18\n\x07payload\x18\x05 \x01(\x0cR\x07payload\"\x9f\x02\n\x08ViewNode\x12]\n\x10view_common_data\x18\x01 \x01(\x0b\x32\x33.com.digitalasset.canton.protocol.v30.BlindableNodeR\x0eviewCommonData\x12g\n\x15view_participant_data\x18\x02 \x01(\x0b\x32\x33.com.digitalasset.canton.protocol.v30.BlindableNodeR\x13viewParticipantData\x12K\n\x08subviews\x18\x03 \x01(\x0b\x32/.com.digitalasset.canton.protocol.v30.MerkleSeqR\x08subviews\"\xb4\x01\n\x0eViewCommonData\x12<\n\x04salt\x18\x01 \x01(\x0b\x32(.com.digitalasset.canton.crypto.v30.SaltR\x04salt\x12\x1c\n\tinformees\x18\x02 \x03(\tR\tinformees\x12\x46\n\x07quorums\x18\x03 \x03(\x0b\x32,.com.digitalasset.canton.protocol.v30.QuorumR\x07quorums\"8\n\x08Informee\x12\x14\n\x05party\x18\x01 \x01(\tR\x05party\x12\x16\n\x06weight\x18\x02 \x01(\x05R\x06weight\"\x1c\n\x16ViewParticipantMessage:\x02\x18\x01\"\xf0\x01\n\x0fInformeeMessage\x12\x64\n\x12\x66ull_informee_tree\x18\x01 \x01(\x0b\x32\x36.com.digitalasset.canton.protocol.v30.FullInformeeTreeR\x10\x66ullInformeeTree\x12w\n submitting_participant_signature\x18\x02 \x01(\x0b\x32-.com.digitalasset.canton.crypto.v30.SignatureR\x1esubmittingParticipantSignature\"\xd5\x01\n\x18LightTransactionViewTree\x12L\n\x04tree\x18\x01 \x01(\x0b\x32\x38.com.digitalasset.canton.protocol.v30.GenTransactionTreeR\x04tree\x12k\n\x17subview_hashes_and_keys\x18\x02 \x03(\x0b\x32\x34.com.digitalasset.canton.protocol.v30.ViewHashAndKeyR\x14subviewHashesAndKeys\"r\n\x0eViewHashAndKey\x12\x1b\n\tview_hash\x18\x01 \x01(\x0cR\x08viewHash\x12\x43\n\x1eview_encryption_key_randomness\x18\x02 \x01(\x0cR\x1bviewEncryptionKeyRandomness\"`\n\x10\x46ullInformeeTree\x12L\n\x04tree\x18\x01 \x01(\x0b\x32\x38.com.digitalasset.canton.protocol.v30.GenTransactionTreeR\x04tree\"\xb4\x01\n\x0f\x43reatedContract\x12V\n\x08\x63ontract\x18\x01 \x01(\x0b\x32:.com.digitalasset.canton.protocol.v30.SerializableContractR\x08\x63ontract\x12(\n\x10\x63onsumed_in_core\x18\x02 \x01(\x08R\x0e\x63onsumedInCore\x12\x1f\n\x0brolled_back\x18\x03 \x01(\x08R\nrolledBack\"\x83\x01\n\rInputContract\x12V\n\x08\x63ontract\x18\x01 \x01(\x0b\x32:.com.digitalasset.canton.protocol.v30.SerializableContractR\x08\x63ontract\x12\x1a\n\x08\x63onsumed\x18\x02 \x01(\x08R\x08\x63onsumed\"\xb8\x01\n\x0e\x43ommonMetadata\x12<\n\x04salt\x18\x01 \x01(\x0b\x32(.com.digitalasset.canton.crypto.v30.SaltR\x04salt\x12\'\n\x0fsynchronizer_id\x18\x03 \x01(\tR\x0esynchronizerId\x12\x12\n\x04uuid\x18\x04 \x01(\tR\x04uuid\x12%\n\x0emediator_group\x18\x05 \x01(\x05R\rmediatorGroupJ\x04\x08\x02\x10\x03\"\x85\x04\n\x11SubmitterMetadata\x12<\n\x04salt\x18\x01 \x01(\x0b\x32(.com.digitalasset.canton.crypto.v30.SaltR\x04salt\x12\x15\n\x06\x61\x63t_as\x18\x02 \x03(\tR\x05\x61\x63tAs\x12\x17\n\x07user_id\x18\x03 \x01(\tR\x06userId\x12\x1d\n\ncommand_id\x18\x04 \x01(\tR\tcommandId\x12<\n\x1asubmitting_participant_uid\x18\x05 \x01(\tR\x18submittingParticipantUid\x12#\n\rsubmission_id\x18\x06 \x01(\tR\x0csubmissionId\x12\\\n\x0c\x64\x65\x64up_period\x18\x07 \x01(\x0b\x32\x39.com.digitalasset.canton.protocol.v30.DeduplicationPeriodR\x0b\x64\x65\x64upPeriod\x12.\n\x13max_sequencing_time\x18\x08 \x01(\x03R\x11maxSequencingTime\x12r\n\x16\x65xternal_authorization\x18\t \x01(\x0b\x32;.com.digitalasset.canton.protocol.v30.ExternalAuthorizationR\x15\x65xternalAuthorization\"\x8b\x04\n\x14\x45ncryptedViewMessage\x12\x1b\n\tview_tree\x18\x01 \x01(\x0cR\x08viewTree\x12\x63\n\x11\x65ncryption_scheme\x18\x02 \x01(\x0e\x32\x36.com.digitalasset.canton.crypto.v30.SymmetricKeySchemeR\x10\x65ncryptionScheme\x12w\n submitting_participant_signature\x18\x03 \x01(\x0b\x32-.com.digitalasset.canton.crypto.v30.SignatureR\x1esubmittingParticipantSignature\x12\x1b\n\tview_hash\x18\x04 \x01(\x0cR\x08viewHash\x12\x65\n\x12session_key_lookup\x18\x05 \x03(\x0b\x32\x37.com.digitalasset.canton.crypto.v30.AsymmetricEncryptedR\x10sessionKeyLookup\x12\'\n\x0fsynchronizer_id\x18\x06 \x01(\tR\x0esynchronizerId\x12K\n\tview_type\x18\x07 \x01(\x0e\x32..com.digitalasset.canton.protocol.v30.ViewTypeR\x08viewType\"\xe0\t\n\x11\x41\x63tionDescription\x12i\n\x06\x63reate\x18\x01 \x01(\x0b\x32O.com.digitalasset.canton.protocol.v30.ActionDescription.CreateActionDescriptionH\x00R\x06\x63reate\x12o\n\x08\x65xercise\x18\x02 \x01(\x0b\x32Q.com.digitalasset.canton.protocol.v30.ActionDescription.ExerciseActionDescriptionH\x00R\x08\x65xercise\x12\x66\n\x05\x66\x65tch\x18\x03 \x01(\x0b\x32N.com.digitalasset.canton.protocol.v30.ActionDescription.FetchActionDescriptionH\x00R\x05\x66\x65tch\x12z\n\rlookup_by_key\x18\x04 \x01(\x0b\x32T.com.digitalasset.canton.protocol.v30.ActionDescription.LookupByKeyActionDescriptionH\x00R\x0blookupByKey\x1aW\n\x17\x43reateActionDescription\x12\x1f\n\x0b\x63ontract_id\x18\x01 \x01(\tR\ncontractId\x12\x1b\n\tnode_seed\x18\x02 \x01(\x0cR\x08nodeSeed\x1a\xef\x02\n\x19\x45xerciseActionDescription\x12*\n\x11input_contract_id\x18\x01 \x01(\tR\x0finputContractId\x12\x16\n\x06\x63hoice\x18\x02 \x01(\tR\x06\x63hoice\x12!\n\x0c\x63hosen_value\x18\x03 \x01(\x0cR\x0b\x63hosenValue\x12\x16\n\x06\x61\x63tors\x18\x04 \x03(\tR\x06\x61\x63tors\x12\x15\n\x06\x62y_key\x18\x05 \x01(\x08R\x05\x62yKey\x12\x1b\n\tnode_seed\x18\x06 \x01(\x0cR\x08nodeSeed\x12\x16\n\x06\x66\x61iled\x18\x08 \x01(\x08R\x06\x66\x61iled\x12&\n\x0cinterface_id\x18\t \x01(\tH\x00R\x0binterfaceId\x88\x01\x01\x12\x1f\n\x0btemplate_id\x18\n \x01(\tR\ntemplateId\x12-\n\x12package_preference\x18\x0b \x03(\tR\x11packagePreferenceB\x0f\n\r_interface_id\x1a\xcd\x01\n\x16\x46\x65tchActionDescription\x12*\n\x11input_contract_id\x18\x01 \x01(\tR\x0finputContractId\x12\x16\n\x06\x61\x63tors\x18\x02 \x03(\tR\x06\x61\x63tors\x12\x15\n\x06\x62y_key\x18\x03 \x01(\x08R\x05\x62yKey\x12\x1f\n\x0btemplate_id\x18\x04 \x01(\tR\ntemplateId\x12&\n\x0cinterface_id\x18\x05 \x01(\tH\x00R\x0binterfaceId\x88\x01\x01\x42\x0f\n\r_interface_id\x1a\x61\n\x1cLookupByKeyActionDescription\x12\x41\n\x03key\x18\x01 \x01(\x0b\x32/.com.digitalasset.canton.protocol.v30.GlobalKeyR\x03keyB\r\n\x0b\x64\x65scription\"\xfd\x07\n\x13ViewParticipantData\x12<\n\x04salt\x18\x01 \x01(\x0b\x32(.com.digitalasset.canton.crypto.v30.SaltR\x04salt\x12T\n\x0b\x63ore_inputs\x18\x02 \x03(\x0b\x32\x33.com.digitalasset.canton.protocol.v30.InputContractR\ncoreInputs\x12X\n\x0c\x63reated_core\x18\x03 \x03(\x0b\x32\x35.com.digitalasset.canton.protocol.v30.CreatedContractR\x0b\x63reatedCore\x12K\n#created_in_subview_archived_in_core\x18\x04 \x03(\tR\x1e\x63reatedInSubviewArchivedInCore\x12j\n\rresolved_keys\x18\x05 \x03(\x0b\x32\x45.com.digitalasset.canton.protocol.v30.ViewParticipantData.ResolvedKeyR\x0cresolvedKeys\x12\x66\n\x12\x61\x63tion_description\x18\x06 \x01(\x0b\x32\x37.com.digitalasset.canton.protocol.v30.ActionDescriptionR\x11\x61\x63tionDescription\x12t\n\x10rollback_context\x18\x07 \x01(\x0b\x32I.com.digitalasset.canton.protocol.v30.ViewParticipantData.RollbackContextR\x0frollbackContext\x1a+\n\x07\x46reeKey\x12 \n\x0bmaintainers\x18\x01 \x03(\tR\x0bmaintainers\x1a\xda\x01\n\x0bResolvedKey\x12\x41\n\x03key\x18\x01 \x01(\x0b\x32/.com.digitalasset.canton.protocol.v30.GlobalKeyR\x03key\x12!\n\x0b\x63ontract_id\x18\x02 \x01(\tH\x00R\ncontractId\x12W\n\x04\x66ree\x18\x03 \x01(\x0b\x32\x41.com.digitalasset.canton.protocol.v30.ViewParticipantData.FreeKeyH\x00R\x04\x66reeB\x0c\n\nresolution\x1aW\n\x0fRollbackContext\x12%\n\x0erollback_scope\x18\x01 \x03(\x05R\rrollbackScope\x12\x1d\n\nnext_child\x18\x02 \x01(\x05R\tnextChild\"\x81\x01\n\x1a\x45xternalPartyAuthorization\x12\x14\n\x05party\x18\x01 \x01(\tR\x05party\x12M\n\nsignatures\x18\x02 \x03(\x0b\x32-.com.digitalasset.canton.crypto.v30.SignatureR\nsignatures\"\xf1\x02\n\x15\x45xternalAuthorization\x12j\n\x0f\x61uthentications\x18\x01 \x03(\x0b\x32@.com.digitalasset.canton.protocol.v30.ExternalPartyAuthorizationR\x0f\x61uthentications\x12\x86\x01\n\x16hashing_scheme_version\x18\x02 \x01(\x0e\x32P.com.digitalasset.canton.protocol.v30.ExternalAuthorization.HashingSchemeVersionR\x14hashingSchemeVersion\"c\n\x14HashingSchemeVersion\x12&\n\"HASHING_SCHEME_VERSION_UNSPECIFIED\x10\x00\x12\x1d\n\x19HASHING_SCHEME_VERSION_V2\x10\x02\"\x04\x08\x01\x10\x01\x42UZSgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v30b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v30.participant_transaction_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZSgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v30'
  _globals['_VIEWPARTICIPANTMESSAGE']._loaded_options = None
  _globals['_VIEWPARTICIPANTMESSAGE']._serialized_options = b'\030\001'
  _globals['_DEDUPLICATIONPERIOD']._serialized_start=400
  _globals['_DEDUPLICATIONPERIOD']._serialized_end=514
  _globals['_PARTICIPANTMETADATA']._serialized_start=517
  _globals['_PARTICIPANTMETADATA']._serialized_end=709
  _globals['_ROOTHASHMESSAGE']._serialized_start=712
  _globals['_ROOTHASHMESSAGE']._serialized_end=960
  _globals['_VIEWNODE']._serialized_start=963
  _globals['_VIEWNODE']._serialized_end=1250
  _globals['_VIEWCOMMONDATA']._serialized_start=1253
  _globals['_VIEWCOMMONDATA']._serialized_end=1433
  _globals['_INFORMEE']._serialized_start=1435
  _globals['_INFORMEE']._serialized_end=1491
  _globals['_VIEWPARTICIPANTMESSAGE']._serialized_start=1493
  _globals['_VIEWPARTICIPANTMESSAGE']._serialized_end=1521
  _globals['_INFORMEEMESSAGE']._serialized_start=1524
  _globals['_INFORMEEMESSAGE']._serialized_end=1764
  _globals['_LIGHTTRANSACTIONVIEWTREE']._serialized_start=1767
  _globals['_LIGHTTRANSACTIONVIEWTREE']._serialized_end=1980
  _globals['_VIEWHASHANDKEY']._serialized_start=1982
  _globals['_VIEWHASHANDKEY']._serialized_end=2096
  _globals['_FULLINFORMEETREE']._serialized_start=2098
  _globals['_FULLINFORMEETREE']._serialized_end=2194
  _globals['_CREATEDCONTRACT']._serialized_start=2197
  _globals['_CREATEDCONTRACT']._serialized_end=2377
  _globals['_INPUTCONTRACT']._serialized_start=2380
  _globals['_INPUTCONTRACT']._serialized_end=2511
  _globals['_COMMONMETADATA']._serialized_start=2514
  _globals['_COMMONMETADATA']._serialized_end=2698
  _globals['_SUBMITTERMETADATA']._serialized_start=2701
  _globals['_SUBMITTERMETADATA']._serialized_end=3218
  _globals['_ENCRYPTEDVIEWMESSAGE']._serialized_start=3221
  _globals['_ENCRYPTEDVIEWMESSAGE']._serialized_end=3744
  _globals['_ACTIONDESCRIPTION']._serialized_start=3747
  _globals['_ACTIONDESCRIPTION']._serialized_end=4995
  _globals['_ACTIONDESCRIPTION_CREATEACTIONDESCRIPTION']._serialized_start=4216
  _globals['_ACTIONDESCRIPTION_CREATEACTIONDESCRIPTION']._serialized_end=4303
  _globals['_ACTIONDESCRIPTION_EXERCISEACTIONDESCRIPTION']._serialized_start=4306
  _globals['_ACTIONDESCRIPTION_EXERCISEACTIONDESCRIPTION']._serialized_end=4673
  _globals['_ACTIONDESCRIPTION_FETCHACTIONDESCRIPTION']._serialized_start=4676
  _globals['_ACTIONDESCRIPTION_FETCHACTIONDESCRIPTION']._serialized_end=4881
  _globals['_ACTIONDESCRIPTION_LOOKUPBYKEYACTIONDESCRIPTION']._serialized_start=4883
  _globals['_ACTIONDESCRIPTION_LOOKUPBYKEYACTIONDESCRIPTION']._serialized_end=4980
  _globals['_VIEWPARTICIPANTDATA']._serialized_start=4998
  _globals['_VIEWPARTICIPANTDATA']._serialized_end=6019
  _globals['_VIEWPARTICIPANTDATA_FREEKEY']._serialized_start=5666
  _globals['_VIEWPARTICIPANTDATA_FREEKEY']._serialized_end=5709
  _globals['_VIEWPARTICIPANTDATA_RESOLVEDKEY']._serialized_start=5712
  _globals['_VIEWPARTICIPANTDATA_RESOLVEDKEY']._serialized_end=5930
  _globals['_VIEWPARTICIPANTDATA_ROLLBACKCONTEXT']._serialized_start=5932
  _globals['_VIEWPARTICIPANTDATA_ROLLBACKCONTEXT']._serialized_end=6019
  _globals['_EXTERNALPARTYAUTHORIZATION']._serialized_start=6022
  _globals['_EXTERNALPARTYAUTHORIZATION']._serialized_end=6151
  _globals['_EXTERNALAUTHORIZATION']._serialized_start=6154
  _globals['_EXTERNALAUTHORIZATION']._serialized_end=6523
  _globals['_EXTERNALAUTHORIZATION_HASHINGSCHEMEVERSION']._serialized_start=6424
  _globals['_EXTERNALAUTHORIZATION_HASHINGSCHEMEVERSION']._serialized_end=6523
# @@protoc_insertion_point(module_scope)
