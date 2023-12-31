// Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

package client

import (
	"context"
	"log"

	"google.golang.org/grpc"

	"github.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1"
)

type LedgerId string

// GetLedgerId attempts to connect to a ledger at the specified host:port and fetch the ledger ID.
func GetLedgerId(ctx context.Context, target string) (LedgerId, error) {
	conn, err := grpc.DialContext(ctx, target, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		return "", err
	}

	client := v1.NewLedgerIdentityServiceClient(conn)
	response, err := client.GetLedgerIdentity(ctx, &v1.GetLedgerIdentityRequest{})
	if err != nil {
		return "", err
	}

	log.Printf("Successful ping; the ledger ID is %s", response.LedgerId)
	return LedgerId(response.LedgerId), nil
}
