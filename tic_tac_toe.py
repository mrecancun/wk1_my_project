import random

row1 = ["1", "2","3"]
row2= ["4","5","6"]
row3 = ["7","8","9"]

# main

def main ():
    
# call functions

    create_board ()
    answer_x = player_x_input () 
    print (answer_x)
    updated_board (answer_x,"x")

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
def player_x_input():
    x = input ("X's turn to choose a square (1-9):")
    return x

def updated_board(player, x):
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
    


# Get player two input
def player_two_input ():
    o = input ("O's turn to choose a square (1-9):")
    return o

# def winner_player ():

main ()