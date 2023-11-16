# Learning about file labels

An SELinux file label consists of 4 (or 5 with MCS) parts, e.g. `system_u:object_r:admin_home_t:s0`.
These parts are:
     user:role:type:mls_level

You can query seinfo to list all available SELinux users, roles and types.

1. List all available SELinux users with:

     seinfo -u

2. List all available SELinux roles with:

     seinfo -r

3. List all available SELinux types with:

     seinfo -t

For most use cases, you will only ever have to worry about the type label ending in `_t`.
