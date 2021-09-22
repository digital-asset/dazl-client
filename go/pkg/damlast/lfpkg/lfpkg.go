package damlast

// classification: lfpkg
type PackageRef string

// classification: lfpkg

type DottedName struct {
	segments []string
}
func (p Parser) ReadDottedName(r io.Reader) (v DottedName, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // segments
			var obj string
			obj, err = p.Readstring(r)
			if err == nil {
				v.segments = append(v.segments, obj)			}
		}
	}
}
// classification: lfpkg

type ModuleRef struct {
	packageRef PackageRef
	moduleName DottedName
}
func (p Parser) ReadModuleRef(r io.Reader) (v ModuleRef, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // package_ref
			v.packageRef, err = p.ReadPackageRef(r)
		case 2: // module_name
			v.moduleName, err = p.ReadDottedName(r)
		}
	}
}
// classification: lfpkg

type TypeConName struct {
	module ModuleRef
	name DottedName
}
func (p Parser) ReadTypeConName(r io.Reader) (v TypeConName, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // module
			v.module, err = p.ReadModuleRef(r)
		case 2: // name
			v.name, err = p.ReadDottedName(r)
		}
	}
}
// classification: lfpkg

type TypeSynName struct {
	module ModuleRef
	name DottedName
}
func (p Parser) ReadTypeSynName(r io.Reader) (v TypeSynName, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // module
			v.module, err = p.ReadModuleRef(r)
		case 2: // name
			v.name, err = p.ReadDottedName(r)
		}
	}
}
// classification: lfpkg

type ValName struct {
	module ModuleRef
	name DottedName
}
func (p Parser) ReadValName(r io.Reader) (v ValName, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // module
			v.module, err = p.ReadModuleRef(r)
		case 2: // name
			v.name, err = p.ReadDottedName(r)
		}
	}
}
// classification: lfpkg

type TemplateChoice struct {
	name string
	consuming bool
	controllers Expr
	observers Expr
	argBinder VarWithType
	retType Type
	update Expr
	selfBinder string
	location Location
}
func (p Parser) ReadTemplateChoice(r io.Reader) (v TemplateChoice, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // name
			v.name, err = p.Readstring(r)
		case 2: // consuming
			v.consuming, err = p.Readbool(r)
		case 3: // controllers
			v.controllers, err = p.ReadExpr(r)
		case 11: // observers
			v.observers, err = p.ReadExpr(r)
		case 4: // arg_binder
			v.argBinder, err = p.ReadVarWithType(r)
		case 5: // ret_type
			v.retType, err = p.ReadType(r)
		case 6: // update
			v.update, err = p.ReadExpr(r)
		case 7: // self_binder
			v.selfBinder, err = p.Readstring(r)
		case 8: // location
			v.location, err = p.ReadLocation(r)
		}
	}
}
// classification: lfpkg

type DefTemplate struct {
	tycon DottedName
	param string
	precond Expr
	signatories Expr
	agreement Expr
	choices []TemplateChoice
	observers Expr
	location Location
	key DefTemplate_DefKey
}
func (p Parser) ReadDefTemplate(r io.Reader) (v DefTemplate, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // tycon
			v.tycon, err = p.ReadDottedName(r)
		case 2: // param
			v.param, err = p.Readstring(r)
		case 4: // precond
			v.precond, err = p.ReadExpr(r)
		case 5: // signatories
			v.signatories, err = p.ReadExpr(r)
		case 6: // agreement
			v.agreement, err = p.ReadExpr(r)
		case 7: // choices
			var obj TemplateChoice
			obj, err = p.ReadTemplateChoice(r)
			if err == nil {
				v.choices = append(v.choices, obj)			}
		case 8: // observers
			v.observers, err = p.ReadExpr(r)
		case 9: // location
			v.location, err = p.ReadLocation(r)
		case 10: // key
			v.key, err = p.ReadDefTemplate_DefKey(r)
		}
	}
}
// classification: lfpkg

type DefTemplate_DefKey struct {
	typ Type
	maintainers Expr
	_keyExpr caseDefTemplate_DefKeyKeyExpr
	keyExpr interface{}
}
func (p Parser) ReadDefTemplate_DefKey(r io.Reader) (v DefTemplate_DefKey, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // type
			v.typ, err = p.ReadType(r)
		case 2: // key
			v._keyExpr = "key"
			v.keyExpr, err = p.ReadKeyExpr(r)
		case 4: // complex_key
			v._keyExpr = "complex_key"
			v.keyExpr, err = p.ReadExpr(r)
		case 3: // maintainers
			v.maintainers, err = p.ReadExpr(r)
		}
	}
}
// classification: lfpkg

type DefException struct {
	name DottedName
	location *Location
	message Expr
}
func (p Parser) ReadDefException(r io.Reader) (v DefException, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 2: // location
			v.location, err = p.Read*Location(r)
		case 3: // message
			v.message, err = p.ReadExpr(r)
		}
	}
}
// classification: lfpkg

type DefDataType struct {
	name DottedName
	params []TypeVarWithKind
	serializable bool
	location Location
	_dataCons caseDefDataTypeDataCons
	dataCons interface{}
}
func (p Parser) ReadDefDataType(r io.Reader) (v DefDataType, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // name
			v.name, err = p.ReadDottedName(r)
		case 2: // params
			var obj TypeVarWithKind
			obj, err = p.ReadTypeVarWithKind(r)
			if err == nil {
				v.params = append(v.params, obj)			}
		case 3: // record
			v._dataCons = "record"
			v.dataCons, err = p.ReadDefDataType_Fields(r)
		case 4: // variant
			v._dataCons = "variant"
			v.dataCons, err = p.ReadDefDataType_Fields(r)
		case 7: // enum
			v._dataCons = "enum"
			v.dataCons, err = p.ReadDefDataType_EnumConstructors(r)
		case 5: // serializable
			v.serializable, err = p.Readbool(r)
		case 6: // location
			v.location, err = p.ReadLocation(r)
		}
	}
}
// classification: lfpkg

type DefDataType_Fields struct {
	fields []FieldWithType
}
func (p Parser) ReadDefDataType_Fields(r io.Reader) (v DefDataType_Fields, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // fields
			var obj FieldWithType
			obj, err = p.ReadFieldWithType(r)
			if err == nil {
				v.fields = append(v.fields, obj)			}
		}
	}
}
// classification: lfpkg

type DefDataType_EnumConstructors struct {
	constructors string
}
func (p Parser) ReadDefDataType_EnumConstructors(r io.Reader) (v DefDataType_EnumConstructors, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // constructors
			v.constructors, err = p.Readstring(r)
		}
	}
}
// classification: lfpkg

type DefTypeSyn struct {
	name DottedName
	params []TypeVarWithKind
	typ Type
	location Location
}
func (p Parser) ReadDefTypeSyn(r io.Reader) (v DefTypeSyn, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // name
			v.name, err = p.ReadDottedName(r)
		case 2: // params
			var obj TypeVarWithKind
			obj, err = p.ReadTypeVarWithKind(r)
			if err == nil {
				v.params = append(v.params, obj)			}
		case 3: // type
			v.typ, err = p.ReadType(r)
		case 4: // location
			v.location, err = p.ReadLocation(r)
		}
	}
}
// classification: lfpkg

type DefValue struct {
	nameWithType DefValue_NameWithType
	expr Expr
	noPartyLiterals bool
	isTest bool
	location Location
}
func (p Parser) ReadDefValue(r io.Reader) (v DefValue, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // name_with_type
			v.nameWithType, err = p.ReadDefValue_NameWithType(r)
		case 2: // expr
			v.expr, err = p.ReadExpr(r)
		case 3: // no_party_literals
			v.noPartyLiterals, err = p.Readbool(r)
		case 4: // is_test
			v.isTest, err = p.Readbool(r)
		case 5: // location
			v.location, err = p.ReadLocation(r)
		}
	}
}
// classification: lfpkg

type DefValue_NameWithType struct {
	name DottedName
	typ Type
}
func (p Parser) ReadDefValue_NameWithType(r io.Reader) (v DefValue_NameWithType, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // name
			v.name, err = p.ReadDottedName(r)
		case 2: // type
			v.typ, err = p.ReadType(r)
		}
	}
}
// classification: lfpkg

type FeatureFlags struct {
	forbidPartyLiterals bool
	dontDivulgeContractIdsInCreateArguments bool
	dontDiscloseNonConsumingChoicesToObservers bool
}
func (p Parser) ReadFeatureFlags(r io.Reader) (v FeatureFlags, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // forbidPartyLiterals
			v.forbidPartyLiterals, err = p.Readbool(r)
		case 2: // dontDivulgeContractIdsInCreateArguments
			v.dontDivulgeContractIdsInCreateArguments, err = p.Readbool(r)
		case 3: // dontDiscloseNonConsumingChoicesToObservers
			v.dontDiscloseNonConsumingChoicesToObservers, err = p.Readbool(r)
		}
	}
}
// classification: lfpkg

type Module struct {
	name DottedName
	flags FeatureFlags
	synonyms []DefTypeSyn
	dataTypes []DefDataType
	values []DefValue
	templates []DefTemplate
	exceptions []DefException
}
func (p Parser) ReadModule(r io.Reader) (v Module, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // name
			v.name, err = p.ReadDottedName(r)
		case 4: // flags
			v.flags, err = p.ReadFeatureFlags(r)
		case 9: // synonyms
			var obj DefTypeSyn
			obj, err = p.ReadDefTypeSyn(r)
			if err == nil {
				v.synonyms = append(v.synonyms, obj)			}
		case 5: // data_types
			var obj DefDataType
			obj, err = p.ReadDefDataType(r)
			if err == nil {
				v.dataTypes = append(v.dataTypes, obj)			}
		case 6: // values
			var obj DefValue
			obj, err = p.ReadDefValue(r)
			if err == nil {
				v.values = append(v.values, obj)			}
		case 7: // templates
			var obj DefTemplate
			obj, err = p.ReadDefTemplate(r)
			if err == nil {
				v.templates = append(v.templates, obj)			}
		case 10: // exceptions
			var obj DefException
			obj, err = p.ReadDefException(r)
			if err == nil {
				v.exceptions = append(v.exceptions, obj)			}
		}
	}
}
// classification: lfpkg

type PackageMetadata struct {
	name string
	version string
}
func (p Parser) ReadPackageMetadata(r io.Reader) (v PackageMetadata, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		}
	}
}
// classification: lfpkg

type Package struct {
	modules []Module
	metadata PackageMetadata
}
func (p Parser) ReadPackage(r io.Reader) (v Package, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // modules
			var obj Module
			obj, err = p.ReadModule(r)
			if err == nil {
				v.modules = append(v.modules, obj)			}
		case 4: // metadata
			v.metadata, err = p.ReadPackageMetadata(r)
		}
	}
}
