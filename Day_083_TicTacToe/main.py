# We gaming with some tic tac toe


## --- Build Board --- ###
# perhaps build the board as a list of lists

from board import Board

board = Board()

# for _ in board.board:
#     print(_)
    
## get input


def symbol_place(board, row, col, player_symbol):
    if row == 1:
        row_index = 0
    elif row == 2:
        row_index = 2
    else:
        row_index = 4
        
    row_string = board[row_index][0]
        
    if col == 1:
        placed_string = row_string[:col] + player_symbol + row_string[col+1:]
    if col == 2:
        placed_string = row_string[:4] + player_symbol + row_string[5:]
    if col == 3:
        placed_string = row_string[:7] + player_symbol + row_string[8:]
    
    board[row_index][0] = placed_string

    return board
    

# row_string = board.board[0][0]
# row_string = row_string[:1] + 'X' + row_string[2:]
# print(row_string)

def play_game():
    player_1 = input("Player 1, would you like to be X or O? ")

    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'
    
    num_round = 1
    
    while num_round <= 9:
        if num_round%2 != 0:
            row_1 = int(input("Player 1, what row would you like to place your symbol?"))
            col_1 = int(input("Player 1, what column would you like to place your symbol?"))
            board.board = symbol_place(board.board, row_1, col_1, player_1)
            for _ in board.board:
                print(_[0])
        if num_round%2 == 0:
            row_2 = int(input("Player 2, what row would you like to place your symbol?"))
            col_2 = int(input("Player 2, what column would you like to place your symbol?"))
            board.board = symbol_place(board.board, row_2, col_2, player_2)
            for _ in board.board:
                print(_[0])
        num_round += 1
        
    return num_round

num_round = play_game()


if num_round > 9:
    print('Game Over!')
    new_game = input('Would you like to play again? Y/N ').upper()
    
if new_game == 'Y':
    board.board = board.new_board
    play_game()
    