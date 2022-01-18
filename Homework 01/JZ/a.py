import random
Computer = random.randint(1,100)

i=1
while i<=5:
    Player1 = int(input('please guess the random number:'))
    if Player1 == Computer:
        print('Bingo!')
        break
    elif Player1 > Computer:
        print('The number should be smaller')
        i+=1
        continue
    else:
        print('The number should be larger')
        i+=1
        continue
else:
    print('You lose')
