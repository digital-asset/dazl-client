package codegen

type codegenCommand struct {
	outputDir string
}

func SubCmd() *cobra.Command {

	cmd.Flags()(--output, -o)
}


func (c *codegenCommand) RunE(*cobra.Command, []string)  error {
	return c.
}