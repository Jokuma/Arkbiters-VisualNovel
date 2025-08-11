transform enlarge:
    zoom 1.5
    center

screen c2:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0.5
        text "Chapter 2: Opening Moves in Bloom " yalign 0.5 xalign 0.5
        
label Chapter2:
    pause 3.0
    show screen c2 with fade
    pause 5.0
    hide screen c2 with fade

    define dissolve = Dissolve(0.2)

    "The warm afternoon sun spills over the park. Gentle wind carries the faint scent of flowers. Birds chirp as children run around laughing."
    scene bg park
    show tristan nervous:
        yoffset 1000
        zoom 2
        center 
    with dissolve
   
    "Tristan waits nervously in the park"

    pause 1

    show bg thoughts
    show tristan nervous:
        yoffset 1000
        zoom 2
        center 
    with dissolve

    Tristan "(In his head){p=0}Why am I here?!"
    Tristan "(In his head){p=0}Wait."
    Tristan "(In his head){p=0}Wait..."
    Tristan "(In his head){p=0}This is so sudden."
    Tristan "..."
    Tristan "(In his head){p=0}A useless loser like me is on a date?"
    Tristan "(In his head){p=0}Heck..."
    Tristan "(In his head){p=0}Why did I even agree."
    Tristan "(In his head){p=0}Ugh!...{w} my head hurts." with hpunch

    show bg park
    show tristan nervous:
        yoffset 1000
        zoom 2
        center 


    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
    with move

    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
    with moveinleft
    with dissolve
    

    #zoe shows up
    pause 1
    
    show zoe teasetalking:
        yoffset 1000
        xoffset -500
        zoom 2
    with dissolve

    Zoe "\"Tristan Garcia, reporting late are we?\""
    show zoe giggletalking:
        yoffset 1000
        xoffset -500
        zoom 2
    with dissolve

    Zoe "\"*giggles* *giggles*\""

    "Zoe hands him a drink"

    #show cutscene here
    scene bg waterbottle1
    with dissolve

    Tristan "\"H-Hey...\""
    Tristan "\"You didn't have to get me this.\""

    Zoe "\"I wanted to!\""
    scene bg waterbottle2
    with dissolve
    pause 1
    scene bg waterbottle3
    with dissolve

    Zoe "\"You looked like you'd melt if you sat here alone too long.\""

    #  *Television static fx* 
    play sound "audio/static.mp3"
    scene bg staticeffect
    with hpunch
    with hpunch
    scene bg waterbottle3
    Tristan "(In his head){p=0}That smile again..."
    Tristan "(In his head){p=0}Why does it feel like I've seen it a before"

    scene bg park
    with dissolve
    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    show tristan nervous:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    with dissolve
    show zoe talking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    "Zoe notices his expression."
    show zoe worriedtalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"Headache again?\""
    show zoe worried:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    show tristan talking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    with dissolve
    Tristan "\"N-no.\""
    Tristan "\"I'm fine, probably just the heat.\""
    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    with dissolve
    show zoe talking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"Hmm...\""
    Zoe "\"If you say so.\""
    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"...\""
    show zoe talking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"Come on.{w} Let's take a walk!\""
    hide tristan normal
    hide zoe normal
    with dissolve

    "They start walking along a shaded path lined with trees, their shadows overlapping on the pavement."
    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    with dissolve

    show zoe talking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "\"So...\""
    Zoe "\"You have any hobbies?\""
    show zoe teasetalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "\"Don't say sleeping!\""
    show tristan nervous:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    "Tristan, hesitant at first, but he felt that Zoe would understand"
    show tristan talking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    Tristan "\"I used to play chess...\""
    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    show zoe talking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "\"Used to?\""
    Zoe "\"What happened?\""
    show zoe teasetalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "\"Hooo...{w} Did the king sue you?\""
    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    show tristan talking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    Tristan "\"No...\""
    show tristan nervoustalking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    Tristan "\"I just...{w} Stopped.\""
    Tristan "\"Lost interest...{w} I guess.\""
    show tristan nervous:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    "..."
    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    show zoe talking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "\"Such a Shame.\""
    Zoe "\"You probably would've crushed me in a match.\""
    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    show tristan talking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    Tristan "\"N-not really...\""
    Tristan "\"I'm not that good.\""
    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left

    show zoe teasetalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "\"Hah!\""
    Zoe "\"You're just saying that so I'll underestimate you.\""
    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    "She nudges Tristan shoulder lightly." with hpunch

    Zoe "\"...\""
    show zoe talking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "\"Well...\""
    Zoe "\"Since you're stuck walking with me, you might as well learn something about me.\""
    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    show tristan talking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    Tristan "\"Yeah, honestly speaking...\""
    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    show zoe talking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "\"Because...\""
    show zoe teasetalking:
        yoffset 1800
        xoffset 0
        zoom 3
        center
    hide tristan normal
    Zoe "\"Deep down...{w}You're curious.\""
    show tristan talking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    show zoe tease:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Tristan "\"M-maybe...\""
    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left

    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    "She looks away briefly, her smile softening."

    show zoe talking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "\"Let's just say...{w} I like doing things I really want to do.\""
    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Tristan "..."
    show tristan talking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    Tristan "\"That seems very vague.\""
    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left

    show zoe talking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "\"Good.\""
    hide tristan normal
    show zoe teasetalking:
        yoffset 1800
        xoffset 0
        zoom 3
        center
    Zoe "\"I like being mysterious.\""

    #  *Television static fx* 
    show bg staticeffect
    play sound "audio/static.mp3"
    hide zoe teasetalking
    with hpunch
    with hpunch
    show tristan nervous:
        yoffset 1000
        xoffset 300
        zoom 2
        left

    hide zoe normal
    show bg thoughts
    show tristan nervous:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    Tristan "(In his head){p=0}That again?!"
    Tristan "..."
    Zoe "\"Earth to Tristan!!!\""
    show tristan talking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    show zoe worried:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    show bg park
    with dissolve

    Tristan "\"S-sorry...\""
    Tristan "\"I just...\""
    show tristan talking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    Tristan "\"You remind me of someone.\""
    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    show zoe tease:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "\"Hooo...\""
    show zoe teasetalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "\"An ex-girlfriend?\""
    Zoe "\"Daydreaming of another when you have a real one here.\""
    show zoe tease:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    show tristan flusteredtalking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    Tristan "\"N-no!\""
    Tristan "\"I mean...\""
    show tristan nervoustalking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    Tristan "\"I don't...{w} It's just\""
    show zoe giggle:
        yoffset 1000
        xoffset -500
        zoom 2
        left

    "..."
    show zoe giggle:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    "Zoe laughs, brushing it off, and starts walking again."
    show tristan flustered:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    pause 2
    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    show zoe talking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    Zoe "\"Alright, enough yapping. Race you to the ice cream stand!\""
    Zoe "\"Loser has to pay\""
    show zoe normal:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    hide zoe normal
    with moveoutleft
    "Zoe bolted ahead"
    
    show tristan flusteredtalking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    Tristan "\"Hey! No fair!\""

    "Tristan showed a conflicted expression before he breaks into a small, genuine smile and chases after her."
    hide tristan flusteredtalking
    with moveoutleft
    with dissolve

    jump Chapter3
    with fade
    return