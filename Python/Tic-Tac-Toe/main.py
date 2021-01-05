##functions
    #board
    #display
    #play game
    #handle turn
    #check win
        #check rows
        #cheak columns
        #cheak diagonals
    #check tie
    #flip player+
    # +---#

board = ['-','-','-','-','-','-','-','-','-',]
game_still_going = True

#who won or tie
winner = None
#Whos turn is it
currunt_player = 'X'

def display_board():
    print(board[0]+'|'+board[1] +'|'+board[2])
    print(board[3]+'|'+board[4] +'|'+board[5])
    print(board[6]+'|'+board[7] +'|'+board[8])

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    #setup global 
    global winner
    #check rows 
    row_winner = check_rows()
    #check columns 
    column_winner = check_columns()
    #check diagonal
    diagonal_winner = check_diagonal()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        #no win
        winner = None
    

def check_rows():
    #setup global variable
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3 :
        game_still_going = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]

def check_columns():
    #setup global variable
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3 :
        game_still_going = False
    if column_1:
        return board[0]
    if column_2:
        return board[3]
    if column_3:
        return board[6]


def check_diagonal():
    #setup global variable
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
   
    if diagonal_1 or diagonal_2 :
        game_still_going = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    

def check_if_tie():
    global game_still_going
    if '-' not in board:
            game_still_going = False
    return

def  flip_player():
    global currunt_player
    if currunt_player == 'X':
        currunt_player = 'O'
    elif currunt_player == 'O':
        currunt_player = 'X'
    return

def play_game():
    display_board() #displaying board
    #while game is still going
    while game_still_going :

        handle_turn(currunt_player)

        check_if_game_over()

        #flip to other player
        flip_player()

    if winner == 'X' or winner == 'O':
        print(winner+' won!!')
    elif winner == None:
        print("Tie..(-_-)")
        



def handle_turn(player):
    global currunt_player
    print(player + "'s turn.")
    position = input("Choose a position from 1-9 : ")
    valid = True
    while valid:
        
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            print()
            print(player + "'s turn.")
            position = input("Choose a position from 1-9 : ")


        position = int(position)-1
        if str(board[position]) != '-':
            print("you cant overwrite f@@king idiot..")
        else:
            valid = False
            
    
    board[position] = player
    display_board()


play_game()




#play = True
#while play == True :
#    print("Play again??! type :(Y/N)")
#    more = str(input())
#    if more != 'Y' or 'N':
#        print()
#        print('invalid entry') 
#        
#    else:
#        if more == "Y" :
#            play = False
#            play_game()
#            
#        else:   
#            play = False
#            exit

