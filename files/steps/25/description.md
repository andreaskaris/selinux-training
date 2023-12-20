# Removing a custom SELinux policy

1. List the open_messages SELinux module:

     semodule --list-modules=full | grep open_messages

2. Remove the open_messages SELinux module:

     semodule -r open_messages

3. List the module again:

     semodule --list-modules=full | grep open_messages

4. Run restorecon to restore the SELinux context of the binary and list the labels after the relabel:

     restorecon -Rv /opt/tutorial/bin/open-messages
     ls -Z /opt/tutorial/bin/open-messages
