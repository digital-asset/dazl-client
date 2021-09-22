package ledger

import (
	"context"
)

type Connection interface {
}


type CommandOpts interface {
}

func WorkflowId() CommandOpts {
}

type HasTemplateId interface {
	TemplateId() string
}

type thing int

const Ledger_ thing = 1


type Ledger struct {
	metadata struct{} `dazltmpl:"xyz123:DABL:Ledger"`

	Operator Party `json:"operator"`

}

func (l Ledger) TemplateId() {
	return "xyz123:DABL:Ledger"
}

func (l *Ledger) Key() _LedgerKey {

}

type _LedgerKey struct {

}

type _Ledger_CCall struct {

}

func Ledger() {

}

func (_Ledger_CCall) Archive() common.ArchiveCall {

}

func Do(ctx context.Context, conn Connection) {
	Ledger{}.Archive().Do(ctx, conn)


	Ledger{}.Create().Do()
	Ledger{}.Exercise(__).Do()
	Ledger.Cid().Exercise(__).Do()
	Ledger.Key().Exercise(__).Do()

	LedgerCommands(ctx, conn).Create(Ledger{})
	LedgerCommands(ctx, conn).Exercise()
	LedgerCommands(ctx, conn).ExerciseByKey()
	LedgerCommands.Create()
	LedgerCommands.CreateAndExercise()
	LedgerCommands.Exercise()
	LedgerCommands.ExerciseByKey(struct {}, )
	Ledger__Key{}.Exercise(Ledger_Op{}).Do(ctx, conn)

}

DefTemplate[T, K, V]

type LedgerA string

type ledgerChoice interface {
	isLedgerChoice()
}

type _Ledger_UpdateMetadata_CECall struct {
	create Ledger
	exercise UpdateMetadata
}

type UpdateMetadata struct {
}

func (_Ledger_UpdateMetadata_CECall) Do (ctx context.Context, conn Connection) error {
	iterator.Done
	_, err = conn.CreateAndExercise(ctx, "", create, "UpdateMetadata", exercise)
	return err
}

type _Ledger_UpdateMetadata_ECall struct {

}

type _Ledger_UpdateMetadata_EKCall struct {

}

type Op struct {
	isLedgerChoice()
	choiceName() string
}

type LedgerContractId struct {
	Value string
}

func (cid LedgerContractId) Archive() _ArchiveExerciseCommand {

}

type _ArchiveExerciseCommand struct {
}

func (_ArchiveExerciseCommand) Do(ctx context.Context, conn Connection) {
	conn.Exercise
}

func (l Ledger) Archive() ExerciseCommand {

}

type LedgerKey struct {

}

type ContractId interface {
	TemplateId() string
	ContractId() string
}

type ExerciseResult interface {

}

type CreateEvent interface {
}

func doaquery() {

	var stream Stream = conn.Query(ctx, Ledger{}, Project{})
	stream.Next()
	create := stream.NextCreate()
	stream.NextEvent()
	stream.Close()
}