# Changing file labels temporarily

1. Create directory /test with file /test/a:

     mkdir /test
     touch /test/a

2. Inspect the current SELinux labels:

     ls -alZ /test

3. Change the SELinux type temporarily, recursively for the entire folder:

     chcon -R -t tmp_t /test

4. Inspect the current SELinux labels:

     ls -alZ /test
