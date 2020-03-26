package ledger

import (
	"github.com/digital-asset/dazl-client/go/pkg/prim"
)

type Command interface {
}

type CreateCommand struct {
	TemplateId string
	Payload interface{}
}

type CreateAndExerciseCommand struct {
	TemplateId string
	Payload interface{}
	Choice string
	Argument interface{}
}

type CreateEvent struct {
	ContractId prim.ContractId
	Payload interface{}
	Signatories prim.Parties
	Observers prim.Parties
	AgreementText string
	Key interface{}
}