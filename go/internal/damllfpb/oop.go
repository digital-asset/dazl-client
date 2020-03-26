// Package for lowest-common denominator types. This is the manifestation of the various DAML-LF message
// types as it can faithfully be represented in almost any language, with some compromises:
//
// * oneof Protobuf messages are typically modelled as interfaces, with each possible variant modelled
//   as an explicit implementation of that type.
package damllfpb

type OopModels struct {
	
}

type OopClass struct {
	// An optional interface that this class is to implement.
	Interface *OopInterface

	// The properties that are specific to this class. The interface may additionally define
	// properties that are to be added to this class, but they will not be repeated here.
	Properties []*OopProperty
}

// An interface in the Java/C# sense. For all sum types that are translated, each case is implemented
// as a concrete class that implements this interface.
type OopInterface struct {
	// The properties that are common to all implementations of this interface.
	Properties []*OopProperty
}

type OopEnum struct {
	Values []OopEnumValue
}

type OopEnumValue struct {
	Name string
	Value int32
}

type OopType interface {
}

type OopPrimitiveType int

const (
	OopUnitType OopPrimitiveType = iota
	OopStringType
)

type OopProperty struct {
	Name string
	Type OopType
}
