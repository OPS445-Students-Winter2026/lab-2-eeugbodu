#!/usr/bin/env python3
# Author: ELvis Ugbodu
# Author ID: 153259239
# Date Created: 2026/01/27

import sys


if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
