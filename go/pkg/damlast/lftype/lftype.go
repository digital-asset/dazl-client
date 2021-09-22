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
	CONTRACT_ID PrimType = 13
	OPTIONAL PrimType = 14
	ARROW PrimType = 15
	TEXTMAP PrimType = 16
	NUMERIC PrimType = 17
	ANY PrimType = 18
	TYPE_REP PrimType = 19
	GENMAP PrimType = 20
	BIGNUMERIC PrimType = 21
	ROUNDING_MODE PrimType = 22
	ANY_EXCEPTION PrimType = 23
)
// classification: lftype

type FieldWithType struct {
	field string
	typ Type
}
func (p Parser) ReadFieldWithType(r io.Reader) (v FieldWithType, err error) {
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
		case 2: // type
			v.typ, err = p.ReadType(r)
		}
	}
}
// classification: lftype

type VarWithType struct {
	var_ string
	typ Type
}
func (p Parser) ReadVarWithType(r io.Reader) (v VarWithType, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // var
			v.var_, err = p.Readstring(r)
		case 2: // type
			v.typ, err = p.ReadType(r)
		}
	}
}
// classification: lftype

type TypeVarWithKind struct {
	var_ string
	kind Kind
}
func (p Parser) ReadTypeVarWithKind(r io.Reader) (v TypeVarWithKind, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // var
			v.var_, err = p.Readstring(r)
		case 2: // kind
			v.kind, err = p.ReadKind(r)
		}
	}
}
// classification: lftype

type Kind struct {
	_sum caseKindSum
	sum interface{}
}
func (p Parser) ReadKind(r io.Reader) (v Kind, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // star
			v._sum = "star"
			v.sum, err = p.ReadUnit(r)
		case 2: // arrow
			v._sum = "arrow"
			v.sum, err = p.ReadKind_Arrow(r)
		case 3: // nat
			v._sum = "nat"
			v.sum, err = p.ReadUnit(r)
		}
	}
}
// classification: lftype

type Kind_Arrow struct {
	params []Kind
	result Kind
}
func (p Parser) ReadKind_Arrow(r io.Reader) (v Kind_Arrow, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // params
			var obj Kind
			obj, err = p.ReadKind(r)
			if err == nil {
				v.params = append(v.params, obj)			}
		case 2: // result
			v.result, err = p.ReadKind(r)
		}
	}
}
// classification: lftype

type Type struct {
	_sum caseTypeSum
	sum interface{}
}
func (p Parser) ReadType(r io.Reader) (v Type, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // var
			v._sum = "var"
			v.sum, err = p.ReadType_Var(r)
		case 2: // con
			v._sum = "con"
			v.sum, err = p.ReadType_Con(r)
		case 3: // prim
			v._sum = "prim"
			v.sum, err = p.ReadType_Prim(r)
		case 5: // forall
			v._sum = "forall"
			v.sum, err = p.ReadType_Forall(r)
		case 7: // struct
			v._sum = "struct"
			v.sum, err = p.ReadType_Struct(r)
		case 11: // nat
			v._sum = "nat"
			v.sum, err = p.Readint64(r)
		case 12: // syn
			v._sum = "syn"
			v.sum, err = p.ReadType_Syn(r)
		}
	}
}
// classification: lftype

type Type_Var struct {
	var_ string
	args []Type
}
func (p Parser) ReadType_Var(r io.Reader) (v Type_Var, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // var
			v.var_, err = p.Readstring(r)
		case 2: // args
			var obj Type
			obj, err = p.ReadType(r)
			if err == nil {
				v.args = append(v.args, obj)			}
		}
	}
}
// classification: lftype

type Type_Con struct {
	tycon TypeConName
	args []Type
}
func (p Parser) ReadType_Con(r io.Reader) (v Type_Con, err error) {
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
		case 2: // args
			var obj Type
			obj, err = p.ReadType(r)
			if err == nil {
				v.args = append(v.args, obj)			}
		}
	}
}
// classification: lftype

type Type_Syn struct {
	tysyn TypeSynName
	args []Type
}
func (p Parser) ReadType_Syn(r io.Reader) (v Type_Syn, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // tysyn
			v.tysyn, err = p.ReadTypeSynName(r)
		case 2: // args
			var obj Type
			obj, err = p.ReadType(r)
			if err == nil {
				v.args = append(v.args, obj)			}
		}
	}
}
// classification: lftype

type Type_Prim struct {
	prim PrimType
	args []Type
}
func (p Parser) ReadType_Prim(r io.Reader) (v Type_Prim, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // prim
			v.prim, err = p.ReadPrimType(r)
		case 2: // args
			var obj Type
			obj, err = p.ReadType(r)
			if err == nil {
				v.args = append(v.args, obj)			}
		}
	}
}
// classification: lftype

type Type_Fun struct {
	params []Type
	result Type
}
func (p Parser) ReadType_Fun(r io.Reader) (v Type_Fun, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // params
			var obj Type
			obj, err = p.ReadType(r)
			if err == nil {
				v.params = append(v.params, obj)			}
		case 2: // result
			v.result, err = p.ReadType(r)
		}
	}
}
// classification: lftype

type Type_Forall struct {
	vars []TypeVarWithKind
	body Type
}
func (p Parser) ReadType_Forall(r io.Reader) (v Type_Forall, err error) {
	var n int64
	for {
		n, err = _pb.ReadVarInt(r)
		if err == io.EOF {
			err = nil; return
		} else if err != nil {
			return
		}
		switch n >> 3 {
		case 1: // vars
			var obj TypeVarWithKind
			obj, err = p.ReadTypeVarWithKind(r)
			if err == nil {
				v.vars = append(v.vars, obj)			}
		case 2: // body
			v.body, err = p.ReadType(r)
		}
	}
}
// classification: lftype

type Type_Struct struct {
	fields []FieldWithType
}
func (p Parser) ReadType_Struct(r io.Reader) (v Type_Struct, err error) {
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
