#!/usr/bin/env bash
set -euo pipefail

function main() (
  set -euo pipefail

  # create directories
  local dirs=(
    /home/circleci/nix
    /home/circleci/nix/cache-keys
    /nix
  )

  echo 'Creating nix directories'
  mkdir -v "${dirs[@]}"

  # write checksum files
  echo 'Writing checksum files'
  git ls-files --error-unmatch --full-name -s "./nix" | tee "/home/circleci/nix/cache-keys/nix-checksums"

  # fix ownerships
  echo 'Fixing ownership'
  chown -vR circleci:circleci "${dirs[@]}"
)

# always run as root
if [ ${EUID} == 0 ]; then
  main
else
  sudo bash -c "$(declare -f main); main"
fi
