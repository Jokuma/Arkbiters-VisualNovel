# Define images at the top level
image chessboard:
    "images/chessboard.png"

# White pieces
# Pawns
image white_pawn_1:
    "images/wP.png"
image white_pawn_3:
    "images/wP.png"
image white_pawn_5:
    "images/wP.png"
image white_pawn_6:
    "images/wP.png"
image white_pawn_7:
    "images/wP.png"
image white_pawn_8:
    "images/wP.png"

# Major white pieces
image white_rook_left:
    "images/wR.png"
image white_bishop_left:
    "images/wB.png"
image white_queen:
    "images/wQ.png"
image white_king:
    "images/wK.png"
image white_bishop_right:
    "images/wB.png"
image white_rook_right:
    "images/wR.png"

# Black pieces
# Pawns
image black_pawn_1:
    "images/bP.png"
image black_pawn_3:
    "images/bP.png"
image black_pawn_4:
    "images/bP.png"
image black_pawn_6:
    "images/bP.png"
image black_pawn_8:
    "images/bP.png"

# Major black pieces
image black_rook_left:
    "images/bR.png"
image black_knight_left:
    "images/bN.png"
image black_bishop_left:
    "images/bB.png"
image black_queen:
    "images/bQ.png"
image black_king:
    "images/bK.png"
image black_bishop_right:
    "images/bB.png"
image black_knight_right:
    "images/bN.png"
image black_rook_right:
    "images/bR.png"


# Chess game
label chess_game:
    scene black
    "Let's play chess!"

    show chessboard at Position(xalign=0.5, yalign=0.1)
    with None

    # Show black pieces
    show black_rook_left at Position(xalign=0.3775, yalign=0.0325) 
    show black_knight_left at Position(xalign=0.4265, yalign=0.2175) 
    show black_bishop_left at Position(xalign=0.3775, yalign=0.1275) 
    show black_queen at Position(xalign=0.5735, yalign=0.4900)
    show black_king at Position(xalign=0.5255, yalign=0.0325)
    show black_bishop_right at Position(xalign=0.3775, yalign=0.2175) 
    show black_knight_right at Position(xalign=0.5255, yalign=0.1275)
    show black_rook_right at Position(xalign=0.6225, yalign=0.0325)

    # Show white pieces
    show white_rook_left at Position(xalign=0.4745, yalign=0.6735)
    show white_bishop_left at Position(xalign=0.3278, yalign=0.4900)
    show white_queen at Position(xalign=0.3278, yalign=0.3975)
    show white_king at Position(xalign=0.6225, yalign=0.6735)
    show white_bishop_right at Position(xalign=0.4745, yalign=0.4900)
    show white_rook_right at Position(xalign=0.5245, yalign=0.6735)

    # Show pawns (white and black)
    show black_pawn_1 at Position(xalign=0.3275, yalign=0.1275)
    show black_pawn_3 at Position(xalign=0.4265, yalign=0.1275)
    show black_pawn_4 at Position(xalign=0.4755, yalign=0.1275)
    show black_pawn_6 at Position(xalign=0.5735, yalign=0.1275)
    show black_pawn_8 at Position(xalign=0.6722, yalign=0.1275)

    show white_pawn_8 at Position(xalign=0.6725, yalign=0.5825)
    show white_pawn_7 at Position(xalign=0.6225, yalign=0.5825)
    show white_pawn_6 at Position(xalign=0.5735, yalign=0.5825)
    show white_pawn_5 at Position(xalign=0.5735, yalign=0.2175)
    show white_pawn_3 at Position(xalign=0.4265, yalign=0.4900)
    show white_pawn_1 at Position(xalign=0.3278, yalign=0.5825)

    "You now enter the ChessGame."

label mate_in_5_puzzle:
    scene black
    "Let's look at the chessboard. Find the best move to mate in 5."
    "Please enter your move using standard algebraic notation.\nExamples:Qh5, Re1, Nf3. If capturing, add 'x' (e.g., Qxa7)."
    show chessboard at Position(xalign=0.5, yalign=0.1)
    # Show black pieces
    show black_rook_left at Position(xalign=0.3775, yalign=0.0325) 
    show black_knight_left at Position(xalign=0.4265, yalign=0.2175) 
    show black_bishop_left at Position(xalign=0.3775, yalign=0.1275) 
    show black_queen at Position(xalign=0.5735, yalign=0.4900)
    show black_king at Position(xalign=0.5255, yalign=0.0325)
    show black_bishop_right at Position(xalign=0.3775, yalign=0.2175) 
    show black_knight_right at Position(xalign=0.5255, yalign=0.1275)
    show black_rook_right at Position(xalign=0.6225, yalign=0.0325)

    # Show white pieces
    show white_rook_left at Position(xalign=0.4745, yalign=0.6735)
    show white_bishop_left at Position(xalign=0.3278, yalign=0.4900)
    show white_queen at Position(xalign=0.3278, yalign=0.3975)
    show white_king at Position(xalign=0.6225, yalign=0.6735)
    show white_bishop_right at Position(xalign=0.4745, yalign=0.4900)
    show white_rook_right at Position(xalign=0.5245, yalign=0.6735)

    # Show pawns (white and black)
    show black_pawn_1 at Position(xalign=0.3275, yalign=0.1275)
    show black_pawn_3 at Position(xalign=0.4265, yalign=0.1275)
    show black_pawn_4 at Position(xalign=0.4755, yalign=0.1275)
    show black_pawn_6 at Position(xalign=0.5735, yalign=0.1275)
    show black_pawn_8 at Position(xalign=0.6722, yalign=0.1275)

    show white_pawn_8 at Position(xalign=0.6725, yalign=0.5825)
    show white_pawn_7 at Position(xalign=0.6225, yalign=0.5825)
    show white_pawn_6 at Position(xalign=0.5735, yalign=0.5825)
    show white_pawn_5 at Position(xalign=0.5735, yalign=0.2175)
    show white_pawn_3 at Position(xalign=0.4265, yalign=0.4900)
    show white_pawn_1 at Position(xalign=0.3278, yalign=0.5825)

    call prompt_for_move("Rxe7")
    "Good job! That's the correct move."
    jump sequence_move
    "You find the first move!"
    return

label prompt_for_move(correct_move):
    $ move_correct = False
    
    while not move_correct:
        $ user_move = renpy.input("White to play Mate in 5 Enter your move:").strip()
        $ user_move_upper = user_move.upper()
        $ correct_move_upper = correct_move.upper()
        if user_move_upper == correct_move_upper:
            $ move_correct = True
        else:
            "Try again! That's not the correct move."
    return

    label sequence_move:
    scene black
    "Your move"
    show chessboard at Position(xalign=0.5, yalign=0.1)
    # Show black pieces
    show black_rook_left at Position(xalign=0.3775, yalign=0.0325) 
    show black_knight_left at Position(xalign=0.4265, yalign=0.2175) 
    show black_bishop_left at Position(xalign=0.3775, yalign=0.1275) 
    show black_queen at Position(xalign=0.5735, yalign=0.4900)
    show black_king at Position(xalign=0.5255, yalign=0.0325)
    show black_bishop_right at Position(xalign=0.3775, yalign=0.2175) 
    show black_rook_right at Position(xalign=0.6225, yalign=0.0325)

    # Show white pieces
    show white_rook_left at Position(xalign=0.4745, yalign=0.6735)
    show white_bishop_left at Position(xalign=0.3278, yalign=0.4900)
    show white_queen at Position(xalign=0.3278, yalign=0.3975)
    show white_king at Position(xalign=0.6225, yalign=0.6735)
    show white_bishop_right at Position(xalign=0.4745, yalign=0.4900)
    show white_rook_right at Position(xalign=0.5255, yalign=0.1275)

    # Show pawns (white and black)
    show black_pawn_1 at Position(xalign=0.3275, yalign=0.1275)
    show black_pawn_3 at Position(xalign=0.4265, yalign=0.1275)
    show black_pawn_4 at Position(xalign=0.4755, yalign=0.1275)
    show black_pawn_6 at Position(xalign=0.5735, yalign=0.1275)
    show black_pawn_8 at Position(xalign=0.6722, yalign=0.1275)

    show white_pawn_8 at Position(xalign=0.6725, yalign=0.5825)
    show white_pawn_7 at Position(xalign=0.6225, yalign=0.5825)
    show white_pawn_6 at Position(xalign=0.5735, yalign=0.5825)
    show white_pawn_5 at Position(xalign=0.5735, yalign=0.2175)
    show white_pawn_3 at Position(xalign=0.4265, yalign=0.4900)
    show white_pawn_1 at Position(xalign=0.3278, yalign=0.5825)
    "Rook takes e7. Double click to continue."
    pause

    label enemy_move:
    scene black
    "Enemy move"
    show chessboard at Position(xalign=0.5, yalign=0.1)
    # Show black piecesx
    show black_rook_left at Position(xalign=0.3775, yalign=0.0325) 
    show black_knight_left at Position(xalign=0.5255, yalign=0.1275) 
    show black_bishop_left at Position(xalign=0.3775, yalign=0.1275) 
    show black_queen at Position(xalign=0.5735, yalign=0.4900)
    show black_king at Position(xalign=0.5255, yalign=0.0325)
    show black_bishop_right at Position(xalign=0.3775, yalign=0.2175) 
    show black_rook_right at Position(xalign=0.6225, yalign=0.0325)

    # Show white pieces
    show white_rook_left at Position(xalign=0.4745, yalign=0.6735)
    show white_bishop_left at Position(xalign=0.3278, yalign=0.4900)
    show white_queen at Position(xalign=0.3278, yalign=0.3975)
    show white_king at Position(xalign=0.6225, yalign=0.6735)
    show white_bishop_right at Position(xalign=0.4745, yalign=0.4900)

    # Show pawns (white and black)
    show black_pawn_1 at Position(xalign=0.3275, yalign=0.1275)
    show black_pawn_3 at Position(xalign=0.4265, yalign=0.1275)
    show black_pawn_4 at Position(xalign=0.4755, yalign=0.1275)
    show black_pawn_6 at Position(xalign=0.5735, yalign=0.1275)
    show black_pawn_8 at Position(xalign=0.6722, yalign=0.1275)

    show white_pawn_8 at Position(xalign=0.6725, yalign=0.5825)
    show white_pawn_7 at Position(xalign=0.6225, yalign=0.5825)
    show white_pawn_6 at Position(xalign=0.5735, yalign=0.5825)
    show white_pawn_5 at Position(xalign=0.5735, yalign=0.2175)
    show white_pawn_3 at Position(xalign=0.4265, yalign=0.4900)
    show white_pawn_1 at Position(xalign=0.3278, yalign=0.5825)
    "Knight Takes the Rook on e7. Double click to continue."
    pause

    label second_move:
    scene black
    "Let's look at the chessboard new position. Find the next best move."
    show chessboard at Position(xalign=0.5, yalign=0.1)
    # Show black pieces
    show black_rook_left at Position(xalign=0.3775, yalign=0.0325) 
    show black_knight_left at Position(xalign=0.5255, yalign=0.1275) 
    show black_bishop_left at Position(xalign=0.3775, yalign=0.1275) 
    show black_queen at Position(xalign=0.5735, yalign=0.4900)
    show black_king at Position(xalign=0.5255, yalign=0.0325)
    show black_bishop_right at Position(xalign=0.3775, yalign=0.2175) 
    show black_rook_right at Position(xalign=0.6225, yalign=0.0325)

    # Show white pieces
    show white_rook_left at Position(xalign=0.4745, yalign=0.6735)
    show white_bishop_left at Position(xalign=0.3278, yalign=0.4900)
    show white_queen at Position(xalign=0.3278, yalign=0.3975)
    show white_king at Position(xalign=0.6225, yalign=0.6735)
    show white_bishop_right at Position(xalign=0.4745, yalign=0.4900)

    # Show pawns (white and black)
    show black_pawn_1 at Position(xalign=0.3275, yalign=0.1275)
    show black_pawn_3 at Position(xalign=0.4265, yalign=0.1275)
    show black_pawn_4 at Position(xalign=0.4755, yalign=0.1275)
    show black_pawn_6 at Position(xalign=0.5735, yalign=0.1275)
    show black_pawn_8 at Position(xalign=0.6722, yalign=0.1275)

    show white_pawn_8 at Position(xalign=0.6725, yalign=0.5825)
    show white_pawn_7 at Position(xalign=0.6225, yalign=0.5825)
    show white_pawn_6 at Position(xalign=0.5735, yalign=0.5825)
    show white_pawn_5 at Position(xalign=0.5735, yalign=0.2175)
    show white_pawn_3 at Position(xalign=0.4265, yalign=0.4900)
    show white_pawn_1 at Position(xalign=0.3278, yalign=0.5825)

    call prompt_for_secondmove("Qxd7")
    "Good job! That's the correct move."
    jump QueenSequence_move
    "You find the second move!"
    return

label prompt_for_secondmove(correct_secondmove):
    $ move_correct = False
    $ correct_secondmove_upper = correct_secondmove.upper()

    while not move_correct:
        $ user_move = renpy.input("White to play Mate in 5 Enter your move:").strip()
        $ user_move_upper = user_move.upper()
        if user_move_upper == correct_secondmove_upper:
            $ move_correct = True
        else:
            "Try again! That's not the correct move."
    return

    label QueenSequence_move:
    scene black
    "Your move"
    show chessboard at Position(xalign=0.5, yalign=0.1)
    # Show black pieces
    show black_rook_left at Position(xalign=0.3775, yalign=0.0325) 
    show black_knight_left at Position(xalign=0.5255, yalign=0.1275) 
    show black_bishop_left at Position(xalign=0.3775, yalign=0.1275) 
    show black_queen at Position(xalign=0.5735, yalign=0.4900)
    show black_king at Position(xalign=0.5255, yalign=0.0325)
    show black_bishop_right at Position(xalign=0.3775, yalign=0.2175) 
    show black_rook_right at Position(xalign=0.6225, yalign=0.0325)

    # Show white pieces
    show white_rook_left at Position(xalign=0.4745, yalign=0.6735)
    show white_bishop_left at Position(xalign=0.3278, yalign=0.4900)
    show white_queen at Position(xalign=0.4755, yalign=0.1275)
    show white_king at Position(xalign=0.6225, yalign=0.6735)
    show white_bishop_right at Position(xalign=0.4745, yalign=0.4900)

    # Show pawns (white and black)
    show black_pawn_1 at Position(xalign=0.3275, yalign=0.1275)
    show black_pawn_3 at Position(xalign=0.4265, yalign=0.1275)
    show black_pawn_6 at Position(xalign=0.5735, yalign=0.1275)
    show black_pawn_8 at Position(xalign=0.6722, yalign=0.1275)

    show white_pawn_8 at Position(xalign=0.6725, yalign=0.5825)
    show white_pawn_7 at Position(xalign=0.6225, yalign=0.5825)
    show white_pawn_6 at Position(xalign=0.5735, yalign=0.5825)
    show white_pawn_5 at Position(xalign=0.5735, yalign=0.2175)
    show white_pawn_3 at Position(xalign=0.4265, yalign=0.4900)
    show white_pawn_1 at Position(xalign=0.3278, yalign=0.5825)
    "Queen takes the Pawn on d7. Double click to continue."
    pause

    label QueenSequenceEnemy_move:
    scene black
    "Enemy move"
    show chessboard at Position(xalign=0.5, yalign=0.1)
    # Show black pieces
    show black_rook_left at Position(xalign=0.3775, yalign=0.0325) 
    show black_knight_left at Position(xalign=0.5255, yalign=0.1275) 
    show black_bishop_left at Position(xalign=0.3775, yalign=0.1275) 
    show black_queen at Position(xalign=0.5735, yalign=0.4900)
    show black_king at Position(xalign=0.4755, yalign=0.1275)
    show black_bishop_right at Position(xalign=0.3775, yalign=0.2175) 
    show black_rook_right at Position(xalign=0.6225, yalign=0.0325)

    # Show white pieces
    show white_rook_left at Position(xalign=0.4745, yalign=0.6735)
    show white_bishop_left at Position(xalign=0.3278, yalign=0.4900)
    show white_king at Position(xalign=0.6225, yalign=0.6735)
    show white_bishop_right at Position(xalign=0.4745, yalign=0.4900)

    # Show pawns (white and black)
    show black_pawn_1 at Position(xalign=0.3275, yalign=0.1275)
    show black_pawn_3 at Position(xalign=0.4265, yalign=0.1275)
    show black_pawn_6 at Position(xalign=0.5735, yalign=0.1275)
    show black_pawn_8 at Position(xalign=0.6722, yalign=0.1275)

    show white_pawn_8 at Position(xalign=0.6725, yalign=0.5825)
    show white_pawn_7 at Position(xalign=0.6225, yalign=0.5825)
    show white_pawn_6 at Position(xalign=0.5735, yalign=0.5825)
    show white_pawn_5 at Position(xalign=0.5735, yalign=0.2175)
    show white_pawn_3 at Position(xalign=0.4265, yalign=0.4900)
    show white_pawn_1 at Position(xalign=0.3278, yalign=0.5825)
    "King takes the Queen on d7. Double click to continue."
    pause


    label third_move:
    scene black
    "Let's look at the chessboard new position. Find the next best move."
    show chessboard at Position(xalign=0.5, yalign=0.1)
    # Show black pieces
    show black_rook_left at Position(xalign=0.3775, yalign=0.0325) 
    show black_knight_left at Position(xalign=0.5255, yalign=0.1275) 
    show black_bishop_left at Position(xalign=0.3775, yalign=0.1275) 
    show black_queen at Position(xalign=0.5735, yalign=0.4900)
    show black_king at Position(xalign=0.4755, yalign=0.1275)
    show black_bishop_right at Position(xalign=0.3775, yalign=0.2175) 
    show black_rook_right at Position(xalign=0.6225, yalign=0.0325)

    # Show white pieces
    show white_rook_left at Position(xalign=0.4745, yalign=0.6735)
    show white_bishop_left at Position(xalign=0.3278, yalign=0.4900)
    show white_king at Position(xalign=0.6225, yalign=0.6735)
    show white_bishop_right at Position(xalign=0.4745, yalign=0.4900)

    # Show pawns (white and black)
    show black_pawn_1 at Position(xalign=0.3275, yalign=0.1275)
    show black_pawn_3 at Position(xalign=0.4265, yalign=0.1275)
    show black_pawn_6 at Position(xalign=0.5735, yalign=0.1275)
    show black_pawn_8 at Position(xalign=0.6722, yalign=0.1275)

    show white_pawn_8 at Position(xalign=0.6725, yalign=0.5825)
    show white_pawn_7 at Position(xalign=0.6225, yalign=0.5825)
    show white_pawn_6 at Position(xalign=0.5735, yalign=0.5825)
    show white_pawn_5 at Position(xalign=0.5735, yalign=0.2175)
    show white_pawn_3 at Position(xalign=0.4265, yalign=0.4900)
    show white_pawn_1 at Position(xalign=0.3278, yalign=0.5825)

    call prompt_for_thirdmove("Bf5") 
    "Good job! That's the correct move."
    jump BishopSequence_move
    "You find the third move!"
    return

label prompt_for_thirdmove(correct_thirdmove):
    $ move_correct = False
    $ correct_thirdmove_upper = correct_thirdmove.upper()

    while not move_correct:
        $ user_move = renpy.input("White to play Mate in 5 Enter your move:").strip()
        $ user_move_upper = user_move.upper()
        if user_move_upper == correct_thirdmove_upper:
            $ move_correct = True
        else:
            "Try again! That's not the correct move."
    return


    label BishopSequence_move:
    scene black
    "Your move"
    show chessboard at Position(xalign=0.5, yalign=0.1)
    # Show black pieces
    show black_rook_left at Position(xalign=0.3775, yalign=0.0325) 
    show black_knight_left at Position(xalign=0.5255, yalign=0.1275) 
    show black_bishop_left at Position(xalign=0.3775, yalign=0.1275) 
    show black_queen at Position(xalign=0.5735, yalign=0.4900)
    show black_king at Position(xalign=0.4755, yalign=0.1275)
    show black_bishop_right at Position(xalign=0.3775, yalign=0.2175) 
    show black_rook_right at Position(xalign=0.6225, yalign=0.0325)

    # Show white pieces
    show white_rook_left at Position(xalign=0.4745, yalign=0.6735)
    show white_bishop_left at Position(xalign=0.3278, yalign=0.4900)
    show white_king at Position(xalign=0.6225, yalign=0.6735)
    show white_bishop_right at Position(xalign=0.5735, yalign=0.3075)

    # Show pawns (white and black)
    show black_pawn_1 at Position(xalign=0.3275, yalign=0.1275)
    show black_pawn_3 at Position(xalign=0.4265, yalign=0.1275)
    show black_pawn_6 at Position(xalign=0.5735, yalign=0.1275)
    show black_pawn_8 at Position(xalign=0.6722, yalign=0.1275)

    show white_pawn_8 at Position(xalign=0.6725, yalign=0.5825)
    show white_pawn_7 at Position(xalign=0.6225, yalign=0.5825)
    show white_pawn_6 at Position(xalign=0.5735, yalign=0.5825)
    show white_pawn_5 at Position(xalign=0.5735, yalign=0.2175)
    show white_pawn_3 at Position(xalign=0.4265, yalign=0.4900)
    show white_pawn_1 at Position(xalign=0.3278, yalign=0.5825)
    "Bishop goes to f5, double check. Double click to continue."
    pause

    label BishopSequenceEnemy_move:
    scene black
    "Enemy move"
    show chessboard at Position(xalign=0.5, yalign=0.1)
    # Show black pieces
    show black_rook_left at Position(xalign=0.3775, yalign=0.0325) 
    show black_knight_left at Position(xalign=0.5255, yalign=0.1275) 
    show black_bishop_left at Position(xalign=0.3775, yalign=0.1275) 
    show black_queen at Position(xalign=0.5735, yalign=0.4900)
    show black_king at Position(xalign=0.5255, yalign=0.0325)
    show black_bishop_right at Position(xalign=0.3775, yalign=0.2175) 
    show black_rook_right at Position(xalign=0.6225, yalign=0.0325)

    # Show white pieces
    show white_rook_left at Position(xalign=0.4745, yalign=0.6735)
    show white_bishop_left at Position(xalign=0.3278, yalign=0.4900)
    show white_king at Position(xalign=0.6225, yalign=0.6735)
    show white_bishop_right at Position(xalign=0.5735, yalign=0.3075)

    # Show pawns (white and black)
    show black_pawn_1 at Position(xalign=0.3275, yalign=0.1275)
    show black_pawn_3 at Position(xalign=0.4265, yalign=0.1275)
    show black_pawn_6 at Position(xalign=0.5735, yalign=0.1275)
    show black_pawn_8 at Position(xalign=0.6722, yalign=0.1275)

    show white_pawn_8 at Position(xalign=0.6725, yalign=0.5825)
    show white_pawn_7 at Position(xalign=0.6225, yalign=0.5825)
    show white_pawn_6 at Position(xalign=0.5735, yalign=0.5825)
    show white_pawn_5 at Position(xalign=0.5735, yalign=0.2175)
    show white_pawn_3 at Position(xalign=0.4265, yalign=0.4900)
    show white_pawn_1 at Position(xalign=0.3278, yalign=0.5825)
    "King goes to e8. Double click to continue."
    pause
    

    label fourth_move:
    scene black
    "Let's look at the chessboard new position. Find the next best move."
    show chessboard at Position(xalign=0.5, yalign=0.1)
    # Show black pieces
    show black_rook_left at Position(xalign=0.3775, yalign=0.0325) 
    show black_knight_left at Position(xalign=0.5255, yalign=0.1275) 
    show black_bishop_left at Position(xalign=0.3775, yalign=0.1275) 
    show black_queen at Position(xalign=0.5735, yalign=0.4900)
    show black_king at Position(xalign=0.5255, yalign=0.0325)
    show black_bishop_right at Position(xalign=0.3775, yalign=0.2175) 
    show black_rook_right at Position(xalign=0.6225, yalign=0.0325)

    # Show white pieces
    show white_rook_left at Position(xalign=0.4745, yalign=0.6735)
    show white_bishop_left at Position(xalign=0.3278, yalign=0.4900)
    show white_king at Position(xalign=0.6225, yalign=0.6735)
    show white_bishop_right at Position(xalign=0.5735, yalign=0.3075)

    # Show pawns (white and black)
    show black_pawn_1 at Position(xalign=0.3275, yalign=0.1275)
    show black_pawn_3 at Position(xalign=0.4265, yalign=0.1275)
    show black_pawn_6 at Position(xalign=0.5735, yalign=0.1275)
    show black_pawn_8 at Position(xalign=0.6722, yalign=0.1275)

    show white_pawn_8 at Position(xalign=0.6725, yalign=0.5825)
    show white_pawn_7 at Position(xalign=0.6225, yalign=0.5825)
    show white_pawn_6 at Position(xalign=0.5735, yalign=0.5825)
    show white_pawn_5 at Position(xalign=0.5735, yalign=0.2175)
    show white_pawn_3 at Position(xalign=0.4265, yalign=0.4900)
    show white_pawn_1 at Position(xalign=0.3278, yalign=0.5825)

    call prompt_for_fourthmove("Bd7")  
    "Good job! That's the correct move."
    jump NextBishopSequence_move
    "You find the fourth move!"
    return

label prompt_for_fourthmove(correct_fourthmove):
    $ move_correct = False
    $ correct_fourthmove_upper = correct_fourthmove.upper()

    while not move_correct:
        $ user_move = renpy.input("White to play Mate in 5 Enter your move:").strip()
        $ user_move_upper = user_move.upper()
        if user_move_upper == correct_fourthmove_upper:
            $ move_correct = True
        else:
            "Try again! That's not the correct move."
    return

    label NextBishopSequence_move:
    scene black
    "Your move"
    show chessboard at Position(xalign=0.5, yalign=0.1)

    # Show black pieces
    show black_rook_left at Position(xalign=0.3775, yalign=0.0325) 
    show black_knight_left at Position(xalign=0.5255, yalign=0.1275) 
    show black_bishop_left at Position(xalign=0.3775, yalign=0.1275) 
    show black_queen at Position(xalign=0.5735, yalign=0.4900)
    show black_king at Position(xalign=0.5255, yalign=0.0325)
    show black_bishop_right at Position(xalign=0.3775, yalign=0.2175) 
    show black_rook_right at Position(xalign=0.6225, yalign=0.0325)

    # Show white pieces
    show white_rook_left at Position(xalign=0.4745, yalign=0.6735)
    show white_bishop_left at Position(xalign=0.3278, yalign=0.4900)
    show white_king at Position(xalign=0.6225, yalign=0.6735)
    show white_bishop_right at Position(xalign=0.4755, yalign=0.1275)

    # Show pawns (white and black)
    show black_pawn_1 at Position(xalign=0.3275, yalign=0.1275)
    show black_pawn_3 at Position(xalign=0.4265, yalign=0.1275)
    show black_pawn_6 at Position(xalign=0.5735, yalign=0.1275)
    show black_pawn_8 at Position(xalign=0.6722, yalign=0.1275)

    show white_pawn_8 at Position(xalign=0.6725, yalign=0.5825)
    show white_pawn_7 at Position(xalign=0.6225, yalign=0.5825)
    show white_pawn_6 at Position(xalign=0.5735, yalign=0.5825)
    show white_pawn_5 at Position(xalign=0.5735, yalign=0.2175)
    show white_pawn_3 at Position(xalign=0.4265, yalign=0.4900)
    show white_pawn_1 at Position(xalign=0.3278, yalign=0.5825)
    "Bishop goes to d7 with check. Double click to continue."
    pause

    label NextBishopSequenceEnemy_move:
    scene black
    "Enemy move"
    show chessboard at Position(xalign=0.5, yalign=0.1)
    # Show black pieces
    show black_rook_left at Position(xalign=0.3775, yalign=0.0325) 
    show black_knight_left at Position(xalign=0.5255, yalign=0.1275) 
    show black_bishop_left at Position(xalign=0.3775, yalign=0.1275) 
    show black_queen at Position(xalign=0.5735, yalign=0.4900)
    show black_king at Position(xalign=0.5735, yalign=0.0325)
    show black_bishop_right at Position(xalign=0.3775, yalign=0.2175) 
    show black_rook_right at Position(xalign=0.6225, yalign=0.0325)

    # Show white pieces
    show white_rook_left at Position(xalign=0.4745, yalign=0.6735)
    show white_bishop_left at Position(xalign=0.3278, yalign=0.4900)
    show white_king at Position(xalign=0.6225, yalign=0.6735)
    show white_bishop_right at Position(xalign=0.4755, yalign=0.1275)

    # Show pawns (white and black)
    show black_pawn_1 at Position(xalign=0.3275, yalign=0.1275)
    show black_pawn_3 at Position(xalign=0.4265, yalign=0.1275)
    show black_pawn_6 at Position(xalign=0.5735, yalign=0.1275)
    show black_pawn_8 at Position(xalign=0.6722, yalign=0.1275)

    show white_pawn_8 at Position(xalign=0.6725, yalign=0.5825)
    show white_pawn_7 at Position(xalign=0.6225, yalign=0.5825)
    show white_pawn_6 at Position(xalign=0.5735, yalign=0.5825)
    show white_pawn_5 at Position(xalign=0.5735, yalign=0.2175)
    show white_pawn_3 at Position(xalign=0.4265, yalign=0.4900)
    show white_pawn_1 at Position(xalign=0.3278, yalign=0.5825)
    "King goes to f8. Double click to continue."
    pause

    label CheckMate_move:
    scene black
    "Let's look at the chessboard new position. Find the Last move to win the Game."
    show chessboard at Position(xalign=0.5, yalign=0.1)
    # Show black pieces
    show black_rook_left at Position(xalign=0.3775, yalign=0.0325) 
    show black_knight_left at Position(xalign=0.5255, yalign=0.1275) 
    show black_bishop_left at Position(xalign=0.3775, yalign=0.1275) 
    show black_queen at Position(xalign=0.5735, yalign=0.4900)
    show black_king at Position(xalign=0.5735, yalign=0.0325)
    show black_bishop_right at Position(xalign=0.3775, yalign=0.2175) 
    show black_rook_right at Position(xalign=0.6225, yalign=0.0325)

    # Show white pieces
    show white_rook_left at Position(xalign=0.4745, yalign=0.6735)
    show white_bishop_left at Position(xalign=0.3278, yalign=0.4900)
    show white_king at Position(xalign=0.6225, yalign=0.6735)
    show white_bishop_right at Position(xalign=0.4755, yalign=0.1275)

    # Show pawns (white and black)
    show black_pawn_1 at Position(xalign=0.3275, yalign=0.1275)
    show black_pawn_3 at Position(xalign=0.4265, yalign=0.1275)
    show black_pawn_6 at Position(xalign=0.5735, yalign=0.1275)
    show black_pawn_8 at Position(xalign=0.6722, yalign=0.1275)

    show white_pawn_8 at Position(xalign=0.6725, yalign=0.5825)
    show white_pawn_7 at Position(xalign=0.6225, yalign=0.5825)
    show white_pawn_6 at Position(xalign=0.5735, yalign=0.5825)
    show white_pawn_5 at Position(xalign=0.5735, yalign=0.2175)
    show white_pawn_3 at Position(xalign=0.4265, yalign=0.4900)
    show white_pawn_1 at Position(xalign=0.3278, yalign=0.5825)

    call prompt_for_CheckMatemove("Be7")  
    "Good job! That's the correct move."
    jump Final_move
    "You find the Final move!"
    return

label prompt_for_CheckMatemove(correct_CheckMatemove):
    $ move_correct = False
    $ correct_CheckMatemove_upper = correct_CheckMatemove.upper()

    while not move_correct:
        $ user_move = renpy.input("White to play Mate in 5 Enter your move:").strip()
        $ user_move_upper = user_move.upper()
        if user_move_upper == correct_CheckMatemove_upper:
            $ move_correct = True
        else:
            "Try again! That's not the correct move."
    return

    label Final_move:
    scene black
    "Your move"
    show chessboard at Position(xalign=0.5, yalign=0.1)
    # Show black pieces
    show black_rook_left at Position(xalign=0.3775, yalign=0.0325) 
    show black_bishop_left at Position(xalign=0.3775, yalign=0.1275) 
    show black_queen at Position(xalign=0.5735, yalign=0.4900)
    show black_king at Position(xalign=0.5735, yalign=0.0325)
    show black_bishop_right at Position(xalign=0.3775, yalign=0.2175) 
    show black_rook_right at Position(xalign=0.6225, yalign=0.0325)

    # Show white pieces
    show white_rook_left at Position(xalign=0.4745, yalign=0.6735)
    show white_bishop_left at Position(xalign=0.5255, yalign=0.1275)
    show white_king at Position(xalign=0.6225, yalign=0.6735)
    show white_bishop_right at Position(xalign=0.4755, yalign=0.1275)

    # Show pawns (white and black)
    show black_pawn_1 at Position(xalign=0.3275, yalign=0.1275)
    show black_pawn_3 at Position(xalign=0.4265, yalign=0.1275)
    show black_pawn_6 at Position(xalign=0.5735, yalign=0.1275)
    show black_pawn_8 at Position(xalign=0.6722, yalign=0.1275)

    show white_pawn_8 at Position(xalign=0.6725, yalign=0.5825)
    show white_pawn_7 at Position(xalign=0.6225, yalign=0.5825)
    show white_pawn_6 at Position(xalign=0.5735, yalign=0.5825)
    show white_pawn_5 at Position(xalign=0.5735, yalign=0.2175)
    show white_pawn_3 at Position(xalign=0.4265, yalign=0.4900)
    show white_pawn_1 at Position(xalign=0.3278, yalign=0.5825)
    "Bishop goes to e7 win the Game. Double click to continue."
    "CheckMate"
    "Congrats you win the Game!!!"
    "..."
    jump Chapter7continue
    return


