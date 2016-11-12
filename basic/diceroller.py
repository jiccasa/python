#Dice Roller

import random

def rolldice():
	return random.randint(1,6)

#Main
dice1 = rolldice()
dice2 = rolldice()
total = dice1 + dice2
print('Dice 1: ', dice1,'Dice 2 : ', dice2, 'Total: ', total )
if (dice1 == dice2):
	print('DOUBLES...ROLL IT AGAIN')


