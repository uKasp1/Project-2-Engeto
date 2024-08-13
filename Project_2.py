"""
Projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jan Kašpárek
email: jan.kasparek96@gmail.com
discord: jankasparek0720
"""

def main_code():
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    board_numbers = [1,2,3,4,5,6,7,8,9]
    rows = 3
    colums = 3 

    def hello_rules():
        # Greets user and prints the rules of the game 
        print("Welcome to TIC TAC TOE",
                "="*42,
                "GAME RULES:",
                "Each player can place one mark (or stone)",
                "per turn on the 3x3 grid. The WINNER is",
                "who succeeds in placing three of their",
                "symbols in a:",
                " * Horizontal",
                " * Vertical",
                " * Diagonal, line.",
                "Each playing field has their own number",
                "from 1-9, n.1 starts in right top corner",
                "="*42,
                "{:^40}".format("Let's start the game"),
                "="*42,
                sep="\n"
                )
    hello_rules()

    def Gameboard():
    # Prints every row and column of the gameboard 
        for i in range(rows):
            print("\n+---+---+---+")
            print("|", end="")
            for j in range(colums):
                print("",board[i][j], end=" |")
        print("\n+---+---+---+")
    Gameboard()
    
    def choose_symbol():
        index = True
        while index:
            print("-"*42)
            player_symbol = input(str("Chose a player symbol [X, O]: "))
            print("-"*42)
            if player_symbol.upper() == "X":
                symbol_1 = player_symbol.upper()
                symbol_2 = "O"
                print(f"Player 1 chose symbol: {symbol_1}, Player 2 has symbol: {symbol_2}") 
                index = False 
            elif player_symbol.upper() == "O":
                symbol_1 = player_symbol.upper()
                symbol_2 = "X"
                print(f"Player 1 chose symbol: {symbol_1}, Player 2 has symbol: {symbol_2}")
                index = False
            else:
                print("This is not a valid input, try again:")
        return symbol_1, symbol_2
    
    def modify_board(number, symbol):
        number -= 1 
        if number >= 0 and number <= 2:
            board[0][number] = symbol
        elif number >= 3 and number <= 5:
            number -= 3 
            board[1][number] = symbol
        elif number >= 6 and number <= 8:
            number -= 6
            board[2][number] = symbol
        Gameboard()

    def check_winner(symbol, move):  
        for i in range(2):
            if (board[i][0] == board[i][1] == board[i][2] == symbol):
                if move == 1:
                    print("-"*50, f"Congratulations, Player 1 won with symbol {symbol}", "-"*50, sep="\n")
                else:
                    print("-"*50, f"Congratulations, Player 2 won with symbol {symbol}", "-"*50, sep="\n")
                
        for j in range(3):
            if (board[0][j] == board[1][j] == board[2][j] == symbol):
                if move == 1:
                    print("-"*50, f"Congratulations, Player 1 won with symbol {symbol}", "-"*50, sep="\n")
                else:
                    print("-"*50, f"Congratulations, Player 2 won with symbol {symbol}", "-"*50, sep="\n")
                
        if (board[0][0] == board[1][1] == board[2][2] == symbol):
            if move == 1:
                print("-"*50, f"Congratulations, Player 1 won with symbol {symbol}", "-"*50, sep="\n")
            else:
                print("-"*50, f"Congratulations, Player 2 won with symbol {symbol}", "-"*50, sep="\n")
            
        elif (board[0][2] == board[1][1] == board[2][0] == symbol):
            if move == 1:
                print("-"*50, f"Congratulations, Player 1 won with symbol {symbol}", "-"*50, sep="\n")
            else:
                print("-"*50, f"Congratulations, Player 2 won with symbol  {symbol}", "-"*50, sep="\n")
            
        elif board_numbers == []:
            print("-"*50, "There are no empty fields left, we have a TIE !!!", "-"*50, sep="\n")

    def player_move():
        symbol_1, symbol_2 = choose_symbol()
        move_counter = 0
        while True:
            try:    
                if move_counter %2 ==0: 
                        print("-"*50)
                        player1_move = input(f"Player {symbol_1}. Please enter your move number (1-9):")
                        print("-"*50)

                        if not player1_move.isdigit():
                            move_counter = 0 
                            print("This is not a number, try again")
                            player_move()
                        else:
                            player1_move = int(player1_move) 
                        if (player1_move >= 1 and player1_move <= 9):
                            move_counter = 1
                            board_numbers.remove(player1_move) 
                            modify_board(player1_move,symbol_1)
                            check_winner(symbol_1, move_counter)
                        else:
                            move_counter = 0
                            print("This number is not in range, try again")
                            player_move()            
                else:
                        print("-"*50)
                        player2_move = input(f"Player {symbol_2}. Please enter your move number (1-9):")
                        print("-"*50)
                        
                        if not player2_move.isdigit():
                            move_counter = 1
                            print("this is not a number, try again")
                            player_move()
                        else:
                            player2_move = int(player2_move)

                        if (player2_move >= 1 and player2_move <= 9): 
                            move_counter = 0
                            board_numbers.remove(player2_move)
                            modify_board(player2_move,symbol_2)
                            check_winner(symbol_2, move_counter)
                        else:
                            move_counter = 1
                            print("This number is not in range, try again")
                            player_move(symbol_1,symbol_2) 
            except ValueError:  
                print("This playing field is already occupied")
                if move_counter == 1:
                    move_counter = 0
                else:
                    move_counter = 1
    player_move()

    
    
        
            
main_code()
    