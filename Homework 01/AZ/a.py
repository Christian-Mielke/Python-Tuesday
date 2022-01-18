import random
number = random.randint(1,10)
print(number)

entry = int(input("Your input is:"))
if entry == number:
    print("oh yes! The number is correct!")
elif entry < number:
    print("the number is too small, try again!")
elif entry > number:
    print("the number is too big, try again!")
