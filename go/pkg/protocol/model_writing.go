package protocol

type Commands struct {
	CommandId string
	Commands  []Command
}

type Command interface {
}

type CreateCommand struct {
	TemplateId string                 `json:"templateId"`
	Payload    map[string]interface{} `json:"payload"`
}

type ExerciseCommand struct {
	TemplateId string                 `json:"templateId"`
	ContractId string                 `json:"contractId"`
	Choice     string                 `json:"choice"`
	Argument   map[string]interface{} `json:"argument"`
}

type CreateAndExerciseCommand struct {
	TemplateId string                 `json:"templateId"`
	Payload    map[string]interface{} `json:"payload"`
	Choice     string                 `json:"choice"`
	Argument   map[string]interface{} `json:"argument"`
}

type ExerciseByKeyCommand struct {
	TemplateId string                 `json:"templateId"`
	Key        interface{}            `json:"key"`
	Choice     string                 `json:"choice"`
	Argument   map[string]interface{} `json:"argument"`
}
