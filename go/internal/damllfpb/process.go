package damllfpb

import (
	"errors"
	"fmt"
	pb "github.com/digital-asset/dazl/go/gen/com/daml/daml_lf_dev"
	"google.golang.org/protobuf/reflect/protoreflect"
)

// Build a Root object that stores a simple representation of the DAML-LF Protobuf files for ease of generating
// code in various target languages.
func BuildRoot() (*Root, error) {
	damlLfProto := pb.File_com_daml_daml_lf_dev_daml_lf_1_proto
	prefix := string(damlLfProto.Name())

	root := NewRoot(prefix)

	damlLfProtoMessages := damlLfProto.Messages()
	for i, length := 0, damlLfProtoMessages.Len(); i < length; i++ {
		if err := processMessage(root, damlLfProtoMessages.Get(i)); err != nil {
			return nil, err
		}
	}

	damlLfProtoEnums := damlLfProto.Enums()
	for i, length := 0, damlLfProtoEnums.Len(); i < length; i++ {
		if err := processEnum(root, damlLfProtoEnums.Get(i)); err != nil {
			return nil, err
		}
	}

	return root, nil
}

func processMessage(root *Root, protoMessage protoreflect.MessageDescriptor) error {
	name := string(protoMessage.FullName())
	message := root.Message(name)
	fields := protoMessage.Fields()
	for f, flen := 0, fields.Len(); f < flen; f++ {
		if _, err := processField(message, fields.Get(f)); err != nil {
			return err
		}
	}

	subMessages := protoMessage.Messages()
	for i, length := 0, subMessages.Len(); i < length; i++ {
		if err := processMessage(root, subMessages.Get(i)); err != nil {
			return err
		}
	}

	return nil
}

func processField(message *Message, field protoreflect.FieldDescriptor) (*MessageField, error) {
	var oneOfName string
	if oneOf := field.ContainingOneof(); oneOf != nil {
		oneOfName = string(oneOf.Name())
	}

	fieldType, err := getFieldType(message.node.root, field)
	if err != nil {
		return nil, err
	}

	return message.ProcessMessageField(string(field.Name()), oneOfName, fieldType)
}

func processEnum(root *Root, protoEnum protoreflect.EnumDescriptor) error {
	enum := root.Enum(string(protoEnum.FullName()))
	values := protoEnum.Values()
	for i, length := 0, values.Len(); i < length; i++ {
		protoEnumValue := values.Get(i)
		enum.Add(string(protoEnumValue.Name()), int32(protoEnumValue.Number()))
	}
	return nil
}

func getFieldType(root *Root, field protoreflect.FieldDescriptor) (FieldType, error) {
	isRepeated := field.Cardinality() == protoreflect.Repeated
	switch field.Kind() {
	case protoreflect.BoolKind:
		return BuiltInType{Repeated: isRepeated, Name: "bool"}, nil
	case protoreflect.EnumKind:
		enumType := field.Enum()
		name := string(enumType.Name())
		valuePB := enumType.Values()
		var values []string
		for i, length := 0, valuePB.Len(); i < length; i++ {
			values = append(values, string(valuePB.Get(i).Name()))
		}
		return EnumFieldType{Repeated: isRepeated, Name: name, Values: values}, nil
	case protoreflect.Int32Kind:
		return BuiltInType{Repeated: isRepeated, Name: "int32"}, nil
	case protoreflect.Sint32Kind:
		return BuiltInType{Repeated: isRepeated, Name: "int32"}, nil
	case protoreflect.Uint32Kind:
		return BuiltInType{Repeated: isRepeated, Name: "uint32"}, nil
	case protoreflect.Int64Kind:
		return BuiltInType{Repeated: isRepeated, Name: "int64"}, nil
	case protoreflect.Sint64Kind:
		return BuiltInType{Repeated: isRepeated, Name: "int64"}, nil
	case protoreflect.Uint64Kind:
		return BuiltInType{Repeated: isRepeated, Name: "uint64"}, nil
	case protoreflect.Sfixed32Kind:
		return BuiltInType{Repeated: isRepeated, Name: "int32"}, nil
	case protoreflect.Fixed32Kind:
		return BuiltInType{Repeated: isRepeated, Name: "uint32"}, nil
	case protoreflect.FloatKind:
		return BuiltInType{Repeated: isRepeated, Name: "float32"}, nil
	case protoreflect.Sfixed64Kind:
		return BuiltInType{Repeated: isRepeated, Name: "int64"}, nil
	case protoreflect.Fixed64Kind:
		return BuiltInType{Repeated: isRepeated, Name: "uint64"}, nil
	case protoreflect.DoubleKind:
		return BuiltInType{Repeated: isRepeated, Name: "float64"}, nil
	case protoreflect.StringKind:
		return BuiltInType{Repeated: isRepeated, Name: "string"}, nil
	case protoreflect.BytesKind:
		return BuiltInType{Repeated: isRepeated, Name: "[]byte"}, nil
	case protoreflect.MessageKind:
		messageType := field.Message()
		name := string(messageType.FullName())
		return root.NewMessageFieldType(name, isRepeated), nil
	case protoreflect.GroupKind:
		return nil, errors.New("don't know how to handle groups")
	default:
		return nil, errors.New(fmt.Sprintf("unknown field type: %s", field.Kind().String()))
	}
}
