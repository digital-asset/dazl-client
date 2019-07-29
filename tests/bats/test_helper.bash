THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
VENVS_DIR=$(realpath "${THIS_DIR}"/../venvs)
DAZL_DIR="$(realpath "${THIS_DIR}"/../../python)"

# make sure a parent directory for virtual environments actually exists
mkdir -p "$VENVS_DIR"


# Create a virtual environment for the specified name.
function make_venv() {
    local venv_name=${1:-${BATS_TEST_NAME}}
    local venv=${VENVS_DIR}/${venv_name}
    rm -fr "${venv}"
    python3 -m venv "${venv}"

    echo ${venv}
}
