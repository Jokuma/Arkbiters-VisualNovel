transform enlarge:
    zoom 1.5
    center

screen c5:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0.5
        text "Chapter 5 : Pawn's Promotion " yalign 0.5 xalign 0.5

label Chapter5:

    show screen c5 with fade
    pause 3.0
    hide screen c5 with fade

    define dissolve = Dissolve(0.2)

    #possible sound effect here

    
    play music "audio/Music/perya.mp3" volume 0.3 loop
    scene bg perya
    with dissolve

    "The faint smell of grilled street food, burnt sugar, and engine oil mixes into a strangely comforting haze."
    "The music from the rides is tiny, slightly warped by old speakers, but the laughter of children cuts through crisp and bright."

    scene bg perya
    with dissolve

    play sound "audio/SFX/walk.mp3" volume 0.3   

    show zoe happytalking:
        xoffset -200
        zoom 1.5
    with moveinright

    Zoe "\"Come on Tristan!!!\""
    Zoe "\"It's been years since I've been to one of these.\""

    hide zoe happytalking

    with dissolve

    "She tugs his sleeve like a child dragging a reluctant parent into a toy store."

    show zoe happy:
        xoffset -200
        zoom 1.5

    show tristan normaltalking:
        xoffset 500
        zoom 1.5

    with dissolve
        
    Tristan "\"Years?{w} I can't even remember the last time I went either...\""
    Tristan "{i}Feels like another lifetime...{/i}"

    hide zoe happy
    hide tristan normaltalking

    with dissolve
    
    "They pass rows of booths like the, ring toss...{p}Balloon darts...{p}And the shaky old Ferris wheel that creaks like it's telling ghost stories to the wind."
    "The perya is alive, but not spotless."
    "There's something imperfect about it..."
    "As if every stall is a little chipped, every prize a little faded."

    show zoe happytalking:
        xoffset -200
        zoom 1.5
    
    show tristan normal:
        xoffset 500
        zoom 1.5

    with dissolve

    Zoe "\"First stop, darts!\""

    show zoe smugtalking:
        xoffset -200
        zoom 1.5
    with dissolve
    
    Zoe "\"Loser buys isaw~\""

    show tristan normaltalking:
        xoffset 500
        zoom 1.5
    with dissolve
    
    Tristan "\"That's...{w} an oddly specific bet.\""

    hide zoe smugtalking
    hide tristan normal

    with dissolve

    "They step up to the dart booth. A man with a cigarette hanging from his lips hands them three dull-looking darts each."
    #-----------------------------------------------------------------------------------------------------------------------------


    scene darts1 with dissolve
    "Zoe throws first..."
    "She takes a slow breath, feeling the weight of the dart in her fingers."
    "Her eyes trace the distance, locking on the bright, water-filled target swaying gently in the breeze."
    "Her grip tightens, the sharp tip glinting under the light."
    "She draws her arm back, feeling the quiet tension in her shoulder."
    "For a split second, time feels heavy and still—only the faint hum of the crowd around them."
    scene darts2 with dissolve
    "Then, with a smooth flick of her wrist, the dart flies—"

    play sound "audio/SFX/pop.mp3" volume 0.3

    "One balloon pops instantly."
    scene darts3 with dissolve
    "She smirks."

    Zoe "\"Let's go! I got a balloon to pop!\""
    Zoe "\"hehe~\""

    Zoe "\"You give it a try next, {w}Tristan!\""

    scene bg perya
    with dissolve
    #-----------------------------------------------------------------------------------------------------------------------------
    "Tristan throws, his first dart landing just shy of the target."
    "he exhales, steadying his hand like a chess player hovering over a piece before committing to the move."

    show zoe happytalking:
        xoffset -200
        zoom 1.5

    show tristan normal:
        xoffset 500
        zoom 1.5
    
    with dissolve
   
    Zoe "\"You're overthinking it...{w} It's not chess Tristan.\""

    show zoe happy:
        xoffset -200
        zoom 1.5

    show tristan normaltalking:
        xoffset 500
        zoom 1.5
    
    with dissolve

    Tristan "\"Everything's chess if you stare long enough\""

    hide zoe happy
    hide tristan normaltalking

    with dissolve

    "By the end, Zoe wins by a single balloon."

    show zoe smugtalking:
        xoffset -200
        zoom 1.5

    show tristan normal:
        xoffset 500
        zoom 1.5

    with dissolve

    Zoe "\"hehe~\""

    Zoe "\"I guess you're buying isaw this time~\""

    show tristan sadhappytalking:
        xoffset 500
        zoom 1.5
    with dissolve

    Tristan "\"{i}Sigh{/i} {p}I guess I don't mind losing this time...\""

    hide zoe smugtalking
    hide tristan sadhappytalking
    with dissolve

    "She cheers, and Tristan hands the vendor a few bills."
    "Soon, they're walking away with skewers of sizzling isaw{p}the smoky aroma wrapping around them like a blanket."

    show zoe happytalking:
        xoffset 100
        zoom 1.5

    with dissolve
    
    Zoe "\"Man...{w} That was sooo fun!\""
    Zoe "\"But so tiring! hehe\""

    show zoe worried 
    with dissolve

    stop music fadeout 1.0
    
    Zoe "\"...\""

    play sound "audio/SFX/explosion.wav"
    with vpunch
    
    Zoe "*cough*"

    play sound "audio/SFX/explosion.wav"
    with vpunch

    Zoe "*cough*"

    hide zoe worried

    with dissolve

    "Tristan's smile fades..."

    show zoe worried:
        xoffset 100
        zoom 1.5

    with dissolve

    Zoe "\"Tristan?\""

    hide zoe worried

    with dissolve

    "He chews slowly, as if the question itself takes time to digest."

    show zoe worried:
        xoffset -200
        zoom 1.5

    show tristan nervoustalking:
        xoffset 500
        zoom 1.5
    
    with dissolve

    Tristan "\"Just...{w} thinking about some stuff.\""

    show zoe happytalking:
        xoffset -200
        zoom 1.5
    with dissolve

    play music "audio/Music/perya.mp3" volume 0.3 loop

    Zoe "\"bzzt...{w} Wrong answer!\""

    hide tristan nervoustalking
    
    show tristan normal:
        xoffset 500
        zoom 1.5
    
    with dissolve

    Tristan "\"Huh?!\""

    Zoe "\"I brought you here to have fun and take your mind off of things.\""
    
    hide tristan normal
    
    show tristan laugh:
        xoffset 500
        zoom 1.5

    show zoe happy:
        xoffset -200
        zoom 1.5
    with dissolve

    Tristan "\"What the heck?...{w} hahaha\""

    "Tristan laugh showing full expression and laughter"

    show zoe happytalking:
        xoffset -200
        zoom 1.5
    with dissolve

    Zoe "\"Hey...{w} Why you are laughing?\""

    show zoe giggle:
        xoffset -200
        zoom 1.5
    with dissolve

    "Zoe smiled back...{p}This is the first time she saw Tristan genuinely smile"

    show zoe happytalking:
        xoffset -200
        zoom 1.5
    with dissolve

    Zoe "\"That's the spirit!!!\""

    hide tristan laugh
    hide zoe happytalking

    show zoe worried:
        xoffset 100
        zoom 1.5
    with dissolve

    stop music fadeout 1.0
    
    Zoe "\"...\""

    play sound "audio/SFX/explosion.wav"
    with vpunch
    
    Zoe "*cough*"

    play sound "audio/SFX/explosion.wav"
    with vpunch

    Zoe "*cough*"

    hide zoe worried

    with dissolve

    "As Zoe shouted she coughed again… this time it looked worse than usual"

    show zoe worried:
        xoffset -200
        zoom 1.5

    show tristan nervoustalking:
        xoffset 500
        zoom 1.5
    with dissolve

    Tristan "\"You okay Zoe?\""

    show tristan nervous
    with dissolve

    show zoe happytalking:
        xoffset -200
        zoom 1.5
    with dissolve
        
    Zoe "\"More okay than you.{p}HAHAHAHAHAHAHA!\""

    show zoe happy:
        xoffset -200
        zoom 1.5
    with dissolve

    "Tristan is worried but still put up a little smile"

    show tristan normaltalking:
        xoffset 500
        zoom 1.5

    with dissolve

    Tristan "\"It's fine...{w} if you're happy{w} then it's all fine\""
    
    play sound "audio/SFX/static.mp3"
    scene bg staticeffect
    with hpunch
    show static2
    with hpunch
    scene bg perya

    show tristan normal:
        xoffset 500
        zoom 1.5

    show zoe happytalking:
        xoffset -200
        zoom 1.5
    with dissolve

    Zoe "\"hmm??{w} What did you say?\""

    show tristan happytalking

    show zoe happy:
        xoffset -200
        zoom 1.5
    with dissolve

    Tristan "\"Nothing...{w} hehe\""

    show zoe smugtalking:
        xoffset -200
        zoom 1.5

    show tristan happy
    
    with dissolve

    Zoe "\"Hooo...{w} So you're taking revenge on me\""

    play sound "audio/SFX/hit.mp3" volume 0.3
    with hpunch

    "Zoe uses punch on Tristan"

    show zoe happy:
        xoffset -200
        zoom 1.5
    with dissolve

    "..."

    "It's Super Effective!"

    show tristan annoyedtalking:
        xoffset 500
        zoom 1.5
    with dissolve

    play music "audio/Music/perya.mp3" volume 0.3 loop

    Tristan "\"Hey cut it out!\""

    show zoe smugtalking:
        xoffset -200
        zoom 1.5
    with dissolve

    Zoe "\"hehe~\""

    #fade transition siguro dito

    hide tristan normal
    hide zoe happy

    with dissolve

    "While the both of them were strolling around the fare, Tristan stumbled upon 2 people having an intense chess match..."

    show tristan normal:
        zoom 2
        yoffset 1000
        center
    play music "audio/Music/Thoughts.mp3"
    with dissolve

    Chessplayer1 "\"Check!\""

    Chessplayer2 "\"What?!{w} I did not see that move! What the heck?!\""

    Chessplayer1 "\"Well... Better look closer or you're going to lose in just a few moves\""

    Chessplayer2 "\"Not gonna lie..{w} You're so good at this game I don't even know if you're joking anymore.\""

    Chessplayer1 "\"hehehe.\""

    Tristan "{i}In his head{/i}{p=0}Looking at this match...{w} reminds me of what Emil said about me in school the other day…"

    Tristan "\"...\""

    # Flashback to when that interaction happened between Tristan and Emil

    "Zoe and Tristan then proceed to conclude their perya date and are heading to the park..."

    scene black screen
    stop music fadeout 1.0
    with dissolve

    jump Chapter6

    return