import random

def display_board(board):
    #scroll previous board out of view
    print('\n'*100)

    #print current board
    print('Current board: \n')
    print(board[7:10])
    print(board[4:7])
    print(board[1:4])
    print('\n')

def player_input():
    #take in player input and assign as 'X' or 'O'
    player1_marker = ' '
    player2_marker = ' '

    #keep asking if player doesn't provide an 'X' or 'O'
    while player1_marker != 'X' and player1_marker != 'O':
        player1_marker = input('Player 1, which marker will you use? ')

        if player1_marker == 'X':
            player1_marker = 'X'
            player2_marker = 'O'
        elif player1_marker == 'O':
            player1_marker = 'O'
            player2_marker = 'X'
        else:
            print("The only markers available are 'X' or 'O'.")

    #let players know their markers
    print(f"Player 1 will be {player1_marker}'s.")
    print(f"Player 2 will be {player2_marker}'s.")

    return player1_marker, player2_marker            

def place_marker(board, marker, position):
    #set the chosen position to be the marker
    board[int(position)] = marker

    return board

def win_check(board, marker):
    #check if there is a winner
    return ((board[1] == marker and board[2] == marker and board[3] == marker) #across bottom
            or (board[4] == marker and board[5] == marker and board[6] == marker) #across middle
            or (board[7] == marker and board[8] == marker and board[9] == marker) #across top
            or (board[1] == marker and board[5] == marker and board[9] == marker) #diagonal (bottom left to top right)
            or (board[7] == marker and board[5] == marker and board[3] == marker) #diagonal (top left to bottom right)
            or (board[7] == marker and board[4] == marker and board[1] == marker) #down left column
            or (board[8] == marker and board[5] == marker and board[2] == marker) #down center column
            or (board[9] == marker and board[6] == marker and board[3] == marker) #down right column
            )

def choose_first():
    #randomly decide who goes first
    x = random.randint(0,1)

    if x == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    #check whether a space on the board is freely available
    return (board[position] != 'X' and board[position] != 'O')
    #return board[position] == ' '

def full_board_check(board):
    #check if the board is full
    for i in range(1,9):
        if space_check(board, i):
            return False
    return True 

def player_choice(board):
    #ask for player's next position
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Please select your next position. "))
    return position

def replay():
    #ask the player if they want to play again
    return input('Would you like to play again? Enter Yes or No: ').lower().startswith('y')


#play the game 
if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")

    while True:
        #reset the board
        board = ['0','1','2','3','4','5','6' ,'7','8','9']
        #board = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first.')

        start_game = input('Are you ready to start the game? Enter Yes or No. ')

        if start_game.lower()[0] == 'y':
            game_on = True 
        else:
            game_on = False
        
        while game_on:
            if turn == 'Player 1':
                #Player 1's turn 
                display_board(board)
                print('Player 1')
                position = player_choice(board)
                place_marker(board, player1_marker, position)

                if win_check(board, player1_marker):
                    display_board(board)
                    print('Congratulations! Player 1 has won!')
                    game_on = False 
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('This round ends in a draw.')
                        break
                    else:
                        turn = 'Player 2'
            else:
                #Player 2's turn
                display_board(board)
                print('Player 2')
                position = player_choice(board)
                place_marker(board, player2_marker, position)

                if win_check(board, player2_marker):
                    display_board(board)
                    print('Congratulations! Player 2 has won!')
                    game_on = False 
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('This round ends in a draw.')
                        break
                    else:
                        turn = 'Player 1'
        
        if not replay():
            break