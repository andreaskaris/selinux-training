# Disabling a custom SELinux policy

1. List the open_messages SELinux module:

     semodule --list-modules=full | grep open_messages

2. Disable the open_messages SELinux module (you can use -e to re-enable):

     semodule -d open_messages
   
3. List the module again:

     semodule --list-modules=full | grep open_messages

4. Run restorecon to restore the SELinux context of the binary and list the labels after the relabel:

     restorecon -Rv /opt/tutorial/bin/open-messages
     ls -Z /opt/tutorial/bin/open-messages

5. Re-enable the module with:

     semodule -e open_messages

6. And verify:

     semodule --list-modules=full | grep open_messages

7. Run restorecon to restore the SELinux context of the binary and list the labels after the relabel:

     restorecon -Rv /opt/tutorial/bin/open-messages
     ls -Z /opt/tutorial/bin/open-messages
