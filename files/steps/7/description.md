# Learning about file labels

All files and processes in a RHEL 9 system have an SELinux label. Many commands such as `ps`, `ls` and `id` come with
the `-Z` parameter to list SELinux labels.

1. Go ahead and inspect different directories now:

     ls -alZ /etc/httpd
     ls -alZ /var/www/html

2. Start httpd how:

     systemctl start httpd

3. List the label that the httpd process runs with. Compare that to the label of the httpd binary.
   The file is labeled with type `httpd_exec_t`. The process runs with type label `httpd_t`.

     ps aux -Z | grep httpd
     ls -alZ /usr/sbin/httpd

4. We will come back to httpd a bit later. For the time being, let's stop the service again:

     systemctl stop httpd
