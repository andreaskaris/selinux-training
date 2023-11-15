# Enabling / disabling SELinux temporarily

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

3. Set SELinux into permissive mode with:
   
     setenforce 0

4. Check the current state of SELinux. It is now in permissive mode. You cannot disable SELinux from user space in
   RHEL 9.

     getenforce

5. Run the service again:

     systemctl start cause-violation

   Observe the service's status. What is happening now?

     systemctl status cause-violation

   Check if there are any SELinux violations with:

     journalctl -t setroubleshoot

   You will see the same SELinux violation, but this time it is not being enforced, it is only being reported.

6. Enforce SELinux again:

     setenforce 1
