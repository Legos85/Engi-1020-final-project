import notes as n
from engi1020.arduino.api import buzzer_note
from time import sleep
tempo = 100
#score taken from https://musescore.com/user/1625206/scores/717751
def chest():
    buzzer_note(5,n.notes['a4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))
    buzzer_note(5,n.notes['as4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))
    buzzer_note(5,n.notes['b4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))
    buzzer_note(5,n.notes['c5'], n.note_len(tempo,5))
    sleep(n.note_len(tempo,0.5))

    return 'done'