#!/usr/bin/env python3

import sys

AHV = 0.087
IV  = 0.014
EO  = 0.005
ALV = 0.011
NBU = 0.0073
PK  = 0.0089


brutto = float(sys.argv[1])


ahv = brutto * AHV
iv  = brutto * IV
eo  = brutto * EO
alv = brutto * ALV
nbu = brutto * NBU
pk  = brutto * PK


netto = brutto - (ahv + iv + eo + alv + nbu + pk)


print(f"Bruttolohn     {brutto:8.2f}")
print(f"AHV:           {-ahv:8.2f}")
print(f"IV:            {-iv:8.2f}")
print(f"EO:            {-eo:8.2f}")
print(f"ALV:           {-alv:8.2f}")
print(f"NBU:           {-nbu:8.2f}")
print(f"PK:            {-pk:8.2f}")
print(f"Nettolohn:     {netto:8.2f}")
