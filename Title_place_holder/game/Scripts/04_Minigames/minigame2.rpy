init python:
    import math, time, random


   



    class OsuNote:
        def __init__(self, x, y, appear_time):
            self.x = x
            self.y = y
            self.appear_time = appear_time
            self.hit = False
            self.radius = 80
            self.approach_radius = 160
            self.missed = False
            self.fade_alpha = 1.0   # For fading out
            self.fading = False     # True if in fade-out mode

    notes = []
    start_time = 0.0
    last_update_time = 0.0
    score = 0
    hit_window = 0.2
    miss_window = 0.5
    fade_duration = 0.5  # seconds to fade

    def start_rhythm_game():
        global notes, start_time, last_update_time, score
        notes = []
        score = 0
        start_time = time.time()
        last_update_time = start_time

        delay = 0.6
        for i in range(10): ############################################################ how many notes will appear
            notes.append(
                OsuNote(
                    random.randint(200, 1720),
                    random.randint(200, 880),
                    appear_time=i * delay + 2.0
                )
            )

    def update_game(dt):
        current_time = time.time() - start_time
        for note in notes:
            # Shrink approach circle when note becomes active
            if not note.hit and not note.missed:
                time_until_hit = note.appear_time - current_time
                if time_until_hit <= 0:
                    shrink_speed = (note.approach_radius - note.radius) / (note.appear_time - (note.appear_time - miss_window))
                    note.approach_radius = max(note.radius, note.approach_radius - 300 * dt)

                # Mark as missed and start fade-out
                if current_time - note.appear_time > miss_window:
                    note.missed = True
                    note.fading = True

            # If fading (missed or hit), reduce alpha
            if note.fading:
                note.fade_alpha -= dt / fade_duration
                if note.fade_alpha < 0:
                    note.fade_alpha = 0

    def timer_tick():
        global last_update_time
        now = time.time()
        dt = now - last_update_time
        if dt > 0.5:
            dt = 0.016
        last_update_time = now
        update_game(dt)

    def click_note(x, y):
        global score
        current_time = time.time() - start_time
        for note in notes:
            if not note.hit and not note.missed:
                dist = math.hypot(x - note.x, y - note.y)
                if dist <= note.radius:
                    timing_error = abs(current_time - note.appear_time)
                    if timing_error <= hit_window:
                        score += 300
                        note.hit = True
                    elif timing_error <= miss_window:
                        score += 100
                        note.hit = True
                    note.fading = True  # Start fade-out immediately after hit
                    return True
        return False

screen osu_game():
    timer 0.016 repeat True action Function(timer_tick)

    text "Score: [score]" xpos 20 ypos 20 size 40 color "#fff"

    $ current_time = time.time() - start_time

    for note in notes:
        if current_time >= note.appear_time - 1.0 and note.fade_alpha > 0:
            # Approach circle
            if note.approach_radius > note.radius and not note.fading:
                add Solid("#0ff") xysize (note.approach_radius*2, note.approach_radius*2) xpos (note.x - note.approach_radius) ypos (note.y - note.approach_radius) alpha (0.45 * note.fade_alpha)
            add Solid("#fff") xysize (note.radius*2, note.radius*2) xpos (note.x - note.radius) ypos (note.y - note.radius) alpha note.fade_alpha

    key "mouseup_1" action Function(lambda: click_note(*renpy.get_mouse_pos()))

image karaoke_animated:
    "images/karaoke1.png"
    pause 0.5
    "images/karaoke2.png"
    pause 0.5
    "images/karaoke3.png"
    pause 0.5
    "images/karaoke2.png"
    pause 0.5
    repeat


label minigamerhythm:
    $ _game_menu_screen = None
    with squares
    show karaoke_animated
    "..."
    "It's time to sing!"
    "..."
    "The game is simple."
    "Click the squares on time... An approaching square will indicate when it's time to click"
    "A simillar game to Osu! (special shoutout)"
    "Let's go!!!"
    window hide
    $ start_rhythm_game()
    show screen osu_game
    
    python:
        while True:
            if all(n.fade_alpha <= 0 for n in notes):
                break
            renpy.pause(0.05, hard=True)


    hide screen osu_game
    "End - Final score: [score]"
    "..."
    jump Chapter3continue
    return
