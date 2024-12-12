package api_test

import (
	"testing"

	_ "github.com/digital-asset/dazl-client/v8/go/api/com/daml/daml_lf_1_16"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/daml/daml_lf_2_1"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v1"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v1/admin"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v1/testing"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2/admin"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2/testing"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/connection/v30"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/crypto/admin/v0"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/crypto/v0"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/admin/v0"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/admin/v0sequencerinitializationservice"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/admin/v1"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/api/v0"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/health/admin/v0"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/participant/admin/v0"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/participant/protocol/v0"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v0"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v1"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v2"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v3"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v4"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/pruning/admin/v0"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/time/admin/v0"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/topology/admin/v0"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/traffic/v0"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/v0"
	_ "github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/version"
)

func Test(_ *testing.T) {}
