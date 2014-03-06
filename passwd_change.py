#!/usr/bin/env python3

import os
import errno
import sys


def passwd_change(keys_file='keys.txt', passwd_orig='passwd',
                  passwd_new='passwd_new', passwd_log='passwd.log',
                  shadow_orig='shadow', shadow_new='shadow_new',
                  shadow_log='shadow.log', missing_log='missing.log'):
    try:
        with open(keys_file, 'r') as k:
            keys = k.readlines()
            keys = [key.strip().split('@')[0] for key in keys]
            keys = [key for key in keys if key != '']

        with open(passwd_orig, 'r') as po:
            passwd_lines = po.readlines()

        passwd_log = open(passwd_log, 'w')
        passwd_new_keys = []

        passwd_new_count = 0
        passwd_del_count = 0
        with open(passwd_new, 'w') as pn:
            for line in passwd_lines:
                if line.split(':')[0] in keys or line.split(':')[3] != '12':
                    pn.write(line)
                    passwd_new_keys.append(line.split(':')[0])
                    passwd_new_count += 1
                else:
                    passwd_log.write(line)
                    passwd_del_count += 1

        passwd_log.close()

        print('New passwd file have ' + str(passwd_new_count) + ' lines.')
        print('Has been deleted ' + str(passwd_del_count) + ' lines.\n')

        with open(shadow_orig, 'r') as so:
            shadow_lines = so.readlines()

        shadow_log = open(shadow_log, 'w')

        shadow_new_count = 0
        shadow_del_count = 0
        with open(shadow_new, 'w') as sn:
            for line in shadow_lines:
                if line.split(':')[0] in passwd_new_keys:
                    sn.write(line)
                    shadow_new_count += 1
                else:
                    shadow_log.write(line)
                    shadow_del_count += 1

        shadow_log.close()

        print('New shadow file have ' + str(shadow_new_count) + ' lines.')
        print('Has been deleted ' + str(shadow_del_count) + ' lines.\n')

        passwd_names = [line.split(':')[0] for line in passwd_lines]

        missing = open(missing_log, 'w')

        missing_count = 0
        for key in keys:
            if key not in passwd_names:
                missing.write(key + '\n')
                missing_count += 1

        missing.close()

        print('There are ' + str(missing_count) +
              ' missing names from ' + keys_file)

    except Exception as e:
        print(str(e))
        sys.exit()


def mails_delete(passwd_log='passwd.log', maildir_path='/var/spool/mail/'):
    with open(passwd_log, 'r') as pl:
        names_for_delete = [line.split(':')[0] for line in pl.readlines()]

    deleted_count = 0
    for name in names_for_delete:
        try:
            path = maildir_path + name
            if path != maildir_path:
                os.remove(maildir_path + name)
                deleted_count += 1
        except OSError as e:
            if e.errno != errno.ENOENT:
                raise

    print('In directory ' + maildir_path + ' has been deleted ' +
          str(deleted_count) + ' files.')


if __name__ == "__main__":
    passwd_change()
    mails_delete()
