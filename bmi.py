#!/usr/bin/env python3

groesse = float(input("Körpergrösse in m: "))
gewicht = float(input("Körpergewicht in kg: "))

bmi = gewicht / (groesse ** 2)

print(f"Dein BMI: {bmi: .2f}")
