import random

Zufallszahl = random.randint(1, 100)

Aktiv = True
versuche = 7

while Aktiv:
    user_input = int(input("schreibe deine Zahl: "))

    if versuche > 0:
        if Zufallszahl > user_input:
            print("die Zahl ist zu niedrig")
            versuche = versuche - 1
        elif Zufallszahl < user_input:
            print("die Zahl die zu groß")
            versuche = versuche - 1
        else:
            print("Die Zahl ist richtig")
            print("Du hast gewonnen!")
            Aktiv = False
    else:
        Aktiv = False
        print("Versuche verbraucht!")
        print(
            f"Die richtige Zahl wäre {Zufallszahl} gewesen")  # das f ist ein formatierter String, damit diese Zufallszahl geraten wird!
