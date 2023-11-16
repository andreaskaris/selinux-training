# Identifying SELinux denials

There is a myriad of ways of identifying SELinux denials. We already saw that in RHEL 9 (although not in RHEL 8),
you can see denials in the system journal.

Go ahead and explore some of the different ways to see why a process was denied an action by SELinux.

1. The journal:

     journalctl -t setroubleshoot

2. The audit log:

     grep denied /var/log/audit/audit.log

Data in the audit log does unfortunately not appear in the most human friendly format. Therefore, tools exist to
make parsing the log easier. These tools also give recommendations for remediation actions.

3. ausearch:

     ausearch -m AVC,USER_AVC,SELINUX_ERR,USER_SELINUX_ERR -ts recent
     ausearch -m AVC,USER_AVC,SELINUX_ERR,USER_SELINUX_ERR -ts today

4. sealert:

     sealert -l "*"
     sealert -a /var/log/audit/audit.log
