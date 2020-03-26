////+build ignore
//package damlast
//
//import (
//	"go/types"
//)
//
//type Unit struct {
//}
//
//
//type DottedName struct {
//  segments []string
//}
//
//
//type FieldWithType struct {
//  Field string
//  Type  Type
//}
//
//type VarWithType struct {
//  Var  string
//  Type Type
//}
//
//type TypeConName struct {
//
//}
//
//type Type struct {
//	// The specific type of this variant. Can be one of TypeVar, TypeCon, TypeSyn...
//	SumType() types.Type
//
//	// Attempt to cast the underlying value as a TypeVar. Returns ErrWrongSumValue if not a TypeVar.
//	AsVar() (*TypeVar, error)
//
//	// Attempt to cast the underlying value as a TypeVar. Returns ErrWrongSumValue if not a TypeVar.
//	AsCon() (*TypeCon, error)
//
//	AsSyn()
//
//	AsPrim()
//
//	AsFun()
//
//	AsForall()
//
//	AsStruct()
//
//	AsNat() (int64, error)
//
//  Visit(ctx context.Context, v TypeVisitor) error
//
//	Match(TypeVarUnapply, TypeConUnapply) T
//}

type TypeVisitor interface {
	Var(ctx context.Context, o *TypeVar) error
	Con(ctx context.Context, o *TypeCon) error
	Syn(ctx context.Context, o *TypeSyn) error
	Nat(ctx context.Context, o int64) error
}

//
//
//
//func (t Type) SumType() types.Type {
//	return type()
//}
//
//type TypeVarUnapply func(var_ string) T
//type TypeConUnapply func(tycon TypeConName, args []Type) T
//type TypeSynUnapply func(tycon TypeConName, args []Type) T
//
//func (t TypeVar) Match(fn TypeVarUnapply, _ TypeConUnapply, _ TypeSynUnapply) T { return fn(t.Var) }
//func (t TypeCon) Match(_ TypeVarUnapply, fn TypeConUnapply, _ TypeSynUnapply) T { return fn(t.TyCon, t.Args) }
//
//type TypeVar struct {
//	Var string
//}
//
//type TypeCon struct {
//	TyCon TypeConName
//	Args  []Type
//}
//
//type T interface {}
//
//
//func produceTheType() Type {
//}
//
//
//func main() {
//  t := produceTheType()
//  val := t.Match(
//    func(var_ string) T { return 0 },
//    func(tycon TypeCon, args []Type) T { return 1 }).(int)
//  _ := val + val
//}
//
//
//
//type LedgerProtocol interface {
//	Connect() error
//	OnCreate(template string, event CreateEvent)
//}
//
//
//func (GrpcLedgerProtocol) Connect() error {
//
//}
//
//func (GrpcLedgerProtocol) OnCreate(template string, event func(CreateEvent)) {
//
//}
//
//func (HttpLedgerProtocol) Connect() error {
//
//}
//
//
//func (client *Client) HandleInit(fn func()) {
//
//}
//
//func AddLedgerReadu() {
//
//}
//
//type Party struct {
//	party string
//}
//
//
//type DABL_Ledger_V3_Ledger struct {
//	Owner Party
//
//}
//
//type DABL_Ledger_V3_Ledger__CID struct {
//	ContractId string
//}
//
//
//func (*DABL_Ledger_V3_Ledger) OnCreate(client *Client, fn func(cid DABL_Ledger_V3_Ledger__CID, cdata DABL_Ledger_V3_Ledger)) {
//	client.protocol.OnCreate("DABL.Ledger.V3.Ledger", func(event CreateEvent) {
//		fn(DABL_Ledger_V3_Ledger__CID{event.ContractId}, DABL_Ledger_V3_Ledger{})
//	})
//}
//
//
//func (client *Client) RegisterPackage(p []byte) {
//}
//
//
//type PackageService struct {
//
//}
//
//
//func (*PackageService) sync() {
//
//}
//
//
//// Register a package. For the gRPC Ledger API, this enables use of "simple types".
//func (*PackageService) Register(p []byte) {
//
//}
//
//func (*PackageService) Upload(p []byte) {
//
//}
//
//
//type Metadata struct {
//	LedgerId string
//}
//
//
//
//
//func main() {
//	client := Client{}
//	client.HandleInit(func() {
//	})
//	client.Submit()
//}

type DefDataType struct {

}