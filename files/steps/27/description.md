# Demonstrating MCS isolation

1. Export the mergeddir of fedora-minimal2:

     export mergeddir=$(podman inspect fedora-minimal2 | jq -r '.[0].GraphDriver.Data.MergedDir')

2. Test that you can write a file there, and that it's visible inside fedora-minimal2:

     touch "${mergeddir}/created_by_root"
     podman exec fedora-minimal2 ls -alZ /created_by_root

3. Run a process with the MCS label of fedora-minimal1:

     runcon $(podman inspect fedora-minimal1 | jq -r '.[0].ProcessLabel') /bin/bash

4. List the merged directory of fedora-minimal2 and try to create a file in there. These attempts will fail:

     echo "${mergeddir}"
     ls -al "${mergeddir}"
     touch "${mergeddir}/created_by_other_container"
     exit

5. Run a process with the MCS label of fedora-minimal2:

     runcon $(podman inspect fedora-minimal2 | jq -r '.[0].ProcessLabel') /bin/bash

6. List the merged directory of fedora-minimal2 and try to create a file in there. These attempts will succeed:

     echo "${mergeddir}"
     ls -al "${mergeddir}"
     touch "${mergeddir}/created_by_same_container"
     exit
     podman exec fedora-minimal2 ls -alZ /created_by_same_container
