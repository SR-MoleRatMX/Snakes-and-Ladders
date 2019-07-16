#from random import *
import random
import tkinter

playagain = ('y')
ps1 = 0
ps2 = 0

def move(ps1, ps2):
    for i in range(2):
        d = random.randint(0,6)
        ps1 += d

    for i in range(2):
        d = random.randint(0,6)
        ps2 += d

    return

def loop():
    move(1, 2)
    print(ps1)
    print(ps2)
    playagain = input('Do you want to play again \n> ')

    return

while playagain == ('y'):
    loop()
