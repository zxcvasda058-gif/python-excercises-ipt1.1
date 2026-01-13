#!/usr/bin/env python3

import sys

letter = sys.argv[1]

match letter:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print(f"'{letter}' ist ein Vokal")

    case 'b' | 'c' | 'd' | 'f' | 'g' | 'h' | 'j' | 'k' | 'l' | 'm' | \
         'n' | 'p' | 'q' | 'r' | 's' | 't' | 'v' | 'w' | 'x' | 'y' | 'z':
        print(f"'{letter}' ist ein Konsonant")

    case _:
        print(f"'{letter}' ist unbekannt")
