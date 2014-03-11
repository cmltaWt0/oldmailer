This application intended for a rare tasks - removing unused mail records according to active records in keys.txt file (format: name or name@mail.com in separate lines).

Keys.txt - file contain records that need to survive.

** At first created new passwd and shadow files without unnecessary lines.

** Then removed user files (pop file format) from /var/spool/mail directory (by default) according to passwd.log.
