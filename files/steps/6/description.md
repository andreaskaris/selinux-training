# Enabling SELinux permanently

In order to enable SELinux permanently, you must remove `selinux=0` from the kernel command line and reboot your
system (https://access.redhat.com/solutions/3176).
Note: Contrary to RHEL 8, in RHEL 9 it is no longer possible to set SELinux=disabled in /etc/selinux/config.

1. Enable SELinux permanently:

     grubby --update-kernel ALL --remove-args selinux

2. Reboot your system:

     reboot

3. Wait for your system to reboot, then run the `cause-violation` service again:

     systemctl start cause-violation

4. Check the journal and /var/log/audit/audit.log. SELinux is enabled, and errors should be logged again:

     journalctl -t setroubleshoot --boot
     less /var/log/audit/audit.log
