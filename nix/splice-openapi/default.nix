# Fetches Ledger API OpenAPI specification from the Splice repository on GitHub
# The Splice project (https://github.com/hyperledger-labs/splice) contains
# the Ledger API spec in canton/community/ledger/ledger-json-api/
#
# This derivation downloads a specific version (v0.5.1) and extracts
# the Ledger API OpenAPI specification for use in generating API client bindings

{ stdenv }:

stdenv.mkDerivation rec {
  pname = "splice-openapi-specs";
  version = "0.5.1";
  src = builtins.fetchTarball {
    url = "https://github.com/hyperledger-labs/splice/archive/${version}.tar.gz";
  };

  installPhase = ''
    mkdir -p "$out/ledger-api"

    # Extract Ledger API OpenAPI spec only
    if [ -f canton/community/ledger/ledger-json-api/src/test/resources/json-api-docs/openapi.yaml ]; then
      cp canton/community/ledger/ledger-json-api/src/test/resources/json-api-docs/openapi.yaml "$out/ledger-api/"
    else
      echo "Warning: Ledger API OpenAPI spec not found"
    fi
  '';
}


