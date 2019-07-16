from random import *
import tkinter

playagain = ('y')
ps1 = 0
ps2 = 0

for i in range(ladders):
    ladLength = randint(5,35)

snakes = randint(5,15)

while playagain == ('y'):
    for i in range (2):
        d1 = randint(1,6)
        d2 = randint(1,6)
        ps1 += d1
        ps2 += d2

    print('Player 1 is on square %s' %ps1)
    print('Player 2 is on square %s' %ps2)

    playagain = input('Do you want to play again? \n> ')
    
