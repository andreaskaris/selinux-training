# Permanently changing file labels

1. If you want to permanently change file labels, meaning that they survive beyond a relabel action, you need to use
   the `semanage` tool. You will see that the fcontext database is quite large, with thousands of entries.
   Go ahead and list the label database now with:

     semanage fcontext -l | wc -l
     semanage fcontext -l | less

2. Create file /test/b/c:

     mkdir -p /test/b
     touch /test/b/c

3. Let's pretend that we want to give our custom `/test` directory the same labels as `/etc`. Go ahead and search for
   `/etc` in the fcontext database:

     semanage fcontext -l | grep '/etc' | grep etc_t

4. Now add a new entry to the database for `/test(/.*)?`. This means /test, /test/, or anything below /test/:

     semanage fcontext -a -t etc_t  '/test(/.*)?'

5. You can list all custom changes to fcontexts with:

     semanage fcontext -C -l

6. Use `restorecon` to relabel all files and directories under /test:

     restorecon -Rv /test

7. And list the SELinux labels of /test/b/c:

     ls -alZ /test/b/c
