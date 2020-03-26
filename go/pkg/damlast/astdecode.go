package damlast

import (
	pb "github.com/digital-asset/dazl/go/gen/com/daml/daml_lf_dev"
)

func DecodeTypeConName(ctx *DecodeContext, message *pb.TypeConName) (TypeConName, error) {
	var module ModuleRef
	var name DottedName

	return NewTypeConName(module, name)
}

func DecodeTypeSynName(ctx *DecodeContext, message *pb.TypeSynName) (TypeSynName, error) {
	var module ModuleRef
	var name DottedName

	return NewTypeSynName(module, name)
}

func DecodeValName(ctx *DecodeContext, message *pb.ValName) (ValName, error) {
	var module ModuleRef
	var name DottedName

	return NewValName(module, name)
}

func DecodeFieldWithType(ctx *DecodeContext, message *pb.FieldWithType) (FieldWithType, error) {
	var field string
	var typ Type

	return NewFieldWithType(field, typ)
}

func DecodeVarWithType(ctx *DecodeContext, message *pb.VarWithType) (VarWithType, error) {
	var var_ string
	var typ Type

	return NewVarWithType(var_, typ)
}

func DecodeTypeVarWithKind(ctx *DecodeContext, message *pb.TypeVarWithKind) (TypeVarWithKind, error) {
	var var_ string
	var kind Kind

	return NewTypeVarWithKind(var_, kind)
}

func DecodeFieldWithExpr(ctx *DecodeContext, message *pb.FieldWithExpr) (FieldWithExpr, error) {
	var field string
	var expr Expr

	return NewFieldWithExpr(field, expr)
}

func DecodeBinding(ctx *DecodeContext, message *pb.Binding) (Binding, error) {
	var binder VarWithType
	var bound Expr

	return NewBinding(binder, bound)
}

func DecodeKind(ctx *DecodeContext, message *pb.Kind) (Kind, error) {
	var star Unit
	var arrow KindArrow
	var nat Unit

	return NewKind(star, arrow, nat)
}

func DecodeKindArrow(ctx *DecodeContext, message *pb.KindArrow) (KindArrow, error) {
	var params []Kind
	var result Kind

	return NewKindArrow(params, result)
}

func DecodeType(ctx *DecodeContext, message *pb.Type) (Type, error) {
	var var_ TypeVar
	var con TypeCon
	var prim TypePrim
	var fun TypeFun
	var forall TypeForall
	var struct_ TypeStruct
	var nat int64
	var syn TypeSyn

	return NewType(var_, con, prim, fun, forall, struct_, nat, syn)
}

func DecodeTypeVar(ctx *DecodeContext, message *pb.TypeVar) (TypeVar, error) {
	var var_ string
	var args []Type

	return NewTypeVar(var_, args)
}

func DecodeTypeCon(ctx *DecodeContext, message *pb.TypeCon) (TypeCon, error) {
	var tycon TypeConName
	var args []Type

	return NewTypeCon(tycon, args)
}

func DecodeTypeSyn(ctx *DecodeContext, message *pb.TypeSyn) (TypeSyn, error) {
	var tysyn TypeSynName
	var args []Type

	return NewTypeSyn(tysyn, args)
}

func DecodeTypePrim(ctx *DecodeContext, message *pb.TypePrim) (TypePrim, error) {
	var prim PrimType
	var args []Type

	return NewTypePrim(prim, args)
}

func DecodeTypeFun(ctx *DecodeContext, message *pb.TypeFun) (TypeFun, error) {
	var params []Type
	var result Type

	return NewTypeFun(params, result)
}

func DecodeTypeForall(ctx *DecodeContext, message *pb.TypeForall) (TypeForall, error) {
	var vars []TypeVarWithKind
	var body Type

	return NewTypeForall(vars, body)
}

func DecodeTypeStruct(ctx *DecodeContext, message *pb.TypeStruct) (TypeStruct, error) {
	var fields []FieldWithType

	return NewTypeStruct(fields)
}

func DecodePrimLit(ctx *DecodeContext, message *pb.PrimLit) (PrimLit, error) {
	var int64 int64
	var decimal string
	var numeric string
	var text string
	var timestamp int64
	var party string
	var date int32

	return NewPrimLit(int64, decimal, numeric, text, timestamp, party, date)
}

func DecodeLocation(ctx *DecodeContext, message *pb.Location) (Location, error) {
	var module ModuleRef
	var rng LocationRange

	return NewLocation(module, rng)
}

func DecodeLocationRange(ctx *DecodeContext, message *pb.LocationRange) (LocationRange, error) {
	var startLine int32
	var startCol int32
	var endLine int32
	var endCol int32

	return NewLocationRange(startLine, startCol, endLine, endCol)
}

func DecodeExpr(ctx *DecodeContext, message *pb.Expr) (Expr, error) {
	var location Location
	var var_ string
	var val ValName
	var builtin BuiltinFunction
	var primCon PrimCon
	var primLit PrimLit
	var recCon ExprRecCon
	var recProj ExprRecProj
	var recUpd ExprRecUpd
	var variantCon ExprVariantCon
	var enumCon ExprEnumCon
	var structCon ExprStructCon
	var structProj ExprStructProj
	var structUpd ExprStructUpd
	var app ExprApp
	var tyApp ExprTyApp
	var abs ExprAbs
	var tyAbs ExprTyAbs
	var case_ Case
	var let Block
	var nil ExprNil
	var cons ExprCons
	var update Update
	var scenario Scenario
	var optionalNone ExprOptionalNone
	var optionalSome ExprOptionalSome
	var toAny ExprToAny
	var fromAny ExprFromAny
	var typeRep Type

	return NewExpr(location, var_, val, builtin, primCon, primLit, recCon, recProj, recUpd, variantCon, enumCon, structCon, structProj, structUpd, app, tyApp, abs, tyAbs, case_, let, nil, cons, update, scenario, optionalNone, optionalSome, toAny, fromAny, typeRep)
}

func DecodeExprRecCon(ctx *DecodeContext, message *pb.ExprRecCon) (ExprRecCon, error) {
	var tycon TypeCon
	var fields []FieldWithExpr

	return NewExprRecCon(tycon, fields)
}

func DecodeExprRecProj(ctx *DecodeContext, message *pb.ExprRecProj) (ExprRecProj, error) {
	var tycon TypeCon
	var field string
	var record Expr

	return NewExprRecProj(tycon, field, record)
}

func DecodeExprRecUpd(ctx *DecodeContext, message *pb.ExprRecUpd) (ExprRecUpd, error) {
	var tycon TypeCon
	var field string
	var record Expr
	var update Expr

	return NewExprRecUpd(tycon, field, record, update)
}

func DecodeExprVariantCon(ctx *DecodeContext, message *pb.ExprVariantCon) (ExprVariantCon, error) {
	var tycon TypeCon
	var variantCon string
	var variantArg Expr

	return NewExprVariantCon(tycon, variantCon, variantArg)
}

func DecodeExprEnumCon(ctx *DecodeContext, message *pb.ExprEnumCon) (ExprEnumCon, error) {
	var tycon TypeConName
	var enumCon string

	return NewExprEnumCon(tycon, enumCon)
}

func DecodeExprStructCon(ctx *DecodeContext, message *pb.ExprStructCon) (ExprStructCon, error) {
	var fields []FieldWithExpr

	return NewExprStructCon(fields)
}

func DecodeExprStructProj(ctx *DecodeContext, message *pb.ExprStructProj) (ExprStructProj, error) {
	var field string
	var struct_ Expr

	return NewExprStructProj(field, struct_)
}

func DecodeExprStructUpd(ctx *DecodeContext, message *pb.ExprStructUpd) (ExprStructUpd, error) {
	var field string
	var struct_ Expr
	var update Expr

	return NewExprStructUpd(field, struct_, update)
}

func DecodeExprApp(ctx *DecodeContext, message *pb.ExprApp) (ExprApp, error) {
	var fun Expr
	var args []Expr

	return NewExprApp(fun, args)
}

func DecodeExprTyApp(ctx *DecodeContext, message *pb.ExprTyApp) (ExprTyApp, error) {
	var expr Expr
	var types []Type

	return NewExprTyApp(expr, types)
}

func DecodeExprAbs(ctx *DecodeContext, message *pb.ExprAbs) (ExprAbs, error) {
	var param []VarWithType
	var body Expr

	return NewExprAbs(param, body)
}

func DecodeExprTyAbs(ctx *DecodeContext, message *pb.ExprTyAbs) (ExprTyAbs, error) {
	var param []TypeVarWithKind
	var body Expr

	return NewExprTyAbs(param, body)
}

func DecodeExprNil(ctx *DecodeContext, message *pb.ExprNil) (ExprNil, error) {
	var typ Type

	return NewExprNil(typ)
}

func DecodeExprCons(ctx *DecodeContext, message *pb.ExprCons) (ExprCons, error) {
	var typ Type
	var front []Expr
	var tail Expr

	return NewExprCons(typ, front, tail)
}

func DecodeExprOptionalNone(ctx *DecodeContext, message *pb.ExprOptionalNone) (ExprOptionalNone, error) {
	var typ Type

	return NewExprOptionalNone(typ)
}

func DecodeExprOptionalSome(ctx *DecodeContext, message *pb.ExprOptionalSome) (ExprOptionalSome, error) {
	var typ Type
	var body Expr

	return NewExprOptionalSome(typ, body)
}

func DecodeExprToAny(ctx *DecodeContext, message *pb.ExprToAny) (ExprToAny, error) {
	var typ Type
	var expr Expr

	return NewExprToAny(typ, expr)
}

func DecodeExprFromAny(ctx *DecodeContext, message *pb.ExprFromAny) (ExprFromAny, error) {
	var typ Type
	var expr Expr

	return NewExprFromAny(typ, expr)
}

func DecodeCaseAlt(ctx *DecodeContext, message *pb.CaseAlt) (CaseAlt, error) {
	var default_ Unit
	var variant CaseAltVariant
	var primCon PrimCon
	var nil Unit
	var cons CaseAltCons
	var optionalNone Unit
	var optionalSome CaseAltOptionalSome
	var enum CaseAltEnum
	var body Expr

	return NewCaseAlt(default_, variant, primCon, nil, cons, optionalNone, optionalSome, enum, body)
}

func DecodeCaseAltVariant(ctx *DecodeContext, message *pb.CaseAltVariant) (CaseAltVariant, error) {
	var con TypeConName
	var variant string
	var binder string

	return NewCaseAltVariant(con, variant, binder)
}

func DecodeCaseAltEnum(ctx *DecodeContext, message *pb.CaseAltEnum) (CaseAltEnum, error) {
	var con TypeConName
	var constructor string

	return NewCaseAltEnum(con, constructor)
}

func DecodeCaseAltCons(ctx *DecodeContext, message *pb.CaseAltCons) (CaseAltCons, error) {
	var varHead string
	var varTail string

	return NewCaseAltCons(varHead, varTail)
}

func DecodeCaseAltOptionalSome(ctx *DecodeContext, message *pb.CaseAltOptionalSome) (CaseAltOptionalSome, error) {
	var varBody string

	return NewCaseAltOptionalSome(varBody)
}

func DecodeCase(ctx *DecodeContext, message *pb.Case) (Case, error) {
	var scrut Expr
	var alts []CaseAlt

	return NewCase(scrut, alts)
}

func DecodeBlock(ctx *DecodeContext, message *pb.Block) (Block, error) {
	var bindings []Binding
	var body Expr

	return NewBlock(bindings, body)
}

func DecodePure(ctx *DecodeContext, message *pb.Pure) (Pure, error) {
	var typ Type
	var expr Expr

	return NewPure(typ, expr)
}

func DecodeUpdate(ctx *DecodeContext, message *pb.Update) (Update, error) {
	var pure Pure
	var block Block
	var create UpdateCreate
	var exercise UpdateExercise
	var fetch UpdateFetch
	var getTime Unit
	var lookupByKey UpdateRetrieveByKey
	var fetchByKey UpdateRetrieveByKey
	var embedExpr UpdateEmbedExpr

	return NewUpdate(pure, block, create, exercise, fetch, getTime, lookupByKey, fetchByKey, embedExpr)
}

func DecodeUpdateCreate(ctx *DecodeContext, message *pb.UpdateCreate) (UpdateCreate, error) {
	var template TypeConName
	var expr Expr

	return NewUpdateCreate(template, expr)
}

func DecodeUpdateExercise(ctx *DecodeContext, message *pb.UpdateExercise) (UpdateExercise, error) {
	var template TypeConName
	var choice string
	var cid Expr
	var actor Expr
	var arg Expr

	return NewUpdateExercise(template, choice, cid, actor, arg)
}

func DecodeUpdateFetch(ctx *DecodeContext, message *pb.UpdateFetch) (UpdateFetch, error) {
	var template TypeConName
	var cid Expr

	return NewUpdateFetch(template, cid)
}

func DecodeUpdateEmbedExpr(ctx *DecodeContext, message *pb.UpdateEmbedExpr) (UpdateEmbedExpr, error) {
	var typ Type
	var body Expr

	return NewUpdateEmbedExpr(typ, body)
}

func DecodeUpdateRetrieveByKey(ctx *DecodeContext, message *pb.UpdateRetrieveByKey) (UpdateRetrieveByKey, error) {
	var template TypeConName
	var key Expr

	return NewUpdateRetrieveByKey(template, key)
}

func DecodeScenario(ctx *DecodeContext, message *pb.Scenario) (Scenario, error) {
	var pure Pure
	var block Block
	var commit ScenarioCommit
	var mustFailAt ScenarioCommit
	var pass Expr
	var getTime Unit
	var getParty Expr
	var embedExpr ScenarioEmbedExpr

	return NewScenario(pure, block, commit, mustFailAt, pass, getTime, getParty, embedExpr)
}

func DecodeScenarioCommit(ctx *DecodeContext, message *pb.ScenarioCommit) (ScenarioCommit, error) {
	var party Expr
	var expr Expr
	var retType Type

	return NewScenarioCommit(party, expr, retType)
}

func DecodeScenarioEmbedExpr(ctx *DecodeContext, message *pb.ScenarioEmbedExpr) (ScenarioEmbedExpr, error) {
	var typ Type
	var body Expr

	return NewScenarioEmbedExpr(typ, body)
}

func DecodeTemplateChoice(ctx *DecodeContext, message *pb.TemplateChoice) (TemplateChoice, error) {
	var name string
	var consuming bool
	var controllers Expr
	var argBinder VarWithType
	var retType Type
	var update Expr
	var selfBinder string
	var location Location

	return NewTemplateChoice(name, consuming, controllers, argBinder, retType, update, selfBinder, location)
}

func DecodeKeyExpr(ctx *DecodeContext, message *pb.KeyExpr) (KeyExpr, error) {
	var projections KeyExprProjections
	var record KeyExprRecord

	return NewKeyExpr(projections, record)
}

func DecodeKeyExprProjection(ctx *DecodeContext, message *pb.KeyExprProjection) (KeyExprProjection, error) {
	var tycon TypeCon
	var field string

	return NewKeyExprProjection(tycon, field)
}

func DecodeKeyExprProjections(ctx *DecodeContext, message *pb.KeyExprProjections) (KeyExprProjections, error) {
	var projections []KeyExprProjection

	return NewKeyExprProjections(projections)
}

func DecodeKeyExprRecordField(ctx *DecodeContext, message *pb.KeyExprRecordField) (KeyExprRecordField, error) {
	var field string
	var expr KeyExpr

	return NewKeyExprRecordField(field, expr)
}

func DecodeKeyExprRecord(ctx *DecodeContext, message *pb.KeyExprRecord) (KeyExprRecord, error) {
	var tycon TypeCon
	var fields []KeyExprRecordField

	return NewKeyExprRecord(tycon, fields)
}

func DecodeDefTemplate(ctx *DecodeContext, message *pb.DefTemplate) (DefTemplate, error) {
	var tycon DottedName
	var param string
	var precond Expr
	var signatories Expr
	var agreement Expr
	var choices []TemplateChoice
	var observers Expr
	var location Location
	var key DefTemplateDefKey

	return NewDefTemplate(tycon, param, precond, signatories, agreement, choices, observers, location, key)
}

func DecodeDefTemplateDefKey(ctx *DecodeContext, message *pb.DefTemplateDefKey) (DefTemplateDefKey, error) {
	var typ Type
	var key KeyExpr
	var complexKey Expr
	var maintainers Expr

	return NewDefTemplateDefKey(typ, key, complexKey, maintainers)
}

func DecodeDefDataType(ctx *DecodeContext, message *pb.DefDataType) (DefDataType, error) {
	var name DottedName
	var params []TypeVarWithKind
	var record DefDataTypeFields
	var variant DefDataTypeFields
	var enum DefDataTypeEnumConstructors
	var serializable bool
	var location Location

	return NewDefDataType(name, params, record, variant, enum, serializable, location)
}

func DecodeDefDataTypeFields(ctx *DecodeContext, message *pb.DefDataTypeFields) (DefDataTypeFields, error) {
	var fields []FieldWithType

	return NewDefDataTypeFields(fields)
}

func DecodeDefDataTypeEnumConstructors(ctx *DecodeContext, message *pb.DefDataTypeEnumConstructors) (DefDataTypeEnumConstructors, error) {
	var constructors []string

	return NewDefDataTypeEnumConstructors(constructors)
}

func DecodeDefTypeSyn(ctx *DecodeContext, message *pb.DefTypeSyn) (DefTypeSyn, error) {
	var name DottedName
	var params []TypeVarWithKind
	var typ Type
	var location Location

	return NewDefTypeSyn(name, params, typ, location)
}

func DecodeDefValue(ctx *DecodeContext, message *pb.DefValue) (DefValue, error) {
	var nameWithType DefValueNameWithType
	var expr Expr
	var noPartyLiterals bool
	var isTest bool
	var location Location

	return NewDefValue(nameWithType, expr, noPartyLiterals, isTest, location)
}

func DecodeDefValueNameWithType(ctx *DecodeContext, message *pb.DefValueNameWithType) (DefValueNameWithType, error) {
	var name DottedName
	var typ Type

	return NewDefValueNameWithType(name, typ)
}

func DecodeFeatureFlags(ctx *DecodeContext, message *pb.FeatureFlags) (FeatureFlags, error) {
	var forbidPartyLiterals bool
	var dontDivulgeContractIdsInCreateArguments bool
	var dontDiscloseNonConsumingChoicesToObservers bool

	return NewFeatureFlags(forbidPartyLiterals, dontDivulgeContractIdsInCreateArguments, dontDiscloseNonConsumingChoicesToObservers)
}

func DecodeModule(ctx *DecodeContext, message *pb.Module) (Module, error) {
	var name DottedName
	var flags FeatureFlags
	var synonyms []DefTypeSyn
	var dataTypes []DefDataType
	var values []DefValue
	var templates []DefTemplate

	return NewModule(name, flags, synonyms, dataTypes, values, templates)
}

func DecodePackageMetadata(ctx *DecodeContext, message *pb.PackageMetadata) (PackageMetadata, error) {
	var name string
	var version string

	return NewPackageMetadata(name, version)
}
