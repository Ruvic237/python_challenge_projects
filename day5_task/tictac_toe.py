# A TicTacToe program

# We need to display the board empty initialy
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
playerX = "X"
playerO = "O"

def display_board(board):
    print("*********************")
    print(f"| {board[0]} |---| {board[1]} |---| {board[2]} |")
    print("*********************")
    print(f"| {board[3]} |---| {board[4]} |---| {board[5]} |")
    print("*********************")
    print(f"| {board[6]} |---| {board[7]} |---| {board[8]} |")
    print("*********************")


# We need to obtain user input position and do some checks 
def user_input():
   choice = " "
   while choice not in ['0','1','2','3','4','5','6','7','8']:
            choice = input("Enter a number between (0,9) \n")
            if choice not in ['0','1','2','3','4','5','6','7','8']:
                    print("Wrong input dear user try again")
   return int(choice)
   
                 
# We need to add user input at desired position
def add_user_input(board,position,player):
    
    if board[position] == ' ':
        board[position] = player
        
    else:
        print("sorry position is occupied try another one")
        position = user_input()
        while board[position] != ' ':
            print("sorry position is occupied try another one")
            position = user_input()
        board[position] = player
    return board



# We need to determine who won
def check_winner():
    if (board[0] == board[1] == board[2] == "X") or (board[0]==board[3]==board[6]=="X") : 
        print("Player X is the winner")
        return True
    elif (board[3] == board[4] == board[5] == "X") or (board[1]==board[4]==board[7]=="X"): 
        print("Player X is the winner")
        return True
    elif (board[6] == board[7] == board[8] == "X") or (board[2]==board[5]==board[8]=="X"): 
        print("Player X is the winner")
        return True
    elif board[0] == 'X' and board[4] == "X" and board[8] == "X": 
        print("Player X is the winner")
        return True
    elif board[2] == 'X' and board[4] == "X" and board[6] == "X": 
        print("Player X is the winner")
        return True
    elif (board[0] == board[1] == board[2] == "O") or (board[0]==board[3]==board[6]=="O"): 
        print("Player O is the winner")
        return True
    elif (board[3] == board[4] == board[5] == "O") or (board[1]==board[4]==board[7]=="O"): 
        print("Player O is the winner")
        return True
    elif (board[6] == board[7] == board[8] == "O") or (board[2]==board[5]==board[8]=="O"): 
        print("Player O is the winner")
        return True
    elif board[0] == 'O' and board[4] == "O" and board[8] == "O": 
        print("Player O is the winner")
        return True
    elif board[2] == 'O' and board[4] == "O" and board[6] == "O": 
        print("Player O is the winner")
        return True
    else:
        pass
    
# We need to know if user want's to play again or not
def user_play():
   choice = " "
   while choice not in ['Y','N']:
            choice = input("Do you wish to play again? (Y or N) \n")
            if choice not in ['Y','N']:
                    print("Wrong input dear user try again to isert Y or N")
   if choice == 'Y':
       return True
   else:
       return False

# game start
game_on = True

def start():
        global board
        display_board(board)
        for r in range(10):
            if r >= 5:
                if check_winner():
                    break
            if r == 9:
                print("Draw")
            if r % 2 == 0:
                option = user_input()
                board = add_user_input(board,option,playerX)
                display_board(board)
            else:
                option = user_input()
                board = add_user_input(board,option,playerO)
                display_board(board)
start()
       

        
    