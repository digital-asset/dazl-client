"""
A simple model for algebraic data types, with a few unexpected twists:

 * Product types and Sum types are both represented, although Sum types in this representation can
   also carry additional fields that are common to all cases.
 * Primitive types here also include representations for all DAML primitive types. This allows this
   code to be reused in the DAML-LF code generators as well as over the wire.
 * DAML-LF Protobuf constructs are also included (notably, string for interning).
"""

from dataclasses import dataclass, field
from typing import AbstractSet, List, Optional, Sequence, Set


@dataclass
class Package:
    type_declarations: 'List[TypeDecl]' = field(default_factory=list)


@dataclass(frozen=True)
class TypeRef:
    """
    A reference to a Type.
    """


@dataclass(frozen=True)
class TypeCon(TypeRef):
    """
    A type constructor. This signifies a reference to a nearby :class:`TypeDecl`.
    """
    name: str


@dataclass(frozen=True)
class PrimitiveType(TypeRef):
    name: str


@dataclass(frozen=True)
class OptionalType(TypeRef):
    arg: 'TypeRef'


@dataclass(frozen=True)
class SeqType(TypeRef):
    arg: 'TypeRef'


TYPE_DOTTED_NAME = TypeCon("DottedName")
TYPE_STRING = PrimitiveType("string")
TYPE_FIXED32 = PrimitiveType("fixed32")
TYPE_FIXED64 = PrimitiveType("fixed64")
TYPE_INT32 = PrimitiveType("int32")
TYPE_INT64 = PrimitiveType("int64")
TYPE_UINT32 = PrimitiveType("uint32")
TYPE_UINT64 = PrimitiveType("uint64")
TYPE_UNIT = PrimitiveType("Unit")
TYPE_BOOL = PrimitiveType("bool")


@dataclass(frozen=True)
class TypeDecl:
    name: str
    doc: str


@dataclass(frozen=True)
class TypeSyn(TypeDecl):
    type: 'TypeRef'


@dataclass(frozen=True)
class Product(TypeDecl):
    """
    A product type. Product types are generally rendered as classes/structs.
    """
    fields: 'Sequence[Field]'


@dataclass(frozen=True)
class Field:
    name: str
    type: 'TypeRef'
    doc: str = ''
    raw_field: 'Optional[str]' = None
    intern_field: 'Optional[str]' = None


@dataclass(frozen=True)
class Sum(TypeDecl):
    """
    The combination of a product and a sum type.

    This only represents a true sum type if all the field names occur in the ``cases`` set.
    """
    fields: 'Sequence[Field]'
    cases: 'AbstractSet[str]'


@dataclass(frozen=True)
class Enum(TypeDecl):
    values: 'Sequence[EnumValue]'


@dataclass(frozen=True)
class EnumValue:
    name: str
    value: int


@dataclass
class TypeDeclBuilder:
    name: Optional[str] = None
    fields: 'List[FieldBuilder]' = field(default_factory=list)
    oneof_names: 'Sequence[str]' = field(default=tuple())
    significant_oneofs: 'Set[str]' = field(default_factory=set)
    syn_type: 'Optional[TypeRef]' = None
    doc: str = ""

    def oneof(self, index: int, significant: bool = False) -> 'str':
        """
        Remember a oneof as "significant" (used for more than just differentiating similarly named
        fields for purposes of string interning). This indicates a possible sum type.

        :return: The name of this oneof.
        """
        name = self.oneof_names[index]
        if significant:
            self.significant_oneofs.add(name)
        return name

    def field(self, name: str) -> 'FieldBuilder':
        """
        Get or create a :class:`FieldBuilder`.
        """
        for fb in self.fields:
            if fb.name == name:
                return fb
        fb = FieldBuilder(name)
        self.fields.append(fb)
        return fb

    def build(self) -> 'TypeDecl':
        """
        Build an appropriate algebraic data type for the fields that have been encountered.
        """
        if self.syn_type is not None:
            return TypeSyn(name=self.name, doc=self.doc, type=self.syn_type)

        it = iter(self.significant_oneofs)
        if sum_type := next(it, None) is None:
            # no significant oneofs
            return self._build_product()
        elif next(it, None) is None:
            # exactly one significant oneof
            return self._build_sum(sum_type)
        else:
            # more than one significant oneof
            raise ValueError(
                'Multiple significant oneofs in a single Message are not yet handled by '
                f'this generator (message {self.name} had oneofs {sorted(self.significant_oneofs)}')

    def _build_product(self) -> 'Product':
        return Product(
            name=self.name,
            doc=self.doc,
            fields=tuple(fb.build() for fb in self.fields))

    def _build_sum(self, sum_type: str) -> 'Sum':
        return Sum(
            name=self.name,
            doc=self.doc,
            fields=tuple(fb.build() for fb in self.fields),
            cases=frozenset(fb.name for fb in self.fields if fb.oneof))

    def make_syn(self, type):
        self.syn_type = type


@dataclass()
class FieldBuilder:
    name: str
    type: 'Optional[TypeRef]' = None
    doc: str = ''
    raw_field: 'Optional[str]' = None
    intern_field: 'Optional[str]' = None
    oneof: 'Optional[str]' = None

    def build(self) -> 'Field':
        return Field(
            name=self.name,
            type=self.type,
            doc=self.doc,
            raw_field=self.raw_field,
            intern_field=self.intern_field)
