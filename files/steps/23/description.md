# Creating a custom SELinux policy (4/4)

1. Rebuild the system policy with the new policy:

    ./open_messages.sh

2. Empty /var/log/audit/audit.log:

     > /var/log/audit/audit.log

3. Start the open-messages service and make sure that it's running correctly:

     systemctl restart open-messages
     systemctl status open-messages
   
4. Inspect the service file. You will see that it is now labeled as `open_messages_exec_t`:

     ps -fZ --pid $(pgrep -f open-messages)

5. Check that there are no SELinux denied messages for open-messages:

     grep denied /var/log/audit/audit.log | grep open_messages_t
