import random
from random import randint
rand_number = randint(1, 100)#Zufallszahl aus Pythonfunktion guess=int

#Test:
#print (rand_number)
#Test:
#print (guess)

while rand_number!=guess:
    guess=int (input("Bitte gib eine Zahl zwischen 0 und 100 ein! "))
    if rand_number>guess:
        print("Deine Zahl ist zu klein")
    elif rand_number<guess:
       print("Deine Zahl ist zu groß")
print("Hurra! Gewonnen!!")
