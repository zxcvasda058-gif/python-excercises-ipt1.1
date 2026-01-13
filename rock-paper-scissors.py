#!/usr/bin/env python3

import sys
import random

player = sys.argv[1]

computer_num = random.randint(0, 2)

if computer_num == 0:
    computer = "rock"
elif computer_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"Spieler: {player.capitalize()}")
print(f"Computer: {computer.capitalize()}")

if player == computer:
    print("Unentschieden")

elif (player == "scissors" and computer == "paper") or \
     (player == "paper" and computer == "rock") or \
     (player == "rock" and computer == "scissors"):
    print("Der Spieler gewinnt")

else:
    print("Der Computer gewinnt")

