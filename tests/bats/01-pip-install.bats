load test_helper


@test "pip install (wheel)" {
    # Ensure tht the dazl wheel can be installed.
    local dazl_version=$(cat ../VERSION)
    local venv=$(make_venv)
    run "${venv}/bin/pip3" install "${DAZL_DIR}/dist/dazl-${dazl_version}-py3-none-any.whl"

    [ "$status" -eq 0 ]
    [ $("${venv}"/bin/dazl version) == ${dazl_version} ]
}


@test "pip install (sdist)" {
    # Ensure tht the dazl wheel can be installed.
    local dazl_version=$(cat ../VERSION)
    local venv=$(make_venv)
    run "${venv}/bin/pip3" install "${DAZL_DIR}/dist/dazl-${dazl_version}.tar.gz"

    [ "$status" -eq 0 ]
    [ $("${venv}"/bin/dazl version) == ${dazl_version} ]
}


@test "pip install --editable" {
    # Ensure that dazl can be installed in editable mode. Useful for developers
    # coding on dazl itself while using other virtualenvs as a "test case".
    local dazl_version=$(cat ../VERSION)
    local venv=$(make_venv)
    run "${venv}/bin/pip3" install --editable "${DAZL_DIR}"

    [ "$status" -eq 0 ]
    [ $("${venv}"/bin/dazl version) == ${dazl_version} ]
}
