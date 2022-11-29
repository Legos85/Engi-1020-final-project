
import zeldas_lullaby
import Mario_underworld_theme
import Chest_opening
def mode1():
    song_list = ["Mario underworld Theme (1)", "Zelda chest opening sound (2)", "Zelda's lullaby (3)"]

    #asks user to input a value then checks to see if it the imput is valid
    print("to chose a song but input the coresponding number or if you link to go back to the select menu press(0)")
    what_song = input(f'{song_list} : ')
    while str.isnumeric(what_song) == False:
        print('Please entre a valid input')
        what_song = input(f'{song_list} : ')

    #plays song based on the imput of the user
    if what_song == '1':
        return Mario_underworld_theme.underworld()

    elif what_song == '2':
        return Chest_opening.chest()

    elif what_song == '3':
        return zeldas_lullaby.lullaby()
        
    elif what_song == '0':
        return 'sending you back'

