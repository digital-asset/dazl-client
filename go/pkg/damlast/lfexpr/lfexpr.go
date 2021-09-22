package damlast

type PrimCon int32

const (
	CON_UNIT PrimCon = 0
	CON_FALSE PrimCon = 1
	CON_TRUE PrimCon = 2
)
type BuiltinFunction int32

const (
	ADD_DECIMAL BuiltinFunction = 0
	SUB_DECIMAL BuiltinFunction = 1
	MUL_DECIMAL BuiltinFunction = 2
	DIV_DECIMAL BuiltinFunction = 3
	ROUND_DECIMAL BuiltinFunction = 6
	ADD_NUMERIC BuiltinFunction = 107
	SUB_NUMERIC BuiltinFunction = 108
	MUL_NUMERIC BuiltinFunction = 109
	DIV_NUMERIC BuiltinFunction = 110
	ROUND_NUMERIC BuiltinFunction = 111
	CAST_NUMERIC BuiltinFunction = 121
	SHIFT_NUMERIC BuiltinFunction = 122
	ADD_INT64 BuiltinFunction = 7
	SUB_INT64 BuiltinFunction = 8
	MUL_INT64 BuiltinFunction = 9
	DIV_INT64 BuiltinFunction = 10
	MOD_INT64 BuiltinFunction = 11
	EXP_INT64 BuiltinFunction = 12
	FOLDL BuiltinFunction = 20
	FOLDR BuiltinFunction = 21
	TEXTMAP_EMPTY BuiltinFunction = 96
	TEXTMAP_INSERT BuiltinFunction = 97
	TEXTMAP_LOOKUP BuiltinFunction = 98
	TEXTMAP_DELETE BuiltinFunction = 99
	TEXTMAP_TO_LIST BuiltinFunction = 100
	TEXTMAP_SIZE BuiltinFunction = 101
	GENMAP_EMPTY BuiltinFunction = 124
	GENMAP_INSERT BuiltinFunction = 125
	GENMAP_LOOKUP BuiltinFunction = 126
	GENMAP_DELETE BuiltinFunction = 127
	GENMAP_KEYS BuiltinFunction = 128
	GENMAP_VALUES BuiltinFunction = 129
	GENMAP_SIZE BuiltinFunction = 130
	EXPLODE_TEXT BuiltinFunction = 23
	APPEND_TEXT BuiltinFunction = 24
	ERROR BuiltinFunction = 25
	ANY_EXCEPTION_MESSAGE BuiltinFunction = 147
	LEQ_INT64 BuiltinFunction = 33
	LEQ_DECIMAL BuiltinFunction = 34
	LEQ_NUMERIC BuiltinFunction = 112
	LEQ_TEXT BuiltinFunction = 36
	LEQ_TIMESTAMP BuiltinFunction = 37
	LEQ_DATE BuiltinFunction = 67
	LEQ_PARTY BuiltinFunction = 89
	LESS_INT64 BuiltinFunction = 39
	LESS_DECIMAL BuiltinFunction = 40
	LESS_NUMERIC BuiltinFunction = 113
	LESS_TEXT BuiltinFunction = 42
	LESS_TIMESTAMP BuiltinFunction = 43
	LESS_DATE BuiltinFunction = 68
	LESS_PARTY BuiltinFunction = 90
	GEQ_INT64 BuiltinFunction = 45
	GEQ_DECIMAL BuiltinFunction = 46
	GEQ_NUMERIC BuiltinFunction = 114
	GEQ_TEXT BuiltinFunction = 48
	GEQ_TIMESTAMP BuiltinFunction = 49
	GEQ_DATE BuiltinFunction = 69
	GEQ_PARTY BuiltinFunction = 91
	GREATER_INT64 BuiltinFunction = 51
	GREATER_DECIMAL BuiltinFunction = 52
	GREATER_NUMERIC BuiltinFunction = 115
	GREATER_TEXT BuiltinFunction = 54
	GREATER_TIMESTAMP BuiltinFunction = 55
	GREATER_DATE BuiltinFunction = 70
	GREATER_PARTY BuiltinFunction = 92
	INT64_TO_TEXT BuiltinFunction = 57
	DECIMAL_TO_TEXT BuiltinFunction = 58
	NUMERIC_TO_TEXT BuiltinFunction = 116
	TEXT_TO_TEXT BuiltinFunction = 60
	TIMESTAMP_TO_TEXT BuiltinFunction = 61
	DATE_TO_TEXT BuiltinFunction = 71
	PARTY_TO_QUOTED_TEXT BuiltinFunction = 63
	PARTY_TO_TEXT BuiltinFunction = 94
	TEXT_TO_PARTY BuiltinFunction = 95
	TEXT_TO_INT64 BuiltinFunction = 103
	TEXT_TO_DECIMAL BuiltinFunction = 104
	TEXT_TO_NUMERIC BuiltinFunction = 117
	CONTRACT_ID_TO_TEXT BuiltinFunction = 136
	SHA256_TEXT BuiltinFunction = 93
	DATE_TO_UNIX_DAYS BuiltinFunction = 72
	UNIX_DAYS_TO_DATE BuiltinFunction = 73
	TIMESTAMP_TO_UNIX_MICROSECONDS BuiltinFunction = 74
	UNIX_MICROSECONDS_TO_TIMESTAMP BuiltinFunction = 75
	INT64_TO_DECIMAL BuiltinFunction = 76
	DECIMAL_TO_INT64 BuiltinFunction = 77
	INT64_TO_NUMERIC BuiltinFunction = 118
	NUMERIC_TO_INT64 BuiltinFunction = 119
	IMPLODE_TEXT BuiltinFunction = 78
	EQUAL_INT64 BuiltinFunction = 79
	EQUAL_DECIMAL BuiltinFunction = 80
	EQUAL_NUMERIC BuiltinFunction = 120
	EQUAL_TEXT BuiltinFunction = 81
	EQUAL_TIMESTAMP BuiltinFunction = 82
	EQUAL_DATE BuiltinFunction = 83
	EQUAL_PARTY BuiltinFunction = 84
	EQUAL_BOOL BuiltinFunction = 85
	EQUAL_CONTRACT_ID BuiltinFunction = 86
	EQUAL_LIST BuiltinFunction = 87
	EQUAL_TYPE_REP BuiltinFunction = 123
	EQUAL BuiltinFunction = 131
	LESS_EQ BuiltinFunction = 132
	LESS BuiltinFunction = 133
	GREATER_EQ BuiltinFunction = 134
	GREATER BuiltinFunction = 135
	TRACE BuiltinFunction = 88
	COERCE_CONTRACT_ID BuiltinFunction = 102
	CODE_POINTS_TO_TEXT BuiltinFunction = 105
	TEXT_POINTS_TO_CODE BuiltinFunction = 106
	SCALE_BIGNUMERIC BuiltinFunction = 137
	PRECISION_BIGNUMERIC BuiltinFunction = 138
	ADD_BIGNUMERIC BuiltinFunction = 139
	SUB_BIGNUMERIC BuiltinFunction = 140
	MUL_BIGNUMERIC BuiltinFunction = 141
	DIV_BIGNUMERIC BuiltinFunction = 142
	SHIFT_RIGHT_BIGNUMERIC BuiltinFunction = 143
	BIGNUMERIC_TO_NUMERIC BuiltinFunction = 144
	NUMERIC_TO_BIGNUMERIC BuiltinFunction = 145
	BIGNUMERIC_TO_TEXT BuiltinFunction = 146
)
// classification: lfexpr

type FieldWithExpr struct {
	field string
	expr Expr
}
func (p Parser) ReadFieldWithExpr(r io.Reader) (v FieldWithExpr, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // field
			v.field, err = p.Readstring(r)
		case 2: // expr
			v.expr, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Binding struct {
	binder VarWithType
	bound Expr
}
func (p Parser) ReadBinding(r io.Reader) (v Binding, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // binder
			v.binder, err = p.ReadVarWithType(r)
		case 2: // bound
			v.bound, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type PrimLit struct {
	_sum casePrimLitSum
	sum interface{}
}
func (p Parser) ReadPrimLit(r io.Reader) (v PrimLit, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // int64
			v._sum = "int64"
			v.sum, err = p.Readint64(r)
		case 2: // decimal
			v._sum = "decimal"
			v.sum, err = p.Readstring(r)
		case 4: // text
			v._sum = "text"
			v.sum, err = p.Readstring(r)
		case 5: // timestamp
			v._sum = "timestamp"
			v.sum, err = p.Readfloat64(r)
		case 7: // party
			v._sum = "party"
			v.sum, err = p.Readstring(r)
		case 8: // date
			v._sum = "date"
			v.sum, err = p.Readint32(r)
		case 13: // rounding_mode
			v._sum = "rounding_mode"
			v.sum, err = p.ReadPrimLit_RoundingMode(r)
		}
	}
}
type PrimLit_RoundingMode int32

const (
	UP PrimLit_RoundingMode = 0
	DOWN PrimLit_RoundingMode = 1
	CEILING PrimLit_RoundingMode = 2
	FLOOR PrimLit_RoundingMode = 3
	HALF_UP PrimLit_RoundingMode = 4
	HALF_DOWN PrimLit_RoundingMode = 5
	HALF_EVEN PrimLit_RoundingMode = 6
	UNNECESSARY PrimLit_RoundingMode = 7
)
// classification: lfexpr

type Expr struct {
	location Location
	_sum caseExprSum
	sum interface{}
}
func (p Parser) ReadExpr(r io.Reader) (v Expr, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 25: // location
			v.location, err = p.ReadLocation(r)
		case 1: // var
			v._sum = "var"
			v.sum, err = p.Readstring(r)
		case 2: // val
			v._sum = "val"
			v.sum, err = p.ReadValName(r)
		case 3: // builtin
			v._sum = "builtin"
			v.sum, err = p.ReadBuiltinFunction(r)
		case 4: // prim_con
			v._sum = "prim_con"
			v.sum, err = p.ReadPrimCon(r)
		case 5: // prim_lit
			v._sum = "prim_lit"
			v.sum, err = p.ReadPrimLit(r)
		case 6: // rec_con
			v._sum = "rec_con"
			v.sum, err = p.ReadExpr_RecCon(r)
		case 7: // rec_proj
			v._sum = "rec_proj"
			v.sum, err = p.ReadExpr_RecProj(r)
		case 22: // rec_upd
			v._sum = "rec_upd"
			v.sum, err = p.ReadExpr_RecUpd(r)
		case 8: // variant_con
			v._sum = "variant_con"
			v.sum, err = p.ReadExpr_VariantCon(r)
		case 28: // enum_con
			v._sum = "enum_con"
			v.sum, err = p.ReadExpr_EnumCon(r)
		case 9: // struct_con
			v._sum = "struct_con"
			v.sum, err = p.ReadExpr_StructCon(r)
		case 10: // struct_proj
			v._sum = "struct_proj"
			v.sum, err = p.ReadExpr_StructProj(r)
		case 23: // struct_upd
			v._sum = "struct_upd"
			v.sum, err = p.ReadExpr_StructUpd(r)
		case 11: // app
			v._sum = "app"
			v.sum, err = p.ReadExpr_App(r)
		case 12: // ty_app
			v._sum = "ty_app"
			v.sum, err = p.ReadExpr_TyApp(r)
		case 13: // abs
			v._sum = "abs"
			v.sum, err = p.ReadExpr_Abs(r)
		case 14: // ty_abs
			v._sum = "ty_abs"
			v.sum, err = p.ReadExpr_TyAbs(r)
		case 15: // case
			v._sum = "case"
			v.sum, err = p.ReadCase(r)
		case 16: // let
			v._sum = "let"
			v.sum, err = p.ReadBlock(r)
		case 17: // nil
			v._sum = "nil"
			v.sum, err = p.ReadExpr_Nil(r)
		case 18: // cons
			v._sum = "cons"
			v.sum, err = p.ReadExpr_Cons(r)
		case 20: // update
			v._sum = "update"
			v.sum, err = p.ReadUpdate(r)
		case 21: // scenario
			v._sum = "scenario"
			v.sum, err = p.ReadScenario(r)
		case 26: // optional_none
			v._sum = "optional_none"
			v.sum, err = p.ReadExpr_OptionalNone(r)
		case 27: // optional_some
			v._sum = "optional_some"
			v.sum, err = p.ReadExpr_OptionalSome(r)
		case 30: // to_any
			v._sum = "to_any"
			v.sum, err = p.ReadExpr_ToAny(r)
		case 31: // from_any
			v._sum = "from_any"
			v.sum, err = p.ReadExpr_FromAny(r)
		case 32: // type_rep
			v._sum = "type_rep"
			v.sum, err = p.ReadType(r)
		case 33: // to_any_exception
			v._sum = "to_any_exception"
			v.sum, err = p.ReadExpr_ToAnyException(r)
		case 34: // from_any_exception
			v._sum = "from_any_exception"
			v.sum, err = p.ReadExpr_FromAnyException(r)
		case 35: // throw
			v._sum = "throw"
			v.sum, err = p.ReadExpr_Throw(r)
		case 9999: // experimental
			v._sum = "experimental"
			v.sum, err = p.ReadExpr_Experimental(r)
		}
	}
}
// classification: lfexpr

type Expr_RecCon struct {
	tycon Type_Con
	fields []FieldWithExpr
}
func (p Parser) ReadExpr_RecCon(r io.Reader) (v Expr_RecCon, err error) {
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
			v.tycon, err = p.ReadType_Con(r)
		case 2: // fields
			var obj FieldWithExpr
			obj, err = p.ReadFieldWithExpr(r)
			if err == nil {
				v.fields = append(v.fields, obj)			}
		}
	}
}
// classification: lfexpr

type Expr_RecProj struct {
	tycon Type_Con
	field string
	record Expr
}
func (p Parser) ReadExpr_RecProj(r io.Reader) (v Expr_RecProj, err error) {
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
			v.tycon, err = p.ReadType_Con(r)
		case 2: // field
			v.field, err = p.Readstring(r)
		case 3: // record
			v.record, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Expr_RecUpd struct {
	tycon Type_Con
	field string
	record Expr
	update Expr
}
func (p Parser) ReadExpr_RecUpd(r io.Reader) (v Expr_RecUpd, err error) {
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
			v.tycon, err = p.ReadType_Con(r)
		case 2: // field
			v.field, err = p.Readstring(r)
		case 3: // record
			v.record, err = p.ReadExpr(r)
		case 4: // update
			v.update, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Expr_VariantCon struct {
	tycon Type_Con
	variantCon string
	variantArg Expr
}
func (p Parser) ReadExpr_VariantCon(r io.Reader) (v Expr_VariantCon, err error) {
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
			v.tycon, err = p.ReadType_Con(r)
		case 2: // variant_con
			v.variantCon, err = p.Readstring(r)
		case 3: // variant_arg
			v.variantArg, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Expr_EnumCon struct {
	tycon TypeConName
	enumCon string
}
func (p Parser) ReadExpr_EnumCon(r io.Reader) (v Expr_EnumCon, err error) {
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
			v.tycon, err = p.ReadTypeConName(r)
		case 2: // enum_con
			v.enumCon, err = p.Readstring(r)
		}
	}
}
// classification: lfexpr

type Expr_StructCon struct {
	fields []FieldWithExpr
}
func (p Parser) ReadExpr_StructCon(r io.Reader) (v Expr_StructCon, err error) {
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
			var obj FieldWithExpr
			obj, err = p.ReadFieldWithExpr(r)
			if err == nil {
				v.fields = append(v.fields, obj)			}
		}
	}
}
// classification: lfexpr

type Expr_StructProj struct {
	field string
	struct_ Expr
}
func (p Parser) ReadExpr_StructProj(r io.Reader) (v Expr_StructProj, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // field
			v.field, err = p.Readstring(r)
		case 2: // struct
			v.struct_, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Expr_StructUpd struct {
	field string
	struct_ Expr
	update Expr
}
func (p Parser) ReadExpr_StructUpd(r io.Reader) (v Expr_StructUpd, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // field
			v.field, err = p.Readstring(r)
		case 2: // struct
			v.struct_, err = p.ReadExpr(r)
		case 3: // update
			v.update, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Expr_App struct {
	fun Expr
	args []Expr
}
func (p Parser) ReadExpr_App(r io.Reader) (v Expr_App, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // fun
			v.fun, err = p.ReadExpr(r)
		case 2: // args
			var obj Expr
			obj, err = p.ReadExpr(r)
			if err == nil {
				v.args = append(v.args, obj)			}
		}
	}
}
// classification: lfexpr

type Expr_TyApp struct {
	expr Expr
	types []Type
}
func (p Parser) ReadExpr_TyApp(r io.Reader) (v Expr_TyApp, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // expr
			v.expr, err = p.ReadExpr(r)
		case 2: // types
			var obj Type
			obj, err = p.ReadType(r)
			if err == nil {
				v.types = append(v.types, obj)			}
		}
	}
}
// classification: lfexpr

type Expr_Abs struct {
	param []VarWithType
	body Expr
}
func (p Parser) ReadExpr_Abs(r io.Reader) (v Expr_Abs, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // param
			var obj VarWithType
			obj, err = p.ReadVarWithType(r)
			if err == nil {
				v.param = append(v.param, obj)			}
		case 2: // body
			v.body, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Expr_TyAbs struct {
	param []TypeVarWithKind
	body Expr
}
func (p Parser) ReadExpr_TyAbs(r io.Reader) (v Expr_TyAbs, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // param
			var obj TypeVarWithKind
			obj, err = p.ReadTypeVarWithKind(r)
			if err == nil {
				v.param = append(v.param, obj)			}
		case 2: // body
			v.body, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Expr_Nil struct {
	typ Type
}
func (p Parser) ReadExpr_Nil(r io.Reader) (v Expr_Nil, err error) {
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
		}
	}
}
// classification: lfexpr

type Expr_Cons struct {
	typ Type
	front []Expr
	tail Expr
}
func (p Parser) ReadExpr_Cons(r io.Reader) (v Expr_Cons, err error) {
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
		case 2: // front
			var obj Expr
			obj, err = p.ReadExpr(r)
			if err == nil {
				v.front = append(v.front, obj)			}
		case 3: // tail
			v.tail, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Expr_OptionalNone struct {
	typ Type
}
func (p Parser) ReadExpr_OptionalNone(r io.Reader) (v Expr_OptionalNone, err error) {
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
		}
	}
}
// classification: lfexpr

type Expr_OptionalSome struct {
	typ Type
	body Expr
}
func (p Parser) ReadExpr_OptionalSome(r io.Reader) (v Expr_OptionalSome, err error) {
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
		case 2: // body
			v.body, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Expr_ToAny struct {
	typ Type
	expr Expr
}
func (p Parser) ReadExpr_ToAny(r io.Reader) (v Expr_ToAny, err error) {
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
		case 2: // expr
			v.expr, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Expr_FromAny struct {
	typ Type
	expr Expr
}
func (p Parser) ReadExpr_FromAny(r io.Reader) (v Expr_FromAny, err error) {
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
		case 2: // expr
			v.expr, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Expr_ToAnyException struct {
	typ Type
	expr Expr
}
func (p Parser) ReadExpr_ToAnyException(r io.Reader) (v Expr_ToAnyException, err error) {
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
		case 2: // expr
			v.expr, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Expr_FromAnyException struct {
	typ Type
	expr Expr
}
func (p Parser) ReadExpr_FromAnyException(r io.Reader) (v Expr_FromAnyException, err error) {
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
		case 2: // expr
			v.expr, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Expr_Throw struct {
	returnType Type
	exceptionType Type
	exceptionExpr Expr
}
func (p Parser) ReadExpr_Throw(r io.Reader) (v Expr_Throw, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // return_type
			v.returnType, err = p.ReadType(r)
		case 2: // exception_type
			v.exceptionType, err = p.ReadType(r)
		case 3: // exception_expr
			v.exceptionExpr, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Expr_Experimental struct {
	name string
	typ Type
}
func (p Parser) ReadExpr_Experimental(r io.Reader) (v Expr_Experimental, err error) {
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
		case 2: // type
			v.typ, err = p.ReadType(r)
		}
	}
}
// classification: lfexpr

type CaseAlt struct {
	body Expr
	_sum caseCaseAltSum
	sum interface{}
}
func (p Parser) ReadCaseAlt(r io.Reader) (v CaseAlt, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // default
			v._sum = "default"
			v.sum, err = p.ReadUnit(r)
		case 2: // variant
			v._sum = "variant"
			v.sum, err = p.ReadCaseAlt_Variant(r)
		case 3: // prim_con
			v._sum = "prim_con"
			v.sum, err = p.ReadPrimCon(r)
		case 4: // nil
			v._sum = "nil"
			v.sum, err = p.ReadUnit(r)
		case 5: // cons
			v._sum = "cons"
			v.sum, err = p.ReadCaseAlt_Cons(r)
		case 7: // optional_none
			v._sum = "optional_none"
			v.sum, err = p.ReadUnit(r)
		case 8: // optional_some
			v._sum = "optional_some"
			v.sum, err = p.ReadCaseAlt_OptionalSome(r)
		case 9: // enum
			v._sum = "enum"
			v.sum, err = p.ReadCaseAlt_Enum(r)
		case 6: // body
			v.body, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type CaseAlt_Variant struct {
	con TypeConName
	variant string
	binder string
}
func (p Parser) ReadCaseAlt_Variant(r io.Reader) (v CaseAlt_Variant, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // con
			v.con, err = p.ReadTypeConName(r)
		case 2: // variant
			v.variant, err = p.Readstring(r)
		case 3: // binder
			v.binder, err = p.Readstring(r)
		}
	}
}
// classification: lfexpr

type CaseAlt_Enum struct {
	con TypeConName
	constructor string
}
func (p Parser) ReadCaseAlt_Enum(r io.Reader) (v CaseAlt_Enum, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // con
			v.con, err = p.ReadTypeConName(r)
		case 2: // constructor
			v.constructor, err = p.Readstring(r)
		}
	}
}
// classification: lfexpr

type CaseAlt_Cons struct {
	varHead string
	varTail string
}
func (p Parser) ReadCaseAlt_Cons(r io.Reader) (v CaseAlt_Cons, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // var_head
			v.varHead, err = p.Readstring(r)
		case 2: // var_tail
			v.varTail, err = p.Readstring(r)
		}
	}
}
// classification: lfexpr

type CaseAlt_OptionalSome struct {
	varBody string
}
func (p Parser) ReadCaseAlt_OptionalSome(r io.Reader) (v CaseAlt_OptionalSome, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // var_body
			v.varBody, err = p.Readstring(r)
		}
	}
}
// classification: lfexpr

type Case struct {
	scrut Expr
	alts []CaseAlt
}
func (p Parser) ReadCase(r io.Reader) (v Case, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // scrut
			v.scrut, err = p.ReadExpr(r)
		case 2: // alts
			var obj CaseAlt
			obj, err = p.ReadCaseAlt(r)
			if err == nil {
				v.alts = append(v.alts, obj)			}
		}
	}
}
// classification: lfexpr

type Block struct {
	bindings []Binding
	body Expr
}
func (p Parser) ReadBlock(r io.Reader) (v Block, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // bindings
			var obj Binding
			obj, err = p.ReadBinding(r)
			if err == nil {
				v.bindings = append(v.bindings, obj)			}
		case 2: // body
			v.body, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Pure struct {
	typ Type
	expr Expr
}
func (p Parser) ReadPure(r io.Reader) (v Pure, err error) {
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
		case 2: // expr
			v.expr, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Update struct {
	_sum caseUpdateSum
	sum interface{}
}
func (p Parser) ReadUpdate(r io.Reader) (v Update, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // pure
			v._sum = "pure"
			v.sum, err = p.ReadPure(r)
		case 2: // block
			v._sum = "block"
			v.sum, err = p.ReadBlock(r)
		case 3: // create
			v._sum = "create"
			v.sum, err = p.ReadUpdate_Create(r)
		case 4: // exercise
			v._sum = "exercise"
			v.sum, err = p.ReadUpdate_Exercise(r)
		case 10: // exercise_by_key
			v._sum = "exercise_by_key"
			v.sum, err = p.ReadUpdate_ExerciseByKey(r)
		case 5: // fetch
			v._sum = "fetch"
			v.sum, err = p.ReadUpdate_Fetch(r)
		case 6: // get_time
			v._sum = "get_time"
			v.sum, err = p.ReadUnit(r)
		case 8: // lookup_by_key
			v._sum = "lookup_by_key"
			v.sum, err = p.ReadUpdate_RetrieveByKey(r)
		case 9: // fetch_by_key
			v._sum = "fetch_by_key"
			v.sum, err = p.ReadUpdate_RetrieveByKey(r)
		case 7: // embed_expr
			v._sum = "embed_expr"
			v.sum, err = p.ReadUpdate_EmbedExpr(r)
		case 11: // try_catch
			v._sum = "try_catch"
			v.sum, err = p.ReadUpdate_TryCatch(r)
		}
	}
}
// classification: lfexpr

type Update_Create struct {
	template TypeConName
	expr Expr
}
func (p Parser) ReadUpdate_Create(r io.Reader) (v Update_Create, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // template
			v.template, err = p.ReadTypeConName(r)
		case 2: // expr
			v.expr, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Update_Exercise struct {
	template TypeConName
	choice string
	cid Expr
	arg Expr
}
func (p Parser) ReadUpdate_Exercise(r io.Reader) (v Update_Exercise, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // template
			v.template, err = p.ReadTypeConName(r)
		case 2: // choice
			v.choice, err = p.Readstring(r)
		case 3: // cid
			v.cid, err = p.ReadExpr(r)
		case 5: // arg
			v.arg, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Update_ExerciseByKey struct {
	template TypeConName
	choice string
	key Expr
	arg Expr
}
func (p Parser) ReadUpdate_ExerciseByKey(r io.Reader) (v Update_ExerciseByKey, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // template
			v.template, err = p.ReadTypeConName(r)
		case 3: // key
			v.key, err = p.ReadExpr(r)
		case 4: // arg
			v.arg, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Update_Fetch struct {
	template TypeConName
	cid Expr
}
func (p Parser) ReadUpdate_Fetch(r io.Reader) (v Update_Fetch, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // template
			v.template, err = p.ReadTypeConName(r)
		case 2: // cid
			v.cid, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Update_EmbedExpr struct {
	typ Type
	body Expr
}
func (p Parser) ReadUpdate_EmbedExpr(r io.Reader) (v Update_EmbedExpr, err error) {
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
		case 2: // body
			v.body, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Update_RetrieveByKey struct {
	template TypeConName
	key Expr
}
func (p Parser) ReadUpdate_RetrieveByKey(r io.Reader) (v Update_RetrieveByKey, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // template
			v.template, err = p.ReadTypeConName(r)
		case 2: // key
			v.key, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Update_TryCatch struct {
	returnType Type
	tryExpr Expr
	var_ string
	catchExpr Expr
}
func (p Parser) ReadUpdate_TryCatch(r io.Reader) (v Update_TryCatch, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // return_type
			v.returnType, err = p.ReadType(r)
		case 2: // try_expr
			v.tryExpr, err = p.ReadExpr(r)
		case 4: // catch_expr
			v.catchExpr, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type Scenario struct {
	_sum caseScenarioSum
	sum interface{}
}
func (p Parser) ReadScenario(r io.Reader) (v Scenario, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // pure
			v._sum = "pure"
			v.sum, err = p.ReadPure(r)
		case 2: // block
			v._sum = "block"
			v.sum, err = p.ReadBlock(r)
		case 3: // commit
			v._sum = "commit"
			v.sum, err = p.ReadScenario_Commit(r)
		case 4: // mustFailAt
			v._sum = "mustFailAt"
			v.sum, err = p.ReadScenario_Commit(r)
		case 5: // pass
			v._sum = "pass"
			v.sum, err = p.ReadExpr(r)
		case 6: // get_time
			v._sum = "get_time"
			v.sum, err = p.ReadUnit(r)
		case 7: // get_party
			v._sum = "get_party"
			v.sum, err = p.ReadExpr(r)
		case 8: // embed_expr
			v._sum = "embed_expr"
			v.sum, err = p.ReadScenario_EmbedExpr(r)
		}
	}
}
// classification: lfexpr

type Scenario_Commit struct {
	party Expr
	expr Expr
	retType Type
}
func (p Parser) ReadScenario_Commit(r io.Reader) (v Scenario_Commit, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // party
			v.party, err = p.ReadExpr(r)
		case 2: // expr
			v.expr, err = p.ReadExpr(r)
		case 3: // ret_type
			v.retType, err = p.ReadType(r)
		}
	}
}
// classification: lfexpr

type Scenario_EmbedExpr struct {
	typ Type
	body Expr
}
func (p Parser) ReadScenario_EmbedExpr(r io.Reader) (v Scenario_EmbedExpr, err error) {
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
		case 2: // body
			v.body, err = p.ReadExpr(r)
		}
	}
}
// classification: lfexpr

type KeyExpr struct {
	_sum caseKeyExprSum
	sum interface{}
}
func (p Parser) ReadKeyExpr(r io.Reader) (v KeyExpr, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // projections
			v._sum = "projections"
			v.sum, err = p.ReadKeyExpr_Projections(r)
		case 2: // record
			v._sum = "record"
			v.sum, err = p.ReadKeyExpr_Record(r)
		}
	}
}
// classification: lfexpr

type KeyExpr_Projection struct {
	tycon Type_Con
	field string
}
func (p Parser) ReadKeyExpr_Projection(r io.Reader) (v KeyExpr_Projection, err error) {
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
			v.tycon, err = p.ReadType_Con(r)
		case 2: // field
			v.field, err = p.Readstring(r)
		}
	}
}
// classification: lfexpr

type KeyExpr_Projections struct {
	projections []KeyExpr_Projection
}
func (p Parser) ReadKeyExpr_Projections(r io.Reader) (v KeyExpr_Projections, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 2: // projections
			var obj KeyExpr_Projection
			obj, err = p.ReadKeyExpr_Projection(r)
			if err == nil {
				v.projections = append(v.projections, obj)			}
		}
	}
}
// classification: lfexpr

type KeyExpr_RecordField struct {
	field string
	expr KeyExpr
}
func (p Parser) ReadKeyExpr_RecordField(r io.Reader) (v KeyExpr_RecordField, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // field
			v.field, err = p.Readstring(r)
		case 2: // expr
			v.expr, err = p.ReadKeyExpr(r)
		}
	}
}
// classification: lfexpr

type KeyExpr_Record struct {
	tycon Type_Con
	fields []KeyExpr_RecordField
}
func (p Parser) ReadKeyExpr_Record(r io.Reader) (v KeyExpr_Record, err error) {
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
			v.tycon, err = p.ReadType_Con(r)
		case 2: // fields
			var obj KeyExpr_RecordField
			obj, err = p.ReadKeyExpr_RecordField(r)
			if err == nil {
				v.fields = append(v.fields, obj)			}
		}
	}
}
