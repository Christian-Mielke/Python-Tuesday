import random

print('Willkommen zum Zahlenratespiel! Ich habe mir eine Zahl zwischen 0 und 100 ausgedacht.')
number: int = random.randint(0, 100)
guess: int = -1

while number != guess:
    guess = int(input('Rate meine Zahl!'))

    if number != guess:
        print(f'Guter Tipp! Aber meine Zahl ist {"größer" if number > guess else "kleiner"}...')

print(f'Sehr gut! Meine Zahl war {number}.')
