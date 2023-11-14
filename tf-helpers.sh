#!/bin/bash

export TF_DATA_DIR=~/.tfdata
export PRIVATE_KEY_LOCATION=~/.ssh/aws_priv

get_tf_binary() {
  if command -v tofu &> /dev/null; then
      echo -n "tofu"
      return
  fi
  
  if command -v terraform &> /dev/null; then
      echo -n "terraform"
      return
  fi
  
  echo -n "unsupported"
}

export TF=$(get_tf_binary)
if [ "${TF}" == "unsupported" ] || [ "${TF}" == "" ]; then
    echo "Could not determine TF binary, exiting."
    exit 1
fi
