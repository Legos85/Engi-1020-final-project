import notes as n
from engi1020.arduino.api import buzzer_note
from time import sleep
tempo = 110

# song score taken from https://github.com/robsoncouto/arduino-songs/blob/master/zeldaslullaby/zeldaslullaby.ino
def lullaby():
    buzzer_note(5, n.notes['e4'], n.note_len(tempo,2))
    sleep(n.note_len(tempo,2))
    buzzer_note(5, n.notes['g5'], n.note_len(tempo,1))
    sleep(n.note_len(tempo,1))

    buzzer_note(5, n.notes['d4'], n.note_len(tempo,2))
    sleep(n.note_len(tempo,2))
    buzzer_note(5, n.notes['c4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))
    buzzer_note(5, n.notes['d4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))

    buzzer_note(5, n.notes['e4'], n.note_len(tempo,2))
    sleep(n.note_len(tempo,2))
    buzzer_note(5, n.notes['g5'], n.note_len(tempo,1))
    sleep(n.note_len(tempo,1))

    buzzer_note(5, n.notes['d4'], n.note_len(tempo,3))
    sleep(n.note_len(tempo,3))

    buzzer_note(5, n.notes['e4'], n.note_len(tempo,2))
    sleep(n.note_len(tempo,2))
    buzzer_note(5, n.notes['g5'], n.note_len(tempo,1))
    sleep(n.note_len(tempo,1))

    buzzer_note(5, n.notes['d5'], n.note_len(tempo,2))
    sleep(n.note_len(tempo,2))
    buzzer_note(5, n.notes['c5'], n.note_len(tempo,1))
    sleep(n.note_len(tempo,1))

    buzzer_note(5, n.notes['g4'], n.note_len(tempo,2))
    sleep(n.note_len(tempo,2))
    buzzer_note(5, n.notes['f4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))
    buzzer_note(5, n.notes['e4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))

    buzzer_note(5, n.notes['d4'], n.note_len(tempo,3))
    sleep(n.note_len(tempo,3))

    buzzer_note(5, n.notes['e4'], n.note_len(tempo,2))
    sleep(n.note_len(tempo,2))
    buzzer_note(5, n.notes['g5'], n.note_len(tempo,1))
    sleep(n.note_len(tempo,1))

    buzzer_note(5, n.notes['d4'], n.note_len(tempo,2))
    sleep(n.note_len(tempo,2))
    buzzer_note(5, n.notes['c4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))
    buzzer_note(5, n.notes['d4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))

    buzzer_note(5, n.notes['e4'], n.note_len(tempo,2))
    sleep(n.note_len(tempo,2))
    buzzer_note(5, n.notes['g5'], n.note_len(tempo,1))
    sleep(n.note_len(tempo,1))

    buzzer_note(5, n.notes['d4'], n.note_len(tempo,3))
    sleep(n.note_len(tempo,3))

    buzzer_note(5, n.notes['e4'], n.note_len(tempo,2))
    sleep(n.note_len(tempo,2))
    buzzer_note(5, n.notes['g5'], n.note_len(tempo,1))
    sleep(n.note_len(tempo,1))

    buzzer_note(5, n.notes['d5'], n.note_len(tempo,2))
    sleep(n.note_len(tempo,2))
    buzzer_note(5, n.notes['c5'], n.note_len(tempo,1))
    sleep(n.note_len(tempo,1))

    buzzer_note(5, n.notes['g4'], n.note_len(tempo,2))
    sleep(n.note_len(tempo,2))
    buzzer_note(5, n.notes['f4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))
    buzzer_note(5, n.notes['e4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))

    buzzer_note(5, n.notes['f4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))
    buzzer_note(5, n.notes['e4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))
    buzzer_note(5, n.notes['c4'], n.note_len(tempo,2))
    sleep(n.note_len(tempo,2))

    buzzer_note(5, n.notes['f4'], n.note_len(tempo,2))
    sleep(n.note_len(tempo,2))
    buzzer_note(5, n.notes['e4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))
    buzzer_note(5, n.notes['d4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))

    buzzer_note(5, n.notes['e4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))
    buzzer_note(5, n.notes['d4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))
    buzzer_note(5, n.notes['a4'], n.note_len(tempo,2))
    sleep(n.note_len(tempo,2))

    buzzer_note(5, n.notes['g4'], n.note_len(tempo,2))
    sleep(n.note_len(tempo,2))
    buzzer_note(5, n.notes['f4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))
    buzzer_note(5, n.notes['e4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))

    buzzer_note(5, n.notes['f4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))
    buzzer_note(5, n.notes['e4'], n.note_len(tempo,0.5))
    sleep(n.note_len(tempo,0.5))
    buzzer_note(5, n.notes['c4'], n.note_len(tempo,1))
    sleep(n.note_len(tempo,1))
    buzzer_note(5, n.notes['f4'], n.note_len(tempo,1))
    sleep(n.note_len(tempo,1))

    buzzer_note(5, n.notes['c5'], n.note_len(tempo,3))
    sleep(n.note_len(tempo,3))

    return 'done'