# Setting SELinux booleans temporarily

1. Temporarily allow httpd to serve files from NFS:

    setsebool httpd_use_nfs on
    getsebool httpd_use_nfs

3. As mentioned earlier, `getsebool` will not show you the persistent state of booleans, which may be different.
   Use `semanage boolean` to query persistent state. You will see that `httpd_use_nfs` is currently in state
   `(on   ,  off)`, meaning it is temporarily enabled, but persistently disabled:

     semanage boolean -l | grep httpd_use_nfs

4. Reboot your system now:

     reboot

5. After the reboot, query the boolean again - you will see that it switched back to off:

     getsebool httpd_use_nfs
     semanage boolean -l | grep httpd_use_nfs
