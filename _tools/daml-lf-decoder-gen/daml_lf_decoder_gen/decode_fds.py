from io import StringIO
from itertools import repeat

from google.protobuf.descriptor_pb2 import FileDescriptorSet, FieldDescriptorProto, SourceCodeInfo
from typing import List, Optional, TextIO

from daml_lf_decoder_gen import adt


class SourceMap:
    def __init__(self):
        self._data: 'List[SourceMap]' = list()
        self.leading_comments = None
        self.trailing_comments = None
        self.leading_detached_comments = None

    def get(self, *indices: int) -> 'Optional[SourceMap]':
        if not indices:
            return self

        if self is not None:
            index = indices[0]
            return SourceMap.get(self._data[index] if index < len(self._data) else None, *indices[1:])
        else:
            return None

    def ensure(self, index: int) -> 'SourceMap':
        """

        >>> sm = SourceMap(); sm.ensure(0)
        SourceMap([])

        >>> sm = SourceMap(); sm.ensure(2)
        SourceMap([])

        :param index:
        :return:
        """
        if (overage := (index - len(self._data) + 1)) > 0:
            self._data.extend(repeat(None, overage))
        if (source_map := self._data[index]) is None:
            source_map = SourceMap()
            self._data[index] = source_map
        if source_map is False:
            raise Exception('huh?')
        return source_map

    def write(self, buf: TextIO, indent=0):
        for i, val in enumerate(self._data):
            if val is not None:
                indent_str = indent * "  "
                if val.leading_comments:
                    buf.write(f'{indent_str}leadingComments: {val.leading_comments}\n')
                if val.trailing_comments:
                    buf.write(f'{indent_str}trailingComments: {val.leading_comments}\n')
                if val.leading_detached_comments:
                    buf.write(f'{indent_str}leadingDetachedComments: {";".join(val.leading_detached_comments)}\n')
                buf.write(f'{indent_str}{i}:\n')
                val.write(buf, indent + 1)

    def __str__(self):
        with StringIO() as buf:
            self.write(buf)
            return buf.getvalue()

    def __repr__(self):
        return f'SourceMap({self._data!r})'


def decode_fds(fds: FileDescriptorSet) -> 'adt.Package':
    package = adt.Package()

    for file in fds.file:
        if file.package == "daml_lf_1":
            source_map = decode_source_map(file.source_code_info)
            for i, message in enumerate(file.message_type):
                visit_message(package, "", message, SourceMap.get(source_map, 4, i))
            for i, enum in enumerate(file.enum_type):
                visit_enum(package, "", enum, SourceMap.get(source_map, 5, i))
    return package


def decode_source_map(sci: 'SourceCodeInfo') -> 'SourceMap':
    source_map = SourceMap()

    for loc in sci.location:
        target = source_map
        for path_item in loc.path:
            target = target.ensure(path_item)
        if loc.HasField('leading_comments'):
            target.leading_comments = loc.leading_comments
        if loc.HasField('trailing_comments'):
            target.trailing_comments = loc.trailing_comments
        target.leading_detached_comments = loc.leading_detached_comments

    return source_map


def visit_message(package, scope, message, source_map: 'SourceMap'):
    builder = adt.TypeDeclBuilder(
        name=f'{scope}.{message.name}' if scope else message.name,
        oneof_names=tuple(oneof.name for oneof in message.oneof_decl))
    if message.name in ('PackageRef', 'DottedName', 'ModuleRef'):
        builder.make_syn(adt.TYPE_STRING)
    else:
        for i, field in enumerate(message.field):
            significant_oneof = False
            if name := chop_suffix(field.name, "_interned_dname"):
                prop = builder.field(name)
                prop.type = adt.TYPE_DOTTED_NAME \
                    if not field.label == FieldDescriptorProto.Label.LABEL_REPEATED \
                    else adt.SeqType(adt.TYPE_DOTTED_NAME)
                prop.intern_field = field.name
            elif name := chop_suffix(field.name, "_dname"):
                prop = builder.field(name)
                prop.type = adt.TYPE_DOTTED_NAME \
                    if not field.label == FieldDescriptorProto.Label.LABEL_REPEATED \
                    else adt.SeqType(adt.TYPE_DOTTED_NAME)
                prop.raw_field = field.name
            elif name := chop_suffix(field.name, "_interned_str"):
                prop = builder.field(name)
                prop.type = adt.TYPE_STRING \
                    if not field.label == FieldDescriptorProto.Label.LABEL_REPEATED \
                    else adt.SeqType(adt.TYPE_STRING)
                prop.intern_field = field.name
            elif name := chop_suffix(field.name, "_str"):
                prop = builder.field(name)
                prop.type = adt.TYPE_STRING \
                    if not field.label == FieldDescriptorProto.Label.LABEL_REPEATED \
                    else adt.SeqType(adt.TYPE_STRING)
                prop.raw_field = field.name
            else:
                name = field.name
                prop = builder.field(name)
                prop.type = proto_type_to_adt_type(field)
                prop.raw_field = field.name
                significant_oneof = True

            if field.HasField('oneof_index'):
                prop.oneof = builder.oneof(field.oneof_index, significant=significant_oneof)

            if (field_src_info := SourceMap.get(source_map, 2)) is not None:
                if field_src_info.leading_comments is not None:
                    prop.doc += field_src_info.leading_comments
                if field_src_info.trailing_comments is not None:
                    prop.doc += field_src_info.trailing_comments

    if source_map is not None:
        if source_map.leading_comments is not None:
            builder.doc += source_map.leading_comments.strip()
        if source_map.trailing_comments is not None:
            builder.doc += source_map.trailing_comments.strip()

    package.type_declarations.append(builder.build())
    for x in message.nested_type:
        visit_message(package, builder.name, x, SourceMap.get(source_map, 4))


def visit_enum(package, scope, enum, source_map: 'SourceMap'):
    name = f'{scope}.{enum.name}' if scope else enum.name
    doc = ''
    values = [adt.EnumValue(value_pb.name, value_pb.number) for value_pb in enum.value]
    enum = adt.Enum(name=name, doc=doc, values=values)
    package.type_declarations.append(enum)


def chop_prefix(s: str, prefix: str) -> 'Optional[str]':
    return s[len(prefix):] if s.startswith(prefix) else None


def chop_suffix(s: str, suffix: str) -> 'Optional[str]':
    return s[:-len(suffix)] if s.endswith(suffix) else None


def proto_type_to_adt_type(fd_proto: FieldDescriptorProto) -> 'adt.TypeRef':
    type_ctor = adt.SeqType if fd_proto.label == FieldDescriptorProto.Label.LABEL_REPEATED \
        else lambda _: _

    if fd_proto.type == FieldDescriptorProto.Type.TYPE_STRING:
        return type_ctor(adt.TYPE_STRING)
    elif fd_proto.type == FieldDescriptorProto.Type.TYPE_BOOL:
        return type_ctor(adt.TYPE_BOOL)
    elif fd_proto.type == FieldDescriptorProto.Type.TYPE_FIXED32:
        return type_ctor(adt.TYPE_FIXED32)
    elif fd_proto.type == FieldDescriptorProto.Type.TYPE_SFIXED32:
        return type_ctor(adt.TYPE_FIXED32)
    elif fd_proto.type == FieldDescriptorProto.Type.TYPE_FIXED64:
        return type_ctor(adt.TYPE_FIXED64)
    elif fd_proto.type == FieldDescriptorProto.Type.TYPE_SFIXED64:
        return type_ctor(adt.TYPE_FIXED64)
    elif fd_proto.type == FieldDescriptorProto.Type.TYPE_INT32:
        return type_ctor(adt.TYPE_INT32)
    elif fd_proto.type == FieldDescriptorProto.Type.TYPE_SINT32:
        return type_ctor(adt.TYPE_INT32)
    elif fd_proto.type == FieldDescriptorProto.Type.TYPE_UINT32:
        return type_ctor(adt.TYPE_UINT32)
    elif fd_proto.type == FieldDescriptorProto.Type.TYPE_INT64:
        return type_ctor(adt.TYPE_INT64)
    elif fd_proto.type == FieldDescriptorProto.Type.TYPE_SINT64:
        return type_ctor(adt.TYPE_INT64)
    elif fd_proto.type == FieldDescriptorProto.Type.TYPE_UINT64:
        return type_ctor(adt.TYPE_UINT64)
    elif type_name := chop_prefix(fd_proto.type_name, '.daml_lf_1.'):
        return type_ctor(adt.TypeCon(type_name))
    else:
        raise ValueError(f"Unknown type {fd_proto.type_name} (type {fd_proto.type}) for field {fd_proto.name}")
