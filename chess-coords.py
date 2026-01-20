#!/usr/bin/env python3


import sys

coords = sys.argv[1]

spalte = coords[0]
zeile = int(coords[1])

spalten_nummer = ord(spalte) - ord('a') + 1

if (spalten_nummer + zeile) % 2 == 0:
    print("Schwarz")
else:
    print("Weiss")


