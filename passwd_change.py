#!/usr/bin/env python3

import sys


_args = sys.argv

if __name__ == "__main__":
    if len(_args) == 4:
        keys_file = _args[1]
        target_file = _args[2]
        result_file = _args[3]

        with open(keys_file, 'r') as k:
            keys = k.readlines()
            keys = [key.strip() for key in keys]
            keys = [key for key in keys if key != '']
        with open(target_file, 'r') as t:
            target_lines = t.readlines()

        with open(result_file, 'w') as r:
            for line in target_lines:
                if line.split(':')[0] in keys:
                    r.write(line)
    else:
        print('./passwd_change.py keys_file.txt passwd_file result_file')

