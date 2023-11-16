# Allowing httpd to listen on port 3333

In the previous step, we ran sealert to analyze why SELinux denied httpd to run.

1. Have a close look at the output of sealert:

     sealert -a /var/log/audit/audit.log
   
   sealert proposes various remediation measures, and it lists a confidence value indicating
   how sure the tooling is that the measure will solve the issue.

2. In this case, sealert suggests with a confidence > 90 percent that you should run
   `semanage port -a -t PORT_TYPE -p tcp 3333`. It also suggests the values for PORT_TYPE,
   among which is `http_port_t`. List the values for `http_port_t`:

     semanage port -l | grep ^http_port_t

3. Add label `http_port_t` to TCP port 3333:

     semanage port -a -t http_port_t -p tcp 3333

4. List the values for `http_port_t` again:

     semanage port -l | grep ^http_port_t

5. Restart httpd:

     systemctl restart httpd

6. Verify that httpd is running. Yet, you cannot retrieve your document from localhost:3333.
   Instead, httpd presents the default Welcome page, meaning that it could not access index.html.

     systemctl status httpd
     curl http://localhost:3333
