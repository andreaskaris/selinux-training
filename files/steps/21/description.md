# Creating a custom SELinux policy (2/4)

1. Generate a custom policy for the daemon:

     sepolicy generate --init /opt/tutorial/bin/open-messages

2. The above command by default generates permissive rules. Remove the permissive line from `open_messages.te` to
   enforce rules:

    sed -i 's/^permissive open_messages_t;$/#permissive open_messages_t;/' open_messages.te 

3. Rebuild the system policy with the new policy:

     ./open_messages.sh

4. Inspect the service file. You will see that it is now labeled as `open_messages_exec_t`:

     ls -Z /opt/tutorial/bin/open-messages

5. Restart the daemon and check its status, the service should fail:

     systemctl restart open-messages
     systemctl status open-messages
