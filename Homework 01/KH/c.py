import random

print('Willkommen zum Zahlenratespiel! Ich habe mir eine Zahl zwischen 0 und 100 ausgedacht.')
number: int = random.randint(0, 100)
attempts: list = []


def ask_for_guess(previous_attempts: list) -> int:
    user_input = int(input('Rate meine Zahl!'))
    previous_attempts += [user_input]

    return user_input


guess: int = ask_for_guess(attempts)
while number != guess:
    print(f'Guter Tipp! Aber meine Zahl ist {"größer" if number > guess else "kleiner"}...')
    guess = ask_for_guess(attempts)

print(f'Sehr gut! Meine Zahl war {number}. Du hast {len(attempts)} Versuch(e) gebraucht: {attempts}')
