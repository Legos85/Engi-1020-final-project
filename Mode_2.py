import notes as n
from engi1020.arduino.api import buzzer_note, buzzer_stop
from time import sleep


def mode2():
    print("""\nSweet, so you chose mode 2. Now for a little tutorial on how this mode will take it's inputs.
    \nSay for an example you wanted to play a 'e4' you would type it like how I just did
    \nor if you wanted to play an 'es4' you would typpe it like that,
    \nthen you would put in for how long to want to play it. Just a heads up
    \na quarter note would be 1 beat, a dotted half note would be 3 beats, an eighth note
    \nwould be 0.5 beats and so on and so forth. Due to the limitations of the buzzer
    \nyou can only input from c4 to c6.""")

    good_to_go = input("if you are ready to start enter 'start' or if you want to quit entre 'quit': ")

    while good_to_go == 'start':

        #gets the tempo from the user and checks to makesure that the value is numeric
        tempo = input("what is the tempo of the song? ")
        while str.isnumeric(tempo) == False:
            print('please entre valid tempo')
            tempo = input("what is the tempo of the song? ")
        else:
            tempo = int(tempo)

        #gets the amount of beats in the song from the user and checks to makesure that value is numeric
        how_long = input("how many notes are in this song? ")
        while str.isnumeric(how_long) == False:
            print('please entre valid amount of beats')
            how_long = input("how many notes are in this song? ")
        else:
            how_long = int(how_long)

        song_list = []
        j = 0
        
        #gets the notes and beats from the user
        for i in range(0,how_long):
            n_l = [input('note: '),(input('beat: '))]

            #checks to see if the note is in the dictonary and if the beat is valid
            while n_l[0] not in n.notes.keys() or str.isnumeric(n_l[1]) == False and n.isfloat(n_l[1]) == False:
                print("invalid note and/or beat")
                n_l = [input('note: '),(input('beat: '))]
            else:
                n_l[1] = float(n_l[1])
            song_list += [n_l]

        for q in song_list:
            
            note = song_list[j][0]
            beat = song_list[j][1]
            buzzer_note(5,n.notes[note], n.note_len(tempo,beat))
            sleep(n.note_len(tempo,beat))
            j += 1
        
        buzzer_stop(5)
        
        return 'done'
        
    if good_to_go == 'quit':
        return 'sending you back'

    while good_to_go != 'start' and good_to_go != 'quit':
        print('please entre valid input')
        good_to_go = input("if you are ready to start enter 'start' or if you want to quit entre 'quit': ")
