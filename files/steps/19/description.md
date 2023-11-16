# Allowing httpd to serve files from /port3333

In the previous step, we allowed httpd to listen on port 3333. However, we
still cannot access /port3333/index.html.

1. Look at the SELinux logs again. For a change, let's look at the journal this time.

     journalctl -t setroubleshoot
   
   Scroll to the very bottom of the journal. You will see that setroubleshoot gives
   a suggestion for modifying the fcontext of file /port3333/index.html.

2. We know that httpd normally serves files from /var/www/html, so let's inspect that
   directory's labels and let's compare the labels to /port3333's labels:

     ls -alZ /var/www/html
     ls -alZ /port3333

3. The directory is labeled with `httpd_sys_content_t`. Let's list the fcontext entry for
   /var/www/:

     semanage fcontext -l | grep httpd_sys_content_t | grep ^/var/www

4. Let's add the correct permanent label to /port3333, and then use restorecon to make the
   label effective:

     semanage fcontext -a -t httpd_sys_content_t '/port3333(/.*)?'
     restorecon -R -v /port3333

5. List the labels in /port3333:

     ls -alZ /port3333

6. Restart httpd:

     systemctl restart httpd

7. And verify that you can retrieve index.html:

     curl http://localhost:3333
