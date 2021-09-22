package damlast

type PackageRef string

type PrimType int

const (
    UNIT PrimType = 0
    BOOL PrimType = 1
    INT64 PrimType = 2
)

type Type interface {
    Sum() (string, typeSum)
    Var() TypeVar
}

type _type struct {

}

type typeSum interface {
    // isTypeSum is an internal marker method that effectively
    isTypeSum()
}

func NewType(sum typeSum) Type {
    return nil
}

func NewTypeVar(var_ string, args []Type) TypeVar {
    return &typeVar{var_: var_, args: args}
}

type TypeVar interface {
    typeSum
    Var() string
    Args() []Type
}

type typeVar struct {
    var_ string
    args []Type
}

func (t typeVar) isTypeSum() {
}

func (t typeVar) Var() string {
    return t.var_
}

func (t typeVar) Args() []Type {
    return t.args
}

var _ TypeVar = (*typeVar)(nil)

type TypeCon interface {
}

type Archive interface {
    Hash() PackageRef
    Package() Package
}

func NewArchive(hash PackageRef, package_ Package) Archive {

}

func NewPackage() Package {

}

type archive struct {
    hash PackageRef
    pkg Package
}

func (a*archive) Hash() PackageRef {
  return a.hash
}

func (a*archive) Package() Package {
  return a.pkg
}

type Package interface {
}
