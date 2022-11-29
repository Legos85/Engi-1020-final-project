from engi1020.arduino.api import *
import notes as n
from time import sleep

def mode3():

    print("""Welcome to mode 3. In this mode you will be using the dial on the arduino to play music.
    \nAll you have to do is turn the dial and the current note will be displayed on the OLED screen
    \nthen when you want to play the note just press the button.
    \nwhen you are done just put your hand over the light sensor to stop\n""")

    good_to_go = input("if you are ready to start enter 'start' or if you want to quit entre 'quit': ")


    
    while good_to_go == 'start':

        #checksthe light sensor to see if it's above the threshold
        if analog_read(6) >= 10:
            #intial clear to get rid of the welcome text
            oled_clear()
            x = analog_read(0)

            #checks the value of the dial
            if 0 <= x <= 127:
                oled_print('e4')
                #checks to see if the button is pressed so it can play the note
                if digital_read(6) == True:
                    buzzer_frequency(5,n.notes['e4'])
                elif digital_read(6) == False:
                    buzzer_stop(5)
                sleep(0.5)
                oled_clear()

            elif 128 <= x <= 255:
                oled_print('f4')
                if digital_read(6) == True:
                    buzzer_frequency(5,n.notes['f4'])
                elif digital_read(6) == False:
                    buzzer_stop(5)
                sleep(0.5)
                oled_clear()

            elif 256 <= x <= 382:
                oled_print('g4')
                if digital_read(6) == True:
                    buzzer_frequency(5,n.notes['g4'])
                elif digital_read(6) == False:
                    buzzer_stop(5)
                sleep(0.5)
                oled_clear()

            elif 383 <= x <= 509:
                oled_print('a5')
                if digital_read(6) == True:
                    buzzer_frequency(5,n.notes['a5'])
                elif digital_read(6) == False:
                    buzzer_stop(5)
                sleep(0.5)
                oled_clear()

            elif 510 <= x <= 636:
                oled_print('b5')
                if digital_read(6) == True:
                    buzzer_frequency(5,n.notes['b5'])
                elif digital_read(6) == False:
                    buzzer_stop(5)
                sleep(0.5)
                oled_clear()

            elif 637 <= x <= 763:
                oled_print('c5')
                if digital_read(6) == True:
                    buzzer_frequency(5,n.notes['c5'])
                elif digital_read(6) == False:
                    buzzer_stop(5)
                sleep(0.5)
                oled_clear()

            elif 764 <= x <= 890:
                oled_print('d5')
                if digital_read(6) == True:
                    buzzer_frequency(5,n.notes['d5'])
                elif digital_read(6) == False:
                    buzzer_stop(5)
                sleep(0.5)
                oled_clear()
                
            elif 891 <= x <= 1023:
                oled_print('e5')
                if digital_read(6) == True:
                    buzzer_frequency(5,n.notes['e5'])
                elif digital_read(6) == False:
                    buzzer_stop(5)
                sleep(0.5)
                oled_clear()

        #when the light sensor is below the threshold it stop the program
        elif analog_read(6) < 10:
            return 'done'

    if good_to_go == 'quit':
        return 'sending you back'

    while good_to_go != 'start' and good_to_go != 'quit':
        print('please entre valid input')
        good_to_go = input("if you are ready to start enter 'start' or if you want to quit entre 'quit': ")

