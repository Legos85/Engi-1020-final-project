import notes as n
from engi1020.arduino.api import buzzer_note
from time import sleep
tempo = 100
# song score taken from https://musescore.com/aarongrooves/mario-underworld-original

def underworld():
    buzzer_note(5, n.notes['gs4'], n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['gs5'], n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['fs4'],n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['fs5'],n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['g4'],n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['g5'],n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['rest'],n.note_len(tempo,1.5))
    sleep(n.note_len(tempo,1.5))

    buzzer_note(5, n.notes['gs4'], n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['gs5'], n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['fs4'],n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['fs5'],n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['g4'],n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['g5'],n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['rest'],n.note_len(tempo,1.5))
    sleep(n.note_len(tempo,1.5))

    buzzer_note(5, n.notes['d4'], n.note_len(tempo, 0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['d5'], n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['as4'], n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5,n.notes['as5'], n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5,n.notes['c4'],n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5,n.notes['c5'], n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['rest'],n.note_len(tempo,1.5))
    sleep(n.note_len(tempo,1.5))
    
    buzzer_note(5, n.notes['d4'], n.note_len(tempo, 0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['d5'], n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['as4'], n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5,n.notes['as5'], n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5,n.notes['c4'],n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5,n.notes['c5'], n.note_len(tempo,0.25))
    sleep(n.note_len(tempo,0.25))
    buzzer_note(5, n.notes['rest'],n.note_len(tempo,1))
    sleep(n.note_len(tempo,1))
    buzzer_note(5, n.notes['c4'], n.note_len(tempo,0.17))
    sleep(n.note_len(tempo,0.17))
    buzzer_note(5, n.notes['as4'], n.note_len(tempo,0.17))
    sleep(n.note_len(tempo,0.17))
    buzzer_note(5, n.notes['a4'], n.note_len(tempo, 0.17))
    sleep(n.note_len(tempo,0.17))

    buzzer_note(5, n.notes['gs4'], n.note_len(tempo,1.5))
    sleep(n.note_len(tempo,1.5))
    buzzer_note(5, n.notes['c4'], n.note_len(tempo, 1.5))
    sleep(n.note_len(tempo,1.5))
    buzzer_note(5, n.notes['as4'], n.note_len(tempo, 1.5))
    sleep(n.note_len(tempo,1.5))
    buzzer_note(5, n.notes['f4'], n.note_len(tempo, 1.5))
    sleep(n.note_len(tempo,1.5))
    buzzer_note(5, n.notes['ds4'], n.note_len(tempo, 1.5))
    sleep(n.note_len(tempo,1.5))
    buzzer_note(5, n.notes['a4'], n.note_len(tempo, 1.5))
    sleep(n.note_len(tempo,1.5))

    buzzer_note(5, n.notes['gs4'], n.note_len(tempo, 0.17))
    sleep(n.note_len(tempo,0.17))
    buzzer_note(5,n.notes['ds4'], n.note_len(tempo, 0.17))
    sleep(n.note_len(tempo,0.17))
    buzzer_note(5, n.notes['d4'], n.note_len(tempo,0.17))
    sleep(n.note_len(tempo,0.17))
    buzzer_note(5, n.notes['cs4'], n.note_len(tempo,0.17))
    sleep(n.note_len(tempo,0.17))
    buzzer_note(5, n.notes['g5'], n.note_len(tempo,0.17))
    sleep(n.note_len(tempo,0.17))
    buzzer_note(5, n.notes['fs5'], n.note_len(tempo,0.17))
    sleep(n.note_len(tempo,0.17))
    buzzer_note(5, n.notes['e5'], n.note_len(tempo,0.49))
    sleep(n.note_len(tempo,0.49))
    buzzer_note(5, n.notes['b4'], n.note_len(tempo,0.49))
    sleep(n.note_len(tempo,0.49))
    buzzer_note(5, n.notes['gs4'], n.note_len(tempo,0.49))
    sleep(n.note_len(tempo,0.49))
    buzzer_note(5, n.notes['g4'], n.note_len(tempo,0.49))
    sleep(n.note_len(tempo,0.49))
    buzzer_note(5, n.notes['fs4'], n.note_len(tempo,0.49))
    sleep(n.note_len(tempo,0.49))
    buzzer_note(5, n.notes['e4'], n.note_len(tempo,0.49))
    sleep(n.note_len(tempo,0.49))

    return 'done'

