

screen c1:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0.5
        text "Chapter 1: Pawn to H-eart's File " yalign 0.5 xalign 0.5
        
        

label start:
    "..."
    play sound "audio/beep.mp3"
    "BEEP!..."
    play sound "audio/beep.mp3"
    "BEEP!....."
    play sound "audio/beep.mp3"
    "BEEP!......."
    "Bzzzt!"


    # play buzz sound to signify the alarm is turned off

    "Tristan woke up in his bed with a buzzing head-ache. He looks around in his room full of clutter and mess."

    show bg tristanroom #place holder 
   
    with fade
    show tristan normal
    play music "audio/tristanhome.ogg" volume 0.09 fadein 1.0 loop
    with fade
    with hpunch
    hide tristan normal
    show tristan talking
    Tristan "ughh my head hurts...."
    

    Tristan "I overslept...."

    Tristan "Wait...."

    Tristan "What time is it?"

    hide tristan normal
    show tristan normal:
        yoffset 1000
        zoom 2
        center
    hide tristan normal
    show tristan talking:
        yoffset 1000
        zoom 2
        center
    Tristan "Crap!!" with hpunch

    
    
    show tristan normal 

    scene bg thoughts
    show tristan normal:
        yoffset 1000
        zoom 2
        center
    stop music 
    play music "audio/thoughts.ogg" volume 0.09 fadein 1 loop
    with dissolve
    
    Tristan "{i}(In his head){/i}{p=0}I gotta go to work!"

    show tristan normal:
        yoffset 1000
        zoom 2
        center

    Tristan "(In his head){p=0}Wait..."
    Tristan "(In his head){p=0}I have school today."
    hide tristan normal
    show tristan nervous:
        yoffset 2000
        zoom 3
        center
    Tristan "..."
    

 
    #*Flashback*
    #Chess tournament he lost at the finale with all the pressure from his parents and school
    #(vague explanation: Tristan dedicates his life to chess because from a young age)
   

    "Tristan looking hesitant..."
    hide tristan nervous
    show tristan normal:
        yoffset 1000
        zoom 2
        center
    Tristan "Oh well...{w} Who cares anyway."
 
    hide tristan normal
    stop music fadeout 1
    with dissolve
    
    pause 2.0
    show screen c1 with fade
    pause 5.0
    hide screen c1 with fade

    #Artist notes: vn style only, walking animation transition to next scene
    #Full art: flashback (purple highlight)
    #Expression: Tristan annoyed, shocked, neutral expression

    show bg store 
    play music "audio/store.ogg" volume 0.05 fadein 1 loop
    with dissolve
    
    "As Tristan enters the store, a lively chime greeted him."
    "..."
    "Following with the look of his manager."

    
    show tristan normal:
        xoffset 800
    
    with moveinleft
    
    pause 1

    show manager normal:
        left
    with moveinleft
    Manager "Oh..."
    Manager "You're finally here Tristan."

    "As the manager look at Tristan, He is at shock at the current state of him."

    Manager "Are you okay?"
    Manager "You don't look so good."

    hide tristan normal
    show tristan talking:
        xoffset 800
    Tristan "Yeah."

    Tristan "I'm in tip-top shape."
    hide tristan talking
    show tristan normal:
        xoffset 800

    Manager "How can you say that in that state."
    Manager "..."
    Manager "And with that face."  
    Manager "Oh well."
    Manager "Look out for yourself okay?"

    "Tristan nods as prepares to work the cash register."
    hide manager normal
    hide tristan normal
    with squares

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
    
    with squares
    show tristan normal:
        yoffset 1000
        zoom 2
        center
    "Tristan is scanning the products with a flatest expression on his face. "
    hide tristan normal
    show tristan talking:
        yoffset 1000
        zoom 2
        center
    Tristan "Will that be all?"
    hide tristan talking
    show tristan normal:
        yoffset 1000
        zoom 2
        center

    "???" "Mhm, That will be all ... hehe"

    "A sudden wave of nostalgia--a deja-vu like feeling flows through him."

    "As Tristan looks up to see the person."
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        left
    with move

    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with moveinleft

    pause 0.5

    #  *Television static fx* 
    stop music
    play sound "audio/static.mp3" volume 0.5
    scene bg staticeffect
    with hpunch
    with hpunch
    pause 0.3
    scene bg thoughts
    show tristan nervous:
        yoffset 1000
        xoffset 500
        zoom 2
        left
    stop music 
    play music "audio/thoughts.ogg" volume 0.05 fadein 0.3 loop
    Tristan "(In his head){p=0} That smile....."
    Tristan "(In his head){p=0} It seems....."
    Tristan "(In his head){p=0} Famillar....."
    show tristan nervous:
        yoffset 1000
        xoffset 500
        zoom 2
        left
   

    "Tristan was in a daze-{p=0}His mind wonders elsewhere."

    "(Girl)" "Earth to mister...."
    "(Girl)" "Earth to mister!!!"
    show tristan talking:
        yoffset 1000
        xoffset 500
        zoom 2
        left
    show bg store
    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    play music "audio/store.ogg" volume 0.05 fadein 1
    with dissolve


    Tristan "Huh?" with hpunch
    Tristan "Oh..."
    Tristan "Uhmm..."
    Tristan "Sorry here is your change."

    hide zoe normal
    show bg thoughts
    show tristan nervous:
        yoffset 1000
        xoffset 500
        zoom 2
        left
    stop music
    play music "audio/thoughts.ogg" volume 0.05 fadein 0.3 loop
    with dissolve
    Tristan "(In his head){p=0}Crap I was lost in my thoughts..."
    Tristan "(In his head){p=0}I messed up..."
    show bg store
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        left
    show zoe worriedtalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    play music "audio/store.ogg" volume 0.05 fadein 1
    with dissolve
    
    "(Girl)" "It's all goodiee!"
    "(Girl)" "Are you fine though?"
    "(Girl)" "Mister..."
    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    "The girl looks at Tristans employee badge on his shirt."
    show zoe talking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    "(Girl)" "Mister Tristan Garcia!!!"
    show zoe giggletalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    "(Girl)" "hehe."

    
    show tristan flustered: 
        yoffset 1000
        xoffset 500
        zoom 2
        left
    with hpunch
    "Tristan was flustered."
    "For the first time, someone accepted his flaw."
    "Her pure smile radiates throughout the store."
    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
        left

    show tristan flusteredtalking:
        yoffset 1000
        xoffset 500
        zoom 2
        left

    Tristan "m-hmm..."
    Tristan "Sorry again."
    Tristan "Miss..."
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        left
    show zoe talking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "Zoe Gonzales reporting in!"
    show zoe giggletalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "hehe."
    Zoe "Pleasure to meet you."

    stop music
    play sound "audio/static.mp3" volume 0.09
    scene bg staticeffect
    with hpunch
    with hpunch
    #  *Television static fx* 
    scene bg store
    play music "audio/store.ogg" volume 0.03 fadein 1
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        left
    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "..."
    show zoe teasetalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "By the way..."
    Zoe "Do you want to go on a date with me?"
    show zoe tease:
        yoffset 1000
        xoffset -500
        zoom 2
        left

    show tristan talking:
        yoffset 1000
        xoffset 500
        zoom 2
        left
    stop music
    Tristan "eh?"

    show tristan flusteredtalking:
        yoffset 1000
        xoffset 500
        zoom 2
        left
    Tristan "eh?!?" with hpunch
 
    show tristan flusteredtalking:
        yoffset 2000
        xoffset -100
        zoom 3
        left
    Tristan "EHHHHH!?!?" with hpunch

    
    hide zoe normal
    show bg thoughts
    with dissolve
    pause 1
    hide tristan flusteredtalking
    with dissolve

    jump Chapter2
    return
