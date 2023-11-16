# Restoring default SELinux labels

1. Temporary changes to file labels persist across reboots. However, they to not survive an SELinux relabel.
   Let's go ahead and tell the OS that we want to relabel the entire file system upon reboot:

     touch /.autorelabel

   NOTE: You could also use command `fixfiles -F onboot` which is a wrapper around the aforementioned action.

2. Reboot the system now. The system will relabel all files, so it can take a while for it to come back online.

     reboot

3. Once the system is back up, inspect directory /test. The labels should be changed back to the default:

     ls -alZ /test

4. It is also possible to restore file labels for specific files, or recursively for directories. First, let's
   add the tmp_t label again:

     chcon -R -t tmp_t /test

5. Inspect the current SELinux labels:

     ls -alZ /test

6. Now, use the `restorecon` command to restore the default file labels:

     restorecon -v -R /test

7. Inspect the current SELinux labels:

     ls -alZ /test
