# Privileged containers and spc_t

The fedora-minimal-privileged container was started with command:

     podman run -d --name fedora-minimal-privileged --privileged -it {{ fedora_container_image }} sleep infinity

1. Inspect the MountLabel and the ProcessLabel of the container:

     podman inspect fedora-minimal-privileged | grep -E 'MountLabel|ProcessLabel'

2. Inspect the SELinux file labels inside of the container:

     podman exec fedora-minimal-privileged ls -alZ

3. Inspect the SELinux process label of the container processes:

     podman exec fedora-minimal-privileged cat /proc/self/attr/current
