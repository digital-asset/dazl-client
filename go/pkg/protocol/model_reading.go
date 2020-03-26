package protocol

type Event interface {
}

type CreatedEvent struct {
	TemplateId   string                 `json:"templateId"`
	ContractId   string                 `json:"contractId"`
	ContractData map[string]interface{} `json:"payload"`
}

type ExercisedEvent struct {
	result interface{}
	events []Event
}

type ArchivedEvent struct {
	TemplateId string `json:"templateId"`
	ContractId string `json:"contractId"`
}
