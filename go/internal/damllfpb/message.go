/*
Internal utilities for parsing the Protobuf files that describe the DAML-LF format.
*/
package damllfpb

import (
	"errors"
	"fmt"
	"strings"
)

//region Object Model

type Root struct {
	prefix string

	// The names of individual Protobuf messages, stored in the order they occur
	// in the spec.
	messageNames []string

	// Messages
	messages map[string]*Message

	enumNames []string

	enums map[string]*Enum
}

// A node in a root. This is the base struct for all nodes.
type node struct {
	root *Root

	// The name of this node, as it is declared in Protobuf. This might not be a legal Go identifier.
	name string
}

type hasFields struct {
	fieldNames []string
	fields     map[string]*MessageField
}

type Message struct {
	node
	hasFields
	builtIn bool
	cases   []*MessageCase
}

// A possible concrete value of a Message.
type MessageCase struct {
	node
	hasFields
}

type MessageField struct {
	node

	// The type of this field.
	Type FieldType

	// The field that holds the value of this message on the wire, or the empty string if this field
	// cannot exist over the wire (most likely because it can only exist in interned form).
	WireField string

	// The field that holds the value of this message when interning is used, or the empty string
	// if this field cannot exist over the wire in interned form (mostly likely because it can only
	// exist non-interned).
	WireInternField string

	OneOf string
}

type Enum struct {
	node
	fieldNames []string
	fields     map[string]int32
}

type EnumValue struct {
	GoName string
	Value  int32
}

//endregion

func NewRoot(prefix string) *Root {
	return &Root{
		prefix:   prefix,
		messages: map[string]*Message{},
		enums:    map[string]*Enum{},
	}
}

func (n *node) Name() string {
	return n.name
}

func (n *node) GoName() string {
	return goName(n.name, true)
}

func (n *node) GoLocalName() string {
	return goName(n.name, false)
}

func (root *Root) Enum(name string) *Enum {
	if strings.HasPrefix(name, root.prefix+".") {
		name = strings.TrimPrefix(name, root.prefix+".")
	}

	enum, ok := root.enums[name]
	if !ok {
		enum = root.newEnum(name)
		root.enums[name] = enum
		root.enumNames = append(root.enumNames, name)
	}
	return enum
}

func (root *Root) Message(name string) *Message {
	if strings.HasPrefix(name, root.prefix+".") {
		name = strings.TrimPrefix(name, root.prefix+".")
	}

	message, ok := root.messages[name]
	if !ok {
		message = root.newMessage(name)
		root.messages[name] = message
		root.messageNames = append(root.messageNames, name)
	}
	return message
}

func (e *Enum) Values() []EnumValue {
	var values []EnumValue
	for _, name := range e.fieldNames {
		value, _ := e.fields[name]
		values = append(values, EnumValue{GoName: goName(name, true), Value: value})

	}
	return values
}

func (e *Enum) Add(name string, value int32) {
	e.fieldNames = append(e.fieldNames, name)
	e.fields[name] = value
}

func (message *Message) BuiltIn() bool {
	return message.builtIn
}

func (root *Root) newMessage(name string) *Message {
	return &Message{
		node:      node{root: root, name: name},
		builtIn:   isBuiltInName(name),
		hasFields: hasFields{fields: map[string]*MessageField{}},
	}
}

func (root *Root) newEnum(name string) *Enum {
	return &Enum{
		node:   node{root: root, name: name},
		fields: map[string]int32{},
	}
}

func isBuiltInName(s string) bool {
	switch s {
	case "Package":
		return true
	case "PackageRef":
		return true
	case "DottedName":
		return true
	case "ModuleRef":
		return true
	case "InternedDottedName":
		return true
	case "Unit":
		return true
	default:
		return false
	}
}

func (root *Root) Enums() []*Enum {
	var enums []*Enum
	for _, name := range root.enumNames {
		enums = append(enums, root.enums[name])
	}
	return enums
}

func (root *Root) Messages() []*Message {
	var messages []*Message
	for _, name := range root.messageNames {
		messages = append(messages, root.messages[name])
	}
	return messages
}

// Add appropriate field information for a field in a message with the appropriate name.
//
// There are some conventions employed in DAML-LF message field names, so exploit them to understand both the type
// and wire format of the specified field.
func (message *Message) ProcessMessageField(messageFieldName string, oneOfContainer string, fieldType FieldType) (*MessageField, error) {
	name := messageFieldName
	isInternField := false

	if strings.HasSuffix(messageFieldName, "_interned_str") {
		name = strings.TrimSuffix(messageFieldName, "_interned_str")
		fieldType = BuiltInType{
			Repeated: fieldType.IsRepeated(),
			Name:     "string",
		}
		isInternField = true
	} else if strings.HasSuffix(messageFieldName, "_str") {
		name = strings.TrimSuffix(messageFieldName, "_str")
		fieldType = BuiltInType{
			Repeated: fieldType.IsRepeated(),
			Name:     "string",
		}
	} else if strings.HasSuffix(messageFieldName, "_interned_dname") {
		name = strings.TrimSuffix(messageFieldName, "_interned_dname")
		fieldType = BuiltInType{
			Repeated: fieldType.IsRepeated(),
			Name:     "DottedName",
		}
		isInternField = true
	} else if strings.HasSuffix(messageFieldName, "_dname") {
		name = strings.TrimSuffix(messageFieldName, "_dname")
		fieldType = BuiltInType{
			Repeated: fieldType.IsRepeated(),
			Name:     "DottedName",
		}
	}

	field := message.Field(name)
	if isInternField {
		field.WireInternField = messageFieldName
	} else {
		field.WireField = messageFieldName
	}
	field.Type = fieldType
	field.OneOf = oneOfContainer
	return field, nil
}

// Indicate that no more fields will be added for this Message, and final cleanup checks should be performed.
// This is where we also determine if this is a product or a sum message.
func (message *Message) Finish() error {
	// If there are any OneOf's that contain just a single element, it's not REALLY a OneOf.
	sumTypes := message.fieldsGroupedByOneOf()
	for _, fields := range sumTypes {
		if len(fields) == 1 {
			fields[0].OneOf = ""
		}
	}

	// Now that we got THAT out of the way, ask again.
	sumTypes = message.fieldsGroupedByOneOf()

	// We can really only deal with zero or one oneof groups. Any more than that is too complicated for us to generate
	// code for.
	allowedGroupCount := 1
	_, hasUnnamedGroup := sumTypes[""]
	if hasUnnamedGroup {
		allowedGroupCount += 1
	}

	if len(sumTypes) > allowedGroupCount {
		return errors.New(fmt.Sprintf("this message has too many oneof groups"))
	}

	commonFields, _ := sumTypes[""]
	delete(sumTypes, "")
	if len(sumTypes) > 0 {
		// this is a sum type; produce cases as appropriate
		for _, sumFields := range sumTypes {
			for _, sumField := range sumFields {
				var fields []*MessageField
				fields = append(fields, commonFields...)
				if sumField.Type.GoName() != "Unit" {
					fields = append(fields, sumField)
				}
				mc := message.root.newMessageCase(message.name+"."+sumField.name, fields)
				message.cases = append(message.cases, mc)
			}
		}
	}

	return nil
}

func (root *Root) newMessageCase(name string, fields []*MessageField) *MessageCase {
	messageCase := MessageCase{
		node:      node{root: root, name: name},
		hasFields: hasFields{fields: map[string]*MessageField{}},
	}
	for _, field := range fields {
		messageCase.fieldNames = append(messageCase.fieldNames, field.name)
		messageCase.fields[field.name] = field
	}

	return &messageCase
}

// Determine if this Message is comprised of more than one possible structure (it is a sum type).
func (message *Message) HasCases() bool {
	return len(message.cases) > 0
}

func (message *Message) Cases() []*MessageCase {
	return message.cases
}

func (message *Message) fieldsGroupedByOneOf() map[string][]*MessageField {
	// Group the fields by their OneOf's.
	sumTypes := map[string][]*MessageField{}
	for _, field := range message.fields {
		fields, _ := sumTypes[field.OneOf]
		sumTypes[field.OneOf] = append(fields, field)
	}

	return sumTypes
}

func (message *hasFields) Fields() []*MessageField {
	var fields []*MessageField
	for _, name := range message.fieldNames {
		fields = append(fields, message.fields[name])
	}
	return fields
}

// Get a MessageField of the specified name. If one does not exist, it will be created.
func (message *Message) Field(name string) *MessageField {
	field, ok := message.fields[name]
	if !ok {
		field = newField(message.root, name)
		message.fields[name] = field
		message.fieldNames = append(message.fieldNames, name)
	}
	return field
}

func newField(root *Root, name string) *MessageField {
	return &MessageField{
		node: node{root: root, name: name},
	}
}

func (field *MessageField) Name() string {
	return field.name
}

func (field *MessageField) GoName() string {
	return goName(field.name, true)
}

func (field *MessageField) GoLocalName() string {
	return goName(field.name, false)
}

type FieldType interface {
	IsRepeated() bool
	GoName() string
	String() string
}

type BuiltInType struct {
	Repeated bool
	Name     string
}

type EnumFieldType struct {
	Repeated bool
	Name     string
	Values   []string
}

type MessageFieldType struct {
	Repeated bool
	Name     string
}

func (root *Root) NewMessageFieldType(name string, repeated bool) MessageFieldType {
	if strings.HasPrefix(name, root.prefix+".") {
		return MessageFieldType{
			Repeated: repeated,
			Name:     strings.TrimPrefix(name, root.prefix+"."),
		}
	} else {
		return MessageFieldType{
			Repeated: repeated,
			Name:     name,
		}
	}
}

func (t BuiltInType) IsRepeated() bool {
	return t.Repeated
}

func (t BuiltInType) String() string {
	if t.Repeated {
		return "[]" + t.Name
	} else {
		return t.Name
	}
}

func (t BuiltInType) GoName() string {
	return t.String()
}

func (t EnumFieldType) IsRepeated() bool {
	return t.Repeated
}

func (t EnumFieldType) String() string {
	if t.Repeated {
		return "[]" + t.Name
	} else {
		return t.Name
	}
}

func (t EnumFieldType) GoName() string {
	return goName(t.String(), true)
}

func (t MessageFieldType) IsRepeated() bool {
	return t.Repeated
}

func (t MessageFieldType) String() string {
	if t.Repeated {
		return "[]" + t.Name
	} else {
		return t.Name
	}
}

func (t MessageFieldType) GoName() string {
	if t.Repeated {
		return "[]" + goName(t.Name, true)
	} else {
		return goName(t.Name, true)
	}
}

// Convert the specified string to a valid Go identifier.
func goName(s string, public bool) string {
	var sb strings.Builder
	for i, c := range strings.Split(s, "_") {
		if i == 0 && !public {
			sb.WriteString(untitle(c))
		} else {
			sb.WriteString(title(c))
		}
	}
	x := sb.String()
	sb.Reset()

	for i, c := range strings.Split(x, ".") {
		if i == 0 && !public {
			sb.WriteString(c)
		} else {
			sb.WriteString(title(c))
		}
	}

	finalName := sb.String()
	switch finalName {
	case "var":
		return "var_"
	case "type":
		return "typ"
	case "struct":
		return "struct_"
	case "range":
		return "rng"
	case "package":
		return "pkg"
	case "case":
		return "case_"
	case "default":
		return "default_"
	default:
		return finalName
	}
}

func untitle(s string) string {
	return strings.ToLower(s[0:1]) + s[1:]
}

func title(s string) string {
	return strings.ToUpper(s[0:1]) + s[1:]
}

// Perform final analysis, cleanup and simplification.
func (root *Root) Finish() error {
	for _, message := range root.messages {
		if err := message.Finish(); err != nil {
			return err
		}
	}

	// Now identify all Messages that occurs as types for at most one MessageCase.
	typesIndexedByUsedCases := map[string][]interface{}{}
	for _, message := range root.messages {
		for _, messageCase := range message.Cases() {
			for _, field := range messageCase.Fields() {
				typesIndexedByUsedCases[field.Type]
				field.Name()
				field.Type
			}
		}
	}


	return nil
}
