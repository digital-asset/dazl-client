package impl

import (
	"github.com/digital-asset/dazl-client/v8/go/pkg/lf"
)

type unit struct {
}

type packageRef struct {
	sum lf._
}

func (o *packageRef) Sum() lf._ {
	return o.sum
}

type dottedName struct {
	segments lf.string
}

func (o *dottedName) Segments() lf.string {
	return o.segments
}

type moduleRef struct {
	packageRef lf.PackageRef
	moduleName lf.DottedName
}

func (o *moduleRef) PackageRef() lf.PackageRef {
	return o.packageRef
}

func (o *moduleRef) ModuleName() lf.DottedName {
	return o.moduleName
}

type typeConName struct {
	module lf.ModuleRef
	name lf.DottedName
}

func (o *typeConName) Module() lf.ModuleRef {
	return o.module
}

func (o *typeConName) Name() lf.DottedName {
	return o.name
}

type typeSynName struct {
	module lf.ModuleRef
	name lf.DottedName
}

func (o *typeSynName) Module() lf.ModuleRef {
	return o.module
}

func (o *typeSynName) Name() lf.DottedName {
	return o.name
}

type valName struct {
	module lf.ModuleRef
	name lf.DottedName
}

func (o *valName) Module() lf.ModuleRef {
	return o.module
}

func (o *valName) Name() lf.DottedName {
	return o.name
}

type fieldWithType struct {
	field lf.string
	type_ lf.Type
}

func (o *fieldWithType) Field() lf.string {
	return o.field
}

func (o *fieldWithType) Type() lf.Type {
	return o.type_
}

type varWithType struct {
	var_ lf.string
	type_ lf.Type
}

func (o *varWithType) Var() lf.string {
	return o.var_
}

func (o *varWithType) Type() lf.Type {
	return o.type_
}

type typeVarWithKind struct {
	var_ lf.string
	kind lf.Kind
}

func (o *typeVarWithKind) Var() lf.string {
	return o.var_
}

func (o *typeVarWithKind) Kind() lf.Kind {
	return o.kind
}

type fieldWithExpr struct {
	field lf.string
	expr lf.Expr
}

func (o *fieldWithExpr) Field() lf.string {
	return o.field
}

func (o *fieldWithExpr) Expr() lf.Expr {
	return o.expr
}

type binding struct {
	binder lf.VarWithType
	bound lf.Expr
}

func (o *binding) Binder() lf.VarWithType {
	return o.binder
}

func (o *binding) Bound() lf.Expr {
	return o.bound
}

type kind struct {
	sum lf._
}

func (o *kind) Sum() lf._ {
	return o.sum
}

type kindArrow struct {
	params lf.Kind
	result lf.Kind
}

func (o *kindArrow) Params() lf.Kind {
	return o.params
}

func (o *kindArrow) Result() lf.Kind {
	return o.result
}

type type_ struct {
	sum lf._
}

func (o *type_) Sum() lf._ {
	return o.sum
}

type typeVar struct {
	var_ lf.string
	args lf.Type
}

func (o *typeVar) Var() lf.string {
	return o.var_
}

func (o *typeVar) Args() lf.Type {
	return o.args
}

type typeCon struct {
	tycon lf.TypeConName
	args lf.Type
}

func (o *typeCon) Tycon() lf.TypeConName {
	return o.tycon
}

func (o *typeCon) Args() lf.Type {
	return o.args
}

type typeSyn struct {
	tysyn lf.TypeSynName
	args lf.Type
}

func (o *typeSyn) Tysyn() lf.TypeSynName {
	return o.tysyn
}

func (o *typeSyn) Args() lf.Type {
	return o.args
}

type typePrim struct {
	prim lf.PrimType
	args lf.Type
}

func (o *typePrim) Prim() lf.PrimType {
	return o.prim
}

func (o *typePrim) Args() lf.Type {
	return o.args
}

type typeForall struct {
	vars lf.TypeVarWithKind
	body lf.Type
}

func (o *typeForall) Vars() lf.TypeVarWithKind {
	return o.vars
}

func (o *typeForall) Body() lf.Type {
	return o.body
}

type typeStruct struct {
	fields lf.FieldWithType
}

func (o *typeStruct) Fields() lf.FieldWithType {
	return o.fields
}

type primLit struct {
	sum lf._
}

func (o *primLit) Sum() lf._ {
	return o.sum
}

type location struct {
	module lf.ModuleRef
	range_ lf.LocationRange
}

func (o *location) Module() lf.ModuleRef {
	return o.module
}

func (o *location) Range() lf.LocationRange {
	return o.range_
}

type locationRange struct {
	startLine lf.int
	startCol lf.int
	endLine lf.int
	endCol lf.int
}

func (o *locationRange) StartLine() lf.int {
	return o.startLine
}

func (o *locationRange) StartCol() lf.int {
	return o.startCol
}

func (o *locationRange) EndLine() lf.int {
	return o.endLine
}

func (o *locationRange) EndCol() lf.int {
	return o.endCol
}

type expr struct {
	location lf.Location
	sum lf._
}

func (o *expr) Location() lf.Location {
	return o.location
}

func (o *expr) Sum() lf._ {
	return o.sum
}

type exprRecCon struct {
	tycon lf.TypeCon
	fields lf.FieldWithExpr
}

func (o *exprRecCon) Tycon() lf.TypeCon {
	return o.tycon
}

func (o *exprRecCon) Fields() lf.FieldWithExpr {
	return o.fields
}

type exprRecProj struct {
	tycon lf.TypeCon
	field lf.string
	record lf.Expr
}

func (o *exprRecProj) Tycon() lf.TypeCon {
	return o.tycon
}

func (o *exprRecProj) Field() lf.string {
	return o.field
}

func (o *exprRecProj) Record() lf.Expr {
	return o.record
}

type exprRecUpd struct {
	tycon lf.TypeCon
	field lf.string
	record lf.Expr
	update lf.Expr
}

func (o *exprRecUpd) Tycon() lf.TypeCon {
	return o.tycon
}

func (o *exprRecUpd) Field() lf.string {
	return o.field
}

func (o *exprRecUpd) Record() lf.Expr {
	return o.record
}

func (o *exprRecUpd) Update() lf.Expr {
	return o.update
}

type exprVariantCon struct {
	tycon lf.TypeCon
	variantCon lf.string
	variantArg lf.Expr
}

func (o *exprVariantCon) Tycon() lf.TypeCon {
	return o.tycon
}

func (o *exprVariantCon) VariantCon() lf.string {
	return o.variantCon
}

func (o *exprVariantCon) VariantArg() lf.Expr {
	return o.variantArg
}

type exprEnumCon struct {
	tycon lf.TypeConName
	enumCon lf.string
}

func (o *exprEnumCon) Tycon() lf.TypeConName {
	return o.tycon
}

func (o *exprEnumCon) EnumCon() lf.string {
	return o.enumCon
}

type exprStructCon struct {
	fields lf.FieldWithExpr
}

func (o *exprStructCon) Fields() lf.FieldWithExpr {
	return o.fields
}

type exprStructProj struct {
	field lf.string
	struct_ lf.Expr
}

func (o *exprStructProj) Field() lf.string {
	return o.field
}

func (o *exprStructProj) Struct() lf.Expr {
	return o.struct_
}

type exprStructUpd struct {
	field lf.string
	struct_ lf.Expr
	update lf.Expr
}

func (o *exprStructUpd) Field() lf.string {
	return o.field
}

func (o *exprStructUpd) Struct() lf.Expr {
	return o.struct_
}

func (o *exprStructUpd) Update() lf.Expr {
	return o.update
}

type exprApp struct {
	fun lf.Expr
	args lf.Expr
}

func (o *exprApp) Fun() lf.Expr {
	return o.fun
}

func (o *exprApp) Args() lf.Expr {
	return o.args
}

type exprTyApp struct {
	expr lf.Expr
	types lf.Type
}

func (o *exprTyApp) Expr() lf.Expr {
	return o.expr
}

func (o *exprTyApp) Types() lf.Type {
	return o.types
}

type exprAbs struct {
	param lf.VarWithType
	body lf.Expr
}

func (o *exprAbs) Param() lf.VarWithType {
	return o.param
}

func (o *exprAbs) Body() lf.Expr {
	return o.body
}

type exprTyAbs struct {
	param lf.TypeVarWithKind
	body lf.Expr
}

func (o *exprTyAbs) Param() lf.TypeVarWithKind {
	return o.param
}

func (o *exprTyAbs) Body() lf.Expr {
	return o.body
}

type exprNil struct {
	type_ lf.Type
}

func (o *exprNil) Type() lf.Type {
	return o.type_
}

type exprCons struct {
	type_ lf.Type
	front lf.Expr
	tail lf.Expr
}

func (o *exprCons) Type() lf.Type {
	return o.type_
}

func (o *exprCons) Front() lf.Expr {
	return o.front
}

func (o *exprCons) Tail() lf.Expr {
	return o.tail
}

type exprOptionalNone struct {
	type_ lf.Type
}

func (o *exprOptionalNone) Type() lf.Type {
	return o.type_
}

type exprOptionalSome struct {
	type_ lf.Type
	body lf.Expr
}

func (o *exprOptionalSome) Type() lf.Type {
	return o.type_
}

func (o *exprOptionalSome) Body() lf.Expr {
	return o.body
}

type exprToAny struct {
	type_ lf.Type
	expr lf.Expr
}

func (o *exprToAny) Type() lf.Type {
	return o.type_
}

func (o *exprToAny) Expr() lf.Expr {
	return o.expr
}

type exprFromAny struct {
	type_ lf.Type
	expr lf.Expr
}

func (o *exprFromAny) Type() lf.Type {
	return o.type_
}

func (o *exprFromAny) Expr() lf.Expr {
	return o.expr
}

type exprToAnyException struct {
	type_ lf.Type
	expr lf.Expr
}

func (o *exprToAnyException) Type() lf.Type {
	return o.type_
}

func (o *exprToAnyException) Expr() lf.Expr {
	return o.expr
}

type exprFromAnyException struct {
	type_ lf.Type
	expr lf.Expr
}

func (o *exprFromAnyException) Type() lf.Type {
	return o.type_
}

func (o *exprFromAnyException) Expr() lf.Expr {
	return o.expr
}

type exprThrow struct {
	returnType lf.Type
	exceptionType lf.Type
	exceptionExpr lf.Expr
}

func (o *exprThrow) ReturnType() lf.Type {
	return o.returnType
}

func (o *exprThrow) ExceptionType() lf.Type {
	return o.exceptionType
}

func (o *exprThrow) ExceptionExpr() lf.Expr {
	return o.exceptionExpr
}

type exprToInterface struct {
	interfaceType lf.TypeConName
	templateType lf.TypeConName
	templateExpr lf.Expr
}

func (o *exprToInterface) InterfaceType() lf.TypeConName {
	return o.interfaceType
}

func (o *exprToInterface) TemplateType() lf.TypeConName {
	return o.templateType
}

func (o *exprToInterface) TemplateExpr() lf.Expr {
	return o.templateExpr
}

type exprFromInterface struct {
	interfaceType lf.TypeConName
	templateType lf.TypeConName
	interfaceExpr lf.Expr
}

func (o *exprFromInterface) InterfaceType() lf.TypeConName {
	return o.interfaceType
}

func (o *exprFromInterface) TemplateType() lf.TypeConName {
	return o.templateType
}

func (o *exprFromInterface) InterfaceExpr() lf.Expr {
	return o.interfaceExpr
}

type exprCallInterface struct {
	interfaceType lf.TypeConName
	methodInternedName lf.int
	interfaceExpr lf.Expr
}

func (o *exprCallInterface) InterfaceType() lf.TypeConName {
	return o.interfaceType
}

func (o *exprCallInterface) MethodInternedName() lf.int {
	return o.methodInternedName
}

func (o *exprCallInterface) InterfaceExpr() lf.Expr {
	return o.interfaceExpr
}

type exprViewInterface struct {
	interface_ lf.TypeConName
	expr lf.Expr
}

func (o *exprViewInterface) Interface() lf.TypeConName {
	return o.interface_
}

func (o *exprViewInterface) Expr() lf.Expr {
	return o.expr
}

type exprSignatoryInterface struct {
	interface_ lf.TypeConName
	expr lf.Expr
}

func (o *exprSignatoryInterface) Interface() lf.TypeConName {
	return o.interface_
}

func (o *exprSignatoryInterface) Expr() lf.Expr {
	return o.expr
}

type exprObserverInterface struct {
	interface_ lf.TypeConName
	expr lf.Expr
}

func (o *exprObserverInterface) Interface() lf.TypeConName {
	return o.interface_
}

func (o *exprObserverInterface) Expr() lf.Expr {
	return o.expr
}

type exprUnsafeFromInterface struct {
	interfaceType lf.TypeConName
	templateType lf.TypeConName
	contractIdExpr lf.Expr
	interfaceExpr lf.Expr
}

func (o *exprUnsafeFromInterface) InterfaceType() lf.TypeConName {
	return o.interfaceType
}

func (o *exprUnsafeFromInterface) TemplateType() lf.TypeConName {
	return o.templateType
}

func (o *exprUnsafeFromInterface) ContractIdExpr() lf.Expr {
	return o.contractIdExpr
}

func (o *exprUnsafeFromInterface) InterfaceExpr() lf.Expr {
	return o.interfaceExpr
}

type exprToRequiredInterface struct {
	requiredInterface lf.TypeConName
	requiringInterface lf.TypeConName
	expr lf.Expr
}

func (o *exprToRequiredInterface) RequiredInterface() lf.TypeConName {
	return o.requiredInterface
}

func (o *exprToRequiredInterface) RequiringInterface() lf.TypeConName {
	return o.requiringInterface
}

func (o *exprToRequiredInterface) Expr() lf.Expr {
	return o.expr
}

type exprFromRequiredInterface struct {
	requiredInterface lf.TypeConName
	requiringInterface lf.TypeConName
	expr lf.Expr
}

func (o *exprFromRequiredInterface) RequiredInterface() lf.TypeConName {
	return o.requiredInterface
}

func (o *exprFromRequiredInterface) RequiringInterface() lf.TypeConName {
	return o.requiringInterface
}

func (o *exprFromRequiredInterface) Expr() lf.Expr {
	return o.expr
}

type exprUnsafeFromRequiredInterface struct {
	requiredInterface lf.TypeConName
	requiringInterface lf.TypeConName
	contractIdExpr lf.Expr
	interfaceExpr lf.Expr
}

func (o *exprUnsafeFromRequiredInterface) RequiredInterface() lf.TypeConName {
	return o.requiredInterface
}

func (o *exprUnsafeFromRequiredInterface) RequiringInterface() lf.TypeConName {
	return o.requiringInterface
}

func (o *exprUnsafeFromRequiredInterface) ContractIdExpr() lf.Expr {
	return o.contractIdExpr
}

func (o *exprUnsafeFromRequiredInterface) InterfaceExpr() lf.Expr {
	return o.interfaceExpr
}

type exprInterfaceTemplateTypeRep struct {
	interface_ lf.TypeConName
	expr lf.Expr
}

func (o *exprInterfaceTemplateTypeRep) Interface() lf.TypeConName {
	return o.interface_
}

func (o *exprInterfaceTemplateTypeRep) Expr() lf.Expr {
	return o.expr
}

type exprExperimental struct {
	name lf.string
	type_ lf.Type
}

func (o *exprExperimental) Name() lf.string {
	return o.name
}

func (o *exprExperimental) Type() lf.Type {
	return o.type_
}

type caseAlt struct {
	sum lf._
	body lf.Expr
}

func (o *caseAlt) Sum() lf._ {
	return o.sum
}

func (o *caseAlt) Body() lf.Expr {
	return o.body
}

type caseAltVariant struct {
	con lf.TypeConName
	variant lf.string
	binder lf.string
}

func (o *caseAltVariant) Con() lf.TypeConName {
	return o.con
}

func (o *caseAltVariant) Variant() lf.string {
	return o.variant
}

func (o *caseAltVariant) Binder() lf.string {
	return o.binder
}

type caseAltEnum struct {
	con lf.TypeConName
	constructor lf.string
}

func (o *caseAltEnum) Con() lf.TypeConName {
	return o.con
}

func (o *caseAltEnum) Constructor() lf.string {
	return o.constructor
}

type caseAltCons struct {
	varHead lf.string
	varTail lf.string
}

func (o *caseAltCons) VarHead() lf.string {
	return o.varHead
}

func (o *caseAltCons) VarTail() lf.string {
	return o.varTail
}

type caseAltOptionalSome struct {
	varBody lf.string
}

func (o *caseAltOptionalSome) VarBody() lf.string {
	return o.varBody
}

type case_ struct {
	scrut lf.Expr
	alts lf.CaseAlt
}

func (o *case_) Scrut() lf.Expr {
	return o.scrut
}

func (o *case_) Alts() lf.CaseAlt {
	return o.alts
}

type block struct {
	bindings lf.Binding
	body lf.Expr
}

func (o *block) Bindings() lf.Binding {
	return o.bindings
}

func (o *block) Body() lf.Expr {
	return o.body
}

type pure struct {
	type_ lf.Type
	expr lf.Expr
}

func (o *pure) Type() lf.Type {
	return o.type_
}

func (o *pure) Expr() lf.Expr {
	return o.expr
}

type update struct {
	sum lf._
}

func (o *update) Sum() lf._ {
	return o.sum
}

type updateCreate struct {
	template lf.TypeConName
	expr lf.Expr
}

func (o *updateCreate) Template() lf.TypeConName {
	return o.template
}

func (o *updateCreate) Expr() lf.Expr {
	return o.expr
}

type updateCreateInterface struct {
	interface_ lf.TypeConName
	expr lf.Expr
}

func (o *updateCreateInterface) Interface() lf.TypeConName {
	return o.interface_
}

func (o *updateCreateInterface) Expr() lf.Expr {
	return o.expr
}

type updateExercise struct {
	template lf.TypeConName
	choice lf.string
	cid lf.Expr
	arg lf.Expr
}

func (o *updateExercise) Template() lf.TypeConName {
	return o.template
}

func (o *updateExercise) Choice() lf.string {
	return o.choice
}

func (o *updateExercise) Cid() lf.Expr {
	return o.cid
}

func (o *updateExercise) Arg() lf.Expr {
	return o.arg
}

type updateExerciseInterface struct {
	interface_ lf.TypeConName
	choice lf.string
	cid lf.Expr
	arg lf.Expr
	guard lf.Expr
}

func (o *updateExerciseInterface) Interface() lf.TypeConName {
	return o.interface_
}

func (o *updateExerciseInterface) Choice() lf.string {
	return o.choice
}

func (o *updateExerciseInterface) Cid() lf.Expr {
	return o.cid
}

func (o *updateExerciseInterface) Arg() lf.Expr {
	return o.arg
}

func (o *updateExerciseInterface) Guard() lf.Expr {
	return o.guard
}

type updateExerciseByKey struct {
	template lf.TypeConName
	choice lf.string
	key lf.Expr
	arg lf.Expr
}

func (o *updateExerciseByKey) Template() lf.TypeConName {
	return o.template
}

func (o *updateExerciseByKey) Choice() lf.string {
	return o.choice
}

func (o *updateExerciseByKey) Key() lf.Expr {
	return o.key
}

func (o *updateExerciseByKey) Arg() lf.Expr {
	return o.arg
}

type updateFetch struct {
	template lf.TypeConName
	cid lf.Expr
}

func (o *updateFetch) Template() lf.TypeConName {
	return o.template
}

func (o *updateFetch) Cid() lf.Expr {
	return o.cid
}

type updateFetchInterface struct {
	interface_ lf.TypeConName
	cid lf.Expr
}

func (o *updateFetchInterface) Interface() lf.TypeConName {
	return o.interface_
}

func (o *updateFetchInterface) Cid() lf.Expr {
	return o.cid
}

type updateEmbedExpr struct {
	type_ lf.Type
	body lf.Expr
}

func (o *updateEmbedExpr) Type() lf.Type {
	return o.type_
}

func (o *updateEmbedExpr) Body() lf.Expr {
	return o.body
}

type updateRetrieveByKey struct {
	template lf.TypeConName
	key lf.Expr
}

func (o *updateRetrieveByKey) Template() lf.TypeConName {
	return o.template
}

func (o *updateRetrieveByKey) Key() lf.Expr {
	return o.key
}

type updateTryCatch struct {
	returnType lf.Type
	tryExpr lf.Expr
	var_ lf.string
	catchExpr lf.Expr
}

func (o *updateTryCatch) ReturnType() lf.Type {
	return o.returnType
}

func (o *updateTryCatch) TryExpr() lf.Expr {
	return o.tryExpr
}

func (o *updateTryCatch) Var() lf.string {
	return o.var_
}

func (o *updateTryCatch) CatchExpr() lf.Expr {
	return o.catchExpr
}

type scenario struct {
	sum lf._
}

func (o *scenario) Sum() lf._ {
	return o.sum
}

type scenarioCommit struct {
	party lf.Expr
	expr lf.Expr
	retType lf.Type
}

func (o *scenarioCommit) Party() lf.Expr {
	return o.party
}

func (o *scenarioCommit) Expr() lf.Expr {
	return o.expr
}

func (o *scenarioCommit) RetType() lf.Type {
	return o.retType
}

type scenarioEmbedExpr struct {
	type_ lf.Type
	body lf.Expr
}

func (o *scenarioEmbedExpr) Type() lf.Type {
	return o.type_
}

func (o *scenarioEmbedExpr) Body() lf.Expr {
	return o.body
}

type templateChoice struct {
	name lf.string
	consuming lf.bool
	controllers lf.Expr
	observers lf.Expr
	argBinder lf.VarWithType
	retType lf.Type
	update lf.Expr
	selfBinder lf.string
	location lf.Location
}

func (o *templateChoice) Name() lf.string {
	return o.name
}

func (o *templateChoice) Consuming() lf.bool {
	return o.consuming
}

func (o *templateChoice) Controllers() lf.Expr {
	return o.controllers
}

func (o *templateChoice) Observers() lf.Expr {
	return o.observers
}

func (o *templateChoice) ArgBinder() lf.VarWithType {
	return o.argBinder
}

func (o *templateChoice) RetType() lf.Type {
	return o.retType
}

func (o *templateChoice) Update() lf.Expr {
	return o.update
}

func (o *templateChoice) SelfBinder() lf.string {
	return o.selfBinder
}

func (o *templateChoice) Location() lf.Location {
	return o.location
}

type keyExpr struct {
	sum lf._
}

func (o *keyExpr) Sum() lf._ {
	return o.sum
}

type keyExprProjection struct {
	tycon lf.TypeCon
	field lf.string
}

func (o *keyExprProjection) Tycon() lf.TypeCon {
	return o.tycon
}

func (o *keyExprProjection) Field() lf.string {
	return o.field
}

type keyExprProjections struct {
	projections lf.KeyExprProjection
}

func (o *keyExprProjections) Projections() lf.KeyExprProjection {
	return o.projections
}

type keyExprRecordField struct {
	field lf.string
	expr lf.KeyExpr
}

func (o *keyExprRecordField) Field() lf.string {
	return o.field
}

func (o *keyExprRecordField) Expr() lf.KeyExpr {
	return o.expr
}

type keyExprRecord struct {
	tycon lf.TypeCon
	fields lf.KeyExprRecordField
}

func (o *keyExprRecord) Tycon() lf.TypeCon {
	return o.tycon
}

func (o *keyExprRecord) Fields() lf.KeyExprRecordField {
	return o.fields
}

type interfaceInstanceBody struct {
	methods lf.InterfaceInstanceBodyInterfaceInstanceMethod
	view lf.Expr
}

func (o *interfaceInstanceBody) Methods() lf.InterfaceInstanceBodyInterfaceInstanceMethod {
	return o.methods
}

func (o *interfaceInstanceBody) View() lf.Expr {
	return o.view
}

type interfaceInstanceBodyInterfaceInstanceMethod struct {
	methodInternedName lf.int
	value lf.Expr
}

func (o *interfaceInstanceBodyInterfaceInstanceMethod) MethodInternedName() lf.int {
	return o.methodInternedName
}

func (o *interfaceInstanceBodyInterfaceInstanceMethod) Value() lf.Expr {
	return o.value
}

type defTemplate struct {
	tycon lf.DottedName
	param lf.string
	precond lf.Expr
	signatories lf.Expr
	agreement lf.Expr
	choices lf.TemplateChoice
	observers lf.Expr
	location lf.Location
	key lf.DefTemplateDefKey
	implements lf.DefTemplateImplements
}

func (o *defTemplate) Tycon() lf.DottedName {
	return o.tycon
}

func (o *defTemplate) Param() lf.string {
	return o.param
}

func (o *defTemplate) Precond() lf.Expr {
	return o.precond
}

func (o *defTemplate) Signatories() lf.Expr {
	return o.signatories
}

func (o *defTemplate) Agreement() lf.Expr {
	return o.agreement
}

func (o *defTemplate) Choices() lf.TemplateChoice {
	return o.choices
}

func (o *defTemplate) Observers() lf.Expr {
	return o.observers
}

func (o *defTemplate) Location() lf.Location {
	return o.location
}

func (o *defTemplate) Key() lf.DefTemplateDefKey {
	return o.key
}

func (o *defTemplate) Implements() lf.DefTemplateImplements {
	return o.implements
}

type defTemplateDefKey struct {
	type_ lf.Type
	keyExpr lf._
	maintainers lf.Expr
}

func (o *defTemplateDefKey) Type() lf.Type {
	return o.type_
}

func (o *defTemplateDefKey) KeyExpr() lf._ {
	return o.keyExpr
}

func (o *defTemplateDefKey) Maintainers() lf.Expr {
	return o.maintainers
}

type defTemplateImplements struct {
	interface_ lf.TypeConName
	body lf.InterfaceInstanceBody
}

func (o *defTemplateImplements) Interface() lf.TypeConName {
	return o.interface_
}

func (o *defTemplateImplements) Body() lf.InterfaceInstanceBody {
	return o.body
}

type interfaceMethod struct {
	location lf.Location
	methodInternedName lf.int
	type_ lf.Type
}

func (o *interfaceMethod) Location() lf.Location {
	return o.location
}

func (o *interfaceMethod) MethodInternedName() lf.int {
	return o.methodInternedName
}

func (o *interfaceMethod) Type() lf.Type {
	return o.type_
}

type defInterface struct {
	location lf.Location
	tycon lf.DottedName
	methods lf.InterfaceMethod
	param lf.string
	choices lf.TemplateChoice
	coImplements lf.DefInterfaceCoImplements
	view lf.Type
	requires lf.TypeConName
}

func (o *defInterface) Location() lf.Location {
	return o.location
}

func (o *defInterface) Tycon() lf.DottedName {
	return o.tycon
}

func (o *defInterface) Methods() lf.InterfaceMethod {
	return o.methods
}

func (o *defInterface) Param() lf.string {
	return o.param
}

func (o *defInterface) Choices() lf.TemplateChoice {
	return o.choices
}

func (o *defInterface) CoImplements() lf.DefInterfaceCoImplements {
	return o.coImplements
}

func (o *defInterface) View() lf.Type {
	return o.view
}

func (o *defInterface) Requires() lf.TypeConName {
	return o.requires
}

type defInterfaceCoImplements struct {
	template lf.TypeConName
	body lf.InterfaceInstanceBody
}

func (o *defInterfaceCoImplements) Template() lf.TypeConName {
	return o.template
}

func (o *defInterfaceCoImplements) Body() lf.InterfaceInstanceBody {
	return o.body
}

type defException struct {
	name lf.DottedName
	location lf.Location
	message lf.Expr
}

func (o *defException) Name() lf.DottedName {
	return o.name
}

func (o *defException) Location() lf.Location {
	return o.location
}

func (o *defException) Message() lf.Expr {
	return o.message
}

type defDataType struct {
	name lf.DottedName
	params lf.TypeVarWithKind
	dataCons lf._
	serializable lf.bool
	location lf.Location
}

func (o *defDataType) Name() lf.DottedName {
	return o.name
}

func (o *defDataType) Params() lf.TypeVarWithKind {
	return o.params
}

func (o *defDataType) DataCons() lf._ {
	return o.dataCons
}

func (o *defDataType) Serializable() lf.bool {
	return o.serializable
}

func (o *defDataType) Location() lf.Location {
	return o.location
}

type defDataTypeFields struct {
	fields lf.FieldWithType
}

func (o *defDataTypeFields) Fields() lf.FieldWithType {
	return o.fields
}

type defDataTypeEnumConstructors struct {
	constructors lf.string
}

func (o *defDataTypeEnumConstructors) Constructors() lf.string {
	return o.constructors
}

type defTypeSyn struct {
	name lf.DottedName
	params lf.TypeVarWithKind
	type_ lf.Type
	location lf.Location
}

func (o *defTypeSyn) Name() lf.DottedName {
	return o.name
}

func (o *defTypeSyn) Params() lf.TypeVarWithKind {
	return o.params
}

func (o *defTypeSyn) Type() lf.Type {
	return o.type_
}

func (o *defTypeSyn) Location() lf.Location {
	return o.location
}

type defValue struct {
	nameWithType lf.DefValueNameWithType
	expr lf.Expr
	noPartyLiterals lf.bool
	isTest lf.bool
	location lf.Location
}

func (o *defValue) NameWithType() lf.DefValueNameWithType {
	return o.nameWithType
}

func (o *defValue) Expr() lf.Expr {
	return o.expr
}

func (o *defValue) NoPartyLiterals() lf.bool {
	return o.noPartyLiterals
}

func (o *defValue) IsTest() lf.bool {
	return o.isTest
}

func (o *defValue) Location() lf.Location {
	return o.location
}

type defValueNameWithType struct {
	name lf.DottedName
	type_ lf.Type
}

func (o *defValueNameWithType) Name() lf.DottedName {
	return o.name
}

func (o *defValueNameWithType) Type() lf.Type {
	return o.type_
}

type featureFlags struct {
	forbidPartyLiterals lf.bool
	dontDivulgeContractIdsInCreateArguments lf.bool
	dontDiscloseNonConsumingChoicesToObservers lf.bool
}

func (o *featureFlags) ForbidPartyLiterals() lf.bool {
	return o.forbidPartyLiterals
}

func (o *featureFlags) DontDivulgeContractIdsInCreateArguments() lf.bool {
	return o.dontDivulgeContractIdsInCreateArguments
}

func (o *featureFlags) DontDiscloseNonConsumingChoicesToObservers() lf.bool {
	return o.dontDiscloseNonConsumingChoicesToObservers
}

type module struct {
	name lf.DottedName
	flags lf.FeatureFlags
	synonyms lf.DefTypeSyn
	dataTypes lf.DefDataType
	values lf.DefValue
	templates lf.DefTemplate
	exceptions lf.DefException
	interfaces lf.DefInterface
}

func (o *module) Name() lf.DottedName {
	return o.name
}

func (o *module) Flags() lf.FeatureFlags {
	return o.flags
}

func (o *module) Synonyms() lf.DefTypeSyn {
	return o.synonyms
}

func (o *module) DataTypes() lf.DefDataType {
	return o.dataTypes
}

func (o *module) Values() lf.DefValue {
	return o.values
}

func (o *module) Templates() lf.DefTemplate {
	return o.templates
}

func (o *module) Exceptions() lf.DefException {
	return o.exceptions
}

func (o *module) Interfaces() lf.DefInterface {
	return o.interfaces
}

type packageMetadata struct {
	name lf.string
	version lf.string
}

func (o *packageMetadata) Name() lf.string {
	return o.name
}

func (o *packageMetadata) Version() lf.string {
	return o.version
}

type package_ struct {
	modules lf.Module
	metadata lf.PackageMetadata
}

func (o *package_) Modules() lf.Module {
	return o.modules
}

func (o *package_) Metadata() lf.PackageMetadata {
	return o.metadata
}

type archive struct {
	hash lf.PackageRef
	package_ lf.Package
}

func (o *archive) Hash() lf.PackageRef {
	return o.hash
}

func (o *archive) Package() lf.Package {
	return o.package_
}

