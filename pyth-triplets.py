#!/usr/bin/env python3

import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a**2 + b**2 == c**2:
    print(f"{a}, {b} und {c} sind ein pythagörisches Triplet")
else:
    print(F"{a}, {b} und {c} sind kein pythagorisches triplet")

