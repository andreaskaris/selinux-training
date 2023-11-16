# Triggering and analyzing SELinux AVC denials by httpd

1. Stop httpd:

     systemctl stop httpd

2. Delete the audit log. Normally, you would not do this, but we want to reduce noise
   from previous operations.

     > /var/log/audit/audit.log

2. Set SELinux back to Enforcing:

     setenforce 1

3. Try starting httpd again - this will fail:

     systemctl start httpd

4. Inspect why this is failing:

     grep denied /var/log/audit/audit.log
     sealert -a /var/log/audit/audit.log

5. sealert proposed remediation instructions.
   We will use these in the next step.
