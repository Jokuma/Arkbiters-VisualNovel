

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
        
        

label start:
    
    pause 3.0

    "BEEP!..."

    "BEEP!....."

    "BEEP!......."

    "Bzzzt!"


    # play buzz sound to signify the alarm is turned off

    "Tristan woke up in his bed with a buzzing head-ache. He looks around in his room full of clutter and mess."

    show bg tristanroom #place holder 
    with fade

    show tristan normal at enlarge
    with fade
    Tristan "ughh my head hurts...."

    Tristan "I overslept...."

    Tristan "Wait...."

    Tristan "What time is it?"

    hide tristan normal
    show tristan normal:
        yoffset 600
        zoom 3
        center
    Tristan "Crap!!" with hpunch
    
    hide tristan normal
    show tristan normal at enlarge

    Tristan "I gotta go to work!"

    hide tristan normal
    show tristan normal:
        yoffset 800
        zoom 3
        center
    
    Tristan "Wait..."
    Tristan "I have school today"
    Tristan "..."

 
    #*Flashback*
    #Chess tournament he lost at the finale with all the pressure from his parents and school
    #(vague explanation: Tristan dedicates his life to chess because from a young age)
   
    hide tristan normal
    show tristan normal at enlarge
    "Tristan looking hesitant..."
    Tristan "Oh well{w}, who cares anyway"
    hide tristan normal
    with moveoutright
    hide bg tristanroom 
    with dissolve
    
    pause 2.0
    show screen c1 with fade
    pause 5.0
    hide screen c1 with fade

    ""
    #Artist notes: vn style only, walking animation transition to next scene
    #Full art: flashback (purple highlight)
    #Expression: Tristan annoyed, shocked, neutral expression

    show bg store 
    with fade
    
    "As Tristan enters the store, a lively chime greeted him."
    "..."
    "following with the look of his manager."

    Manager "Oh..."
    Manager "You're finally here Tristan."

    "As the manager look at Tristan, He is at shock at the current state of him."

    Manager "Are you okay?"
    Manager "You don't look so good."

    Tristan "Yeah."
    Tristan "I'm in tip-top shape."

    Manager "How can you say that in that state."
    Manager "..."
    Manager "and with that face."  
    Manager "Oh well."
    Manager "Look out for yourself okay?"

    "Tristan nods as prepares to work the cash register."

    #           ** Cash Register Minigame **
    #         Tristan has to input the correct amount of change to pass
    #        Simple math minigame
    #
    #        At first it will have a tutorial on how to play the minigame
    #        It will play for only 1 person
    #
    #        After the 1 person there are no more guides
    #
    #        After 3 persons Zoe the Main Heroine will appear

    "Tristan is scanning the products with a flatest expression on his face. "

    Tristan "Will that be all?"

    "???" "mhm, That will be all ... hehe"

    "A sudden wave of nostalgia--a deja-vu like feeling flows through him."

    "As Tristan looks up to see the person."

    #  *Television static fx* 

    Tristan "(In his head)  That smile....."
    Tristan "(In his head)  It seems....."
    Tristan "(In his head)  famillar....."

    "Tristan was in a daze--His mind wonders elsewhere."

    "(Girl)" "Earth to mister...."
    "(Girl)" "Earth to mister!!!"

    Tristan "Huh?"
    Tristan "Oh..."
    Tristan "uhmm..."
    Tristan "sorry here is your change."

    "(Girl)" "It's all goodiee!"
    "(Girl)" "Are you fine though?"
    "(Girl)" "Mister..."

    "The girl looks at Tristans employee badge on his shir.t"

    "(Girl)" "Mister Tristan Garcia!!!"
    "(Girl)" "hehe."

    "Tristan was shocked."
    "For the first time, someone accepted his flaw."
    "Her pure smile radiates throughout the store."

    Tristan "m-hmm..."
    Tristan "Sorry again."
    Tristan "Miss..."

    Zoe "Zoe Gonzales reporting in!"
    Zoe "hehe."
    Zoe "Pleasure to meet you."

    #  *Television static fx* 

    Zoe "..."
    Zoe "By the way..."
    Zoe "Do you want to go on a date with me?"

    Tristan "eh?"
    Tristan "eh?!?" with hpunch
    Tristan "EHHHHH!?!?" with hpunch

    ""
    with fade
    jump Chapter2
    with fade
    return
