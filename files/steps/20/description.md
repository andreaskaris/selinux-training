# Creating a custom SELinux policy (1/4)

1. Inspect file /opt/tutorial/bin/open-messages and service file /etc/systemd/system/open-messages.service:

     cat /opt/tutorial/bin/open-messages
     cat /etc/systemd/system/open-messages.service

2. Start the open-messages service and make sure that it's running correctly:

     systemctl start open-messages
     systemctl status open-messages
   
3. Check the daemon's current SELinux label (it should run as unconfined_service_t):

     ps -fZ --pid $(pgrep -f open-messages)

4. /opt/tutorial/bin/open-messages copies the last log line from /var/log/messages to /tmp/out. Check that file:

     cat /tmp/out
