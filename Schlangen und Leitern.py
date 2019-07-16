from random import *
import tkinter

playagain = ('y')
ps1 = 0
ps2 = 0

def roll(playersquare):
    for i in range (2):
        d = randint(1,6)
        playersquare += d
        
    return playersquare;

def loop(ps1, ps2):
    ps3 = ps1
    ps1 = roll(playersquare = ps1)
    ps1 += ps3 
    print(ps3)

    ps4 = ps2
    ps2 = roll(playersquare = ps2)
    ps4 += ps2
    print(ps4)
    
    playagain = input('Play again? \n> ')
 
while playagain == ('y'):
    loop(ps1, ps2)
