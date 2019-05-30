# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase, skip

from dazl.client._writer_verify import ValidateSerializer
from dazl.model.types import TypeReference, ModuleRef, RecordType, NamedArgumentList, \
    SCALAR_TYPE_INTEGER
from dazl.model.types_store import PackageStoreBuilder


class TestSerializationErrors(TestCase):

    @skip('TODO: Enforce structural validations in ValidateSerializer')
    def test_validations(self):
        type_ref = TypeReference(ModuleRef('pkg0', 'Some'), ('Template',))
        data_type = RecordType(name=type_ref, named_args=NamedArgumentList((('a', SCALAR_TYPE_INTEGER),)), type_args=())

        psb = PackageStoreBuilder()
        psb.add_type(type_ref, data_type)
        serializer = ValidateSerializer(psb.build())
        result1 = serializer.serialize_value(type_ref, {'a': {}})
        result2 = serializer.serialize_value(type_ref, {'b': 2})
        print(result1)
        print(result2)
