# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Tristan = Character('Tristan', color="#1e4e9c")

transform enlarge:
    zoom 1.5
    center

screen c1:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0.5
        text "Chapter 1: Pawn to H-eart's File " yalign 0.5 xalign 0.5
        
        
        


# The game starts here.

label start:
    
    with fade
    show screen c1
    with fade

    "BEEP!..."

    "BEEP!....."

    "BEEP!......."

    "Bzzz!"

    "test"

    # play buzz sound to signify the alarm is turned off

    "Tristan woke up in his bed with a buzzing head-ache. He looks around in his room full of clutter and mess."

    show tristan normal at enlarge
    Tristan "ughh my head hurts...."
    Tristan "I overslept...."
    Tristan "Wait...."
    Tristan "What time is it?"
    Tristan "Crap!!"
    Tristan "I gotta go to work!"

    return
