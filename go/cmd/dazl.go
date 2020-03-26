package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
	"os"
)

var (
	rootCmd = &cobra.Command{
		Use:   "dazl",
		Short: "Interact with your DAML ledger",
	}
)

func RunCommandLine() {
	rootCmd.AddCommand(metadataCmd)
	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
