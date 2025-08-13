transform enlarge:
    zoom 1.5
    center

screen c4:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0.5
        text "Chapter 4 : Unmoved Pieces " yalign 0.5 xalign 0.5

label Chapter4:

    scene black screen
    with dissolve
    pause 3.0

    define dissolve = Dissolve(0.2)
    define fade1 = Fade(0.5, 0.0, 0.5)
    define slow_right = MoveTransition(2.0, leave=offscreenright, leave_time_warp=_warper.easeout)
    define slow_left = MoveTransition(2.0, leave=offscreenleft, leave_time_warp=_warper.easeout)

    play sound "audio/SFX/beep.mp3"
    "BEEP!..."
    play sound "audio/SFX/beep.mp3"
    "BEEP!....."
    play sound "audio/SFX/beep.mp3"
    "BEEP!......."
    play sound "audio/SFX/click.mp3"
    "Click..."

    scene bg tristanroom
    show tristan normaltalking:
        xoffset 100
        yoffset 20
        zoom 1.5
    play music "audio/Music/tristanhome.ogg" volume 0.3 fadein 1
    with dissolve

    play sound "audio/SFX/explosion.wav"
    Tristan "{i}grunts{/i}" with hpunch

    Tristan "\"I feel exhausted from last time… but it sure is fun.\""

    Tristan "\"Well… I guess it's time to go to work.\""

    show tristan normal
    with dissolve

    "A flicker of memory — {p}He remembers Zoe saying they both go to the same school."
    
    show tristan normaltalking:
        xoffset -100
        yoffset 1000
        center
        zoom 2

    Tristan "\"What if… {w}Nah, not a chance. {w}You shouldn't get your hopes up, Tristan.\""

    stop music fadeout 1.0

    show black screen
    with dissolve

    "Tristan then went to school."
    stop music
    show screen c4 with fade
    pause 5.0
    hide screen c4 with fade

    hide black screen

    show bg schoolhallway

    show tristan nervoustalking:
        yoffset 1000
        zoom 2
    play music "audio/Music/school.mp3" volume 0.3 fadein 1
    with dissolve

    Tristan "\"It's been awhile since I last went here…\""

    Tristan "\"I honestly can't recall the last time I set foot in this university.\""

    Tristan "\"I don't even know what gave me the courage to go back here…\""

    Tristan "\"What was the drive that made me go to this university anyway, was it really…\""

    Tristan "\"Her?\""

    show tristan flustered:
        yoffset 1000
        zoom 2
        center
    with dissolve

    Tristan "\"...\""
    
    play sound "audio/SFX/static.mp3"
    scene bg staticeffect
    with hpunch
    show static2
    with hpunch


    scene bg schoolhallway
    show thoughts zorder 2
    show tristan annoyedtalking zorder 2:
        yoffset 1000
        zoom 2
        center
    with dissolve

    Tristan "\"Ow! This stupid headache again…\""

    show tristan normaltalking:
        yoffset 1000
        zoom 2
    with dissolve

    Tristan "\"Welp, whatever the reason may be I am here anyways, so might as well…\""
    
    show tristan normal:
        yoffset 1000
        zoom 2
        center
    with dissolve
    hide tristan normal
    play sound "audio/SFX/walk.mp3" volume 0.3 loop
    with slow_right
    stop sound fadeout 0.5
    scene black screen
    with fade
    stop sound

    "Afternoon sunlight spills through the tall hallway windows, painting golden streaks across the floor."
    "Students drift past in pairs and groups, chatting as they leave for the day."
    
   
    scene bg schoolhallway
    show thoughts zorder 2
    show tristan nervoustalking zorder 2:
        yoffset 1000
        zoom 2
        center
    with dissolve

    Tristan "{i}In his head{/i}{p=0}Knew it...{w} didn't see her all day."
    
    show tristan normal:
        yoffset 1000
        zoom 2
        center
    hide tristan normal
    with dissolve
    
    scene black screen
    play sound "audio/SFX/schoolbell.mp3"
    play music "audio/Music/school.mp3" volume 0.3 fadein 1
    "The bell rings..."
    "He steps out of the classroom, adjusting his bag strap."
    "As he turns the corner—" 
    scene bg schoolhallway
    show tristan normal:
        yoffset 1000
        zoom 2
        center
    with dissolve

    "???" "Tristan?"

    "Tristan stops."
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    with move
    show emil normal:
        yoffset -10
        xoffset -100
        zoom 1.9

    with moveinleft

    "Standing in front of him is Emil Navarro.{p}Taller than before."
    "His expression somewhere between relief and frustration."

    show tristan nervoustalking:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    with dissolve

    Tristan "\"…Emil.\""

    show tristan nervous:
        yoffset 1000
        xoffset 500
        zoom 2
        center

    show emil surprised:
        yoffset -10
        xoffset -100
        zoom 1.9
    with dissolve

    Emil "\"Man, it's really you.\""
    Emil "\"I thought you dropped off the face of the earth.\""

    show tristan nervoustalking:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    show emil normal:
        yoffset -10
        xoffset -100
        zoom 1.9
    with dissolve

    Tristan "\"Been...{w} busy.\""

    show emil surprised:
        yoffset -10
        xoffset -100
        zoom 1.9

    show tristan nervous:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    with dissolve

    Emil "{i}sighs{/i}{p=0}\"Busy, huh?\""
    Emil "\"I've been checking every tournament list for months. Your name's never there.\""

    Tristan "\"...\""

    show emil worried:
        yoffset -10
        xoffset -100
        zoom 1.9

    show tristan nervoustalking:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    with dissolve

    Tristan "\"Guess I moved on.\""

    show tristan nervous:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    pause 1.0
    show emil frustratedtalking:
        yoffset -10
        xoffset -100
        zoom 1.9
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    with dissolve

    Emil "\"Moved on?!\"" 
    Emil "\"Tristan...{w} you love the game.{p}You fought for every piece on the board.\""
    Emil "\"What happened to you?!\""

    play music "audio/Music/school.mp3" volume 0.3 fadein 1
    play sound "audio/SFX/static.mp3"
    scene bg staticeffect
    with hpunch
    show static2
    with hpunch

    scene bg schoolhallway
    show tristan nervous:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    show emil frustrated:
        yoffset -10
        xoffset -100
        zoom 1.9
    with dissolve

    Tristan "\"...\""

    show emil frustratedtalking:
        yoffset -10
        xoffset -100
        zoom 1.9
    with dissolve
    
    Emil "\"Would you say something!\""
    show emil frustrated:
        yoffset -10
        xoffset -100
        zoom 1.9
    show tristan nervoustalking:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    with dissolve
    Tristan "\"Like I said…{w} I moved on!\""
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    show emil frustratedtalking:
        yoffset -10
        xoffset -100
        zoom 1.9
    with dissolve

    Emil "\"Don't give me that answer...{p=0}We both know you love chess.\""
    Emil "\"As your rival I won't allow this!\""

    #  *Television static fx* 
    play sound "audio/SFX/static.mp3"
    scene bg staticeffect
    with hpunch
    show static2
    with hpunch
    scene bg schoolhallway
    
    ########################################################################################## cutscene

    "Emil grabs Tristan by the collar."

    Emil "\"As your friend...{w} I won't allow this!\""

    "The air feels tense and heavy…"
    
    scene bg schoolhallway
    show thoughts zorder 2
    show zoe happytalking zorder 2:
        yoffset 1000
        center
        zoom 2
    with fade

    Zoe "{i}(in her head){/i}{p=0}Is that Tristan's voice?"

    scene bg schoolhallway
    show zoe happytalking:
        yoffset 1000
        zoom 2
        center
    with dissolve

    Zoe "\"I don't doubt that monotonous voice hehehe.\""
    Zoe "\"Yo Tristan!\""
    Zoe "\"Zoe Gonzales is reporting for du-\""

    show zoe worried:
        yoffset 1000
        zoom 2
        center
    with dissolve

    Zoe "\"...\""

    show zoe worriedtalking:
        yoffset 1000
        zoom 2
        center
    with dissolve

    Zoe "\"Tristan...?\""

    play sound "audio/SFX/walk.mp3"
    hide zoe worriedtalking
    with moveoutleft

    Zoe "Zoe quickly went to the scene..."

    with fade

    "Zoe is shocked at the scene in front of her."

    show zoe worried:
        yoffset 1000
        xoffset 700
        zoom 2
        right

    show tristan nervous:
        yoffset 1000
        zoom 2
        center
    
    show emil frustrated:
        yoffset 1000
        xoffset -400
        zoom 2
        center
    with dissolve
    
    "Tristan and Emil glanced over Zoe's direction."
    show tristan nervoustalking:
        yoffset 1000
        zoom 2
        center
    Tristan "\"Oh… perfect timing. Want to go home together?\""
    show tristan nervous:
        yoffset 1000
        zoom 2
        center
    
    "Zoe is still in shock."

    show zoe worriedtalking:
        yoffset 1000
        xoffset 700
        zoom 2
        right
    with dissolve

    Zoe "\"U-hmm… yes, let's go together.\""

    "She says reluctantly."

    show emil worried:
        yoffset 1000
        xoffset -700
        zoom 2
        center
    with move

    "Emil lets go of Tristan...{p=0}Tristan slowly walks toward Zoe."

    show emil worriedtalk:
        yoffset 1000
        xoffset -700
        zoom 2
        center
    with dissolve

    Emil "\"I...{w}I did not mean to-\""

    show tristan nervoustalking:
        yoffset 1000
        zoom 2
        center

    Tristan "\"It's okay...{p=0}I'm all out of pieces...{p=0}My king is cornered...\""
    Tristan "\"I resign...{w} I quit chess.\""
    show tristan nervous:
        yoffset 1000
        zoom 2
        center
    

    "Emil felt guilt, frustration, and hopelessness as Tristan utters those words."

    scene black screen
    with dissolve
    "A rival without adversary — {p=0}A lone king on an empty board.{p=0}Every square a silent grave where knights once leapt and queens once danced."
    "Now only the ticking clock remains...{p=0}making moves for no one."

    scene bg schoolhallway
    show tristan nervous:
        yoffset 1000
        xoffset -500
        zoom 2
        center
    show zoe worriedtalking:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve

    Zoe "\"What happened...{w} Tristan?\""

    show tristan nervoustalking:
        yoffset 1000
        xoffset -500
        zoom 2
        center
    show zoe worried:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve

    Tristan "\"It's nothing...{w} just a little bit of catching up with an old friend.\""

    show tristan nervous:
        yoffset 1000
        xoffset -500
        zoom 2
        center
    show zoe worriedtalking:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve

    Zoe "\"Well, if you say so...\""

    show zoe worried:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve

    "Zoe casts suspicion and doubt on the words Tristan said"

    show zoe smug:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve

    "..."

    show zoe smugtalking:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve

    Zoe "\"I have an idea...\""

    show zoe smug:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    with dissolve

    Zoe "\"hehe.\""


    show black screen
    with dissolve

    hide zoe smug
    hide tristan nervous

    jump Chapter5

    return