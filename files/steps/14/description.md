# Setting SELinux permanently

1. You can enable SELinux booleans persistently with 2 different commands. In order to switch on `httpd_use_nfs`
   permanently, use either of:

     semanage boolean -m --on httpd_use_nfs
     setsebool -P httpd_use_nfs on

2. Then, reboot your system:

     reboot

3. After reboot, query the SELinux boolean's state:

     semanage boolean -l | grep httpd_use_nfs
