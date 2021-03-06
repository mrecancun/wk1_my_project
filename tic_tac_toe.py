import random


row1 = ["1", "2","3"]
row2= ["4","5","6"]
row3 = ["7","8","9"]

# main

def main ():
    turn = "x"
    is_winner = winner (updated_board) 

    # call functions
    total_turns = create_board ()
    while final_result or winner == False:
    
        player_input = player_input (turn) 
        updated_board (player_input, turn)
        turn = player (turn)
        final_result (total_turns)
        winner ()
# This function creates the board and keeps track of total turns up to 9 moves. 
def create_board (): 
    # total_turns = 9
    # while total_turns >0:
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
        # total_turns -= 1    
        # return total_turns

# Get players input
def player_input(turn):
    move = input (f" {turn}'s turn to choose a square (1-9):")
    return move

# The board will update based on user input
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
    

# Figure out players turn to input. Switch at the end of their turn. It adds up total turns up to 9.
def player (turn):
    if turn == "x":
            turn = "o"
    elif turn == "o":
            turn = "x"
    return turn

#iterate through rows to check if there are no numbers left on the board
def winner (updated_board):
    str ="0123"
    #Top row across
    if row1 [0] and row1 [1] and row1 [2] ==  str.isdigit:
        return True
    #Middle row
    elif row2 [0] and row2 [1] and row2 [2] ==  str.isdigit:
        return True
    #Bottom row
    elif row3 [0] and row3 [1] and row3 [2] ==  str.isdigit:
        return True
    # diagonal left to bottom
    elif row1 [0] and row2 [1] and row3 [2] ==  str.isdigit:
        return True
    # diagonal right to bottom
    elif row1 [2] and row2 [1] and row3 [0] ==  str.isdigit:
        return True
    # vertical line middle
    elif row1 [1] and row2 [1] and row3 [1] ==  str.isdigit:
        return True
# Check if all board spaces are filled with a letter but no winner
def final_result (total_turns, true):

    if total_turns == 0:
        print ("You have tied")
    pass

main ()