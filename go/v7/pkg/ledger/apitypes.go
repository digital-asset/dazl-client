package ledger

type CreateCommand struct {
	TemplateId string
	Payload interface{}
}

type ExerciseCommand struct {
	ContractId ContractId
	Choice string
	Argument interface{}
}

type ExerciseByKeyCommand struct {
	TemplateId string
	Key interface{}
	Choice string
	Argument interface{}
}

type CreateAndExerciseCommand struct {
	TemplateId string
	Payload interface{}
	Choice string
	Argument interface{}
}
