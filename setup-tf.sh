#!/bin/bash

DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source "${DIR}/tf-helpers.sh"

CMD="${1}"
INSTANCE_COUNT="${2}"

if [ "${CMD}" == "apply" ]; then
    if ! [[ "${INSTANCE_COUNT}" =~ ^[1-9]$ ]]; then
        echo "Unsupported instance count: '${INSTANCE_COUNT}'. Supported values 1 - 9."
        exit 1
    fi
    mkdir -p "${TF_DATA_DIR}"
    ${TF} init
    ${TF} apply -auto-approve -var="instance_count=${INSTANCE_COUNT}"
    exit 0
fi

if [ "${CMD}" == "destroy" ]; then
    env
    ${TF} destroy -auto-approve -var='instance_count=9'
    exit 0
fi

if [ "${CMD}" == "show" ]; then
    ${TF} show
    exit 0
fi

echo "Unsupported command '${CMD}'."
exit 1
