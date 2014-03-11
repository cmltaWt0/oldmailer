This application intended for a rare tasks - removing unused mail records according to keys.txt file (format: name or name@mail.com in separate line).
At first removed unnecessary lines from passwd file and then from shadow file.
Then removed user files (pop file format) from /var/spool/mail directory (by default) according to passwd.log.
