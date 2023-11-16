# Inspecting allowed ports

SELinux restricts ports that specific processes are allowed to listen on. In a later tutorial, we will make use of
this feature. As for booleans, it may not be trivial to understand which port label is uses by which process.
Therefore, for each component, you will have to read the component's documentation or follow instructions from tools
such as sealert.

1. List the list of all allowed listening ports:

     semanage port -l

2. List the list of allowed listening ports specifically for process httpd:

     semanage port -l | grep http_port_t
