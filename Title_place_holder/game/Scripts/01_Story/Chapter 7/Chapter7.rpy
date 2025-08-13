screen c7:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0.5
        text "Chapter 7 : When the Clock Runs Out " yalign 0.5 xalign 0.5

label Chapter7:
    
    show screen c7 with fade
    pause 5.0
    hide screen c7 with fade

    define fade = Fade(0.5, 2.0, 0.5)
    define dissolve = Dissolve(0.2)
    
    play music "audio/Music/chess.mp3" volume 0.3 loop

    scene bg gym
    with dissolve

    #-------------------SCENE 1: GYM-------------------

    "Tristan stood at the edge of the crowded gymnasium, heart pounding. After hearing Zoe's encouraging words, he had finally built up the courage to play again."

    "As he entered, Emil's eyes widened in surprise."

    show emil surprised:
        yoffset -70
        xoffset -100
        zoom 2.0

    show tristan normal:
        xoffset 350
        yoffset -80
        zoom 2.0
    with dissolve

    Emil "\"Tristan? You're really here.\""

    show emil normal:
        yoffset -70
        xoffset -100
        zoom 2.0

    show tristan normaltalking:
        xoffset 350
        yoffset -80
        zoom 2.0
    with dissolve

    Tristan "\"Yeah… and Emil, about what happened before… I'm sorry.\""

    show emil normal:
        yoffset -70
        xoffset -100
        zoom 2.0

    show tristan normal:
        xoffset 350
        yoffset -80
        zoom 2.0
    with dissolve

    "Emil shrugged and smirked."

    show emil surprised:
        yoffset -70
        xoffset -100
        zoom 2.0
    with dissolve

    Emil "\"If you're really sorry… give me an entertaining chess match.\""

    show emil normal:
        yoffset -70
        xoffset -100
        zoom 2.0

    show tristan sadhappytalking:
        xoffset 350
        yoffset -80
        zoom 2.0
    with dissolve

    Tristan "\"Yeah, you're right... Let's have a fun match, Emil.\""

    show bg bracket
    hide emil happy
    hide tristan sadhappytalking

    with dissolve

    "The Chess Tournament has officially started..."

    "Each battle was heated, no one wants to back down without showing a proper fight..."

    hide bg bracket
    show bg finalbracket
    with dissolve
    
    "As the tournament goes on… Emil and Tristan climbs through the ranks and faced each other in the final round."

    "The two sat across the board, the crowd buzzing around them. Pieces clicked, clocks ticked, and tension filled the room."

    scene bg gym

    show emil surprised:
        yoffset -70
        xoffset -100
        zoom 2.0

    show tristan sadhappy:
        xoffset 350
        yoffset -80
        zoom 2.0
    with dissolve

    Emil "\"Hey, never thought we will be facing head to head again on the big stage...{p}I guess you still have it, huh?\""

    show emil normal:
        yoffset -70
        xoffset -100
        zoom 2.0

    show tristan sadhappytalking:
        xoffset 350
        yoffset -80
        zoom 2.0
    with dissolve

    Tristan "\"Yeah, guess so... I've been preparing after all.\""

    show emil surprised:
        yoffset -70
        xoffset -100
        zoom 2.0

    show tristan sadhappy:
        xoffset 350
        yoffset -80
        zoom 2.0
    with dissolve

    Emil "\"Looks like I can't underestimate you...\""

    Emil "\"Don't come crying when I win hehehe...\""

    show emil normal:
        yoffset -70
        xoffset -100
        zoom 2.0

    show tristan sadhappytalking:
        xoffset 350
        yoffset -80
        zoom 2.0
    with dissolve

    Tristan "\"Right back at you!\""

    hide emil happy
    hide tristan sadhappytalking

    with dissolve

    jump chess_game
    return

    ################################################################################

    label Chapter7continue:
    #Chess Minigame // The Evergreen Game
    with squares
    scene bg gym
    #over speaker ----
    Commentator "\"Checkmate! Tristan wins the tournament!\""
    #----------

    play sound "audio/SFX/applause.mp3" volume 0.5

    Tristan "\"Wow I... {w}Actually won...\""

    show emil surprised:
        yoffset -70
        xoffset -100
        zoom 2.0

    show tristan normal:
        xoffset 350
        yoffset -80
        zoom 2.0
    with dissolve

    Emil "\"Damn I lost... haha...\""

    show emil surprised:
        yoffset -70
        xoffset -100
        zoom 2.0

    show tristan normal:
        xoffset 350
        yoffset -80
        zoom 2.0
    with dissolve

    Emil "\"I guess I need to get better...\""

    show emil normal:
        yoffset -70
        xoffset -100
        zoom 2.0

    show tristan sadhappytalking:
        xoffset 350
        yoffset -80
        zoom 2.0
    with dissolve

    Tristan "\"Emil...\""

    show emil surprised:
        yoffset -70
        xoffset -100
        zoom 2.0

    show tristan sadhappy:
        xoffset 350
        yoffset -80
        zoom 2.0
    with dissolve

    Emil "\"Hey, Tristan...\""

    show emil normal:
        yoffset -70
        xoffset -100
        zoom 2.0

    show tristan sadhappytalking:
        xoffset 350
        yoffset -80
        zoom 2.0
    with dissolve

    Tristan "\"Yeah...?\""

    hide tristan sadhappytalking

    show emil normal:
        yoffset -70
        xoffset 300
        zoom 2.0

    with dissolve

    Emil "\"Welcome back!\""

    hide emil happytalking
    with dissolve

    "Overwhelmed with joy, Tristan looked around the crowd to find Zoe… but she was nowhere."

    show tristan nervoustalking:
        xoffset -130
        yoffset -150
        zoom 2
    
    with dissolve

    Tristan "\"Wait where is she? Wasn't she here a few moments ago?\""

    Tristan "\"There's no way she went home immediately right?\""

    stop music fadeout 1.0

    play music "audio/Music/parknight.mp3" volume 0.3 loop

    hide tristan nervoustalking
    with dissolve
    scene bg parknight
    with fade

    #-----------------Sky Scene-----------------

    "After nearly an hour of searching, frustration grew."

    play sound "audio/SFX/static.mp3"
    scene bg staticeffect
    with hpunch
    show static2
    with hpunch
    scene bg parknight

    "Tristan thought back to the park... their first date..."

    with dissolve

    #-----------------Sky Scene-----------------

    #-------------------SCENE 2: PARK-------------------

    "Zoe sat quietly on the worn wooden bench, the dark playground stretching before her like a silent witness." 
    "The faint rustle of leaves whispered in the cold night air, and distant streetlights cast long, shaky shadows." 
    "She didn't look at Tristan when he approached... her gaze fixed on the empty swings swaying gently in the breeze."

    #Tristan (voice soft, tentative):

    show tristan nervoustalking:
        xoffset 500
        zoom 1.5

    show zoe worried:
        xoffset -200
        zoom 1.5

    with dissolve
    
    Tristan "\"There you are! Why did you leave the gym? Why come here, all alone?\""

    show tristan nervous:
        xoffset 500
        zoom 1.5
    with dissolve

    "Zoe's lips trembled, but her voice was barely more than a fragile whisper."

    show zoe worriedtalking:
        xoffset -200
        zoom 1.5
    with dissolve

    Zoe "\"I guess i have to tell you the truth now...\"" #said sadly

    hide zoe worriedtalking
    hide tristan nervous
    with dissolve

    show zoe worried:
        xoffset 100
        zoom 1.5

    play sound "audio/SFX/explosion.wav"
    with vpunch
    
    Zoe "*cough*"

    play sound "audio/SFX/explosion.wav"
    with vpunch

    with dissolve

    Zoe "*cough*"

    hide zoe worried

    with dissolve

    "Her words hung in the air, heavy and fragile like glass about to shatter. Tristan's breath caught in his throat."

    #Tristan (voice tembling):

    show tristan nervoustalking:
        xoffset 500
        zoom 1.5

    show zoe worried:
        xoffset -200
        zoom 1.5
    
    with dissolve

    Tristan "\"What… what do you mean?\""

    show tristan nervous:
        xoffset 500
        zoom 1.5
    
    show zoe worried:
        xoffset -200
        zoom 1.5

    hide zoe worried
    hide tristan nervous

    hide bg parknight

    with dissolve

    #------------Crying Scene------------

    "Zoe slowly turned to him, tears swelling up in her eyes but not falling... {w} yet."

    Zoe "\"I have been a selfish girl\""

    "For a moment, everything went silent except the pounding of Tristan's heart—louder than anything else in the world."

    "His smile faded, cracking like ice underfoot. His hands clenched into fists, but the world felt too heavy to move."

    #Tristan (voice tembling):

    Tristan "\"Y-y-you are not making any sense!\""

    #Zoe voice breaking:

    Zoe "\"I tried to run away so you don't see me like this… Every time we play, I beat you… I guess i can't beat you in a simple game of hide and seek hehe\""

    play sound "audio/SFX/static.mp3"
    scene bg staticeffect
    with hpunch
    show static2
    with hpunch
    scene bg parknight

    "Tears spilled over Zoe's cheeks, glistening like fragile diamonds in the dim light. Yet through the sorrow, she managed a small, bittersweet smile—a smile filled with both gratitude and farewell."

    #Zoe Whispers, Barely Audible

    Zoe "\"Thank you… for everything. For the laughter, the dreams, the moments I never thought I'd have. Because of you… I got to cross off my bucket list.\""

    #Tristan (voice trembling):

    Tristan "\"wait...\""

    "Her voice trembled with emotion, as if speaking these words used the last of her strength."

    play sound "audio/SFX/static.mp3"
    scene bg staticeffect
    with hpunch
    show static2
    with hpunch
    scene bg crying #-----------------------------------------------------------------------------------

    "Zoe's eyes searched Tristan's, desperate to leave something behind, some piece of herself in the moment they shared."

    #Zoe (barely a breath):

    Zoe "\"...\""

    Zoe "\"I love you.\""

    #------------Crying Scene------------

    with dissolve

    #Tristan (voice trembling):

    Tristan "\"wait...\""

    play sound "audio/SFX/static.mp3"
    scene bg staticeffect
    with hpunch
    show static2
    with hpunch
    scene bg blackscreen

    stop music fadeout 1.0

    "......."

    "....."

    "..."

    play sound "audio/SFX/thud.mp3" volume 0.5

    with vpunch

    "{i}Thud{/i}"

    pause 5.0

    with fade

    #-------------------SCENE 3: HOSPITAL-------------------

    play music "audio/Music/hospital.mp3" volume 0.5 fadein 1.0 loop
    
    scene bg hospital
    
    Tristan "\"What is happening… {w} Am I dreaming?\""

    with dissolve

    #----------------Black Screen----------------

    "Tristan is in shock… not really understanding everything"

    Tristan "\"Why...\""

    "Whilst Tristan is thinking about the past events that may cause what happened"

    "He tried to approach the room where Zoe is but he is not permitted it only added more anxiety and fear to him."

    "Seconds passed… {p}Minutes passed… {p}Hours passed…"

    "Suddenly, Tristan saw some doctors and nurses running through the halls… He realized they are running towards the same direction where Zoe's room is..."

    show bg hallway
    with dissolve

    #----------------Black Screen----------------

    #----------------POV Scene----------------

    play sound "audio/SFX/running.mp3" volume 0.5 loop
    
    "Panicked, he rushed over to see if they are going to Zoe's room"

    "As he came closer… he saw a crowd of panicked nurses and doctors around Zoe's room."

    Tristan "\"please… please…\" he said whilst panting"

    "Some of the nurses blocked Tristan from going further"

    "Tristan pushes through and disregarded the heeds of the nurses"

    stop sound

    "As he looks into the room…"

    #----------------POV Scene----------------

    #----------------Black Screen----------------
    
    play sound "audio/SFX/heartbeat.mp3" volume 0.5 loop
    scene bg blackscreen
    with dissolve

    "Tristan stopped..."
    #----------------Black Screen----------------

    #----------------Hospital Room----------------

    #[Flat line sounds]
    stop sound
    play sound "audio/SFX/flatline.mp3" volume 0.5 loop

    "beep..."

    play sound "audio/SFX/static.mp3"
    scene bg staticeffect
    with hpunch
    show static2
    with hpunch
    scene bg blackscreen

    play sound "audio/SFX/flatline.mp3" volume 0.5 loop

    Doctor "\"Time of death-\""

    Tristan "\".{w}.{w}.{w}.{w}.\""

    stop sound

    #----------------Hospital Room----------------

    play sound "audio/SFX/static.mp3"
    scene bg staticeffect
    with hpunch
    show static2
    with hpunch
    scene bg blackscreen

    with fade

    #-------------------SCENE 4: PARK-NIGHT-------------------

    #*Cut to Tristan sitting on the bench at the park*

    "Tristan lost in his thoughts… showing nothing but the face of a mannequin, emotionless… empty."

    "As he looked down… he saw a piece of paper…"

    play sound "audio/SFX/crumple.mp3"

    scene bg paper
    with dissolve

    "As he finishes unfolding a paper…"

    #*show a picture of Zoe’s bucket list with all check marks except one… “To live together with Tristan ”*

    "Tears came flowing down"

    #----------------Show Paper----------------

    play sound "audio/SFX/static.mp3"
    scene bg staticeffect
    with hpunch
    show static2
    with hpunch
    scene bg blackscreen

    #Tristan (voice trembling):

    Tristan "\"I keep thinking back… to all those moments with her.\""

    Tristan "\"The times she smiled… the times she looked at me like I mattered.\""
    
    Tristan "\"And I… I just took it for granted.\""

    Tristan "\"I thought… there would always be more time.\""

    Tristan "\"But time… just slipped away before I even realized it.\""

    #clenches his fists

    Tristan "\"I didn't listen closely enough… I didn't see the signs.\""

    Tristan "\"And now… all I'm left with is this emptiness, this ache that won't go away.\""
    
    Tristan "\"What I regret most of all is that I didn't even get to confess to her properly\""

    Tristan "\"I didn't even get the chance to say those words to her yet…\""

    Tristan "\"I didn't even get to say…\""

    Tristan "\"...\""

    Tristan "\"I love you…\""

    Tristan "\"ughhh why didn't I notice sooner!!! Why am I feeling this way again!!!\""
    
    Tristan "\"if only i knew… if only i was there for her\""

    Tristan "\"if.....\""

    Tristan "\"if...\""

    Tristan "\".......\""

    Tristan "\".....\""

    Tristan "\"...\""

    play sound "audio/SFX/static.mp3"
    scene bg staticeffect
    with hpunch
    show static2
    with hpunch
    scene bg blackscreen

    stop music fadeout 1.0
    with fade

    #-------------------SCENE 5: CONVINIENCE STORE-------------------

    #*Cuts to Black*

    #*cuts back to the very beginning*

    Girl "\"Earth to mister… Earth to mister!!\""

    scene bg supermarket
    with dissolve

    "Tristan Looks up… hearing a familiar voice."

    Tristan "\"eh?\""

    scene bg blackscreen
    with dissolve

    jump FinalChapter

    return