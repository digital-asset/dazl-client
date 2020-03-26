package ledger

type Connection struct {
	config *config.Config
}

func Connect() (Connection, error) {
}

type CommandOpts struct {
	WorkflowId string
	CommandId string
}

func (c *Connection) Create(templateId string, payload interface{}, opts CommandOpts) (CreateEvent, error) {

}

func (c *Connection) Close() error {

}