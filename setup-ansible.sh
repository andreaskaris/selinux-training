#!/bin/bash

set -eu

DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source "${DIR}/tf-helpers.sh"

ANSIBLE_CFG="${DIR}/ansible.cfg"
ANSIBLE_INVENTORY="${DIR}/inventory"

echo "Exporting private key and storing it in ${PRIVATE_KEY_LOCATION}"
${TF} output -raw private_key > "${PRIVATE_KEY_LOCATION}"
chmod 600 "${PRIVATE_KEY_LOCATION}"

echo "Checking if ${ANSIBLE_CFG} exists"
if ! [ -f "${ANSIBLE_CFG}" ]; then
  echo "Creating new ${ANSIBLE_CFG}"
  cat <<EOF > "${ANSIBLE_CFG}"
[defaults]
inventory=inventory

become_user=root
remote_user=ec2-user
private_key_file=${PRIVATE_KEY_LOCATION}
host_key_checking = False
EOF
fi

echo "Creating ansible inventory at ${ANSIBLE_INVENTORY}"
echo "[virtual_machines]" > "${ANSIBLE_INVENTORY}"
terraform show -json | \
    jq -r '.values.root_module.resources[] | select(.type=="aws_instance") | .values.public_ip' >> inventory

echo "Checking VM reachability"
i=0
while ! ansible -m ping virtual_machines; do
  i=$((i+1))
  if [ ${i} -ge 10 ]; then
    echo "Reachability check failed too many times, aborting."
  fi
  echo "Reachability check failed, sleeping and trying again."
  sleep 30
done
