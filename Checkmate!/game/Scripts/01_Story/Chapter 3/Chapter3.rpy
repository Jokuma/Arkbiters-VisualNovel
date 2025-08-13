transform enlarge:
    zoom 1.5
    center

screen c3:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0.5
        text "Chapter 3 : Harmony on the Board " yalign 0.5 xalign 0.5

label Chapter3:

    show black screen
    with dissolve

    show screen c3 with fade
    pause 5.0
    hide screen c3 with fade

    define dissolve = Dissolve(0.2)

    play music "audio/Music/Karaoke.mp3" volume 0.3 fadein 1

    "The faint hum of other rooms singing drifts through the walls. "
    "A table sits between Tristan and Zoe, cluttered with empty cups of soda and a plate of untouched fries."

    "Zoe is singing in the background"
    ".{w=0.3}.{w=0.3}."

    scene bg karaoke with dissolve
    
    show zoe happytalking:
        yoffset 1000
        xoffset 0
        zoom 2
        center
    with dissolve
    Zoe "\"Alright, Tristan Garcia--\""
    show zoe worriedtalking:
        yoffset 1000
        xoffset 0
        zoom 2
        center
    with dissolve
    play sound "audio/SFX/explosion.wav"
    Zoe "*cough*" with hpunch
    show zoe happytalking:
        yoffset 1000
        xoffset 0
        zoom 2
        center
    with dissolve
    Zoe "\"It's your turn to sing!\""
    play sound "audio/SFX/explosion.wav"
    with hpunch
    "Zoe throws the microphone towards him with a grin"
    show zoe happy:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with move
    show tristan flusteredtalking:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with moveinright
    Tristan "\"M-me?\""
    Tristan "\"No way!\""
    show tristan nervoustalking:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve
    Tristan "\"...{w}I can't sing.\""
    show tristan normaltalking:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve
    Tristan "\"Besides, are you okay?... That's a harsh cough\""
    show tristan normaltalking:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    
    show zoe smile:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"I'm fine... The song is just that hard.\""
    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"With that said...{w} Everyone can sing!\""
    Zoe "\"Besides...\""
    
    hide tristan normal
    show zoe smugtalking:
        yoffset 1800
        xoffset 0
        zoom 3
        center
    with dissolve
    "Zoe leans closer to Tristan with teasing look on her face"
    show zoe smugtalking:
        yoffset 1800
        xoffset 0
        zoom 3
        center
    with dissolve
    Zoe "\"You owe me for losing our ice cream race...{w} hehe.\""
    show zoe smugtalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    show tristan flustered:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve
    "..."
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve
    pause 1
    
    
    show thoughts zorder 2
    show tristan nervous zorder 2:
        yoffset 1000
        xoffset 500
        right
        zoom 2
    with dissolve
    play music "audio/Music/Thoughts.mp3" volume 0.3 fadein 0.3 loop
    Tristan "{i}In his head{/i}{p=0}Why did I even agree to this date?"
    Tristan "{i}In his head{/i}{p=0}I'm just embarrasing myself over and over..."
    play sound "audio/SFX/static.mp3"
    scene bg staticeffect
    with hpunch
    show static2
    with hpunch
    scene bg karaoke 
    show thoughts zorder 2
    show zoe smugtalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    show tristan nervous zorder 2:
        yoffset 1000
        xoffset 500
        zoom 2
        right


    with dissolve
    
    "Tristan flinches slightly, clutching the mic."
    ####################

    show tristan nervous:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve

    Tristan "{i}In his head{/i}{p=0}Again?"
    Tristan "{i}In his head{/i}{p=0}Everytime I'm with her...{w} It's like...{w} The board resets."
    show zoe worriedtalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"Earth to Tristan!!!{p}Oh no, not this again.\""

    scene bg karaoke
    show tristan nervoustalking:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    show zoe worriedtalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    play music "audio/Music/Karaoke.mp3" volume 0.3 fadein 1

    ####################
    show tristan normaltalking:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    show zoe worried:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Tristan "\"Oh...{w} sorry\""
    Tristan "\"I'm fine, just picking a song.\""
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve

    "He scrolls through the screen, fingers hovering."
    show zoe smug:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    "His mind is blank...{w}until Zoe reaches over and taps a title."
    show zoe smugtalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"This one!\""
    Zoe "\"It's simple... You'll do great!\""
    show zoe smug:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    show tristan normaltalking:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve
    Tristan "\"I...{w} fine.\""
    show tristan flusteredtalking:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve
    Tristan "\"But dont laugh!\""

    hide tristan flusteredtalking
    hide zoe normal
    hide bg karaoke
    show karaoke_animated
    $ quick_menu = False
    with squares
    #** Karaoke Minigame **
    # Rhythm game (Friday Night Funkin, Osu!Mania basta rhythm game na madaling ma implement HAHAHAHAHAHA)
    
    jump minigamerhythm
    return
    #####################################################################
    label Chapter3continue:
    $ _game_menu_screen = 'save'
    $ quick_menu = True
    $ renpy.block_rollback()
    scene bg karaoke
    show tristan flusteredtalking:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    show zoe smile:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with squares

    "As Tristan is singing...{p=0}Zoe smiles at him—warm, genuine."
    
    # Television static fx again, but this time a flash of another memory bleeds through — the same booth, same song, same smile 
    play music "audio/Music/Thoughts.mp3" volume 0.3 fadein 0.3 loop
    
    play sound "audio/SFX/static.mp3"
    scene bg staticeffect
    with hpunch
    show static2
    with hpunch

    scene bg karaoke
    show thoughts zorder 2
    show tristan nervous zorder 2:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    show zoe smile:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Tristan "{i}In his head{/i}{p=0}What...{w} was that?{p}A memory?..{p}A dream?.."
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    show bg karaoke
    hide thoughts
    with dissolve

    play music "audio/Music/Karaoke.mp3" volume 0.3 fadein 1

    Zoe "\"Hey...{w} That was pretty good!\""
    Zoe "\"Not bad for a \"useless loser\" huh? \""
    show zoe smug:
        yoffset 1000
        xoffset -500
        zoom 2
        left

    show tristan flusteredtalking:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve
    Tristan "\"H-hey...when did I call myself—\""
    show tristan nervous:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"You didn't have to...{p}I can read it in your eyes..\""
    show zoe smug:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"...\""
    show zoe smugtalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"But I think you're wrong...hehe\""
    show zoe smug:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    show tristan flustered:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve
    "Zoe leans back, sipping her drink. Tristan stares at her for a moment longer, the lyrics of the song still echoing in his head."
    "..."
    show zoe worried:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    play sound "audio/SFX/explosion.wav"
    "Suddenly Zoe jumped out from her seat" with vpunch

    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    show zoe worriedtalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"Uwaaa!..\"" with vpunch
    Zoe "\"I forgot I have school tomorrow! Man that sucks! I was having a lot of fun.\""
    show tristan normaltalking:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    show zoe worried:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Tristan "\"Now that you said it… I have school tomorrow too.\""
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"Really? Which school do you go to?\""
    show zoe happy:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    show tristan normaltalking:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve
    Tristan "\"ARK-University.\""
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    play sound "audio/SFX/explosion.wav"
    Zoe "\"NO WAY!! … we go to the same school then hehe!\"" with hpunch
    show zoe smile:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    show tristan flustered:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve
    "Tristan was shocked and speechless upon realizing they go to the same school."
    "He felt a sigh of relief, as if deep down he had been hoping for this."
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"Alright enough of that… let's make the most of today, your turn to pick my song, and no mercy!\""
    show zoe smile:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    "Tristan scrolls through the machine."
    show tristan flustered:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve
    "His eyes kept darting toward Zoe— {p}like a player glancing at a chessboard{p}unsure if the next move will win or lose the game."
    
    show bg blackscreen
    hide zoe normal
    hide tristan flustered
    stop music fadeout 1.0
    with dissolve
    jump Chapter4
    return