# SELinux MCS container labels

1. Inspect the fedora-minimal1 container's ProcessLabel. All processes inside the container will run with this label:

     podman inspect fedora-minimal1 | jq -r '.[0].ProcessLabel'

2. Inspect the fedora-minimal1 container's MountLabel. All files inside the container will be labeles with this label:

     podman inspect fedora-minimal1 | jq -r '.[0].MountLabel'

3. Inspect the fedora-minimal1 container's storage configuration:

     podman inspect fedora-minimal1 | jq '.[0].GraphDriver.Data'

4. Use the value that you found in MergedDir and list the directory contents:

     mergeddir=$(podman inspect fedora-minimal1 | jq -r '.[0].GraphDriver.Data.MergedDir')
     ls -alZ "${mergeddir}"

5. List information about the process running inside the container:

     ps aux -Z | grep "[s]leep infinity"
