# Creating a custom SELinux policy (3/4)

1. Rerun the service, but with permissive rules:

     sed -i 's/^#permissive open_messages_t;$/permissive open_messages_t;/' open_messages.te
     ./open_messages.sh

2. Restart the service and make sure that it's running:

     systemctl restart open-messages
     systemctl status open-messages

3. Generate the list of rules needed to make the service run:

     ausearch -m AVC -ts recent | audit2allow -R

4. Copy the list of rules from the output and append them to open_messages.te:

     cat <<'EOF' >> open_messages.te
auth_read_passwd_file(open_messages_t)
corecmd_exec_bin(open_messages_t)
corecmd_mmap_bin_files(open_messages_t)
files_manage_generic_tmp_files(open_messages_t)
insights_client_filetrans_tmp(open_messages_t)
logging_read_generic_logs(open_messages_t)
sssd_read_public_files(open_messages_t)
sssd_search_lib(open_messages_t)
EOF

5. And enforce SELinux again for the policy:

     sed -i 's/^permissive open_messages_t;$/#permissive open_messages_t;/' open_messages.te
