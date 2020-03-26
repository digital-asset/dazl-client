package cmd

import (
	"fmt"
	"github.com/digital-asset/dazl/go/pkg/client"
	"github.com/spf13/cobra"
)

var (
	metadataCmd = &cobra.Command{
		Use:   "metadata",
		Short: "Get package information from the ledger",
		RunE: func(cmd *cobra.Command, args []string) error {
			return showMetadata()
		},
	}
)

func showMetadata() error {
	c := client.Client{}
	if err := c.Connect("localhost:6865"); err != nil {
		return err
	}

	packageIds, err := c.Protocol.FetchPackageIds()
	if err != nil {
		return err
	}

	fmt.Println(packageIds)
	return nil
}
