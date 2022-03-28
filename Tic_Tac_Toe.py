#The list of all avaialable moves on the board
board = ['A','B','C','D','E','F','G','H','I']
restricted = []
#The function responsible for visual representaion of the board
def display_board():
    print ("------------")
    print ("|", board[0],"|", board[1], "|", board[2], "|")
    print ("------------")
    print ("|", board[3],"|", board[4], "|", board[5], "|")
    print ("------------")
    print ("|", board[6],"|", board[7], "|", board[8], "|")
    print ("------------")

def get_player_action(player):
    valid = False
    while (not valid):
     message = "Please select a letter for the player who plays " + player
     action = input(message)
     if not action.isalpha() or len(action) != 1:
         print("Please select a valid index")
         continue
     else:
         valid = ord(action) >= 65 and ord(action) <= 73
         if (valid):
             if (action in restricted):
                 valid = False
                 print("Please make sure to pick a cell that's not already taken!")
             else:
                 valid = True
                 return action


def update_game_board(action , player):
    board[ord(action) - 65] = player
    display_board()


def is_winner():
    diagonal1 = (ord(board[0]) + ord(board[4]) + ord(board[8])) - 3 * ord('0') == 15
    diagonal2 = (ord(board[2]) + ord(board[4]) + ord(board[6])) - 3 * ord('0') == 15
    row1 = (ord(board[0]) + ord(board[1]) + ord(board[2])) - 3 * ord('0') == 15
    row2 = (ord(board[3]) + ord(board[4]) + ord(board[5]))  - 3 * ord('0') == 15
    row3 = (ord(board[6]) + ord(board[7]) + ord(board[8])) - 3 * ord('0') == 15
    column1 = (ord(board[0])) + ord(board[3]) + ord(board[6]) - 3 * ord('0') == 15
    column2 = (ord(board[1]) + ord(board[4]) + ord(board[7])) - 3 * ord('0') == 15
    column3 = (ord(board[2]) + ord(board[5]) + ord(board[8])) - 3 * ord('0') == 15
    return  diagonal1 or diagonal2 or row1 or row2 or row3 or column1 or column2 or column3


def get_player_value(type):
    if (type == "odd"):
        valid = False
        while(not valid):
            value = input()
            if (value.isdigit()):
                if (int(value) >= 1 and int(value) <= 9 and int(value) % 2 != 0):
                    valid = True
                    return str(value)
                else:
                    print ("The number you picked is out of the allowed range!")
            else:
                print("Please make sure to pick a number!")
        

    if (type == "even"):
        valid = False
        while(not valid):
            value = input()
            if (value.isdigit()):
                if (int(value) >= 0 and int(value) <= 8 and int(value) % 2 == 0):
                    valid = True
                    return str(value)
                else:
                    print ("The number you picked is out of the allowed range!")
            else:
                print("Please make sure to pick a number!")





#The main function which controls the game in different states
def start_game():
    display_board()
    n_actions = 0
    #Let the odd player make a move and end the game if they won, if not just record their last move
    while (n_actions != 9):
        action = get_player_action ("odd")
        value = get_player_value("odd")
        update_game_board (action , value)
        restricted.append(action)

        if (is_winner()):
            print ("Odd player wins!")
            break
        n_actions += 1
        if (n_actions == 9):
            break

        action = get_player_action ("even")
        value = get_player_value("even")
        update_game_board (action , value)
        restricted.append(action)
        if (is_winner()):
            print ("Even player wins!")
            break
        n_actions += 1
    if (not is_winner()):
     print("Draw!")
 
  
start_game()