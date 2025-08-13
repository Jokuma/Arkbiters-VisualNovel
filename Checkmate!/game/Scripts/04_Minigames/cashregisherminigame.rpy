
image ZoomInCashregister_frame = "images/Background/storecashregister.png"

default output_text = ""
default message_to_display = None
default current_problem = 1
default answer_input = ""
default correct_answers = {1: "177", 2: "459", 3: "657", 4: "4", 5: "13"}

define buttons = ["0","1","2","3","4","5","6","7","8","9"]

init python:
    def append_value(val):
        global output_text
        output_text += val

    def delete_value():
        global output_text
        output_text = ""

    def enter_output():
        global output_text, answer_input
        answer_input = output_text.strip()
        output_text = ""
        if answer_input == "":
            renpy.notify("Please enter an answer before submitting.")
        else:
            renpy.jump("check_answer")

label check_answer:
    if not answer_input:
        "Please enter an answer before submitting."
        jump current_problem_label
    elif answer_input == correct_answers.get(current_problem, ""):
        if current_problem == 1:
            $ current_problem = 2
            jump problem_2
        elif current_problem == 2:
            $ current_problem = 3
            jump problem_3
        elif current_problem == 3:
            $ current_problem = 4
            jump problem_4
        elif current_problem == 4:
            $ current_problem = 5
            jump problem_5
        elif current_problem == 5:
            "Congratulations! You completed all problems!"
            hide screen number_buttons
            hide screen output_square
            hide screen output_squareDEMO
            hide screen Bill
            hide screen CashReceived
            hide tristan normal
            hide image ZoomInCashregister_frame
            with squares
            jump Chapter1continue
    else:
        "That's not correct. Try again."
        $ answer_input = ""
        if current_problem == 1:
            jump problem_1
        elif current_problem == 2:
            jump problem_2
        elif current_problem == 3:
            jump problem_3
        elif current_problem == 4:
            jump problem_4
        elif current_problem == 5:
            jump problem_5

screen number_buttons():
    textbutton "1" action Function(append_value, "1") xpos 320 ypos 420
    textbutton "2" action Function(append_value, "2") xpos 380 ypos 420
    textbutton "3" action Function(append_value, "3") xpos 440 ypos 420
    textbutton "4" action Function(append_value, "4") xpos 320 ypos 480
    textbutton "5" action Function(append_value, "5") xpos 380 ypos 480
    textbutton "6" action Function(append_value, "6") xpos 440 ypos 480
    textbutton "7" action Function(append_value, "7") xpos 320 ypos 540
    textbutton "8" action Function(append_value, "8") xpos 380 ypos 540
    textbutton "9" action Function(append_value, "9") xpos 440 ypos 540
    textbutton "0" action Function(append_value, "0") xpos 380 ypos 600
    textbutton "Delete" action Function(delete_value) xpos 240 ypos 660

screen output_squareDEMO():
    frame:
        background "#000000"
        xalign 0.4
        yalign 0.65
        xsize 300
        ysize 75

        vbox:
            spacing 15 

        frame:
            background "#ffffff"
            xpadding 4
            ypadding 4
            xalign 0.5
            yalign 0.5
            xsize (300 - 8)
            ysize (75 - 8)

            viewport:
                xsize (300 - 8)
                ysize (75 - 8)
                scrollbars ("horizontal")
                text output_text color "#000000"

        textbutton "Enter" action Function(enter_output) xalign -0.9+(-0.65) yalign 0
        text "Input " color "#000000" xalign 0.5 yalign 0.0

screen output_square():
    frame:
        background "#000000"
        xalign 0.4
        yalign 0.65
        xsize 300
        ysize 75

        vbox:
            spacing 10  

        frame:
            background "#ffffff"
            xpadding 4
            ypadding 4
            xalign 0.5
            yalign 0.5
            xsize (300 - 8)
            ysize (75 - 8)

            viewport:
                xsize (300 - 8)
                ysize (75 - 8)
                scrollbars ("horizontal")

        text output_text:
            color "#000000"
            xalign 0.5

        textbutton "Enter" action Function(enter_output) xalign -0.9+(-0.65) yalign 0

screen Bill(label_text="Bill"):
    frame:
        background "#000000"
        xalign 0.4
        yalign 0.53
        xsize 300
        ysize 75

        frame:
            background "#ffffff"
            xpadding 4
            ypadding 4
            xalign 0.5
            yalign 0.5
            xsize (300 - 8)
            ysize (75 - 8)
            text label_text color "#000000" xalign 0.5 yalign 0.0

screen CashReceived(cash_text="Cash Received"):
    frame:
        background "#000000"
        xalign 0.4
        yalign 0.43
        xsize 300
        ysize 75

        frame:
            background "#ffffff"
            xpadding 4
            ypadding 4
            xalign 0.5
            yalign 0.5
            xsize (300 - 8)
            ysize (75 - 8)
            text cash_text color "#000000" xalign 0.5 yalign 0.0


scene black

label registerminigame:
    scene storecashregister
    "Welcome to the Cash Register Game!"
    "Click the screen to start."
    scene black

label main_game:
    
    show ZoomInCashregister_frame:
        xalign 1
        yalign 0.5
        zoom 1.5

    show screen number_buttons
    show screen output_squareDEMO
    show screen CashReceived
    show screen Bill

    show tristan normal:
        xoffset 500
        yoffset 1850
        zoom 3
        center 

    "Let's play Simple Subtraction Game!"
    "Get Ready for the first problem"

    jump problem_1

label problem_1:
    scene black 
    
    show ZoomInCashregister_frame:
        xalign 1
        yalign 0.5
        zoom 1.5

    $ bill_display_text = "323"
    $ cash_display_text = "500"

    show screen number_buttons
    show screen output_square
    show screen Bill(label_text=bill_display_text)
    show screen CashReceived(cash_text=cash_display_text)
    show tristan normal:
        xoffset 500
        yoffset 1850
        zoom 3
        center 
    $ answer_input = ""
    "Problem 1: What is 500 - 323?"
    "Please input your answer by clicking the buttons 0-9."
    "Double click to continue."
label wait_for_answer_1:
        if answer_input == "":
            "Please enter an answer before submitting."
            jump wait_for_answer_1
        elif answer_input == correct_answers[1]:
            jump problem_2
        else:
            "That's not correct. Try again."
            $ answer_input = ""
            jump wait_for_answer_1

label problem_2:
    scene black 
    
    show ZoomInCashregister_frame:
        xalign 1
        yalign 0.5
        zoom 1.5

    $ bill_display_text = "541"
    $ cash_display_text = "1000"

    show screen number_buttons
    show screen output_square
    show screen Bill(label_text=bill_display_text)
    show screen CashReceived(cash_text=cash_display_text)
    show tristan normal:
        xoffset 500
        yoffset 1850
        zoom 3
        center 
    $ answer_input = ""
    "Problem 2: What is 1000 - 541?"
    "Please input your answer by clicking the buttons on the left side."
    "Double click to continue."
label wait_for_answer_2:
        if answer_input == "":
            "Please enter an answer before submitting."
            jump wait_for_answer_2
        elif answer_input == correct_answers[2]:
            jump problem_3
        else:
            "That's not correct. Try again."
            $ answer_input = ""
            jump wait_for_answer_2

label problem_3:
    scene black
    show ZoomInCashregister_frame:
        xalign 1
        yalign 0.5
        zoom 1.5

    $ bill_display_text = "343"
    $ cash_display_text = "1000"

    show screen number_buttons
    show screen output_square
    show screen Bill(label_text=bill_display_text)
    show screen CashReceived(cash_text=cash_display_text)
    show tristan normal:
        xoffset 500
        yoffset 1850
        zoom 3
        center 
    $ answer_input = ""
    "Problem 3: What is 1000 - 343?"
    "Please input your answer by clicking the buttons on the left side."
    label wait_for_answer_3:
        if answer_input == "":
            "Please enter an answer before submitting."
            jump wait_for_answer_3
        elif answer_input == correct_answers[3]:
            jump problem_4
        else:
            "That's not correct. Try again."
            $ answer_input = ""
            jump wait_for_answer_3
            
label problem_4:
    scene black
    show ZoomInCashregister_frame:
        xalign 1
        yalign 0.5
        zoom 1.5

    $ bill_display_text = "996"
    $ cash_display_text = "1000"

    show screen number_buttons
    show screen output_square
    show screen Bill(label_text=bill_display_text)
    show screen CashReceived(cash_text=cash_display_text)
    show tristan normal:
        xoffset 500
        yoffset 1850
        zoom 3
        center 
    $ answer_input = ""
    "Problem 3: What is 1000 - 996?"
    "Please input your answer by clicking the buttons on the left side."
    label wait_for_answer_4:
        if answer_input == "":
            "Please enter an answer before submitting."
            jump wait_for_answer_4
        elif answer_input == correct_answers[4]:
            jump problem_5
        else:
            "That's not correct. Try again."
            $ answer_input = ""
            jump wait_for_answer_4

label problem_5:
    scene black
    show ZoomInCashregister_frame:
        xalign 1
        yalign 0.5
        zoom 1.5

    $ bill_display_text = "187"
    $ cash_display_text = "200"

    show screen number_buttons
    show screen output_square
    show screen Bill(label_text=bill_display_text)
    show screen CashReceived(cash_text=cash_display_text)
    show tristan normal:
        xoffset 500
        yoffset 1850
        zoom 3
        center 
    $ answer_input = ""
    "Problem 3: What is 200 - 187?"
    "Please input your answer by clicking the buttons on the left side."
    label wait_for_answer_5:
        if answer_input == "":
            "Please enter an answer before submitting."
            jump wait_for_answer_5
        elif answer_input == correct_answers[5]:
            return
        else:
            "That's not correct. Try again."
            $ answer_input = ""
            jump wait_for_answer_5
