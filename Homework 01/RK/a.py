import random
random = (random.randint(0,100))
x = input("Bitte Tipp eingeben: ")
x = int(x)
#Loop start
while x != random:
    if x > random: print("zu groß")
    if x < random: print("zu klein")
    x = input("Bitte Tipp eingeben: ")
    x = int(x)
#Loop end
print("gewonnen!")
