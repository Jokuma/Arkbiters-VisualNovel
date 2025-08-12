screen c1:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0.5
        text "Chapter 1: Pawn to H-eart's File " yalign 0.5 xalign 0.5
        

label start:

    define dissolve = Dissolve(0.2)
    define fade1 = Fade(0.5, 0.0, 0.5)

    "..."
    play sound "audio/SFX/beep.mp3"
    "BEEP!......."
    play sound "audio/SFX/beep.mp3"
    "BEEP!....."
    play sound "audio/SFX/beep.mp3"
    "BEEP!..."
    play sound "audio/SFX/click.mp3"
    "Click..."

    # play click sound to signify the alarm is turned off

    "Tristan woke up in his bed with a buzzing head-ache. He looks around in his room full of clutter and mess."

    scene bg tristanroom #place holder 
    
    with fade1
    show tristan normal
    play music "audio/Music/tristanhome.ogg" volume 0.09 fadein 1.0 loop
    with fade1
    with hpunch
    
    show tristan normaltalking
    Tristan "\"ughh my head hurts....\""
    
    Tristan "\"I overslept....\""

    Tristan "\"Wait....\""

    Tristan "\"What time is it?\""

    show tristan normal:
        yoffset 1000
        zoom 2
        center

    show tristan normaltalking:
        yoffset 1000
        zoom 2
        center
    
    play sound "audio/SFX/explosion.wav"
    Tristan "\"Crap!!\"" with hpunch 
    
    scene bg thoughts

    show tristan normal:
        yoffset 1000
        zoom 2
        center
    stop music 
    play music "audio/Music/Thoughts.mp3" volume 0.09 fadein 1 loop
    with dissolve
    
    Tristan "{i}(In his head){/i}{p=0}I gotta go to work!"

    show tristan normal:
        yoffset 1000
        zoom 2
        center

    Tristan "{i}(In his head){/i}{p=0}Wait..."
    Tristan "{i}(In his head){/i}{p=0}I have school today."

    hide tristan normal
    show tristan nervous:
        yoffset 2000
        zoom 3
        center
    Tristan "\"...\""

    "Tristan looking hesitant..."

    scene bg tristanroom
    show tristan normal:
        yoffset 1000
        zoom 2
        center
    with dissolve

    Tristan "\"Oh well...{w} Who cares anyway.\""

    hide tristan normal
    with dissolve
    scene black screen
    with dissolve
    stop music fadeout 1
    
    show screen c1 with fade
    pause 3.0
    hide screen c1 with fade

    show bg store 
    play music "audio/store.ogg" volume 0.05 fadein 1 loop
    with dissolve
    
    "As Tristan enters the store, a lively chime greeted him."
    "..."
    "Following with the look of his manager."

    show tristan normal:
        xoffset 600
        zoom 1.5
    with dissolve

    play sound "audio/SFX/walk.mp3"
    show manager normal:
        left
    with moveinleft

    Manager "\"Oh...\""
    Manager "\"You're finally here Tristan.\""

    "As the manager look at Tristan, He is at shock at the current state of him."

    Manager "\"Are you okay?\""
    Manager "\"You don't look so good.\""

    show tristan normaltalking:
        xoffset 600
        zoom 1.5
    with dissolve

    Tristan "\"Yeah.\""

    Tristan "\"I'm in tip-top shape.\""

    show tristan normal:
        xoffset 600
        zoom 1.5
    with dissolve

    Manager "\"How can you say that in that state.\""
    Manager "\"...\""
    Manager "\"And with that face.\""  
    Manager "\"Oh well."
    Manager "\"Look out for yourself okay?\""

    "Tristan nods as prepares to work the cash register."
    hide manager normal
    hide tristan normal

    with squares

    show tristan normal:
        yoffset 1000
        zoom 2
        center
    with dissolve

    "Tristan is scanning the products with a flatest expression on his face. "


    show tristan normaltalking:
        yoffset 1000
        zoom 2
        center
    with dissolve

    Tristan "\"Will that be all?\""

    show tristan normal:
        yoffset 1000
        zoom 2
        center
    with dissolve

    "???" "\"Mhm, That will be all ... hehe\""

    "A sudden wave of nostalgia... a deja-vu like feeling flows through him."

    show tristan normal:
        yoffset 1000
        xoffset 450
        zoom 2
        left
    with move

    show zoe happy:
        yoffset 1000
        xoffset -700
        zoom 2
        left
    with moveinleft

    "As Tristan looks up to see the person."

    stop music
    play sound "audio/SFX/static.mp3" volume 0.5
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
    Tristan "{i}(In his head){/i}{p=0} That smile....."
    Tristan "{i}(In his head){/i}{p=0} It seems....."
    Tristan "{i}(In his head){/i}{p=0} Famillar....."

    show tristan nervous:
        yoffset 1000
        xoffset 500
        zoom 2
        left

    "Tristan was in a daze-{p=0}His mind wonders elsewhere."

    "Girl" "\"Earth to mister....\""
    "Girl" "\"Earth to mister!!!\""
    
    show bg store
    
    show tristan normaltalking:
        yoffset 1000
        xoffset 500
        zoom 2
        left
    show zoe happy:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    play music "audio/store.ogg" volume 0.05 fadein 1
    with dissolve

    play sound "audio/SFX/explosion.wav"
    Tristan "\"Huh?\"" with hpunch
    Tristan "\"Oh...\""
    Tristan "\"Uhmm...\""
    Tristan "\"Sorry here is your change.\""

    hide zoe happy
    show bg thoughts

    show tristan nervous:
        yoffset 1000
        xoffset 500
        zoom 2
        left
    stop music
    play music "audio/thoughts.ogg" volume 0.05 fadein 0.3 loop
    with dissolve

    Tristan "{i}(In his head){/i}{p=0}Crap I was lost in my thoughts..."
    Tristan "{i}(In his head){/i}{p=0}I messed up..."

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
    
    "Girl" "\"It's all goodiee!\""
    "Girl" "\"Are you fine though?\""
    "Girl" "\"Mister...\""

    show zoe happy:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    "The girl looks at Tristans employee badge on his shirt."

    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    "Girl" "\"Mister Tristan Garcia!!!\""

    show zoe giggle:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    "Girl" "\"hehe.\""

    show tristan flustered: 
        yoffset 1000
        xoffset 500
        zoom 2
        left
    with dissolve

    "Tristan was flustered."
    "For the first time, someone accepted his flaw."
    "Her pure smile radiates throughout the store."

    show zoe happy:
        yoffset 1000
        xoffset -500
        zoom 2
        left

    show tristan flusteredtalking:
        yoffset 1000
        xoffset 500
        zoom 2
        left
    with dissolve

    Tristan "\"m-hmm...\""
    Tristan "\"Sorry again.\""
    Tristan "\"Miss...\""

    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        left
    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    Zoe "\"Zoe Gonzales reporting in!\""
    show zoe giggle:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    Zoe "\"hehe.\""
    Zoe "\"Pleasure to meet you.\""

    stop music
    play sound "audio/SFX/static.mp3" volume 0.5
    scene bg staticeffect
    with hpunch
    with hpunch
    scene bg store
    play music "audio/store.ogg" volume 0.03 fadein 1
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        left
    show zoe happy:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "\"...\""
    show zoe smugtalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    Zoe "\"By the way...\""
    Zoe "\"Do you want to go on a date with me?\""
    
    show zoe smug:
        yoffset 1000
        xoffset -500
        zoom 2
        left

    show tristan normaltalking:
        yoffset 1000
        xoffset 500
        zoom 2
        left
    stop music
    with dissolve

    Tristan "\"eh?\""

    show tristan flusteredtalking:
        yoffset 1000
        xoffset 500
        zoom 2
        left
    with dissolve

    play sound "audio/SFX/explosion.wav"
    Tristan "\"eh?!?\"" with hpunch

    show tristan flusteredtalking:
        yoffset 2000
        xoffset -100
        zoom 3
        left
    with dissolve

    play sound "audio/SFX/explosion.wav"
    Tristan "\"EHHHHH!?!?\"" with hpunch

    show black screen

    with dissolve

    jump Chapter2
    return