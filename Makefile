INSTANCE_COUNT ?= 1

.PHONY: apply
apply: # Install with TF (provide INSTANCE_COUNT=... to specify the number of instances, default 1)
	./setup-tf.sh apply $(INSTANCE_COUNT)

.PHONY: block-egress
block-egress: # Install with TF with egress blocked(provide INSTANCE_COUNT=... to specify the number of instances, default 1)
	./setup-tf.sh block-egress $(INSTANCE_COUNT)

.PHONY: setup-ansible
setup-ansible: # Configure ansible.
	./setup-ansible.sh

.PHONY: run-ansible
run-ansible: # Run ansible playbook.
	ansible-playbook playbook.yml

.PHONY: all
all: apply setup-ansible run-ansible block-egress # Deploy and configure ansible.

.PHONY: destroy
destroy: # Destroy environment.
	./setup-tf.sh destroy

.PHONY: show
show: # Show TF state.
	./setup-tf.sh show

# Curtesy of https://dwmkerr.com/makefile-help-command/
.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done
