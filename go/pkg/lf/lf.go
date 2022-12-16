package lf

type PrimType int

const PrimTypeUNIT PrimType = 0
const PrimTypeBOOL PrimType = 1
const PrimTypeINT64 PrimType = 2
const PrimTypeDECIMAL PrimType = 3
const PrimTypeTEXT PrimType = 5
const PrimTypeTIMESTAMP PrimType = 6
const PrimTypePARTY PrimType = 8
const PrimTypeLIST PrimType = 9
const PrimTypeUPDATE PrimType = 10
const PrimTypeSCENARIO PrimType = 11
const PrimTypeDATE PrimType = 12
const PrimTypeCONTRACT_ID PrimType = 13
const PrimTypeOPTIONAL PrimType = 14
const PrimTypeARROW PrimType = 15
const PrimTypeTEXTMAP PrimType = 16
const PrimTypeNUMERIC PrimType = 17
const PrimTypeANY PrimType = 18
const PrimTypeTYPE_REP PrimType = 19
const PrimTypeGENMAP PrimType = 20
const PrimTypeBIGNUMERIC PrimType = 21
const PrimTypeROUNDING_MODE PrimType = 22
const PrimTypeANY_EXCEPTION PrimType = 23

type PrimCon int

const PrimConCON_UNIT PrimCon = 0
const PrimConCON_FALSE PrimCon = 1
const PrimConCON_TRUE PrimCon = 2

type BuiltinFunction int

const BuiltinFunctionADD_DECIMAL BuiltinFunction = 0
const BuiltinFunctionSUB_DECIMAL BuiltinFunction = 1
const BuiltinFunctionMUL_DECIMAL BuiltinFunction = 2
const BuiltinFunctionDIV_DECIMAL BuiltinFunction = 3
const BuiltinFunctionROUND_DECIMAL BuiltinFunction = 6
const BuiltinFunctionADD_NUMERIC BuiltinFunction = 107
const BuiltinFunctionSUB_NUMERIC BuiltinFunction = 108
const BuiltinFunctionMUL_NUMERIC BuiltinFunction = 109
const BuiltinFunctionDIV_NUMERIC BuiltinFunction = 110
const BuiltinFunctionROUND_NUMERIC BuiltinFunction = 111
const BuiltinFunctionCAST_NUMERIC BuiltinFunction = 121
const BuiltinFunctionSHIFT_NUMERIC BuiltinFunction = 122
const BuiltinFunctionADD_INT64 BuiltinFunction = 7
const BuiltinFunctionSUB_INT64 BuiltinFunction = 8
const BuiltinFunctionMUL_INT64 BuiltinFunction = 9
const BuiltinFunctionDIV_INT64 BuiltinFunction = 10
const BuiltinFunctionMOD_INT64 BuiltinFunction = 11
const BuiltinFunctionEXP_INT64 BuiltinFunction = 12
const BuiltinFunctionFOLDL BuiltinFunction = 20
const BuiltinFunctionFOLDR BuiltinFunction = 21
const BuiltinFunctionTEXTMAP_EMPTY BuiltinFunction = 96
const BuiltinFunctionTEXTMAP_INSERT BuiltinFunction = 97
const BuiltinFunctionTEXTMAP_LOOKUP BuiltinFunction = 98
const BuiltinFunctionTEXTMAP_DELETE BuiltinFunction = 99
const BuiltinFunctionTEXTMAP_TO_LIST BuiltinFunction = 100
const BuiltinFunctionTEXTMAP_SIZE BuiltinFunction = 101
const BuiltinFunctionGENMAP_EMPTY BuiltinFunction = 124
const BuiltinFunctionGENMAP_INSERT BuiltinFunction = 125
const BuiltinFunctionGENMAP_LOOKUP BuiltinFunction = 126
const BuiltinFunctionGENMAP_DELETE BuiltinFunction = 127
const BuiltinFunctionGENMAP_KEYS BuiltinFunction = 128
const BuiltinFunctionGENMAP_VALUES BuiltinFunction = 129
const BuiltinFunctionGENMAP_SIZE BuiltinFunction = 130
const BuiltinFunctionEXPLODE_TEXT BuiltinFunction = 23
const BuiltinFunctionAPPEND_TEXT BuiltinFunction = 24
const BuiltinFunctionERROR BuiltinFunction = 25
const BuiltinFunctionANY_EXCEPTION_MESSAGE BuiltinFunction = 147
const BuiltinFunctionLEQ_INT64 BuiltinFunction = 33
const BuiltinFunctionLEQ_DECIMAL BuiltinFunction = 34
const BuiltinFunctionLEQ_NUMERIC BuiltinFunction = 112
const BuiltinFunctionLEQ_TEXT BuiltinFunction = 36
const BuiltinFunctionLEQ_TIMESTAMP BuiltinFunction = 37
const BuiltinFunctionLEQ_DATE BuiltinFunction = 67
const BuiltinFunctionLEQ_PARTY BuiltinFunction = 89
const BuiltinFunctionLESS_INT64 BuiltinFunction = 39
const BuiltinFunctionLESS_DECIMAL BuiltinFunction = 40
const BuiltinFunctionLESS_NUMERIC BuiltinFunction = 113
const BuiltinFunctionLESS_TEXT BuiltinFunction = 42
const BuiltinFunctionLESS_TIMESTAMP BuiltinFunction = 43
const BuiltinFunctionLESS_DATE BuiltinFunction = 68
const BuiltinFunctionLESS_PARTY BuiltinFunction = 90
const BuiltinFunctionGEQ_INT64 BuiltinFunction = 45
const BuiltinFunctionGEQ_DECIMAL BuiltinFunction = 46
const BuiltinFunctionGEQ_NUMERIC BuiltinFunction = 114
const BuiltinFunctionGEQ_TEXT BuiltinFunction = 48
const BuiltinFunctionGEQ_TIMESTAMP BuiltinFunction = 49
const BuiltinFunctionGEQ_DATE BuiltinFunction = 69
const BuiltinFunctionGEQ_PARTY BuiltinFunction = 91
const BuiltinFunctionGREATER_INT64 BuiltinFunction = 51
const BuiltinFunctionGREATER_DECIMAL BuiltinFunction = 52
const BuiltinFunctionGREATER_NUMERIC BuiltinFunction = 115
const BuiltinFunctionGREATER_TEXT BuiltinFunction = 54
const BuiltinFunctionGREATER_TIMESTAMP BuiltinFunction = 55
const BuiltinFunctionGREATER_DATE BuiltinFunction = 70
const BuiltinFunctionGREATER_PARTY BuiltinFunction = 92
const BuiltinFunctionINT64_TO_TEXT BuiltinFunction = 57
const BuiltinFunctionDECIMAL_TO_TEXT BuiltinFunction = 58
const BuiltinFunctionNUMERIC_TO_TEXT BuiltinFunction = 116
const BuiltinFunctionTEXT_TO_TEXT BuiltinFunction = 60
const BuiltinFunctionTIMESTAMP_TO_TEXT BuiltinFunction = 61
const BuiltinFunctionDATE_TO_TEXT BuiltinFunction = 71
const BuiltinFunctionPARTY_TO_QUOTED_TEXT BuiltinFunction = 63
const BuiltinFunctionPARTY_TO_TEXT BuiltinFunction = 94
const BuiltinFunctionTEXT_TO_PARTY BuiltinFunction = 95
const BuiltinFunctionTEXT_TO_INT64 BuiltinFunction = 103
const BuiltinFunctionTEXT_TO_DECIMAL BuiltinFunction = 104
const BuiltinFunctionTEXT_TO_NUMERIC BuiltinFunction = 117
const BuiltinFunctionCONTRACT_ID_TO_TEXT BuiltinFunction = 136
const BuiltinFunctionSHA256_TEXT BuiltinFunction = 93
const BuiltinFunctionDATE_TO_UNIX_DAYS BuiltinFunction = 72
const BuiltinFunctionUNIX_DAYS_TO_DATE BuiltinFunction = 73
const BuiltinFunctionTIMESTAMP_TO_UNIX_MICROSECONDS BuiltinFunction = 74
const BuiltinFunctionUNIX_MICROSECONDS_TO_TIMESTAMP BuiltinFunction = 75
const BuiltinFunctionINT64_TO_DECIMAL BuiltinFunction = 76
const BuiltinFunctionDECIMAL_TO_INT64 BuiltinFunction = 77
const BuiltinFunctionINT64_TO_NUMERIC BuiltinFunction = 118
const BuiltinFunctionNUMERIC_TO_INT64 BuiltinFunction = 119
const BuiltinFunctionIMPLODE_TEXT BuiltinFunction = 78
const BuiltinFunctionEQUAL_INT64 BuiltinFunction = 79
const BuiltinFunctionEQUAL_DECIMAL BuiltinFunction = 80
const BuiltinFunctionEQUAL_NUMERIC BuiltinFunction = 120
const BuiltinFunctionEQUAL_TEXT BuiltinFunction = 81
const BuiltinFunctionEQUAL_TIMESTAMP BuiltinFunction = 82
const BuiltinFunctionEQUAL_DATE BuiltinFunction = 83
const BuiltinFunctionEQUAL_PARTY BuiltinFunction = 84
const BuiltinFunctionEQUAL_BOOL BuiltinFunction = 85
const BuiltinFunctionEQUAL_CONTRACT_ID BuiltinFunction = 86
const BuiltinFunctionEQUAL_LIST BuiltinFunction = 87
const BuiltinFunctionEQUAL_TYPE_REP BuiltinFunction = 123
const BuiltinFunctionEQUAL BuiltinFunction = 131
const BuiltinFunctionLESS_EQ BuiltinFunction = 132
const BuiltinFunctionLESS BuiltinFunction = 133
const BuiltinFunctionGREATER_EQ BuiltinFunction = 134
const BuiltinFunctionGREATER BuiltinFunction = 135
const BuiltinFunctionTRACE BuiltinFunction = 88
const BuiltinFunctionCOERCE_CONTRACT_ID BuiltinFunction = 102
const BuiltinFunctionCODE_POINTS_TO_TEXT BuiltinFunction = 105
const BuiltinFunctionTEXT_TO_CODE_POINTS BuiltinFunction = 106
const BuiltinFunctionSCALE_BIGNUMERIC BuiltinFunction = 137
const BuiltinFunctionPRECISION_BIGNUMERIC BuiltinFunction = 138
const BuiltinFunctionADD_BIGNUMERIC BuiltinFunction = 139
const BuiltinFunctionSUB_BIGNUMERIC BuiltinFunction = 140
const BuiltinFunctionMUL_BIGNUMERIC BuiltinFunction = 141
const BuiltinFunctionDIV_BIGNUMERIC BuiltinFunction = 142
const BuiltinFunctionSHIFT_RIGHT_BIGNUMERIC BuiltinFunction = 143
const BuiltinFunctionBIGNUMERIC_TO_NUMERIC BuiltinFunction = 144
const BuiltinFunctionNUMERIC_TO_BIGNUMERIC BuiltinFunction = 145
const BuiltinFunctionBIGNUMERIC_TO_TEXT BuiltinFunction = 146

type Unit interface {
}

type PackageRef string

type DottedName interface {
	Segments() string
}

type ModuleRef interface {
	PackageRef() PackageRef
	ModuleName() DottedName
}

type TypeConName interface {
	Module() ModuleRef
	Name() DottedName
}

type TypeSynName interface {
	Module() ModuleRef
	Name() DottedName
}

type ValName interface {
	Module() ModuleRef
	Name() DottedName
}

type FieldWithType interface {
	Field() string
	Type() Type
}

type VarWithType interface {
	Var() string
	Type() Type
}

type TypeVarWithKind interface {
	Var() string
	Kind() Kind
}

type FieldWithExpr interface {
	Field() string
	Expr() Expr
}

type Binding interface {
	Binder() VarWithType
	Bound() Expr
}

type Kind interface {
	Sum() KindSum
	Star() Unit
	Arrow() KindArrow
	Nat() Unit
}

type KindSum string

const KindSumStar = "star"
const KindSumArrow = "arrow"
const KindSumNat = "nat"

type KindArrow interface {
	Params() Kind
	Result() Kind
}

type Type interface {
	Sum() TypeSum
	Var() TypeVar
	Con() TypeCon
	Prim() TypePrim
	Forall() TypeForall
	Struct() TypeStruct
	Nat() int
	Syn() TypeSyn
}

type TypeSum string

const TypeSumVar = "var"
const TypeSumCon = "con"
const TypeSumPrim = "prim"
const TypeSumForall = "forall"
const TypeSumStruct = "struct"
const TypeSumNat = "nat"
const TypeSumSyn = "syn"

type TypeVar interface {
	Var() string
	Args() Type
}

type TypeCon interface {
	Tycon() TypeConName
	Args() Type
}

type TypeSyn interface {
	Tysyn() TypeSynName
	Args() Type
}

type TypePrim interface {
	Prim() PrimType
	Args() Type
}

type TypeForall interface {
	Vars() TypeVarWithKind
	Body() Type
}

type TypeStruct interface {
	Fields() FieldWithType
}

type PrimLit interface {
	Sum() PrimLitSum
	Int64() int
	Decimal() string
	Numeric() string
	Text() string
	Timestamp() float64
	Party() string
	Date() int
	RoundingMode() PrimLitRoundingMode
}

type PrimLitSum string

const PrimLitSumInt64 = "int64"
const PrimLitSumDecimal = "decimal"
const PrimLitSumNumeric = "numeric"
const PrimLitSumText = "text"
const PrimLitSumTimestamp = "timestamp"
const PrimLitSumParty = "party"
const PrimLitSumDate = "date"
const PrimLitSumRoundingMode = "rounding_mode"

type Location interface {
	Module() ModuleRef
	Range() LocationRange
}

type LocationRange interface {
	StartLine() int
	StartCol() int
	EndLine() int
	EndCol() int
}

type Expr interface {
	Location() Location
	Sum() ExprSum
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
	ToAnyException() ExprToAnyException
	FromAnyException() ExprFromAnyException
	Throw() ExprThrow
	ToInterface() ExprToInterface
	FromInterface() ExprFromInterface
	CallInterface() ExprCallInterface
	SignatoryInterface() ExprSignatoryInterface
	ObserverInterface() ExprObserverInterface
	ViewInterface() ExprViewInterface
	UnsafeFromInterface() ExprUnsafeFromInterface
	InterfaceTemplateTypeRep() ExprInterfaceTemplateTypeRep
	ToRequiredInterface() ExprToRequiredInterface
	FromRequiredInterface() ExprFromRequiredInterface
	UnsafeFromRequiredInterface() ExprUnsafeFromRequiredInterface
	Experimental() ExprExperimental
}

type ExprSum string

const ExprSumVar = "var"
const ExprSumVal = "val"
const ExprSumBuiltin = "builtin"
const ExprSumPrimCon = "prim_con"
const ExprSumPrimLit = "prim_lit"
const ExprSumRecCon = "rec_con"
const ExprSumRecProj = "rec_proj"
const ExprSumRecUpd = "rec_upd"
const ExprSumVariantCon = "variant_con"
const ExprSumEnumCon = "enum_con"
const ExprSumStructCon = "struct_con"
const ExprSumStructProj = "struct_proj"
const ExprSumStructUpd = "struct_upd"
const ExprSumApp = "app"
const ExprSumTyApp = "ty_app"
const ExprSumAbs = "abs"
const ExprSumTyAbs = "ty_abs"
const ExprSumCase = "case"
const ExprSumLet = "let"
const ExprSumNil = "nil"
const ExprSumCons = "cons"
const ExprSumUpdate = "update"
const ExprSumScenario = "scenario"
const ExprSumOptionalNone = "optional_none"
const ExprSumOptionalSome = "optional_some"
const ExprSumToAny = "to_any"
const ExprSumFromAny = "from_any"
const ExprSumTypeRep = "type_rep"
const ExprSumToAnyException = "to_any_exception"
const ExprSumFromAnyException = "from_any_exception"
const ExprSumThrow = "throw"
const ExprSumToInterface = "to_interface"
const ExprSumFromInterface = "from_interface"
const ExprSumCallInterface = "call_interface"
const ExprSumSignatoryInterface = "signatory_interface"
const ExprSumObserverInterface = "observer_interface"
const ExprSumViewInterface = "view_interface"
const ExprSumUnsafeFromInterface = "unsafe_from_interface"
const ExprSumInterfaceTemplateTypeRep = "interface_template_type_rep"
const ExprSumToRequiredInterface = "to_required_interface"
const ExprSumFromRequiredInterface = "from_required_interface"
const ExprSumUnsafeFromRequiredInterface = "unsafe_from_required_interface"
const ExprSumExperimental = "experimental"

type ExprRecCon interface {
	Tycon() TypeCon
	Fields() FieldWithExpr
}

type ExprRecProj interface {
	Tycon() TypeCon
	Field() string
	Record() Expr
}

type ExprRecUpd interface {
	Tycon() TypeCon
	Field() string
	Record() Expr
	Update() Expr
}

type ExprVariantCon interface {
	Tycon() TypeCon
	VariantCon() string
	VariantArg() Expr
}

type ExprEnumCon interface {
	Tycon() TypeConName
	EnumCon() string
}

type ExprStructCon interface {
	Fields() FieldWithExpr
}

type ExprStructProj interface {
	Field() string
	Struct() Expr
}

type ExprStructUpd interface {
	Field() string
	Struct() Expr
	Update() Expr
}

type ExprApp interface {
	Fun() Expr
	Args() Expr
}

type ExprTyApp interface {
	Expr() Expr
	Types() Type
}

type ExprAbs interface {
	Param() VarWithType
	Body() Expr
}

type ExprTyAbs interface {
	Param() TypeVarWithKind
	Body() Expr
}

type ExprNil interface {
	Type() Type
}

type ExprCons interface {
	Type() Type
	Front() Expr
	Tail() Expr
}

type ExprOptionalNone interface {
	Type() Type
}

type ExprOptionalSome interface {
	Type() Type
	Body() Expr
}

type ExprToAny interface {
	Type() Type
	Expr() Expr
}

type ExprFromAny interface {
	Type() Type
	Expr() Expr
}

type ExprToAnyException interface {
	Type() Type
	Expr() Expr
}

type ExprFromAnyException interface {
	Type() Type
	Expr() Expr
}

type ExprThrow interface {
	ReturnType() Type
	ExceptionType() Type
	ExceptionExpr() Expr
}

type ExprToInterface interface {
	InterfaceType() TypeConName
	TemplateType() TypeConName
	TemplateExpr() Expr
}

type ExprFromInterface interface {
	InterfaceType() TypeConName
	TemplateType() TypeConName
	InterfaceExpr() Expr
}

type ExprCallInterface interface {
	InterfaceType() TypeConName
	MethodInternedName() int
	InterfaceExpr() Expr
}

type ExprViewInterface interface {
	Interface() TypeConName
	Expr() Expr
}

type ExprSignatoryInterface interface {
	Interface() TypeConName
	Expr() Expr
}

type ExprObserverInterface interface {
	Interface() TypeConName
	Expr() Expr
}

type ExprUnsafeFromInterface interface {
	InterfaceType() TypeConName
	TemplateType() TypeConName
	ContractIdExpr() Expr
	InterfaceExpr() Expr
}

type ExprToRequiredInterface interface {
	RequiredInterface() TypeConName
	RequiringInterface() TypeConName
	Expr() Expr
}

type ExprFromRequiredInterface interface {
	RequiredInterface() TypeConName
	RequiringInterface() TypeConName
	Expr() Expr
}

type ExprUnsafeFromRequiredInterface interface {
	RequiredInterface() TypeConName
	RequiringInterface() TypeConName
	ContractIdExpr() Expr
	InterfaceExpr() Expr
}

type ExprInterfaceTemplateTypeRep interface {
	Interface() TypeConName
	Expr() Expr
}

type ExprExperimental interface {
	Name() string
	Type() Type
}

type CaseAlt interface {
	Sum() CaseAltSum
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

type CaseAltSum string

const CaseAltSumDefault = "default"
const CaseAltSumVariant = "variant"
const CaseAltSumPrimCon = "prim_con"
const CaseAltSumNil = "nil"
const CaseAltSumCons = "cons"
const CaseAltSumOptionalNone = "optional_none"
const CaseAltSumOptionalSome = "optional_some"
const CaseAltSumEnum = "enum"

type CaseAltVariant interface {
	Con() TypeConName
	Variant() string
	Binder() string
}

type CaseAltEnum interface {
	Con() TypeConName
	Constructor() string
}

type CaseAltCons interface {
	VarHead() string
	VarTail() string
}

type CaseAltOptionalSome interface {
	VarBody() string
}

type Case interface {
	Scrut() Expr
	Alts() CaseAlt
}

type Block interface {
	Bindings() Binding
	Body() Expr
}

type Pure interface {
	Type() Type
	Expr() Expr
}

type Update interface {
	Sum() UpdateSum
	Pure() Pure
	Block() Block
	Create() UpdateCreate
	Exercise() UpdateExercise
	ExerciseByKey() UpdateExerciseByKey
	Fetch() UpdateFetch
	GetTime() Unit
	LookupByKey() UpdateRetrieveByKey
	FetchByKey() UpdateRetrieveByKey
	EmbedExpr() UpdateEmbedExpr
	TryCatch() UpdateTryCatch
	CreateInterface() UpdateCreateInterface
	ExerciseInterface() UpdateExerciseInterface
	FetchInterface() UpdateFetchInterface
}

type UpdateSum string

const UpdateSumPure = "pure"
const UpdateSumBlock = "block"
const UpdateSumCreate = "create"
const UpdateSumExercise = "exercise"
const UpdateSumExerciseByKey = "exercise_by_key"
const UpdateSumFetch = "fetch"
const UpdateSumGetTime = "get_time"
const UpdateSumLookupByKey = "lookup_by_key"
const UpdateSumFetchByKey = "fetch_by_key"
const UpdateSumEmbedExpr = "embed_expr"
const UpdateSumTryCatch = "try_catch"
const UpdateSumCreateInterface = "create_interface"
const UpdateSumExerciseInterface = "exercise_interface"
const UpdateSumFetchInterface = "fetch_interface"

type UpdateCreate interface {
	Template() TypeConName
	Expr() Expr
}

type UpdateCreateInterface interface {
	Interface() TypeConName
	Expr() Expr
}

type UpdateExercise interface {
	Template() TypeConName
	Choice() string
	Cid() Expr
	Arg() Expr
}

type UpdateExerciseInterface interface {
	Interface() TypeConName
	Choice() string
	Cid() Expr
	Arg() Expr
	Guard() Expr
}

type UpdateExerciseByKey interface {
	Template() TypeConName
	Choice() string
	Key() Expr
	Arg() Expr
}

type UpdateFetch interface {
	Template() TypeConName
	Cid() Expr
}

type UpdateFetchInterface interface {
	Interface() TypeConName
	Cid() Expr
}

type UpdateEmbedExpr interface {
	Type() Type
	Body() Expr
}

type UpdateRetrieveByKey interface {
	Template() TypeConName
	Key() Expr
}

type UpdateTryCatch interface {
	ReturnType() Type
	TryExpr() Expr
	Var() string
	CatchExpr() Expr
}

type Scenario interface {
	Sum() ScenarioSum
	Pure() Pure
	Block() Block
	Commit() ScenarioCommit
	MustFailAt() ScenarioCommit
	Pass() Expr
	GetTime() Unit
	GetParty() Expr
	EmbedExpr() ScenarioEmbedExpr
}

type ScenarioSum string

const ScenarioSumPure = "pure"
const ScenarioSumBlock = "block"
const ScenarioSumCommit = "commit"
const ScenarioSumMustFailAt = "mustFailAt"
const ScenarioSumPass = "pass"
const ScenarioSumGetTime = "get_time"
const ScenarioSumGetParty = "get_party"
const ScenarioSumEmbedExpr = "embed_expr"

type ScenarioCommit interface {
	Party() Expr
	Expr() Expr
	RetType() Type
}

type ScenarioEmbedExpr interface {
	Type() Type
	Body() Expr
}

type TemplateChoice interface {
	Name() string
	Consuming() bool
	Controllers() Expr
	Observers() Expr
	ArgBinder() VarWithType
	RetType() Type
	Update() Expr
	SelfBinder() string
	Location() Location
}

type KeyExpr interface {
	Sum() KeyExprSum
	Projections() KeyExprProjections
	Record() KeyExprRecord
}

type KeyExprSum string

const KeyExprSumProjections = "projections"
const KeyExprSumRecord = "record"

type KeyExprProjection interface {
	Tycon() TypeCon
	Field() string
}

type KeyExprProjections interface {
	Projections() KeyExprProjection
}

type KeyExprRecordField interface {
	Field() string
	Expr() KeyExpr
}

type KeyExprRecord interface {
	Tycon() TypeCon
	Fields() KeyExprRecordField
}

type InterfaceInstanceBody interface {
	Methods() InterfaceInstanceBodyInterfaceInstanceMethod
	View() Expr
}

type InterfaceInstanceBodyInterfaceInstanceMethod interface {
	MethodInternedName() int
	Value() Expr
}

type DefTemplate interface {
	Tycon() DottedName
	Param() string
	Precond() Expr
	Signatories() Expr
	Agreement() Expr
	Choices() TemplateChoice
	Observers() Expr
	Location() Location
	Key() DefTemplateDefKey
	Implements() DefTemplateImplements
}

type DefTemplateDefKey interface {
	Type() Type
	KeyExpr() DefTemplateDefKeyKeyExpr
	Key() KeyExpr
	ComplexKey() Expr
	Maintainers() Expr
}

type DefTemplateDefKeyKeyExpr string

const DefTemplateDefKeyKeyExprKey = "key"
const DefTemplateDefKeyKeyExprComplexKey = "complex_key"

type DefTemplateImplements interface {
	Interface() TypeConName
	Body() InterfaceInstanceBody
}

type InterfaceMethod interface {
	Location() Location
	MethodInternedName() int
	Type() Type
}

type DefInterface interface {
	Location() Location
	Tycon() DottedName
	Methods() InterfaceMethod
	Param() string
	Choices() TemplateChoice
	CoImplements() DefInterfaceCoImplements
	View() Type
	Requires() TypeConName
}

type DefInterfaceCoImplements interface {
	Template() TypeConName
	Body() InterfaceInstanceBody
}

type DefException interface {
	Name() DottedName
	Location() Location
	Message() Expr
}

type DefDataType interface {
	Name() DottedName
	Params() TypeVarWithKind
	DataCons() DefDataTypeDataCons
	Record() DefDataTypeFields
	Variant() DefDataTypeFields
	Enum() DefDataTypeEnumConstructors
	Interface() Unit
	Serializable() bool
	Location() Location
}

type DefDataTypeDataCons string

const DefDataTypeDataConsRecord = "record"
const DefDataTypeDataConsVariant = "variant"
const DefDataTypeDataConsEnum = "enum"
const DefDataTypeDataConsInterface = "interface"

type DefDataTypeFields interface {
	Fields() FieldWithType
}

type DefDataTypeEnumConstructors interface {
	Constructors() string
}

type DefTypeSyn interface {
	Name() DottedName
	Params() TypeVarWithKind
	Type() Type
	Location() Location
}

type DefValue interface {
	NameWithType() DefValueNameWithType
	Expr() Expr
	NoPartyLiterals() bool
	IsTest() bool
	Location() Location
}

type DefValueNameWithType interface {
	Name() DottedName
	Type() Type
}

type FeatureFlags interface {
	ForbidPartyLiterals() bool
	DontDivulgeContractIdsInCreateArguments() bool
	DontDiscloseNonConsumingChoicesToObservers() bool
}

type Module interface {
	Name() DottedName
	Flags() FeatureFlags
	Synonyms() DefTypeSyn
	DataTypes() DefDataType
	Values() DefValue
	Templates() DefTemplate
	Exceptions() DefException
	Interfaces() DefInterface
}

type PackageMetadata interface {
	Name() string
	Version() string
}

type Package interface {
	Modules() Module
	Metadata() PackageMetadata
}

type Archive interface {
	Hash() PackageRef
	Package() Package
}
