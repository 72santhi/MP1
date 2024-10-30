# Name: Santhi Daggubati
# Date: 15-09-2024
# 
# This program is a text-based Connect Four game where two players (X and O) take turns 
# placing their pieces in a 6X7 grid. Players must enter a column-letter and row number 
# to place their pieces, and the game checks(check_board()) for a winner by finding four consecutive 
# cells horizontally, vertically, or diagonally. The game allows players to replay and 
# ends when one player wins or the board is full. 


def valid_input(board, r, c):
    #Validates if the input is with in the boundary of the game board
    if not (0 <= r < 6) or not (0 <= c < 7):    
        print("Invalid entry: try again.")
        print("Row & column numbers must be either 0, 1 or 2") 
        return False
    
    #Validates if the cell is empty
    if board[r][c] != " ":
        print("That cell is already taken.")
        print("Please make another selection.") 
        return False
    
    return True

def display_board(board):
    #Displays the current board whenever the function is called
    for i in range(5, -1, -1):
        print(
            f"| {i+1} | {board[i][0]} | {board[i][1]} | {board[i][2]} |"
            f" {board[i][3]} | {board[i][4]} | {board[i][5]} | {board[i][6]} |")
        print("-"*34)
    print("|R\\C| a | b | c | d | e | f | g |")
    print("-"*34)

def available_positions(board):
    pos_maps = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g"}
    empty_pos = []

    for col in range(7):
        for row in range(6):
            if board[row][col] == " ":
                empty_pos.append(pos_maps[col]+str(row + 1))
                break
    
    return empty_pos

def check_board(board, player):
    """
    Checks if the current player has won the game.
    Scans rows, columns, and diagonals for four consecutive cells of the player's symbol.
    Returns:
        int: 1 if the player has won, 0 otherwise.
    """
    rows, cols = 6, 7
    #row checking
    for i in range(6):
        for j in range(cols-3):
            if (board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == player):
                return 1
            
    #column checking        
    for i in range(7):
        for j in range(0, rows-3):
            if (board[j][i] == board[j+1][i] == board[j+2][i] == board[j+3][i] == player):
                return 1
            
    #diagnol checking
    for i in range(rows-3): #r-3
        for j in range(cols-3): #c-3
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == player:
                return 1
            
    for i in range(rows-3): #r-3
        for j in range(6, 2, -1): #(c-1)-3-1
            if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] == player:
                return 1
            
    return -1

def connect4(board):
    """
    Main game loop that allows players to take turns, input their moves, 
    and check for wins or a draw.
    """
    turns = 1
    player = "X"
    pos_maps = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6}

    while True:
        #Take input from user and validating it
        print(f"\n{player}'s turn.")
        print(f"Where do you want your {player} placed?")
        avail_pos = available_positions(board)
        print("Available positions are: ", avail_pos)

        pos = input("\nPlease enter column-letter and row number (e.g., a1): ")
    
        if len(pos) != 2:
            print("The input format should be as provided in example")
            print("Please enter the correct input.")
            continue

        if pos not in avail_pos:
            print("The cell should be in the available positions.")
            print("Please make the selection again")
            continue

        r, c = int(pos[1]) - 1, pos_maps[pos[0]]    

        if not valid_input(board, r, c):
            continue

        print("Thank you for your selection.")
        board[r][c] = player
        
        #checks the board if there is a win or draw after every move
        check = check_board(board, player)

        if check == 1:
            print(f"{player} IS THE WINNER!!!")
            break
        elif turns == 6*7:
            print("DRAW! NOBODY WINS!")
            break
        else:
            display_board(board)
            player = "O" if player == "X" else "X" #Switch players after valid move
            turns += 1

    return -1

repeat = "y"

while repeat[0].lower() == "y":
    board = [[" " for _ in range(7)] for _ in range(6)]
    print("\nNew Game: X goes first.\n")
    display_board(board)
    connect4(board) 
    repeat = input("\nAnother game (y/n)? ")

print("Thank you for playing!")
