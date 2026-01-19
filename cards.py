#!/usr/bin/env python3

import sys

karte = sys.argv[1]

farbe = karte[0]
wert = karte[1]

match farbe:
    case "C":
        farbe_text = "Clubs"
    case "D":
        farbe_text = "Diamonds"
    case "H":
        farbe_text = "Hearths"
    case "S":
        farbe_text = "Spades"

match wert:
    case "A":
        wert_text = "Ace"
    case "X":
        wert_text = "10"
    case "J":
        wert_text = "Jack"
    case "Q":
        wert_text = "Queen"
    case "K":
        wert_text = "King"
    case _:
        wert_text = wert

print(f"{farbe_text} {wert_text}")
