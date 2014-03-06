#!/usr/bin/env python3

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

        with open(passwd_new, 'w') as pn:
            for line in passwd_lines:
                if line.split(':')[0] in keys or line.split(':')[3] != '12':
                    pn.write(line)
                    passwd_new_keys.append(line.split(':')[0])
                else:
                    passwd_log.write(line)

        passwd_log.close()

        with open(shadow_orig, 'r') as so:
            shadow_lines = so.readlines()

        shadow_log = open(shadow_log, 'w')

        with open(shadow_new, 'w') as sn:
            for line in shadow_lines:
                if line.split(':')[0] in passwd_new_keys:
                    sn.write(line)
                else:
                    shadow_log.write(line)

        shadow_log.close()

        passwd_names = [line.split(':')[0] for line in passwd_lines]

        missing = open(missing_log, 'w')

        for key in keys:
            if key not in passwd_names:
                missing.write(key + '\n')

        missing.close()

    except Exception as e:
        print(str(e))
        sys.exit()


if __name__ == "__main__":
    passwd_change()
