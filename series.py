#!/usr/bin/env python3

import sys

zahl = int(sys.argv[1])
lange = int(sys.argv[2])

for i in range(1, lange + 1):
    print(zahl * i, end=" ")



