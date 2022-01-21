print('Welcome! Please think of a number from 0 to 100 and do not tell me!')
input('Hit Enter when you are ready!')

min: int = 0
max: int = 101
guess: int
user_input: str = ''

while user_input != 'c':
    guess = int((min + max) / 2)
    print(f"My guess is that your number is: {guess}")

    user_input = input("Am I (c)orrect? Is your number (l)arger or (s)maller? Please type 'c', 'l', or 's' and hit Enter!")
    if user_input == 'l':
        min = guess
    elif user_input == 's':
        max = guess

print(f"That's it! Your number was {guess}.")
