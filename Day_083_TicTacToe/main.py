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

def symbol_place(board, row, col, player_symbol):
    if col == 1:
        board[row-1][col] = player_symbol
    if col == 2:
        board[row-1][4] = player_symbol
    if col == 3:
        board[row-1][7] = player_symbol
    return board
        

round = 1

while round <= 9:
    if round%2 != 0:
        row_1 = int(input("Player 1, what row would you like to place your symbol?"))
        col_1 = int(input("Player 1, what column would you like to place your symbol?"))
        board.board = symbol_place(board.board, row_1, col_1, player_1)
        for _ in board.board:
            print(_)
    if round%2 == 0:
        row_2 = int(input("Player 2, what row would you like to place your symbol?"))
        col_2 = int(input("Player 2, what column would you like to place your symbol?"))
        board.board = symbol_place(board.board, row_2, col_2, player_2)
        for _ in board.board:
            print(_)