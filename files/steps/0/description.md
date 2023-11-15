# Causing an SElinux violation

1. Run `getenforce`:

     getenforce

   getenforce shows the current enforcement state. It is either of:
     Enforcing: SELinux enforces its policies.
     Permissive: SELinux reports violations, but does not enforce its policies.
     Disabled: SELinux is completely disabled.

2. Run a systemd service that makes a prohibited call:

     systemctl start cause-violation

   Observe the service's status:

     systemctl status cause-violation

   You should see the service failing.
   Check if there are any SELinux violations with:

     journalctl -t setroubleshoot
