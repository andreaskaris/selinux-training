# Disabling SELinux permanently

In order to disable SELinux permanently, you must append `selinux=0` to the kernel command line and reboot your
system (https://access.redhat.com/solutions/3176).
Note: Contrary to RHEL 8, in RHEL 9 it is no longer possible to set SELinux=disabled in /etc/selinux/config.

1. Disable SELinux permanently:

     grubby --update-kernel ALL --args selinux=0

2. Reboot your system:

     reboot

3. Wait for your system to reboot.

4. Check the SELinux status as well as /proc/cmdline:

     sestatus
     cat /proc/cmdline

 5. Then, run the `cause-violation` service again:

     systemctl start cause-violation

6. Check the journal and /var/log/audit/audit.log. SELinux is disabled, and nothing should be logged:

     journalctl -t setroubleshoot --boot
