import notes as n
from engi1020.arduino.api import *

import Mode_1 as m1
import Mode_2 as m2
import Mode_3 as m3

print("""\n"hello user, this is a program for my engineering 1020 final project, and you get to use it.
\nNow you might be wondering who the person is who made this amazing code, that would be me, Logan Smith.
\nYou might also be wondering what this program does and if it wasn't clear from the name of the file you're running but this program plays music from 
the Arduino that you should have hooked up to the device that you're running this code off.
\nThis program has three different modes. 
\nThe first mode allows you to play a small selection of premade songs that are built into the code. 
\nThe second mode allows you to input a string of notes and it will automatically play them. 
\nthe last mode will allow you to use the dial and the button on the Arduino to manually play your own music. 
\nSo, what mode do you intend on using?
"\n""")
while True:
    what_mode =  input('Mode 1, Mode 2, Mode 3, Quit? ')

    if what_mode == 'Mode 1':
        m1.mode1()
        
    elif what_mode == 'Mode 2':
        m2.mode2()

    elif what_mode == 'Mode 3':
        m3.mode3()

    elif what_mode == 'Quit':
        print('thank you for running my code. Have a good day :)')
        break

    elif what_mode != 'Mode 1' and what_mode != 'Mode 2' and what_mode != 'Mode 3' and what_mode != 'Quit': 
        print('Come on now, input what mode you want ')

