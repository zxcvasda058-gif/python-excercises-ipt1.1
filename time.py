#!/usr/bin/env python3

import sys

s = int(sys.argv[1])

stunden = s // 3600
rest = s % 3600
minuten = rest // 60
sekunden = rest % 60

print(f"{stunden}h{minuten}m{sekunden}s")
