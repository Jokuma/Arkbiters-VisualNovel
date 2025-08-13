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

    scene bg park
    play music "audio/Music/ParkDay.mp3" volume 0.3 fadein 1
    with dissolve

    "The warm afternoon sun spills over the park. Gentle wind carries the faint scent of flowers. Birds chirp as children run around laughing."

    show tristan nervous:
        yoffset 1000
        zoom 2
        center
    with dissolve
   
    "Tristan waits nervously in the park"

    show thoughts
    play music "audio/Music/Thoughts.mp3" volume 0.3 fadein 0.3 loop
    show tristan nervous zorder 2:
        yoffset 1000
        center
        zoom 2
    with dissolve

    Tristan "{i}In his head{/i}{p=0}Why am I here?!"
    Tristan "{i}In his head{/i}{p=0}Wait."
    Tristan "{i}In his head{/i}{p=0}Wait..."
    Tristan "{i}In his head{/i}{p=0}This is so sudden."
    Tristan "..."
    Tristan "{i}In his head{/i}{p=0}A useless loser like me is on a date?"
    Tristan "{i}In his head{/i}{p=0}Heck..."
    Tristan "{i}In his head{/i}{p=0}Why did I even agree to this..."

    show bg park
    hide thoughts
    play music "audio/Music/ParkDay.mp3" volume 0.3 fadein 1
    with dissolve
 
    show tristan normal:
        yoffset 1000
        xoffset 500
        zoom 2
    with move

    play sound "audio/SFX/walk.mp3"
    show zoe happy:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with moveinleft
    
    show zoe smugtalking:
        yoffset 1000
        xoffset -500
        zoom 2
    with dissolve

    Zoe "\"Tristan Garcia, reporting late are we?\""
    show zoe giggle:
        yoffset 1000
        xoffset -500
        zoom 2
    with dissolve

    Zoe "{i}giggles{/i}"

    "Zoe hands him a drink"

    #show cutscene here
    scene bg waterbottle1
    play music "audio/Music/WaterBottle.mp3" volume 0.3 fadein 1
    with dissolve  

    Tristan "\"H-Hey...\""
    Tristan "\"You didn't have to get me this.\""
    
    Zoe "\"I wanted to!\""
    scene bg waterbottle2
    with dissolve
    Zoe "\"Besides...\""
    Zoe "\"You looked like you'd melt if you sat here alone too long...\""  
    scene bg waterbottle3
    with dissolve
    Zoe "\"Like an ice cream!\""

    play sound "audio/SFX/static.mp3"
    scene bg staticeffect
    with hpunch
    show static2
    with hpunch
    scene bg waterbottle3
    show thoughts
    with dissolve
    Tristan "{i}In his head{/i}{p=0}That smile again..."
    Tristan "{i}In his head{/i}{p=0}Why does it feel like I've seen it a before"
    play music "audio/Music/ParkDay.mp3" volume 0.3 fadein 1
    
    scene bg park
    show zoe worried:
        yoffset 1000
        xoffset -500
        zoom 2
        left

    show tristan nervous:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    hide thoughts
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

    show tristan normaltalking:
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

    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"Hmm...\""
    Zoe "\"If you say so.\""
    show zoe happy:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    Zoe "\"...\""
    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"Come on.{w} Let's take a walk!\""
    hide tristan normal
    hide zoe happy
    with dissolve

    "They start walking along a shaded path lined with trees, their shadows overlapping on the pavement."

    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left

    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"So...\""
    Zoe "\"You have any hobbies?\""
    show zoe smugtalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"Don't say sleeping!\""
    show tristan nervous:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    show zoe happy:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    "Tristan, hesitant at first, but he felt that Zoe would understand"
    
    Tristan "\"I used to play chess...\""

    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left

    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    Zoe "\"Used to?\""
    Zoe "\"What happened?\""

    show zoe smugtalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    Zoe "\"Hooo...{w} Did the king sue you?\""

    show zoe happy:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    show tristan normaltalking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    with dissolve

    Tristan "\"No...\""

    show tristan nervoustalking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    with dissolve
    Tristan "\"I just...{w} Stopped.\""
    Tristan "\"Lost interest...{w} I guess.\""
    
    show tristan nervous:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    with dissolve

    "..."

    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    Zoe "\"Such a Shame.\""
    Zoe "\"You probably would've crushed me in a match.\""

    show zoe happy:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    show tristan normaltalking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    with dissolve

    Tristan "\"N-not really...\""
    Tristan "\"I'm not that good.\""

    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left

    show zoe smugtalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    Zoe "\"Hah!\""
    Zoe "\"You're just saying that so I'll underestimate you.\""

    show zoe happy:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    play sound "audio/SFX/hit.mp3" volume 0.3

    with hpunch

    "She nudges Tristan shoulder lightly." 

    Zoe "\"...\""

    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    Zoe "\"Well...\""
    Zoe "\"Since you're stuck walking with me, you might as well learn something about me.\""

    show zoe happy:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    show tristan normaltalking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    with dissolve

    Tristan "\"Yeah, honestly speaking...\""

    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    Zoe "\"Because...\""

    show zoe smugtalking:
        yoffset 1800
        xoffset 0
        zoom 3
        center
    
    hide tristan normal
    with dissolve

    Zoe "\"Deep down...{w} You're curious.\""

    show tristan normaltalking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    show zoe smug:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    Tristan "\"M-maybe...\""

    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left

    show zoe happy:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    "She looks away briefly, her smile softening."

    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    Zoe "\"Let's just say...{w} I like doing things I really want to do.\""

    show zoe happy:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    Tristan "..."

    show tristan normaltalking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    with dissolve

    Tristan "\"That seems very vague.\""

    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left

    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    Zoe "\"Good.\""

    hide tristan normal
    show zoe smugtalking:
        yoffset 1800
        xoffset 0
        zoom 3
        center
    with dissolve

    Zoe "\"I like being mysterious.\""

    play sound "audio/SFX/static.mp3"
    scene bg staticeffect
    with hpunch
    show static2
    with hpunch

    scene bg park
    show zoe smugtalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    show thoughts zorder 2
    show tristan nervous zorder 2:
        yoffset 1000
        xoffset 300
        left
        zoom 2
    with dissolve
    play music "audio/Music/Thoughts.mp3" volume 0.3 fadein 0.3 loop

    Tristan "{i}In his head{/i}{p=0}That again?!"
    Tristan "..."
    hide thoughts
    show zoe worriedtalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve
    play music "audio/Music/ParkDay.mp3" volume 0.3 fadein 1
    Zoe "\"Earth to Tristan!!!\""

    show tristan normaltalking:
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

    show tristan normaltalking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    with dissolve

    Tristan "\"You remind me of someone.\""

    show tristan normal:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    show zoe smug:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    Zoe "\"Hooo...\""

    show zoe smugtalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    Zoe "\"An ex-girlfriend?\""
    Zoe "\"Daydreaming of another when you have a real one here.\""

    show zoe smug:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    show tristan flusteredtalking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    with dissolve

    Tristan "\"N-no!\""
    Tristan "\"I mean...\""

    show tristan nervoustalking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    with dissolve

    Tristan "\"I don't...{w} It's just\""

    show zoe smile:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    "..."

    show zoe smile:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

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
    show zoe happytalking:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    with dissolve

    Zoe "\"Alright, enough yapping. Race you to the ice cream stand!\""
    Zoe "\"Loser has to pay\""

    show zoe happy:
        yoffset 1000
        xoffset -500
        zoom 2
        left
    hide zoe happy
    play sound "audio/SFX/walk.mp3" volume 0.3
    with moveoutleft

    "Zoe bolted ahead"
    
    show tristan flusteredtalking:
        yoffset 1000
        xoffset 300
        zoom 2
        left
    with dissolve

    Tristan "\"Hey! No fair!\""

    "Tristan showed a conflicted expression before he breaks into a small, genuine smile and chases after her."
    
    play sound "audio/SFX/walk.mp3" volume 0.3
    hide tristan flusteredtalking
    with moveoutleft
    with dissolve

    stop music
    jump Chapter3
    return