# Inspecting SELinux booleans

SELinux booleans are simple on/off switches. They allow you to customize your system's behavior without having to
resort to writing custom SELinux policies. SELinux booleans are only meaningful in the context of specific SELinux
policies. Therefore, while you can list all existing SELinux booleans, there is unfortunately no comprehensive
description for what all of them do, although most of them do have self-explaining names.

1. Use getsebool to query the current effective state of booleans:

     getsebool -a
     getsebool httpd_use_nfs

2. You can query the permanent state of SELinux booleans with semanage. More on this later:

     semanage boolean -l

3. You can also query the state directly from the sys filesystem:

     cat /sys/fs/selinux/booleans/httpd_use_nfs
