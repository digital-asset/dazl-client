# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from typing import Dict, List, Sequence, Union

from ..damlast.daml_lf_1 import Module
from ..model.types import ModuleRef


class ModuleHierarchy:
    START = 'START'
    ITEM = 'ITEM'
    END = 'END'

    def __init__(self, package_id, module_name: 'Sequence[str]' = ()):
        self.ref = ModuleRef(package_id, module_name)
        self._items = dict()  # type: Dict[str, ModuleHierarchy]
        self._modules = list()  # type: List[Module]

    def __getitem__(self, item: str):
        """
        Retrieve the sub-:class:`ModuleBuilder` prefixed by a name.
        :param item:
        :return:
        """
        mb = self._items.get(item)
        if mb is None:
            mb = ModuleHierarchy(self.ref.package_id, self.ref.module_name + (item,))
            self._items[item] = mb
        return mb

    def add_module(self, module: 'Module') -> None:
        obj = self
        components = module.name.segments
        for component in components:
            obj = obj[component]
        obj._modules.append(module)

    def __iter__(self):
        yield ModuleHierarchy.START, self.ref, None
        for child in self._items.values():
            yield from child
        for mod in self._modules:
            yield ModuleHierarchy.ITEM, self.ref, mod
        yield ModuleHierarchy.END, self.ref, None

    # def lines(self, depth: int = 0) -> Generator[str, None, None]:
    #     prefix = (depth * 4) * ' '
    #     for key, mb in self._items.items():
    #         yield ''
    #         yield ''
    #         yield f'{prefix}class {key}:'
    #         for leaf, template in mb._leaves.items():
    #             template_fn = template.data_type.name.full_name
    #             slot_names = tuple(name for name, _ in template.data_type.named_args)
    #
    #             yield f'{prefix}    class {leaf}(metaclass=TemplateMeta, template_name={template_fn!r}):'
    #             yield f'{prefix}        """'
    #             yield f'{prefix}        Example usage:'
    #             yield f'{prefix}            create({template_fn},'
    #             yield f'{prefix}                {python_example_object(self.store, template.data_type)}'
    #             yield f'{prefix}            )'
    #             for choice in template.choices:
    #                 yield f'{prefix}            exercise(cid, {choice.name!r}, {python_example_object(self.store, choice.data_type)})'
    #             yield f'{prefix}        """'
    #             yield f'{prefix}        __slots__ = {slot_names!r}'
    #             yield f'{prefix}'
    #             if slot_names:
    #                 yield f'{prefix}        def __init__(self, {", ".join(slot_names)}):'
    #                 for slot_name in slot_names:
    #                     yield f'{prefix}            self.{slot_name} = {slot_name}'
    #                 yield ''
    #                 yield f'{prefix}        def _asdict(self) -> dict:'
    #                 yield f'{prefix}            return {{'
    #                 for slot_name in slot_names:
    #                     yield f'{prefix}                {slot_name!r}: self.{slot_name},'
    #                 yield f'{prefix}                }}'
    #             else:
    #                 yield f'{prefix}        def _asdict(self) -> dict:'
    #                 yield f'{prefix}            return {{}}'
    #
    #             for choice in template.choices:
    #                 choice_data_type = self.store.resolve_type_reference(choice.data_type) if isinstance(choice.data_type, TypeReference) else choice.data_type
    #                 choice_slot_names = tuple(name for name, _ in choice_data_type.named_args) if isinstance(choice_data_type, RecordType) else ()
    #                 yield ''
    #                 yield f'{prefix}        class {choice.name}(metaclass=ChoiceMeta, template_name={template_fn!r}, choice_name={choice.name!r}):'
    #                 yield f'{prefix}            __slots__ = {choice_slot_names!r}'
    #
    #                 if choice_slot_names:
    #                     yield ''
    #                     yield f'{prefix}            def __init__(self, {", ".join(choice_slot_names)}):'
    #                     for choice_slot_name in choice_slot_names:
    #                         yield f'{prefix}                self.{choice_slot_name} = {choice_slot_name}'
    #                     yield ''
    #                     yield f'{prefix}            def _asdict(self) -> dict:'
    #                     yield f'{prefix}                return {{'
    #                     for choice_slot_name in choice_slot_names:
    #                         yield f'{prefix}                    {choice_slot_name!r}: self.{choice_slot_name},'
    #                     yield f'{prefix}                    }}'
    #                 else:
    #                     yield f'{prefix}            def _asdict(self) -> dict:'
    #                     yield f'{prefix}                return {{}}'
    #             yield f''
    #         for line in mb.lines(depth + 1):
    #             yield line

    def __repr__(self):
        return f'ModuleBuilder(ref={self.ref}, items={self._items})'

