# Name: Santhi Daggubati
# Date: 15-09-2024
# 
# This program implements a simple Tic-Tac-Toe game(tic_tac_toe()) where two players (X and O) take turns 
# placing their pieces in a 3x3 grid. The players input the row and column numbers 
# to place their pieces on the board. The game checks(check_board()) for a winner when one player gets three cells
# in a row, column, or diagonal. It also handles the case of a draw if the board is full.
# Players can choose to play multiple games.


def valid_input(board, r, c):
    #Validates if the input is with in the boundary of the game board
    if not (0 <= r < 3) or not (0 <= c < 3):    
        print("Invalid entry: try again.")
        print("Row & column numbers must be either 0, 1 or 2") 
        return 0
    
    #Validates if the cell is empty
    if board[r][c] != " ":
        print("That cell is already taken.")
        print("Please make another selection.") 
        return 0
    
    return 1

def display_board(board):
    #Displays the current board whenever the function is called
    print("-"*23)
    print("|R\\C|  0  |  1  |  2  |")
    for i in range(0, 3):
        print("-"*23)
        print(f"| {i} |  {board[i][0]}  |  {board[i][1]}  |  {board[i][2]}  |")
    print("-"*23)
    return -1

def check_board(board, player):
    """
    Checks if the current player has won the game.
    Scans rows, columns, and diagonals for four consecutive cells of the player's symbol.
    Returns:
        int: 1 if the player has won, 0 otherwise.
    """
    #row & column check
    for i in range(0, 3):
        if (board[i][0] == board[i][1] == board[i][2] == player):
            return 1
        if (board[0][i] == board[1][i] == board[2][i] == player):
            return 1
        
    #diagnol check    
    if board[0][0] == board[1][1] == board[2][2] == player:
        return 1
    if board[0][2] == board[1][1] == board[2][0] == player:
        return 1
       
    return 0       

def tic_tac_toe(board):
    """
    Main game loop that allows players to take turns, input their moves, 
    and check for wins or a draw.
    """
    player, turns = "X", 1
 
    while True:
        #Take input from user
        print(f"\n{player}'s turn.")
        print(f"Where do you want your {player} placed?")
        print("Please enter row number and column number seperated by a comma.")
        r, c = map(int, input().split(","))

        print(f"You have entered row #{r} \n  \t  and column  #{c}")
        
        #Validating the input
        if not valid_input(board, r, c):
            continue

        print("Thank you for your selection.")
        board[r][c] = player
            
        #checks the board if there is a win or draw after every move
        check = check_board(board, player)

        if check == 1:
            print(f"{player} IS THE WINNER!!!")
            break
        elif turns == 9:
            print("DRAW! NOBODY WINS!")
            break
        else:
            display_board(board)
            player = "O" if player == "X" else "X" #Switch player
            turns += 1
            
    return -1

repeat = "y"

while repeat[0].lower() == "y":
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("\nNew Game: X goes first.\n")
    display_board(board)
    tic_tac_toe(board) 
    repeat = input("\nAnother game? Enter Y or y for yes.\n")

print("Thank you for playing!")

