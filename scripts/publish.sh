#!/usr/bin/env bash
# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

root_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )"/.. >/dev/null 2>&1 && pwd )"
root_version=$(cat "${root_dir}/VERSION")
py_version=$(python3 -c "import configparser; config = configparser.ConfigParser(); config.read('${root_dir}/pyproject.toml'); print(config['tool.poetry']['version'][1:-1])")
git_sha="$(git rev-parse HEAD)"

if ! command -v gh &>/dev/null ; then
    echo "GitHub CLI is required!"
    echo "https://cli.github.com/"
    exit 1
fi

echo $root_dir/VERSION
if [ -z "{root_version}" ]; then
    echo "Could not determine our version!"
    exit 1
fi

if [ "${root_version}" != "${py_version}" ]; then
    echo "The versions in the repo do not agree!"
    echo "    VERSION: ${root_version}"
    echo "    pyproject.toml: ${py_version}"
    exit 1
fi

if [ -z "${git_sha}" ]; then
    echo "Could not determine the SHA of the current commit!"
    exit 1
fi

# version strings like "1.0.0" are treated as normal releases;
# any version string that contains extra letters (such as "1.0.0b1")
# is treated as a prerelease version
gh_flags="$(python3 -c "import re; print('' if re.match("^\d+\.\d+\.\d+$") else '--prerelease')")"


echo "Version: ${root_version}"
echo "Git SHA: ${git_sha}"
echo "Files: $@"
echo "Flags: ${gh_flags}"

gh release create "v${root_version}" ${gh_flags} -t "dazl v${root_version}" $@
poetry publish
