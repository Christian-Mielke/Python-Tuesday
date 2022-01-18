# funktioniert noch nicht richtig
import numpy
numbers = [1,2,3,4,5]

def guessnumbers(numbers):
    return numpy.random.choice(numbers)
print("The number is: ", guessnumbers(numbers))

result = guessnumbers(numbers)
entry= int(input("Your Input is " ))

if entry == result:
    print("oh yes! The number is correct!")
elif entry < result:
    print("the number is too small")
elif entry > result:
    print("the number is too big")
