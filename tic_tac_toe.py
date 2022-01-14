import random


row1 = ["1", "2","3"]
row2= ["4","5","6"]
row3 = ["7","8","9"]

# main

def main ():
    turn = "x"
    is_winner = winner (updated_board) 

    # call functions
    create_board ()
    while tie or winner == False:
    
        player_input = player_input (turn) 
        updated_board (player_input, turn)
        turn = player (turn)

        winner ()

def create_board (): 

    for num in row1:
        print (num, end=" ")
    print (" ")
    print ("-+-+-")
    for num in row2:
        print (num, end=" ")
    print (" ")
    print ("-+-+-")
    for num in row3:
        print (num, end=" ")
    print (" ")

# Get player one input
def player_input(turn):
    move = input (f" {turn}'s turn to choose a square (1-9):")
    return move

# 
def updated_board (player, x):
    if player == "1":
        row1[0] = x    
    elif player == "2":
        row1[1] = x
    elif player == "3":
        row1[2] = x    
    elif player == "4":
        row2[0] = x
    elif player == "5":
        row2[1] = x
    elif player == "6":
        row2[2] = x
    elif player == "7":
        row3[0] = x
    elif player == "8":
        row3[1] = x
    elif player == "9":
        row1[2] = x
    create_board ()
    

# Figure out players turn to input. Switch at the end of their turn.
def player (turn):
    if turn == "x":
        turn = "o"
    elif turn == "o":
        turn = "x"
    return turn

    # if player_x_input == "x":
    #     player_o_input = o

def winner (updated_board):
    str ="0123"
    #Top row across
    if row1 [0] and row1 [1] and row1 [2] ==  str.isdigit:
        return True
    #Middle row
    elif row2 [0] and row1 [1] and row1 [2] ==  str.isdigit:
        return True
    #Bottom row
    elif row3 [0] and row1 [1] and row1 [2] ==  str.isdigit:
        return True
    # diagnol 
    elif row1 [0] and row1 [1] and row1 [2] ==  str.isdigit:
        return True
    elif row1 [0] and row1 [1] and row1 [2] ==  str.isdigit:
        return True
    elif row1 [0] and row1 [1] and row1 [2] ==  str.isdigit:
        return True
    elif row1 [0] and row1 [1] and row1 [2] ==  str.isdigit:
        return True
    elif row1 [0] and row1 [1] and row1 [2] ==  str.isdigit:
        return True
    elif row1 [0] and row1 [1] and row1 [2] ==  str.isdigit:
        return True
    elif row1 [0] and row1 [1] and row1 [2] ==  str.isdigit:
        return True

def tie ():
    while tie or winner == False:

main ()