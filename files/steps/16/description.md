# Configuring httpd to use a custom directory and port

To wrap things up, we will go through a concrete example in this and the following steps. We want to configure
httpd so that it serves documents from directory `/port3333`, over TCP port `3333`.

1. Create directory `/port3333`:

     mkdir /port3333

2. Create file `/port3333/index.html`:

     echo "Listening on port 3333" > /port3333/index.html

3. Configure an httpd virtual host:

     cat <<'EOF' > /etc/httpd/conf.d/port3333.conf
Listen 3333
<VirtualHost *:3333>
  DocumentRoot "/port3333"
  ServerName www.example.com


  <Directory "/port3333">
  	Options Indexes FollowSymLinks  
  	AllowOverride None
  	Require all granted
  	Order allow,deny
  	Allow from all
  </Directory>
</VirtualHost>
EOF

4. Set SELinux temporarily to permissive mode:

     setenforce 0

 5. Start httpd:

     systemctl start httpd

6. Make sure that httpd was started, is listening on port 3333 and that you can query localhost:3333:

     systemctl status httpd
     ss -lntp | grep 3333
     curl http://localhost:3333
