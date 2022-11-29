
#note frenquencys taken from https://en.wikipedia.org/wiki/Piano_key_frequencies#List

#after some testing there seem to be a dead zone on the buzzer where it won't play 
#any frquencys between 135-255
notes = {
    'rest': 0,
    'c4': 262,
    'cs4': 277,
    'd4': 294,
    'ds4': 311,
    'e4': 330,
    'f4': 349,
    'fs4': 370,
    'g4': 392,
    'gs4': 415,
    'a4': 440,
    'as4': 466,
    'b4': 494,
    'c5': 523,
    'cs5': 554,
    'd5': 587,
    'ds5': 622,
    'e5': 659,
    'f5': 698,
    'fs5': 740,
    'g5': 784,
    'gs5': 831,
    'a5': 880,
    'as5': 932,
    'b5': 988,
    'c6': 1047,
}

def note_len(tempo, note_type):
    """this function takes the tempo of a song and gives back how long the desired note lasts
    
    Parameters:
    tempo(int): speed of the song in tempo
    note_type(int): type of note you want to find the length of in seconds (eg. half note(2), quarter note(1), dotted quarter note(1.5) ... )
    
    """
    if tempo > 0:
        if note_type > 0:
            return note_type*(60/tempo)
        else:
            return 'invalid note type'
    else:
        return 'invalid tempo'


#Function taken from https://www.programiz.com/python-programming/examples/check-string-number
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

