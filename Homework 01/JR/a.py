import sys
import random

RandomNumber: int = (random.randint(0, 100))

MyGuess: int = 101
CountofGuess: int = 0

print("Sie müssen eine Zahl zwischen 1 und 100 raten")

while MyGuess != RandomNumber:
    MyGuess = int(input("Geben Sie ihre Zahl ein: "))
    CountofGuess += 1

    if MyGuess > RandomNumber:
        print("Die zu ratende Zahl ist kleiner!")
    else:
        print("Die zu ratende Zahl ist größer!")

else:
    print(f"Sie haben die Zahl erraten mit {CountofGuess}! Versuchen")
