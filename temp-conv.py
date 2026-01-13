#!/usr/bin/env python3

import sys

value = float(sys.argv[1])
unit = sys.argv[2]

if unit == 'F' or unit == 'f':
    c = (value - 32) * 5 / 9
    print(f"{value:.1f}°F = {c:.1f}°C")

elif unit == 'C' or unit == 'c':
    f = value * 9 / 5 + 32
    print(f"{value:.1f}°C = {f:.1f}°F")

