package damlast

type PrimType int32

const (
	UNIT PrimType = 0

	BOOL PrimType = 1

	INT64 PrimType = 2

	DECIMAL PrimType = 3

	TEXT PrimType = 5

	TIMESTAMP PrimType = 6

	PARTY PrimType = 8

	LIST PrimType = 9

	UPDATE PrimType = 10

	SCENARIO PrimType = 11

	DATE PrimType = 12

	CONTRACTID PrimType = 13

	OPTIONAL PrimType = 14

	ARROW PrimType = 15

	TEXTMAP PrimType = 16

	NUMERIC PrimType = 17

	ANY PrimType = 18

	TYPEREP PrimType = 19

	GENMAP PrimType = 20
)

type PrimCon int32

const (
	CONUNIT PrimCon = 0

	CONFALSE PrimCon = 1

	CONTRUE PrimCon = 2
)

type BuiltinFunction int32

const (
	ADDDECIMAL BuiltinFunction = 0

	SUBDECIMAL BuiltinFunction = 1

	MULDECIMAL BuiltinFunction = 2

	DIVDECIMAL BuiltinFunction = 3

	ROUNDDECIMAL BuiltinFunction = 6

	ADDNUMERIC BuiltinFunction = 107

	SUBNUMERIC BuiltinFunction = 108

	MULNUMERIC BuiltinFunction = 109

	DIVNUMERIC BuiltinFunction = 110

	ROUNDNUMERIC BuiltinFunction = 111

	CASTNUMERIC BuiltinFunction = 121

	SHIFTNUMERIC BuiltinFunction = 122

	ADDINT64 BuiltinFunction = 7

	SUBINT64 BuiltinFunction = 8

	MULINT64 BuiltinFunction = 9

	DIVINT64 BuiltinFunction = 10

	MODINT64 BuiltinFunction = 11

	EXPINT64 BuiltinFunction = 12

	FOLDL BuiltinFunction = 20

	FOLDR BuiltinFunction = 21

	TEXTMAPEMPTY BuiltinFunction = 96

	TEXTMAPINSERT BuiltinFunction = 97

	TEXTMAPLOOKUP BuiltinFunction = 98

	TEXTMAPDELETE BuiltinFunction = 99

	TEXTMAPTOLIST BuiltinFunction = 100

	TEXTMAPSIZE BuiltinFunction = 101

	GENMAPEMPTY BuiltinFunction = 124

	GENMAPINSERT BuiltinFunction = 125

	GENMAPLOOKUP BuiltinFunction = 126

	GENMAPDELETE BuiltinFunction = 127

	GENMAPKEYS BuiltinFunction = 128

	GENMAPVALUES BuiltinFunction = 129

	GENMAPSIZE BuiltinFunction = 130

	EXPLODETEXT BuiltinFunction = 23

	APPENDTEXT BuiltinFunction = 24

	ERROR BuiltinFunction = 25

	LEQINT64 BuiltinFunction = 33

	LEQDECIMAL BuiltinFunction = 34

	LEQNUMERIC BuiltinFunction = 112

	LEQTEXT BuiltinFunction = 36

	LEQTIMESTAMP BuiltinFunction = 37

	LEQDATE BuiltinFunction = 67

	LEQPARTY BuiltinFunction = 89

	LESSINT64 BuiltinFunction = 39

	LESSDECIMAL BuiltinFunction = 40

	LESSNUMERIC BuiltinFunction = 113

	LESSTEXT BuiltinFunction = 42

	LESSTIMESTAMP BuiltinFunction = 43

	LESSDATE BuiltinFunction = 68

	LESSPARTY BuiltinFunction = 90

	GEQINT64 BuiltinFunction = 45

	GEQDECIMAL BuiltinFunction = 46

	GEQNUMERIC BuiltinFunction = 114

	GEQTEXT BuiltinFunction = 48

	GEQTIMESTAMP BuiltinFunction = 49

	GEQDATE BuiltinFunction = 69

	GEQPARTY BuiltinFunction = 91

	GREATERINT64 BuiltinFunction = 51

	GREATERDECIMAL BuiltinFunction = 52

	GREATERNUMERIC BuiltinFunction = 115

	GREATERTEXT BuiltinFunction = 54

	GREATERTIMESTAMP BuiltinFunction = 55

	GREATERDATE BuiltinFunction = 70

	GREATERPARTY BuiltinFunction = 92

	TOTEXTINT64 BuiltinFunction = 57

	TOTEXTDECIMAL BuiltinFunction = 58

	TOTEXTNUMERIC BuiltinFunction = 116

	TOTEXTTEXT BuiltinFunction = 60

	TOTEXTTIMESTAMP BuiltinFunction = 61

	TOTEXTDATE BuiltinFunction = 71

	TOQUOTEDTEXTPARTY BuiltinFunction = 63

	TOTEXTPARTY BuiltinFunction = 94

	FROMTEXTPARTY BuiltinFunction = 95

	FROMTEXTINT64 BuiltinFunction = 103

	FROMTEXTDECIMAL BuiltinFunction = 104

	FROMTEXTNUMERIC BuiltinFunction = 117

	SHA256TEXT BuiltinFunction = 93

	DATETOUNIXDAYS BuiltinFunction = 72

	UNIXDAYSTODATE BuiltinFunction = 73

	TIMESTAMPTOUNIXMICROSECONDS BuiltinFunction = 74

	UNIXMICROSECONDSTOTIMESTAMP BuiltinFunction = 75

	INT64TODECIMAL BuiltinFunction = 76

	DECIMALTOINT64 BuiltinFunction = 77

	INT64TONUMERIC BuiltinFunction = 118

	NUMERICTOINT64 BuiltinFunction = 119

	IMPLODETEXT BuiltinFunction = 78

	EQUALINT64 BuiltinFunction = 79

	EQUALDECIMAL BuiltinFunction = 80

	EQUALNUMERIC BuiltinFunction = 120

	EQUALTEXT BuiltinFunction = 81

	EQUALTIMESTAMP BuiltinFunction = 82

	EQUALDATE BuiltinFunction = 83

	EQUALPARTY BuiltinFunction = 84

	EQUALBOOL BuiltinFunction = 85

	EQUALCONTRACTID BuiltinFunction = 86

	EQUALLIST BuiltinFunction = 87

	EQUALTYPEREP BuiltinFunction = 123

	EQUAL BuiltinFunction = 131

	LESSEQ BuiltinFunction = 132

	LESS BuiltinFunction = 133

	GREATEREQ BuiltinFunction = 134

	GREATER BuiltinFunction = 135

	TRACE BuiltinFunction = 88

	COERCECONTRACTID BuiltinFunction = 102

	TEXTFROMCODEPOINTS BuiltinFunction = 105

	TEXTTOCODEPOINTS BuiltinFunction = 106

	TEXTTOUPPER BuiltinFunction = 9901

	TEXTTOLOWER BuiltinFunction = 9902

	TEXTSLICE BuiltinFunction = 9903

	TEXTSLICEINDEX BuiltinFunction = 9904

	TEXTCONTAINSONLY BuiltinFunction = 9905

	TEXTREPLICATE BuiltinFunction = 9906

	TEXTSPLITON BuiltinFunction = 9907

	TEXTINTERCALATE BuiltinFunction = 9908
)

type TypeConName interface {
	Module() ModuleRef
	Name() DottedName
}

// Fields for message TypeConName
type typeConName struct {
	module ModuleRef
	name   DottedName
}

func (obj typeConName) Module() ModuleRef {
	return obj.module
}

func (obj typeConName) Name() DottedName {
	return obj.name
}

func NewTypeConName(module ModuleRef, name DottedName) (TypeConName, error) {
	return typeConName{
		module: module,
		name:   name,
	}, nil
}

type TypeSynName interface {
	Module() ModuleRef
	Name() DottedName
}

// Fields for message TypeSynName
type typeSynName struct {
	module ModuleRef
	name   DottedName
}

func (obj typeSynName) Module() ModuleRef {
	return obj.module
}

func (obj typeSynName) Name() DottedName {
	return obj.name
}

func NewTypeSynName(module ModuleRef, name DottedName) (TypeSynName, error) {
	return typeSynName{
		module: module,
		name:   name,
	}, nil
}

type ValName interface {
	Module() ModuleRef
	Name() DottedName
}

// Fields for message ValName
type valName struct {
	module ModuleRef
	name   DottedName
}

func (obj valName) Module() ModuleRef {
	return obj.module
}

func (obj valName) Name() DottedName {
	return obj.name
}

func NewValName(module ModuleRef, name DottedName) (ValName, error) {
	return valName{
		module: module,
		name:   name,
	}, nil
}

type FieldWithType interface {
	Field() string
	Type() Type
}

// Fields for message FieldWithType
type fieldWithType struct {
	field string
	typ   Type
}

func (obj fieldWithType) Field() string {
	return obj.field
}

func (obj fieldWithType) Type() Type {
	return obj.typ
}

func NewFieldWithType(field string, typ Type) (FieldWithType, error) {
	return fieldWithType{
		field: field,
		typ:   typ,
	}, nil
}

type VarWithType interface {
	Var() string
	Type() Type
}

// Fields for message VarWithType
type varWithType struct {
	var_ string
	typ  Type
}

func (obj varWithType) Var() string {
	return obj.var_
}

func (obj varWithType) Type() Type {
	return obj.typ
}

func NewVarWithType(var_ string, typ Type) (VarWithType, error) {
	return varWithType{
		var_: var_,
		typ:  typ,
	}, nil
}

type TypeVarWithKind interface {
	Var() string
	Kind() Kind
}

// Fields for message TypeVarWithKind
type typeVarWithKind struct {
	var_ string
	kind Kind
}

func (obj typeVarWithKind) Var() string {
	return obj.var_
}

func (obj typeVarWithKind) Kind() Kind {
	return obj.kind
}

func NewTypeVarWithKind(var_ string, kind Kind) (TypeVarWithKind, error) {
	return typeVarWithKind{
		var_: var_,
		kind: kind,
	}, nil
}

type FieldWithExpr interface {
	Field() string
	Expr() Expr
}

// Fields for message FieldWithExpr
type fieldWithExpr struct {
	field string
	expr  Expr
}

func (obj fieldWithExpr) Field() string {
	return obj.field
}

func (obj fieldWithExpr) Expr() Expr {
	return obj.expr
}

func NewFieldWithExpr(field string, expr Expr) (FieldWithExpr, error) {
	return fieldWithExpr{
		field: field,
		expr:  expr,
	}, nil
}

type Binding interface {
	Binder() VarWithType
	Bound() Expr
}

// Fields for message Binding
type binding struct {
	binder VarWithType
	bound  Expr
}

func (obj binding) Binder() VarWithType {
	return obj.binder
}

func (obj binding) Bound() Expr {
	return obj.bound
}

func NewBinding(binder VarWithType, bound Expr) (Binding, error) {
	return binding{
		binder: binder,
		bound:  bound,
	}, nil
}

type Kind interface {
	Star() Unit
	Arrow() KindArrow
	Nat() Unit
}

// Fields for message Kind
type kind struct {
	star  Unit
	arrow KindArrow
	nat   Unit
}

func (obj kind) Star() Unit {
	return obj.star
}

func (obj kind) Arrow() KindArrow {
	return obj.arrow
}

func (obj kind) Nat() Unit {
	return obj.nat
}

func NewKind(star Unit, arrow KindArrow, nat Unit) (Kind, error) {
	return kind{
		star:  star,
		arrow: arrow,
		nat:   nat,
	}, nil
}

type KindArrow interface {
	Params() []Kind
	Result() Kind
}

// Fields for message Kind.Arrow
type kindArrow struct {
	params []Kind
	result Kind
}

func (obj kindArrow) Params() []Kind {
	return obj.params
}

func (obj kindArrow) Result() Kind {
	return obj.result
}

func NewKindArrow(params []Kind, result Kind) (KindArrow, error) {
	return kindArrow{
		params: params,
		result: result,
	}, nil
}

type Type interface {
	Var() TypeVar
	Con() TypeCon
	Prim() TypePrim
	Fun() TypeFun
	Forall() TypeForall
	Struct() TypeStruct
	Nat() int64
	Syn() TypeSyn
}

// Fields for message Type
type typ struct {
	var_    TypeVar
	con     TypeCon
	prim    TypePrim
	fun     TypeFun
	forall  TypeForall
	struct_ TypeStruct
	nat     int64
	syn     TypeSyn
}

func (obj typ) Var() TypeVar {
	return obj.var_
}

func (obj typ) Con() TypeCon {
	return obj.con
}

func (obj typ) Prim() TypePrim {
	return obj.prim
}

func (obj typ) Fun() TypeFun {
	return obj.fun
}

func (obj typ) Forall() TypeForall {
	return obj.forall
}

func (obj typ) Struct() TypeStruct {
	return obj.struct_
}

func (obj typ) Nat() int64 {
	return obj.nat
}

func (obj typ) Syn() TypeSyn {
	return obj.syn
}

func NewType(var_ TypeVar, con TypeCon, prim TypePrim, fun TypeFun, forall TypeForall, struct_ TypeStruct, nat int64, syn TypeSyn) (Type, error) {
	return typ{
		var_:    var_,
		con:     con,
		prim:    prim,
		fun:     fun,
		forall:  forall,
		struct_: struct_,
		nat:     nat,
		syn:     syn,
	}, nil
}

type TypeVar interface {
	Var() string
	Args() []Type
}

// Fields for message Type.Var
type typeVar struct {
	var_ string
	args []Type
}

func (obj typeVar) Var() string {
	return obj.var_
}

func (obj typeVar) Args() []Type {
	return obj.args
}

func NewTypeVar(var_ string, args []Type) (TypeVar, error) {
	return typeVar{
		var_: var_,
		args: args,
	}, nil
}

type TypeCon interface {
	Tycon() TypeConName
	Args() []Type
}

// Fields for message Type.Con
type typeCon struct {
	tycon TypeConName
	args  []Type
}

func (obj typeCon) Tycon() TypeConName {
	return obj.tycon
}

func (obj typeCon) Args() []Type {
	return obj.args
}

func NewTypeCon(tycon TypeConName, args []Type) (TypeCon, error) {
	return typeCon{
		tycon: tycon,
		args:  args,
	}, nil
}

type TypeSyn interface {
	Tysyn() TypeSynName
	Args() []Type
}

// Fields for message Type.Syn
type typeSyn struct {
	tysyn TypeSynName
	args  []Type
}

func (obj typeSyn) Tysyn() TypeSynName {
	return obj.tysyn
}

func (obj typeSyn) Args() []Type {
	return obj.args
}

func NewTypeSyn(tysyn TypeSynName, args []Type) (TypeSyn, error) {
	return typeSyn{
		tysyn: tysyn,
		args:  args,
	}, nil
}

type TypePrim interface {
	Prim() PrimType
	Args() []Type
}

// Fields for message Type.Prim
type typePrim struct {
	prim PrimType
	args []Type
}

func (obj typePrim) Prim() PrimType {
	return obj.prim
}

func (obj typePrim) Args() []Type {
	return obj.args
}

func NewTypePrim(prim PrimType, args []Type) (TypePrim, error) {
	return typePrim{
		prim: prim,
		args: args,
	}, nil
}

type TypeFun interface {
	Params() []Type
	Result() Type
}

// Fields for message Type.Fun
type typeFun struct {
	params []Type
	result Type
}

func (obj typeFun) Params() []Type {
	return obj.params
}

func (obj typeFun) Result() Type {
	return obj.result
}

func NewTypeFun(params []Type, result Type) (TypeFun, error) {
	return typeFun{
		params: params,
		result: result,
	}, nil
}

type TypeForall interface {
	Vars() []TypeVarWithKind
	Body() Type
}

// Fields for message Type.Forall
type typeForall struct {
	vars []TypeVarWithKind
	body Type
}

func (obj typeForall) Vars() []TypeVarWithKind {
	return obj.vars
}

func (obj typeForall) Body() Type {
	return obj.body
}

func NewTypeForall(vars []TypeVarWithKind, body Type) (TypeForall, error) {
	return typeForall{
		vars: vars,
		body: body,
	}, nil
}

type TypeStruct interface {
	Fields() []FieldWithType
}

// Fields for message Type.Struct
type typeStruct struct {
	fields []FieldWithType
}

func (obj typeStruct) Fields() []FieldWithType {
	return obj.fields
}

func NewTypeStruct(fields []FieldWithType) (TypeStruct, error) {
	return typeStruct{
		fields: fields,
	}, nil
}

type PrimLit interface {
	Int64() int64
	Decimal() string
	Numeric() string
	Text() string
	Timestamp() int64
	Party() string
	Date() int32
}

// Fields for message PrimLit
type primLit struct {
	int64     int64
	decimal   string
	numeric   string
	text      string
	timestamp int64
	party     string
	date      int32
}

func (obj primLit) Int64() int64 {
	return obj.int64
}

func (obj primLit) Decimal() string {
	return obj.decimal
}

func (obj primLit) Numeric() string {
	return obj.numeric
}

func (obj primLit) Text() string {
	return obj.text
}

func (obj primLit) Timestamp() int64 {
	return obj.timestamp
}

func (obj primLit) Party() string {
	return obj.party
}

func (obj primLit) Date() int32 {
	return obj.date
}

func NewPrimLit(int64 int64, decimal string, numeric string, text string, timestamp int64, party string, date int32) (PrimLit, error) {
	return primLit{
		int64:     int64,
		decimal:   decimal,
		numeric:   numeric,
		text:      text,
		timestamp: timestamp,
		party:     party,
		date:      date,
	}, nil
}

type Location interface {
	Module() ModuleRef
	Range() LocationRange
}

// Fields for message Location
type location struct {
	module ModuleRef
	rng    LocationRange
}

func (obj location) Module() ModuleRef {
	return obj.module
}

func (obj location) Range() LocationRange {
	return obj.rng
}

func NewLocation(module ModuleRef, rng LocationRange) (Location, error) {
	return location{
		module: module,
		rng:    rng,
	}, nil
}

type LocationRange interface {
	StartLine() int32
	StartCol() int32
	EndLine() int32
	EndCol() int32
}

// Fields for message Location.Range
type locationRange struct {
	startLine int32
	startCol  int32
	endLine   int32
	endCol    int32
}

func (obj locationRange) StartLine() int32 {
	return obj.startLine
}

func (obj locationRange) StartCol() int32 {
	return obj.startCol
}

func (obj locationRange) EndLine() int32 {
	return obj.endLine
}

func (obj locationRange) EndCol() int32 {
	return obj.endCol
}

func NewLocationRange(startLine int32, startCol int32, endLine int32, endCol int32) (LocationRange, error) {
	return locationRange{
		startLine: startLine,
		startCol:  startCol,
		endLine:   endLine,
		endCol:    endCol,
	}, nil
}

type Expr interface {
	Location() Location
	Var() string
	Val() ValName
	Builtin() BuiltinFunction
	PrimCon() PrimCon
	PrimLit() PrimLit
	RecCon() ExprRecCon
	RecProj() ExprRecProj
	RecUpd() ExprRecUpd
	VariantCon() ExprVariantCon
	EnumCon() ExprEnumCon
	StructCon() ExprStructCon
	StructProj() ExprStructProj
	StructUpd() ExprStructUpd
	App() ExprApp
	TyApp() ExprTyApp
	Abs() ExprAbs
	TyAbs() ExprTyAbs
	Case() Case
	Let() Block
	Nil() ExprNil
	Cons() ExprCons
	Update() Update
	Scenario() Scenario
	OptionalNone() ExprOptionalNone
	OptionalSome() ExprOptionalSome
	ToAny() ExprToAny
	FromAny() ExprFromAny
	TypeRep() Type
}

// Fields for message Expr
type expr struct {
	location     Location
	var_         string
	val          ValName
	builtin      BuiltinFunction
	primCon      PrimCon
	primLit      PrimLit
	recCon       ExprRecCon
	recProj      ExprRecProj
	recUpd       ExprRecUpd
	variantCon   ExprVariantCon
	enumCon      ExprEnumCon
	structCon    ExprStructCon
	structProj   ExprStructProj
	structUpd    ExprStructUpd
	app          ExprApp
	tyApp        ExprTyApp
	abs          ExprAbs
	tyAbs        ExprTyAbs
	case_        Case
	let          Block
	nil          ExprNil
	cons         ExprCons
	update       Update
	scenario     Scenario
	optionalNone ExprOptionalNone
	optionalSome ExprOptionalSome
	toAny        ExprToAny
	fromAny      ExprFromAny
	typeRep      Type
}

func (obj expr) Location() Location {
	return obj.location
}

func (obj expr) Var() string {
	return obj.var_
}

func (obj expr) Val() ValName {
	return obj.val
}

func (obj expr) Builtin() BuiltinFunction {
	return obj.builtin
}

func (obj expr) PrimCon() PrimCon {
	return obj.primCon
}

func (obj expr) PrimLit() PrimLit {
	return obj.primLit
}

func (obj expr) RecCon() ExprRecCon {
	return obj.recCon
}

func (obj expr) RecProj() ExprRecProj {
	return obj.recProj
}

func (obj expr) RecUpd() ExprRecUpd {
	return obj.recUpd
}

func (obj expr) VariantCon() ExprVariantCon {
	return obj.variantCon
}

func (obj expr) EnumCon() ExprEnumCon {
	return obj.enumCon
}

func (obj expr) StructCon() ExprStructCon {
	return obj.structCon
}

func (obj expr) StructProj() ExprStructProj {
	return obj.structProj
}

func (obj expr) StructUpd() ExprStructUpd {
	return obj.structUpd
}

func (obj expr) App() ExprApp {
	return obj.app
}

func (obj expr) TyApp() ExprTyApp {
	return obj.tyApp
}

func (obj expr) Abs() ExprAbs {
	return obj.abs
}

func (obj expr) TyAbs() ExprTyAbs {
	return obj.tyAbs
}

func (obj expr) Case() Case {
	return obj.case_
}

func (obj expr) Let() Block {
	return obj.let
}

func (obj expr) Nil() ExprNil {
	return obj.nil
}

func (obj expr) Cons() ExprCons {
	return obj.cons
}

func (obj expr) Update() Update {
	return obj.update
}

func (obj expr) Scenario() Scenario {
	return obj.scenario
}

func (obj expr) OptionalNone() ExprOptionalNone {
	return obj.optionalNone
}

func (obj expr) OptionalSome() ExprOptionalSome {
	return obj.optionalSome
}

func (obj expr) ToAny() ExprToAny {
	return obj.toAny
}

func (obj expr) FromAny() ExprFromAny {
	return obj.fromAny
}

func (obj expr) TypeRep() Type {
	return obj.typeRep
}

func NewExpr(location Location, var_ string, val ValName, builtin BuiltinFunction, primCon PrimCon, primLit PrimLit, recCon ExprRecCon, recProj ExprRecProj, recUpd ExprRecUpd, variantCon ExprVariantCon, enumCon ExprEnumCon, structCon ExprStructCon, structProj ExprStructProj, structUpd ExprStructUpd, app ExprApp, tyApp ExprTyApp, abs ExprAbs, tyAbs ExprTyAbs, case_ Case, let Block, nil ExprNil, cons ExprCons, update Update, scenario Scenario, optionalNone ExprOptionalNone, optionalSome ExprOptionalSome, toAny ExprToAny, fromAny ExprFromAny, typeRep Type) (Expr, error) {
	return expr{
		location:     location,
		var_:         var_,
		val:          val,
		builtin:      builtin,
		primCon:      primCon,
		primLit:      primLit,
		recCon:       recCon,
		recProj:      recProj,
		recUpd:       recUpd,
		variantCon:   variantCon,
		enumCon:      enumCon,
		structCon:    structCon,
		structProj:   structProj,
		structUpd:    structUpd,
		app:          app,
		tyApp:        tyApp,
		abs:          abs,
		tyAbs:        tyAbs,
		case_:        case_,
		let:          let,
		nil:          nil,
		cons:         cons,
		update:       update,
		scenario:     scenario,
		optionalNone: optionalNone,
		optionalSome: optionalSome,
		toAny:        toAny,
		fromAny:      fromAny,
		typeRep:      typeRep,
	}, nil
}

type ExprRecCon interface {
	Tycon() TypeCon
	Fields() []FieldWithExpr
}

// Fields for message Expr.RecCon
type exprRecCon struct {
	tycon  TypeCon
	fields []FieldWithExpr
}

func (obj exprRecCon) Tycon() TypeCon {
	return obj.tycon
}

func (obj exprRecCon) Fields() []FieldWithExpr {
	return obj.fields
}

func NewExprRecCon(tycon TypeCon, fields []FieldWithExpr) (ExprRecCon, error) {
	return exprRecCon{
		tycon:  tycon,
		fields: fields,
	}, nil
}

type ExprRecProj interface {
	Tycon() TypeCon
	Field() string
	Record() Expr
}

// Fields for message Expr.RecProj
type exprRecProj struct {
	tycon  TypeCon
	field  string
	record Expr
}

func (obj exprRecProj) Tycon() TypeCon {
	return obj.tycon
}

func (obj exprRecProj) Field() string {
	return obj.field
}

func (obj exprRecProj) Record() Expr {
	return obj.record
}

func NewExprRecProj(tycon TypeCon, field string, record Expr) (ExprRecProj, error) {
	return exprRecProj{
		tycon:  tycon,
		field:  field,
		record: record,
	}, nil
}

type ExprRecUpd interface {
	Tycon() TypeCon
	Field() string
	Record() Expr
	Update() Expr
}

// Fields for message Expr.RecUpd
type exprRecUpd struct {
	tycon  TypeCon
	field  string
	record Expr
	update Expr
}

func (obj exprRecUpd) Tycon() TypeCon {
	return obj.tycon
}

func (obj exprRecUpd) Field() string {
	return obj.field
}

func (obj exprRecUpd) Record() Expr {
	return obj.record
}

func (obj exprRecUpd) Update() Expr {
	return obj.update
}

func NewExprRecUpd(tycon TypeCon, field string, record Expr, update Expr) (ExprRecUpd, error) {
	return exprRecUpd{
		tycon:  tycon,
		field:  field,
		record: record,
		update: update,
	}, nil
}

type ExprVariantCon interface {
	Tycon() TypeCon
	VariantCon() string
	VariantArg() Expr
}

// Fields for message Expr.VariantCon
type exprVariantCon struct {
	tycon      TypeCon
	variantCon string
	variantArg Expr
}

func (obj exprVariantCon) Tycon() TypeCon {
	return obj.tycon
}

func (obj exprVariantCon) VariantCon() string {
	return obj.variantCon
}

func (obj exprVariantCon) VariantArg() Expr {
	return obj.variantArg
}

func NewExprVariantCon(tycon TypeCon, variantCon string, variantArg Expr) (ExprVariantCon, error) {
	return exprVariantCon{
		tycon:      tycon,
		variantCon: variantCon,
		variantArg: variantArg,
	}, nil
}

type ExprEnumCon interface {
	Tycon() TypeConName
	EnumCon() string
}

// Fields for message Expr.EnumCon
type exprEnumCon struct {
	tycon   TypeConName
	enumCon string
}

func (obj exprEnumCon) Tycon() TypeConName {
	return obj.tycon
}

func (obj exprEnumCon) EnumCon() string {
	return obj.enumCon
}

func NewExprEnumCon(tycon TypeConName, enumCon string) (ExprEnumCon, error) {
	return exprEnumCon{
		tycon:   tycon,
		enumCon: enumCon,
	}, nil
}

type ExprStructCon interface {
	Fields() []FieldWithExpr
}

// Fields for message Expr.StructCon
type exprStructCon struct {
	fields []FieldWithExpr
}

func (obj exprStructCon) Fields() []FieldWithExpr {
	return obj.fields
}

func NewExprStructCon(fields []FieldWithExpr) (ExprStructCon, error) {
	return exprStructCon{
		fields: fields,
	}, nil
}

type ExprStructProj interface {
	Field() string
	Struct() Expr
}

// Fields for message Expr.StructProj
type exprStructProj struct {
	field   string
	struct_ Expr
}

func (obj exprStructProj) Field() string {
	return obj.field
}

func (obj exprStructProj) Struct() Expr {
	return obj.struct_
}

func NewExprStructProj(field string, struct_ Expr) (ExprStructProj, error) {
	return exprStructProj{
		field:   field,
		struct_: struct_,
	}, nil
}

type ExprStructUpd interface {
	Field() string
	Struct() Expr
	Update() Expr
}

// Fields for message Expr.StructUpd
type exprStructUpd struct {
	field   string
	struct_ Expr
	update  Expr
}

func (obj exprStructUpd) Field() string {
	return obj.field
}

func (obj exprStructUpd) Struct() Expr {
	return obj.struct_
}

func (obj exprStructUpd) Update() Expr {
	return obj.update
}

func NewExprStructUpd(field string, struct_ Expr, update Expr) (ExprStructUpd, error) {
	return exprStructUpd{
		field:   field,
		struct_: struct_,
		update:  update,
	}, nil
}

type ExprApp interface {
	Fun() Expr
	Args() []Expr
}

// Fields for message Expr.App
type exprApp struct {
	fun  Expr
	args []Expr
}

func (obj exprApp) Fun() Expr {
	return obj.fun
}

func (obj exprApp) Args() []Expr {
	return obj.args
}

func NewExprApp(fun Expr, args []Expr) (ExprApp, error) {
	return exprApp{
		fun:  fun,
		args: args,
	}, nil
}

type ExprTyApp interface {
	Expr() Expr
	Types() []Type
}

// Fields for message Expr.TyApp
type exprTyApp struct {
	expr  Expr
	types []Type
}

func (obj exprTyApp) Expr() Expr {
	return obj.expr
}

func (obj exprTyApp) Types() []Type {
	return obj.types
}

func NewExprTyApp(expr Expr, types []Type) (ExprTyApp, error) {
	return exprTyApp{
		expr:  expr,
		types: types,
	}, nil
}

type ExprAbs interface {
	Param() []VarWithType
	Body() Expr
}

// Fields for message Expr.Abs
type exprAbs struct {
	param []VarWithType
	body  Expr
}

func (obj exprAbs) Param() []VarWithType {
	return obj.param
}

func (obj exprAbs) Body() Expr {
	return obj.body
}

func NewExprAbs(param []VarWithType, body Expr) (ExprAbs, error) {
	return exprAbs{
		param: param,
		body:  body,
	}, nil
}

type ExprTyAbs interface {
	Param() []TypeVarWithKind
	Body() Expr
}

// Fields for message Expr.TyAbs
type exprTyAbs struct {
	param []TypeVarWithKind
	body  Expr
}

func (obj exprTyAbs) Param() []TypeVarWithKind {
	return obj.param
}

func (obj exprTyAbs) Body() Expr {
	return obj.body
}

func NewExprTyAbs(param []TypeVarWithKind, body Expr) (ExprTyAbs, error) {
	return exprTyAbs{
		param: param,
		body:  body,
	}, nil
}

type ExprNil interface {
	Type() Type
}

// Fields for message Expr.Nil
type exprNil struct {
	typ Type
}

func (obj exprNil) Type() Type {
	return obj.typ
}

func NewExprNil(typ Type) (ExprNil, error) {
	return exprNil{
		typ: typ,
	}, nil
}

type ExprCons interface {
	Type() Type
	Front() []Expr
	Tail() Expr
}

// Fields for message Expr.Cons
type exprCons struct {
	typ   Type
	front []Expr
	tail  Expr
}

func (obj exprCons) Type() Type {
	return obj.typ
}

func (obj exprCons) Front() []Expr {
	return obj.front
}

func (obj exprCons) Tail() Expr {
	return obj.tail
}

func NewExprCons(typ Type, front []Expr, tail Expr) (ExprCons, error) {
	return exprCons{
		typ:   typ,
		front: front,
		tail:  tail,
	}, nil
}

type ExprOptionalNone interface {
	Type() Type
}

// Fields for message Expr.OptionalNone
type exprOptionalNone struct {
	typ Type
}

func (obj exprOptionalNone) Type() Type {
	return obj.typ
}

func NewExprOptionalNone(typ Type) (ExprOptionalNone, error) {
	return exprOptionalNone{
		typ: typ,
	}, nil
}

type ExprOptionalSome interface {
	Type() Type
	Body() Expr
}

// Fields for message Expr.OptionalSome
type exprOptionalSome struct {
	typ  Type
	body Expr
}

func (obj exprOptionalSome) Type() Type {
	return obj.typ
}

func (obj exprOptionalSome) Body() Expr {
	return obj.body
}

func NewExprOptionalSome(typ Type, body Expr) (ExprOptionalSome, error) {
	return exprOptionalSome{
		typ:  typ,
		body: body,
	}, nil
}

type ExprToAny interface {
	Type() Type
	Expr() Expr
}

// Fields for message Expr.ToAny
type exprToAny struct {
	typ  Type
	expr Expr
}

func (obj exprToAny) Type() Type {
	return obj.typ
}

func (obj exprToAny) Expr() Expr {
	return obj.expr
}

func NewExprToAny(typ Type, expr Expr) (ExprToAny, error) {
	return exprToAny{
		typ:  typ,
		expr: expr,
	}, nil
}

type ExprFromAny interface {
	Type() Type
	Expr() Expr
}

// Fields for message Expr.FromAny
type exprFromAny struct {
	typ  Type
	expr Expr
}

func (obj exprFromAny) Type() Type {
	return obj.typ
}

func (obj exprFromAny) Expr() Expr {
	return obj.expr
}

func NewExprFromAny(typ Type, expr Expr) (ExprFromAny, error) {
	return exprFromAny{
		typ:  typ,
		expr: expr,
	}, nil
}

type CaseAlt interface {
	Default() Unit
	Variant() CaseAltVariant
	PrimCon() PrimCon
	Nil() Unit
	Cons() CaseAltCons
	OptionalNone() Unit
	OptionalSome() CaseAltOptionalSome
	Enum() CaseAltEnum
	Body() Expr
}

// Fields for message CaseAlt
type caseAlt struct {
	default_     Unit
	variant      CaseAltVariant
	primCon      PrimCon
	nil          Unit
	cons         CaseAltCons
	optionalNone Unit
	optionalSome CaseAltOptionalSome
	enum         CaseAltEnum
	body         Expr
}

func (obj caseAlt) Default() Unit {
	return obj.default_
}

func (obj caseAlt) Variant() CaseAltVariant {
	return obj.variant
}

func (obj caseAlt) PrimCon() PrimCon {
	return obj.primCon
}

func (obj caseAlt) Nil() Unit {
	return obj.nil
}

func (obj caseAlt) Cons() CaseAltCons {
	return obj.cons
}

func (obj caseAlt) OptionalNone() Unit {
	return obj.optionalNone
}

func (obj caseAlt) OptionalSome() CaseAltOptionalSome {
	return obj.optionalSome
}

func (obj caseAlt) Enum() CaseAltEnum {
	return obj.enum
}

func (obj caseAlt) Body() Expr {
	return obj.body
}

func NewCaseAlt(default_ Unit, variant CaseAltVariant, primCon PrimCon, nil Unit, cons CaseAltCons, optionalNone Unit, optionalSome CaseAltOptionalSome, enum CaseAltEnum, body Expr) (CaseAlt, error) {
	return caseAlt{
		default_:     default_,
		variant:      variant,
		primCon:      primCon,
		nil:          nil,
		cons:         cons,
		optionalNone: optionalNone,
		optionalSome: optionalSome,
		enum:         enum,
		body:         body,
	}, nil
}

type CaseAltVariant interface {
	Con() TypeConName
	Variant() string
	Binder() string
}

// Fields for message CaseAlt.Variant
type caseAltVariant struct {
	con     TypeConName
	variant string
	binder  string
}

func (obj caseAltVariant) Con() TypeConName {
	return obj.con
}

func (obj caseAltVariant) Variant() string {
	return obj.variant
}

func (obj caseAltVariant) Binder() string {
	return obj.binder
}

func NewCaseAltVariant(con TypeConName, variant string, binder string) (CaseAltVariant, error) {
	return caseAltVariant{
		con:     con,
		variant: variant,
		binder:  binder,
	}, nil
}

type CaseAltEnum interface {
	Con() TypeConName
	Constructor() string
}

// Fields for message CaseAlt.Enum
type caseAltEnum struct {
	con         TypeConName
	constructor string
}

func (obj caseAltEnum) Con() TypeConName {
	return obj.con
}

func (obj caseAltEnum) Constructor() string {
	return obj.constructor
}

func NewCaseAltEnum(con TypeConName, constructor string) (CaseAltEnum, error) {
	return caseAltEnum{
		con:         con,
		constructor: constructor,
	}, nil
}

type CaseAltCons interface {
	VarHead() string
	VarTail() string
}

// Fields for message CaseAlt.Cons
type caseAltCons struct {
	varHead string
	varTail string
}

func (obj caseAltCons) VarHead() string {
	return obj.varHead
}

func (obj caseAltCons) VarTail() string {
	return obj.varTail
}

func NewCaseAltCons(varHead string, varTail string) (CaseAltCons, error) {
	return caseAltCons{
		varHead: varHead,
		varTail: varTail,
	}, nil
}

type CaseAltOptionalSome interface {
	VarBody() string
}

// Fields for message CaseAlt.OptionalSome
type caseAltOptionalSome struct {
	varBody string
}

func (obj caseAltOptionalSome) VarBody() string {
	return obj.varBody
}

func NewCaseAltOptionalSome(varBody string) (CaseAltOptionalSome, error) {
	return caseAltOptionalSome{
		varBody: varBody,
	}, nil
}

type Case interface {
	Scrut() Expr
	Alts() []CaseAlt
}

// Fields for message Case
type case_ struct {
	scrut Expr
	alts  []CaseAlt
}

func (obj case_) Scrut() Expr {
	return obj.scrut
}

func (obj case_) Alts() []CaseAlt {
	return obj.alts
}

func NewCase(scrut Expr, alts []CaseAlt) (Case, error) {
	return case_{
		scrut: scrut,
		alts:  alts,
	}, nil
}

type Block interface {
	Bindings() []Binding
	Body() Expr
}

// Fields for message Block
type block struct {
	bindings []Binding
	body     Expr
}

func (obj block) Bindings() []Binding {
	return obj.bindings
}

func (obj block) Body() Expr {
	return obj.body
}

func NewBlock(bindings []Binding, body Expr) (Block, error) {
	return block{
		bindings: bindings,
		body:     body,
	}, nil
}

type Pure interface {
	Type() Type
	Expr() Expr
}

// Fields for message Pure
type pure struct {
	typ  Type
	expr Expr
}

func (obj pure) Type() Type {
	return obj.typ
}

func (obj pure) Expr() Expr {
	return obj.expr
}

func NewPure(typ Type, expr Expr) (Pure, error) {
	return pure{
		typ:  typ,
		expr: expr,
	}, nil
}

type Update interface {
	Pure() Pure
	Block() Block
	Create() UpdateCreate
	Exercise() UpdateExercise
	Fetch() UpdateFetch
	GetTime() Unit
	LookupByKey() UpdateRetrieveByKey
	FetchByKey() UpdateRetrieveByKey
	EmbedExpr() UpdateEmbedExpr
}

// Fields for message Update
type update struct {
	pure        Pure
	block       Block
	create      UpdateCreate
	exercise    UpdateExercise
	fetch       UpdateFetch
	getTime     Unit
	lookupByKey UpdateRetrieveByKey
	fetchByKey  UpdateRetrieveByKey
	embedExpr   UpdateEmbedExpr
}

func (obj update) Pure() Pure {
	return obj.pure
}

func (obj update) Block() Block {
	return obj.block
}

func (obj update) Create() UpdateCreate {
	return obj.create
}

func (obj update) Exercise() UpdateExercise {
	return obj.exercise
}

func (obj update) Fetch() UpdateFetch {
	return obj.fetch
}

func (obj update) GetTime() Unit {
	return obj.getTime
}

func (obj update) LookupByKey() UpdateRetrieveByKey {
	return obj.lookupByKey
}

func (obj update) FetchByKey() UpdateRetrieveByKey {
	return obj.fetchByKey
}

func (obj update) EmbedExpr() UpdateEmbedExpr {
	return obj.embedExpr
}

func NewUpdate(pure Pure, block Block, create UpdateCreate, exercise UpdateExercise, fetch UpdateFetch, getTime Unit, lookupByKey UpdateRetrieveByKey, fetchByKey UpdateRetrieveByKey, embedExpr UpdateEmbedExpr) (Update, error) {
	return update{
		pure:        pure,
		block:       block,
		create:      create,
		exercise:    exercise,
		fetch:       fetch,
		getTime:     getTime,
		lookupByKey: lookupByKey,
		fetchByKey:  fetchByKey,
		embedExpr:   embedExpr,
	}, nil
}

type UpdateCreate interface {
	Template() TypeConName
	Expr() Expr
}

// Fields for message Update.Create
type updateCreate struct {
	template TypeConName
	expr     Expr
}

func (obj updateCreate) Template() TypeConName {
	return obj.template
}

func (obj updateCreate) Expr() Expr {
	return obj.expr
}

func NewUpdateCreate(template TypeConName, expr Expr) (UpdateCreate, error) {
	return updateCreate{
		template: template,
		expr:     expr,
	}, nil
}

type UpdateExercise interface {
	Template() TypeConName
	Choice() string
	Cid() Expr
	Actor() Expr
	Arg() Expr
}

// Fields for message Update.Exercise
type updateExercise struct {
	template TypeConName
	choice   string
	cid      Expr
	actor    Expr
	arg      Expr
}

func (obj updateExercise) Template() TypeConName {
	return obj.template
}

func (obj updateExercise) Choice() string {
	return obj.choice
}

func (obj updateExercise) Cid() Expr {
	return obj.cid
}

func (obj updateExercise) Actor() Expr {
	return obj.actor
}

func (obj updateExercise) Arg() Expr {
	return obj.arg
}

func NewUpdateExercise(template TypeConName, choice string, cid Expr, actor Expr, arg Expr) (UpdateExercise, error) {
	return updateExercise{
		template: template,
		choice:   choice,
		cid:      cid,
		actor:    actor,
		arg:      arg,
	}, nil
}

type UpdateFetch interface {
	Template() TypeConName
	Cid() Expr
}

// Fields for message Update.Fetch
type updateFetch struct {
	template TypeConName
	cid      Expr
}

func (obj updateFetch) Template() TypeConName {
	return obj.template
}

func (obj updateFetch) Cid() Expr {
	return obj.cid
}

func NewUpdateFetch(template TypeConName, cid Expr) (UpdateFetch, error) {
	return updateFetch{
		template: template,
		cid:      cid,
	}, nil
}

type UpdateEmbedExpr interface {
	Type() Type
	Body() Expr
}

// Fields for message Update.EmbedExpr
type updateEmbedExpr struct {
	typ  Type
	body Expr
}

func (obj updateEmbedExpr) Type() Type {
	return obj.typ
}

func (obj updateEmbedExpr) Body() Expr {
	return obj.body
}

func NewUpdateEmbedExpr(typ Type, body Expr) (UpdateEmbedExpr, error) {
	return updateEmbedExpr{
		typ:  typ,
		body: body,
	}, nil
}

type UpdateRetrieveByKey interface {
	Template() TypeConName
	Key() Expr
}

// Fields for message Update.RetrieveByKey
type updateRetrieveByKey struct {
	template TypeConName
	key      Expr
}

func (obj updateRetrieveByKey) Template() TypeConName {
	return obj.template
}

func (obj updateRetrieveByKey) Key() Expr {
	return obj.key
}

func NewUpdateRetrieveByKey(template TypeConName, key Expr) (UpdateRetrieveByKey, error) {
	return updateRetrieveByKey{
		template: template,
		key:      key,
	}, nil
}

type Scenario interface {
	Pure() Pure
	Block() Block
	Commit() ScenarioCommit
	MustFailAt() ScenarioCommit
	Pass() Expr
	GetTime() Unit
	GetParty() Expr
	EmbedExpr() ScenarioEmbedExpr
}

// Fields for message Scenario
type scenario struct {
	pure       Pure
	block      Block
	commit     ScenarioCommit
	mustFailAt ScenarioCommit
	pass       Expr
	getTime    Unit
	getParty   Expr
	embedExpr  ScenarioEmbedExpr
}

func (obj scenario) Pure() Pure {
	return obj.pure
}

func (obj scenario) Block() Block {
	return obj.block
}

func (obj scenario) Commit() ScenarioCommit {
	return obj.commit
}

func (obj scenario) MustFailAt() ScenarioCommit {
	return obj.mustFailAt
}

func (obj scenario) Pass() Expr {
	return obj.pass
}

func (obj scenario) GetTime() Unit {
	return obj.getTime
}

func (obj scenario) GetParty() Expr {
	return obj.getParty
}

func (obj scenario) EmbedExpr() ScenarioEmbedExpr {
	return obj.embedExpr
}

func NewScenario(pure Pure, block Block, commit ScenarioCommit, mustFailAt ScenarioCommit, pass Expr, getTime Unit, getParty Expr, embedExpr ScenarioEmbedExpr) (Scenario, error) {
	return scenario{
		pure:       pure,
		block:      block,
		commit:     commit,
		mustFailAt: mustFailAt,
		pass:       pass,
		getTime:    getTime,
		getParty:   getParty,
		embedExpr:  embedExpr,
	}, nil
}

type ScenarioCommit interface {
	Party() Expr
	Expr() Expr
	RetType() Type
}

// Fields for message Scenario.Commit
type scenarioCommit struct {
	party   Expr
	expr    Expr
	retType Type
}

func (obj scenarioCommit) Party() Expr {
	return obj.party
}

func (obj scenarioCommit) Expr() Expr {
	return obj.expr
}

func (obj scenarioCommit) RetType() Type {
	return obj.retType
}

func NewScenarioCommit(party Expr, expr Expr, retType Type) (ScenarioCommit, error) {
	return scenarioCommit{
		party:   party,
		expr:    expr,
		retType: retType,
	}, nil
}

type ScenarioEmbedExpr interface {
	Type() Type
	Body() Expr
}

// Fields for message Scenario.EmbedExpr
type scenarioEmbedExpr struct {
	typ  Type
	body Expr
}

func (obj scenarioEmbedExpr) Type() Type {
	return obj.typ
}

func (obj scenarioEmbedExpr) Body() Expr {
	return obj.body
}

func NewScenarioEmbedExpr(typ Type, body Expr) (ScenarioEmbedExpr, error) {
	return scenarioEmbedExpr{
		typ:  typ,
		body: body,
	}, nil
}

type TemplateChoice interface {
	Name() string
	Consuming() bool
	Controllers() Expr
	ArgBinder() VarWithType
	RetType() Type
	Update() Expr
	SelfBinder() string
	Location() Location
}

// Fields for message TemplateChoice
type templateChoice struct {
	name        string
	consuming   bool
	controllers Expr
	argBinder   VarWithType
	retType     Type
	update      Expr
	selfBinder  string
	location    Location
}

func (obj templateChoice) Name() string {
	return obj.name
}

func (obj templateChoice) Consuming() bool {
	return obj.consuming
}

func (obj templateChoice) Controllers() Expr {
	return obj.controllers
}

func (obj templateChoice) ArgBinder() VarWithType {
	return obj.argBinder
}

func (obj templateChoice) RetType() Type {
	return obj.retType
}

func (obj templateChoice) Update() Expr {
	return obj.update
}

func (obj templateChoice) SelfBinder() string {
	return obj.selfBinder
}

func (obj templateChoice) Location() Location {
	return obj.location
}

func NewTemplateChoice(name string, consuming bool, controllers Expr, argBinder VarWithType, retType Type, update Expr, selfBinder string, location Location) (TemplateChoice, error) {
	return templateChoice{
		name:        name,
		consuming:   consuming,
		controllers: controllers,
		argBinder:   argBinder,
		retType:     retType,
		update:      update,
		selfBinder:  selfBinder,
		location:    location,
	}, nil
}

type KeyExpr interface {
	Projections() KeyExprProjections
	Record() KeyExprRecord
}

// Fields for message KeyExpr
type keyExpr struct {
	projections KeyExprProjections
	record      KeyExprRecord
}

func (obj keyExpr) Projections() KeyExprProjections {
	return obj.projections
}

func (obj keyExpr) Record() KeyExprRecord {
	return obj.record
}

func NewKeyExpr(projections KeyExprProjections, record KeyExprRecord) (KeyExpr, error) {
	return keyExpr{
		projections: projections,
		record:      record,
	}, nil
}

type KeyExprProjection interface {
	Tycon() TypeCon
	Field() string
}

// Fields for message KeyExpr.Projection
type keyExprProjection struct {
	tycon TypeCon
	field string
}

func (obj keyExprProjection) Tycon() TypeCon {
	return obj.tycon
}

func (obj keyExprProjection) Field() string {
	return obj.field
}

func NewKeyExprProjection(tycon TypeCon, field string) (KeyExprProjection, error) {
	return keyExprProjection{
		tycon: tycon,
		field: field,
	}, nil
}

type KeyExprProjections interface {
	Projections() []KeyExprProjection
}

// Fields for message KeyExpr.Projections
type keyExprProjections struct {
	projections []KeyExprProjection
}

func (obj keyExprProjections) Projections() []KeyExprProjection {
	return obj.projections
}

func NewKeyExprProjections(projections []KeyExprProjection) (KeyExprProjections, error) {
	return keyExprProjections{
		projections: projections,
	}, nil
}

type KeyExprRecordField interface {
	Field() string
	Expr() KeyExpr
}

// Fields for message KeyExpr.RecordField
type keyExprRecordField struct {
	field string
	expr  KeyExpr
}

func (obj keyExprRecordField) Field() string {
	return obj.field
}

func (obj keyExprRecordField) Expr() KeyExpr {
	return obj.expr
}

func NewKeyExprRecordField(field string, expr KeyExpr) (KeyExprRecordField, error) {
	return keyExprRecordField{
		field: field,
		expr:  expr,
	}, nil
}

type KeyExprRecord interface {
	Tycon() TypeCon
	Fields() []KeyExprRecordField
}

// Fields for message KeyExpr.Record
type keyExprRecord struct {
	tycon  TypeCon
	fields []KeyExprRecordField
}

func (obj keyExprRecord) Tycon() TypeCon {
	return obj.tycon
}

func (obj keyExprRecord) Fields() []KeyExprRecordField {
	return obj.fields
}

func NewKeyExprRecord(tycon TypeCon, fields []KeyExprRecordField) (KeyExprRecord, error) {
	return keyExprRecord{
		tycon:  tycon,
		fields: fields,
	}, nil
}

type DefTemplate interface {
	Tycon() DottedName
	Param() string
	Precond() Expr
	Signatories() Expr
	Agreement() Expr
	Choices() []TemplateChoice
	Observers() Expr
	Location() Location
	Key() DefTemplateDefKey
}

// Fields for message DefTemplate
type defTemplate struct {
	tycon       DottedName
	param       string
	precond     Expr
	signatories Expr
	agreement   Expr
	choices     []TemplateChoice
	observers   Expr
	location    Location
	key         DefTemplateDefKey
}

func (obj defTemplate) Tycon() DottedName {
	return obj.tycon
}

func (obj defTemplate) Param() string {
	return obj.param
}

func (obj defTemplate) Precond() Expr {
	return obj.precond
}

func (obj defTemplate) Signatories() Expr {
	return obj.signatories
}

func (obj defTemplate) Agreement() Expr {
	return obj.agreement
}

func (obj defTemplate) Choices() []TemplateChoice {
	return obj.choices
}

func (obj defTemplate) Observers() Expr {
	return obj.observers
}

func (obj defTemplate) Location() Location {
	return obj.location
}

func (obj defTemplate) Key() DefTemplateDefKey {
	return obj.key
}

func NewDefTemplate(tycon DottedName, param string, precond Expr, signatories Expr, agreement Expr, choices []TemplateChoice, observers Expr, location Location, key DefTemplateDefKey) (DefTemplate, error) {
	return defTemplate{
		tycon:       tycon,
		param:       param,
		precond:     precond,
		signatories: signatories,
		agreement:   agreement,
		choices:     choices,
		observers:   observers,
		location:    location,
		key:         key,
	}, nil
}

type DefTemplateDefKey interface {
	Type() Type
	Key() KeyExpr
	ComplexKey() Expr
	Maintainers() Expr
}

// Fields for message DefTemplate.DefKey
type defTemplateDefKey struct {
	typ         Type
	key         KeyExpr
	complexKey  Expr
	maintainers Expr
}

func (obj defTemplateDefKey) Type() Type {
	return obj.typ
}

func (obj defTemplateDefKey) Key() KeyExpr {
	return obj.key
}

func (obj defTemplateDefKey) ComplexKey() Expr {
	return obj.complexKey
}

func (obj defTemplateDefKey) Maintainers() Expr {
	return obj.maintainers
}

func NewDefTemplateDefKey(typ Type, key KeyExpr, complexKey Expr, maintainers Expr) (DefTemplateDefKey, error) {
	return defTemplateDefKey{
		typ:         typ,
		key:         key,
		complexKey:  complexKey,
		maintainers: maintainers,
	}, nil
}

type DefDataType interface {
	Name() DottedName
	Params() []TypeVarWithKind
	Record() DefDataTypeFields
	Variant() DefDataTypeFields
	Enum() DefDataTypeEnumConstructors
	Serializable() bool
	Location() Location
}

// Fields for message DefDataType
type defDataType struct {
	name         DottedName
	params       []TypeVarWithKind
	record       DefDataTypeFields
	variant      DefDataTypeFields
	enum         DefDataTypeEnumConstructors
	serializable bool
	location     Location
}

func (obj defDataType) Name() DottedName {
	return obj.name
}

func (obj defDataType) Params() []TypeVarWithKind {
	return obj.params
}

func (obj defDataType) Record() DefDataTypeFields {
	return obj.record
}

func (obj defDataType) Variant() DefDataTypeFields {
	return obj.variant
}

func (obj defDataType) Enum() DefDataTypeEnumConstructors {
	return obj.enum
}

func (obj defDataType) Serializable() bool {
	return obj.serializable
}

func (obj defDataType) Location() Location {
	return obj.location
}

func NewDefDataType(name DottedName, params []TypeVarWithKind, record DefDataTypeFields, variant DefDataTypeFields, enum DefDataTypeEnumConstructors, serializable bool, location Location) (DefDataType, error) {
	return defDataType{
		name:         name,
		params:       params,
		record:       record,
		variant:      variant,
		enum:         enum,
		serializable: serializable,
		location:     location,
	}, nil
}

type DefDataTypeFields interface {
	Fields() []FieldWithType
}

// Fields for message DefDataType.Fields
type defDataTypeFields struct {
	fields []FieldWithType
}

func (obj defDataTypeFields) Fields() []FieldWithType {
	return obj.fields
}

func NewDefDataTypeFields(fields []FieldWithType) (DefDataTypeFields, error) {
	return defDataTypeFields{
		fields: fields,
	}, nil
}

type DefDataTypeEnumConstructors interface {
	Constructors() []string
}

// Fields for message DefDataType.EnumConstructors
type defDataTypeEnumConstructors struct {
	constructors []string
}

func (obj defDataTypeEnumConstructors) Constructors() []string {
	return obj.constructors
}

func NewDefDataTypeEnumConstructors(constructors []string) (DefDataTypeEnumConstructors, error) {
	return defDataTypeEnumConstructors{
		constructors: constructors,
	}, nil
}

type DefTypeSyn interface {
	Name() DottedName
	Params() []TypeVarWithKind
	Type() Type
	Location() Location
}

// Fields for message DefTypeSyn
type defTypeSyn struct {
	name     DottedName
	params   []TypeVarWithKind
	typ      Type
	location Location
}

func (obj defTypeSyn) Name() DottedName {
	return obj.name
}

func (obj defTypeSyn) Params() []TypeVarWithKind {
	return obj.params
}

func (obj defTypeSyn) Type() Type {
	return obj.typ
}

func (obj defTypeSyn) Location() Location {
	return obj.location
}

func NewDefTypeSyn(name DottedName, params []TypeVarWithKind, typ Type, location Location) (DefTypeSyn, error) {
	return defTypeSyn{
		name:     name,
		params:   params,
		typ:      typ,
		location: location,
	}, nil
}

type DefValue interface {
	NameWithType() DefValueNameWithType
	Expr() Expr
	NoPartyLiterals() bool
	IsTest() bool
	Location() Location
}

// Fields for message DefValue
type defValue struct {
	nameWithType    DefValueNameWithType
	expr            Expr
	noPartyLiterals bool
	isTest          bool
	location        Location
}

func (obj defValue) NameWithType() DefValueNameWithType {
	return obj.nameWithType
}

func (obj defValue) Expr() Expr {
	return obj.expr
}

func (obj defValue) NoPartyLiterals() bool {
	return obj.noPartyLiterals
}

func (obj defValue) IsTest() bool {
	return obj.isTest
}

func (obj defValue) Location() Location {
	return obj.location
}

func NewDefValue(nameWithType DefValueNameWithType, expr Expr, noPartyLiterals bool, isTest bool, location Location) (DefValue, error) {
	return defValue{
		nameWithType:    nameWithType,
		expr:            expr,
		noPartyLiterals: noPartyLiterals,
		isTest:          isTest,
		location:        location,
	}, nil
}

type DefValueNameWithType interface {
	Name() DottedName
	Type() Type
}

// Fields for message DefValue.NameWithType
type defValueNameWithType struct {
	name DottedName
	typ  Type
}

func (obj defValueNameWithType) Name() DottedName {
	return obj.name
}

func (obj defValueNameWithType) Type() Type {
	return obj.typ
}

func NewDefValueNameWithType(name DottedName, typ Type) (DefValueNameWithType, error) {
	return defValueNameWithType{
		name: name,
		typ:  typ,
	}, nil
}

type FeatureFlags interface {
	ForbidPartyLiterals() bool
	DontDivulgeContractIdsInCreateArguments() bool
	DontDiscloseNonConsumingChoicesToObservers() bool
}

// Fields for message FeatureFlags
type featureFlags struct {
	forbidPartyLiterals                        bool
	dontDivulgeContractIdsInCreateArguments    bool
	dontDiscloseNonConsumingChoicesToObservers bool
}

func (obj featureFlags) ForbidPartyLiterals() bool {
	return obj.forbidPartyLiterals
}

func (obj featureFlags) DontDivulgeContractIdsInCreateArguments() bool {
	return obj.dontDivulgeContractIdsInCreateArguments
}

func (obj featureFlags) DontDiscloseNonConsumingChoicesToObservers() bool {
	return obj.dontDiscloseNonConsumingChoicesToObservers
}

func NewFeatureFlags(forbidPartyLiterals bool, dontDivulgeContractIdsInCreateArguments bool, dontDiscloseNonConsumingChoicesToObservers bool) (FeatureFlags, error) {
	return featureFlags{
		forbidPartyLiterals:                        forbidPartyLiterals,
		dontDivulgeContractIdsInCreateArguments:    dontDivulgeContractIdsInCreateArguments,
		dontDiscloseNonConsumingChoicesToObservers: dontDiscloseNonConsumingChoicesToObservers,
	}, nil
}

type Module interface {
	Name() DottedName
	Flags() FeatureFlags
	Synonyms() []DefTypeSyn
	DataTypes() []DefDataType
	Values() []DefValue
	Templates() []DefTemplate
}

// Fields for message Module
type module struct {
	name      DottedName
	flags     FeatureFlags
	synonyms  []DefTypeSyn
	dataTypes []DefDataType
	values    []DefValue
	templates []DefTemplate
}

func (obj module) Name() DottedName {
	return obj.name
}

func (obj module) Flags() FeatureFlags {
	return obj.flags
}

func (obj module) Synonyms() []DefTypeSyn {
	return obj.synonyms
}

func (obj module) DataTypes() []DefDataType {
	return obj.dataTypes
}

func (obj module) Values() []DefValue {
	return obj.values
}

func (obj module) Templates() []DefTemplate {
	return obj.templates
}

func NewModule(name DottedName, flags FeatureFlags, synonyms []DefTypeSyn, dataTypes []DefDataType, values []DefValue, templates []DefTemplate) (Module, error) {
	return module{
		name:      name,
		flags:     flags,
		synonyms:  synonyms,
		dataTypes: dataTypes,
		values:    values,
		templates: templates,
	}, nil
}

type PackageMetadata interface {
	Name() string
	Version() string
}

// Fields for message PackageMetadata
type packageMetadata struct {
	name    string
	version string
}

func (obj packageMetadata) Name() string {
	return obj.name
}

func (obj packageMetadata) Version() string {
	return obj.version
}

func NewPackageMetadata(name string, version string) (PackageMetadata, error) {
	return packageMetadata{
		name:    name,
		version: version,
	}, nil
}
