# Inspecting /etc/selinux/config

1. Inspect file /etc/selinux/config:

    cat /etc/selinux/config

You can change parameter SELINUX to `SELINUX=permissive` to set SELinux to permissive mode, permanently. This is not
part of this exercise.

However, if you want to permanently disable SELinux, in RHEL 9, it is no longer possible to set SELinux=disabled in
/etc/selinux/config. Instead, you must add an argument to the kernel command line. More on this in the next step.

If you had to switch SELinux from targeted mode to Multi-Level Security (MLS), you would do that with variable
SELINUXTYPE in file /etc/selinux/config. This is out of scope of this tutorial.

Go ahead to the next step now with `tutorial next`.
