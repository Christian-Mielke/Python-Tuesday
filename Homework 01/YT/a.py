import random

rdm_number = random.randint(0, 100)

while True:
    guess = int(input("Guess:"))

    if guess < rdm_number:
        print("zu niedrig")
    elif guess > rdm_number:
        print("zu groß")
    else:
        print("richtig")
        break
