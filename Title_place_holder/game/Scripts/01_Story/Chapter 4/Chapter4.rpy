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
    scene bg thoughts
    with dissolve
    pause 3.0

    play sound "audio/beep.mp3"
    "BEEP!..."
    play sound "audio/beep.mp3"
    "BEEP!....."
    play sound "audio/beep.mp3"
    "BEEP!......."

    "Bzzzt!"

    scene bg room
    with fade

    show tristan talking at center
    
    Tristan "\"*grunts*{p=0}I feel exhausted from last time… but it sure is fun.\""

    Tristan "\"Well… I guess it's time to go to work.\""

    show tristan normal

    "A flicker of memory — {p}he remembers Zoe saying they both go to the same school."
    
    show tristan talking:
        yoffset 1000
        zoom 2
        center
    Tristan "\"What if… {w}Nah, not a chance. {w}You shouldn't get your hopes up, Tristan.\""
    show tristan nervous:
        yoffset 1000
        zoom 2
        center
    "Tristan then went to school hoping to meet Zoe."

    show bg thoughts
    with dissolve
    pause 1
    hide tristan flustered
    with dissolve

    pause 3.0
    show screen c4 with fade
    pause 5.0
    hide screen c4 with fade

    show bg schoolhallway

    show tristan nervoustalking:
        yoffset 1000
        zoom 2
        center
    Tristan "\"It's been awhile since I last went here…\""

    Tristan "\"I honestly can't recall the last time I set foot in this university.\""

    Tristan "\"I don't even know what gave me the courage to go back here…\""

    Tristan "\"What was the drive that made me go to this university anyway, was it really…\""

    Tristan "\"Her?\""
    show tristan flustered:
        yoffset 1000
        zoom 2
        center
    pause 2

    #  *Television static fx* 
    scene bg staticeffect
    play sound "audio/static.mp3"
    with hpunch
    with hpunch

    scene bg schoolhallway
    show tristan normal:
        yoffset 1000
        zoom 2
        center
    pause 2.0
    show tristan talking:
        yoffset 1000
        zoom 2
        center

    Tristan "\"Ow! This stupid headache again…\""

    Tristan "\"Welp, whatever the reason may be I am here anyways, so might as well…\""
    show tristan normal:
        yoffset 1000
        zoom 2
        center
    pause 1.0
    hide tristan normal
    with fade
    "Afternoon sunlight spills through the tall hallway windows, painting golden streaks across the floor."
    
    "Students drift past in pairs and groups, chatting as they leave for the day."
    
    scene bg thoughts
    show tristan nervoustalking:
        yoffset 1000
        zoom 2
        center
    with dissolve
    Tristan "(in his head){p=0}Knew it...{w} didn't see her all day."
    scene bg schoolhallway
    show tristan normal:
        yoffset 1000
        zoom 2
        center
    hide tristan normal
    with dissolve
    
    play sound "audio/bell.mp3"
    "The bell rings..."
    "He Steps out of the classroom, adjusting his bag strap."
    "As he turns the corner—" 
    show tristan normal:
        yoffset 1000
        zoom 2
        center
    with moveinleft

    "???" "Tristan?"

    "Tristan stops."
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    with move
    show emil normal:
        yoffset 1000
        xoffset -500
        zoom 2
        center
    with moveinleft

    "Standing in front of him is Emil Navarro.{p}Taller than before."
    "His expression somewhere between relief and frustration."
    show tristan nervoustalking:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    Tristan "\"…Emil.\""
    show tristan nervous:
        yoffset 1000
        xoffset 500
        zoom 2
        center

    Emil "Man, it's really you."
    Emil "I thought you dropped off the face of the earth."

    show tristan nervoustalking:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    Tristan "\"Been...{w}busy.\""
    show tristan nervous:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    Emil "*sighs*{p=0} Busy, huh?"
    Emil "I've been checking every tournament list for months. Your name's never there."

    Tristan "\"...\""
    show tristan nervoustalking:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    Tristan "\"Guess I moved on.\""
    show tristan nervous:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    pause 1.0
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        center

    Emil "Moved on?!" 
    Emil "Tristan...{w}you love the game.{p}You fought for every piece on the board."
    Emil "What happened to you?!"

    #  *Television static fx* 
    scene bg staticeffect
    play sound "audio/static.mp3"
    with hpunch
    with hpunch

    scene bg schoolhallway
    show tristan nervous:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    show emil normal:
        yoffset 1000
        xoffset -500
        zoom 2
        center
    Tristan "\"...\""
    
    Emil "Would you say something!"
    show tristan nervoustalking:
        yoffset 1000
        xoffset 500
        zoom 2
        center
    Tristan "\"Like I said…{w}I moved on!\""
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
        center

    Emil "Don't give me that answer...{p=0}We both know you love chess."
    Emil "As your rival I won't allow this!"

    #  *Television static fx* 

    "Emil grabs Tristan by the collar."

    Emil "As your friend...{w} I won't allow this!"

    "The air feels tense and heavy…"

    scene bg thoughts
    show zoe talking:
        yoffset 1000
        zoom 2
        center
    with fade
    Zoe "(in her head){p=0}Is that Tristan's voice?"
    Zoe "\"I don't doubt that monotonous voice hehehe.\""
    Zoe "\"Yo Tristan!\""
    Zoe "\"Zoe Gonzales is reporting for du-\""

    scene bg schoolhallway
    show zoe normal:
        yoffset 1000
        xoffset 700
        zoom 2
        right
    with move
    show tristan nervous:
        yoffset 1000
        zoom 2
        center
    show emil normal:
        yoffset 1000
        xoffset -400
        zoom 2
        center
    with moveinleft

    with fade

    "Zoe is shocked at the scene in front of her."
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

    show emil normal:
        yoffset 1000
        xoffset -700
        zoom 2
        center
    with move

    "Emil lets go of Tristan...{p=0}Tristan slowly walks toward Zoe."

    Emil "I...{w}I did not mean to-"

    show tristan nervoustalking:
        yoffset 1000
        zoom 2
        center

    Tristan "\"It's okay...{p=0}I'm all out of pieces...{p=0}My king is cornered...\""
    Tristan "\"I resign...{w}I quit chess.\""
    show tristan nervous:
        yoffset 1000
        zoom 2
        center
    

    "Emil felt guilt, frustration, and hopelessness as Tristan utters those words."

    scene bg thoughts
    with dissolve
    "A rival without adversary — {p=0}A lone king on an empty board.{p=0}Every square a silent grave where knights once leapt and queens once danced."
    "Now only the ticking clock remains...{p=0}making moves for no one."

    Zoe "\"What happened...{w}Tristan?\""

    scene bg schoolhallway
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

    Tristan "\"It's nothing...{w}just a little bit of catching up with an old friend.\""
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
    Zoe "\"Well, if you say so...\""
    show zoe worried:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    "Zoe casts suspicion and doubt on the words Tristan said"
    show zoe tease:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    "..."
    show zoe teasetalking:
        yoffset 1000
        xoffset 500
        zoom 2
        right
    Zoe "\"I have an idea...\""
    Zoe "\"hehe.\""


    show bg thoughts
    with dissolve
    pause 1
    hide tristan flustered
    hide zoe normal
    with dissolve
    jump Chapter5
    return
