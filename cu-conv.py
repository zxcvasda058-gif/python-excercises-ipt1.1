#!/usr/bin/env python3

import sys

amount = float(sys.argv[1])
currency = sys.argv[2]

if currency == "USD":
    chf = amount * 0.80
elif currency == "EUR":
    chf = amount * 0.93
elif currency == "GBP":
    chf = amount * 1.08

print(f"CHF {chf:.2f}")
