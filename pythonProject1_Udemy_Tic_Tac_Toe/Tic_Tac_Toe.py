# Display the board to the players
def display_board(board):

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-' + '+' + '-' + '+' + '-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-' + '+' + '-' + '+' + '-')
    print(board[1] + '|' + board[2] + '|' + board[3])


# Set the marker for the players and returns player1 marker and player2 marker
def player_marker():
    ''''
    OUTPUT = (Player1_marker, Player2_marker)
    '''
    marker = ''
    # Keep asking player 1 to choose X or O
    while marker not in ['X', 'O']:
        marker = input("Do you want to be X or O? ")

        if marker not in ['X', 'O']:
            print('Invalid Entry!!')

    player_1 = marker

    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'
    return (player_1, player_2)


# Update the board after taking the position index from players
def place_maker(test_board, marker, user_index):
    test_board[user_index] = marker
    return test_board


# Check if the player1 or player2 becomes the winner
def win_check(board, marker):
    # To Win the Game all the rows should be same to marker
    # all the colums should to be same to marker
    # 2 diagonals should be same to marker
    if (board[1] == board[2] == board[3] == marker) or (board[4] == board[5] == board[6] == marker) or \
            (board[7] == board[8] == board[9] == marker) or (board[3] == board[5] == board[7] == marker) or \
            (board[1] == board[5] == board[9] == marker) or (board[1] == board[4] == board[7] == marker) or \
            (board[2] == board[5] == board[8] == marker) or (board[3] == board[6] == board[9] == marker):
        return True


# choose the player who will play first
from random import randint
def choose_first():
    flip = randint(0,1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'


# Check if there is any empty space available on the board
def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


# Checks if board is full
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    else:
        # BOARD IS FULL IF IT RETURNS TRUE
        return True


# Player enters the position or index
def player_choice(board):
    position = 'wrong'
    accept_range = range(1, 10)
    within_range = False
    while within_range == False:
        position = int(input("Enter a position on the tic-tac board (1-9): "))
        if position in accept_range:
            if space_check(board, position):
                return position
            else:
                print('This position is not empty(full)')
        else:
            within_range = False
            print("The index value is not within the range")


# checks if the players want to play more
def replay():
    ask_ques = input('Do you want to play again? (Yes/No): ')
    if ask_ques == 'Yes':
        return True
    else:
        return False


while True:
    # Set the game up here
    print('Welcome to Tic Tac Toe!')
    # Set and Display the board
    test_board = ['0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(test_board)
    # set the marker for the two players
    player1_mark, player2_mark = player_marker()
    # Select the player who will go first
    turn = choose_first()
    print(turn,"will go first!")

    # Play the game
    game_on = True
    while game_on:
        # Player1 turn
        if turn == 'Player1':
            # Choose a position on the board
            position = player_choice(test_board)
            # Update the board
            place_maker(test_board, player1_mark, position)
            display_board(test_board)
            # Check if player1 is winner
            if win_check(test_board, player1_mark):
                print(turn, 'is the Winner!')
                game_on = False
            else:
                # Check for Tie
                if full_board_check(test_board):
                    print('It is a Tie!')
                    game_on = False
                else:
                    # Else its Player2 turn
                    turn = 'Player2'
        else:
            # Player2 turn
            # Choose a position on the board
            position = player_choice(test_board)
            # Update the board
            place_maker(test_board, player2_mark, position)
            display_board(test_board)
            # Check if player2 is winner
            if win_check(test_board, player2_mark):
                print(turn, 'is the Winner!')
                game_on = False
            else:
                # Check for Tie
                if full_board_check(test_board):
                    print('It is a Tie!')
                    game_on = False
                else:
                    # Else its Player2 turn
                    turn = 'Player1'

    # Checks if players want to play again and get out from the while loop
    if not replay():
        break
