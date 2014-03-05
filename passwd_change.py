#!/usr/bin/env python3

import sys

_args = sys.argv

if __name__ == "__main__":
    if len(_args) == 5:
        keys_file = _args[1]
        target_file = _args[2]
        result_file = _args[3]
        log_file = _args[4]

        try:
            with open(keys_file, 'r') as k:
                keys = k.readlines()
                keys = [key.strip().split('@')[0] for key in keys]
                keys = [key for key in keys if key != '']
            with open(target_file, 'r') as t:
                target_lines = t.readlines()

            log = open(log_file, 'w')

            with open(result_file, 'w') as r:
                for line in target_lines:
                    if line.split(':')[0] in keys or \
                       line.split(':')[3] != '12':
                        r.write(line)
                    else:
                        log.write(line)

            log.close()

        except Exception as e:
            print(str(e))
            sys.exit()
    else:
        print('==================================================')
        print('python passwd_change.py keys passwd passwd_new log')
        print('==================================================')
