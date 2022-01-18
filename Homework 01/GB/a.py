from random import randint

r = int(randint(0, 100))

a = int(0)

while True:
    guess = int(input('Rate eine Zahle zwischen 0 und 100:'))

    if guess == r:
        print(f'Richtig geraten. Du hast {a} Versuche gebraucht, um zu erraten, dass ich mir {r} gedacht habe.')
        break

    if guess < r:
        print('Die Zufallszahl ist größer als deine Eingabe.')
        a = a + 1

    if guess > r:
        print('Die Zufallszahl ist kleiner als deine Eingabe.')
        a = a + 1
