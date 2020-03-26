package cmd

import (
	"github.com/digital-asset/dazl/go/pkg/client"
	"github.com/spf13/cobra"
)

var lsCmd = &cobra.Command{
	Use:   "ls",
	Short: "Dump the state of a ledger",
	RunE: func(cmd *cobra.Command, args []string) error {
		return ls()
	},
}

func ls() error {
	c := client.Client{}
	if err := c.Connect("localhost:6865"); err != nil {
		return err
	}

	acs, err := c.Protocol.FetchACS(nil)
	if err != nil {
		return err
	}

	print(acs.Contracts)
	return nil
}
