# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# type: ignore

from io import StringIO
from typing import Dict, List, Tuple

from dazl.model.types import ContractIdType, ListType, RecordType, Type, TypeReference
from dazl.model.types_store import PackageStore


def write_csv(store: PackageStore) -> str:
    templates = {
        template.data_type.name.full_name: template for template in store.resolve_template("*")
    }

    with StringIO() as buf:
        for template_name in sorted(templates):
            template = templates[template_name]
            buf.write(f"# {template_name}\n")

            field_types = {}  # type: Dict[str, Type]
            queue = [("", template.data_type)]  # type: List[Tuple[str, Type]]
            while queue:
                prefix, data_type = queue.pop(0)
                if isinstance(data_type, TypeReference):
                    data_type = store.resolve_type_reference(data_type)
                if isinstance(data_type, RecordType):
                    pfx = (prefix + ".") if prefix else ""
                    queue[0:0] = [(f"{pfx}{n}", dt) for n, dt in data_type.named_args]
                elif isinstance(data_type, ListType):
                    queue.insert(0, (f"{prefix}[]", data_type.type_parameter))
                else:
                    field_types[prefix] = data_type

            for name, terminal_type in field_types.items():
                if isinstance(terminal_type, ContractIdType):
                    buf.write(f"#    {name}: ContractId {terminal_type.type_parameter}\n")
                else:
                    buf.write(f"#    {name}: {terminal_type}\n")
            buf.write(",".join(f'"{k}"' for k in field_types))
            buf.write("\n\n")

        return buf.getvalue()
