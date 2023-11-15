# Disabling SELinux temporarily

1. Set SELinux into permissive mode with:
   
     setenforce 0

2. Check the current state of SELinux. It is now in permissive mode. You cannot disable SELinux from user space in
   RHEL 9.

     getenforce
     sestatus

3. Run the service again:

     systemctl start cause-violation

   Observe the service's status. What is happening now?

     systemctl status cause-violation

   Check if there are any SELinux violations in /var/log/audit/audit.log, and pay close attention to the last part
   of each line (`permissive=0` vs `permissive=1`):

     grep -i denied /var/log/audit/audit.log

   You will see the same SELinux violation, but this time it is not being enforced, it is only being reported.
