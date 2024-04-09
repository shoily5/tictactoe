from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

test_board = ['','','','','','','','','','']
display_board(test_board)

def player_input():
    marker = ''
    player1 = ''
    player2 = ''
    #ask player 1 to choose x or O
    while marker not in ['X','O']:
        marker = input("Choose X or O:" ).upper()
        if marker not in ['X','O']:
            print("Sorry you did not choose 'X' or 'O'")
        else:
            player1 = marker
            if player1 == 'X':
                player2 = 'O'
            else:
                player2 = 'X'
        return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal



def choose_first():
    choice_player = 2
    player = ''
    while choice_player != 0 or choice_player !=1:
        choice_player = random.randint(0,1)
        if choice_player == 1:
            player = 'Player 1'
        else:
            player = 'Player 2'
        return player
    
def space_check(board, position):
    return board[position] == ''

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    next_input=0
    while next_input not in range(1,10):
        next_input = int(input('Which position do you want to play?'))
        if board[next_input]=='':
            return next_input
        else:
            next_input=0
    return next_input

def replay():
    return input('Do you want to play again?').lower() == 'yes'

print('Welcome to Tic Tac Toe!')

gameon = True
turn = choose_first()   #choose who goes first eg player 2 
print(f'{turn} goes first')
player1_marker, player2_marker = player_input()    #player1 chooses either x or o as a sign eg p1 = x p2 = o
display_board(test_board)
while gameon:
    if turn== 'Player 1':
        position = player_choice(test_board)              #Which position does player 1 want to play?
        place_marker(test_board, player1_marker, position)   #place a marker there
        display_board(test_board)
        if win_check(test_board, player1_marker):
            display_board(test_board)
            print('Congratulations! You have won the game!')
            gameon = False
        elif full_board_check(test_board):
            print('It is a draw!')
        else:
            turn= 'Player 2'
            
    else:
        position = player_choice(test_board)              #Which position does player 1 want to play?
        place_marker(test_board, player2_marker, position)   #place a marker there
        display_board(test_board)
        turn= 'Player 1'
        if win_check(test_board, player2_marker):
            display_board(test_board)
            print('Congratulations! You have won the game!')
            gameon = False
        elif full_board_check(test_board):
            print('It is a draw!')
        else:
            turn= 'Player 1'
    if not replay():
        break
