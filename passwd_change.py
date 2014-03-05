#!/usr/bin/env python3

import sys

_args = sys.argv

if __name__ == "__main__":
    if len(_args) == 8:
        keys_file = _args[1]
        passwd_orig = _args[2]
        passwd_new = _args[3]
        passwd_log = _args[4]
        shadow_orig = _args[5]
        shadow_new = _args[6]
        shadow_log = _args[7]

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
                    if line.split(':')[0] in keys or \
                       line.split(':')[3] != '12':
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

        except Exception as e:
            print(str(e))
            sys.exit()
    else:
        print('==================================================')
        print('python passwd_change.py keys passwd passwd_new passwd_log' +
              ' shadow shadow_new shadow_log')
        print('==================================================')
