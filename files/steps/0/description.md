# Enabling / disabling SELinux temporarily

1. Run `getenforce`.

   getenforce shows the current enforcement state. It is either of:
     Enforcing: SELinux enforces its policies.
     Permissive: SELinux reports violations, but does not enforce its policies.
     Disabled: SELinux is completely disabled.

2. Run a script that makes a prohibited call:

   /usr/local/bin/cause-violation

   Observe the script's output. You should see the script failing.
   Check if there are any SELinux violations with:

   journalctl -t setroubleshoot

3. Set SELinux into permissive mode with:
   
   setenforce 0

4. Run the script again:

   /usr/local/bin/cause-violation

   Observe the script's output. What is happening now?
   Check if there are any SELinux violations with:

   journalctl -t setroubleshoot
