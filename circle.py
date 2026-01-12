#!/usr/bin/env python3

import sys
import math

r = float(sys.argv[1])

A = math.pi * r ** 2
U = 2 * math.pi * r

print(f"A={A:.2f}")
print(f"U={U:.2f}")
