package protocol

type ContractId interface {
	Value() string
	TemplateId() string
}
