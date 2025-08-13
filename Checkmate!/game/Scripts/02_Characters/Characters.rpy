define Tristan = Character('Tristan Garcia',bold=True, color="#1e4e9c")
define Zoe = Character('Zoe Gonzales', color = "#e6379d")
define Emil = Character('Emil Navarro', color ="#ff0000")
define Manager = Character('Manager', color="#8f491a")
define Doctor = Character('Doctor', color="#be35e7")
define Girl = Character('Girl', color="#be35e7")
define CrowdM = Character('Man In Crowd', color="#ff9100")
define CrowdF = Character('Woman In Crowd', color="#ff9100")
define Chessplayer1 = Character('Chess Player 1', color="#01ac17")
define Chessplayer2 = Character('Chess Player 2', color="#01ac17")
define Commentator = Character('Commentator',color="#ffffff")


image TAGA9animation = Movie(channel="movie_dp", play="images/popvid.ogv")
image Arkbiters_Logo = "images/Background/arkbiters.png"
#define splashmusic = 
label splashscreen:
    scene Arkbiters_Logo zorder 2:
        xoffset 0
        zoom 0.3
        center
        yoffset -400
    show black screen
    show text "Arkbiters Presents" zorder 2:
        yoffset 200
    with dissolve
    pause 3.0

    show bg staticeffect zorder 2
    pause 0.2
    show static2 zorder 2  
    play sound "audio/SFX/static.mp3"
    with hpunch
    with hpunch
    hide text with dissolve
    hide Arkbiters_Logo with dissolve
    hide bg staticeffect
    hide static2
    stop music fadeout 1
    show  TAGA9animation
    pause 2.0
    return