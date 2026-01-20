#!/usr/bin/env python3

import sys

operator = sys.argv[1]
zahlen = [int(x) for x in sys.argv[2:]]

resultat = zahlen[0]

if operator == "+":
    for z in zahlen[1:]:
        resultat += z

elif operator == "-":
    for z in zahlen[1:]:
        resultat -= z

elif operator == "x":
    for z in zahlen[1:]:
        resultat *= z

elif operator == ":":
    for z in zahlen[1:]:
        resultat //= z

elif operator == "^":
    for z in zahlen[1:]:
        resultat **= z

print(resultat)
