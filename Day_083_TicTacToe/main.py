# We gaming with some tic tac toe


## --- Build Board --- ###
# perhaps build the board as a list of lists

from board import Board

board = Board()

for _ in board.board:
    print(_)
    
## get input

player_1 = input("Would you like to be X or O? ")

if player_1 == 'X':
    player_2 = 'O'
else:
    player_2 = 'X'

round = 1

while round <= 9: