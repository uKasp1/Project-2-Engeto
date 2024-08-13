"""
Projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jan Kašpárek
email: jan.kasparek96@gmail.com
discord: jankasparek0720
"""
# Switching value between First run of the code and New game option 
New_game_value = False
# For changover between players 
move_counter = 0 

# Main code 
def Main_code():
    # definitions of the used variables 
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    board_numbers = [1,2,3,4,5,6,7,8,9]
    symbols = ["X", "O"]
    rows = 3
    colums = 3 

    #Main loop where we run the code 
    def Main_loop():
        # if this is a first run of the game start all functions 
        if New_game_value == False:    
            Hello_Rules()
            Gameboard()
            Choose_symbol()
        # if its a new game run without the Rules function 
        else:
            print("="*50, "{:^50}".format("--Let's play again, then--"), "="*50, sep="\n")
            Gameboard()
            Choose_symbol()
             
    # Hello User/Game Rules
    def Hello_Rules():

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
    
    # Gameboard 
    def Gameboard():
        # Prints every row and column of the gameboard 
        for i in range(rows):
            print("\n+---+---+---+")
            print("|", end="")
            for j in range(colums):
                print("",board[i][j], end=" |")
        print("\n+---+---+---+")

    # Player choses symbol
    def Choose_symbol():
        symbol_1 = ""
        symbol_2 = ""
        # Player input 
        print("-"*42)
        player_symbol = input(str("Chose a player symbol [X, O]: "))
        print("-"*42)
        # First player chooses a symbol which is then deleted from variable symbols and second player gets the left one 
        if player_symbol.upper() in symbols:
            symbol_1 = player_symbol.upper()
            symbols.remove(player_symbol.upper())
            symbol_2 = str(symbols[0])
            print(f"Player 1 chose symbol: {symbol_1}")
            print(f"Player 2 has symbol: {symbol_2}")
            player_move(symbol_1,symbol_2)  
        # If its not a valid input, user tries again 
        else:
            print("This is not a valid input, try again:")
            Choose_symbol()

    # Changover between players 
    def player_move(symbol_1, symbol_2):
        # Move counter for changover between players 
        global move_counter
        
        while Index := True:
            # The code is tried for errors 
            try:    
                # If this condition is met, player can choose a number input.
                if move_counter %2 ==0: 
                        # Player input 
                        print("-"*50)
                        player1_move = input(f"Player {symbol_1}. Please enter your move number (1-9):")
                        print("-"*50)
                        # If not a digit then set counter to number for player_1 and restar block player move 
                        if not player1_move.isdigit():
                            move_counter = 0 
                            print("This is not a number, try again")
                            player_move(symbol_1,symbol_2)
                        # If yes, set input as integer and continue 
                        else:
                            player1_move = int(player1_move)

                        # If the number input is in range, set counter to player_2, remove input number from board numbers
                        # Run the fnctions modify board and check winners 
                        if (player1_move >= 1 and player1_move <= 9):
                            move_counter = 1
                            board_numbers.remove(player1_move) 
                            modify_board(player1_move,symbol_1)
                            check_winner(symbol_1, move_counter)
                        else:
                            # If number is out of range
                            move_counter = 0
                            print("This number is not in range, try again")
                            player_move(symbol_1,symbol_2)    
                          
                else:
                        # Same as player one 
                        print("-"*50)
                        player2_move = input(f"Player {symbol_2}. Please enter your move number (1-9):")
                        print("-"*50)
                        
                        if not player2_move.isdigit():
                            move_counter = 1
                            print("this is not a number, try again")
                            player_move(symbol_1,symbol_2)
                        else:
                            player2_move = int(player2_move)

                        # Same as for Player 1
                        if (player2_move >= 1 and player2_move <= 9): 
                            move_counter = 0
                            board_numbers.remove(player2_move)
                            modify_board(player2_move,symbol_2)
                            check_winner(symbol_2, move_counter)
                        else:
                          move_counter = 1
                          print("This number is not in range, try again")
                          player_move(symbol_1,symbol_2) 
                          
            # If the input is not in list on number boards. 
            except ValueError:  
                # Print message and set move_counter, to stay in current player_move
                print("This playing field is already occupied")
                if move_counter == 1:
                    move_counter = 0
                else:
                    move_counter = 1
                                 
    # Fill the board with symbols
    def modify_board(number, symbol):
        # number -1 because the board index start with 0
        number -= 1 
        # At the start we defined a board with 3 list in 1. Each list is one row with indexing 0[0,1,2], 1[0,1,2], 2[0,1,2]
        # If the input number is ((from 1 to 3) - 1) then, its the same as indexing of the list, symbol is add to corresponding possition 
        if number >= 0 and number <= 2:
            board[0][number] = symbol
        elif number >= 3 and number <= 5:
            # Here is - 3 because we are in second list but the indexes are still form 0 to 2. If we have input 5, then - 3
            # that is 2 and we have corresponding possition in the list  
            number -= 3 
            board[1][number] = symbol
        elif number >= 6 and number <= 8:
            # Same goes for list number 3 we have to reduce the input value by 6 
            number -= 6
            board[2][number] = symbol
        # Prints changed gameboard after every move 
        Gameboard()
       
    # Decides winning conditions 
    def check_winner(symbol, move):
        
        # Check all rows if the symbol is the same 
        for i in range(2):
            if (board[i][0] == board[i][1] == board[i][2] == symbol):
                if move == 1:
                    print("-"*50, f"Congratulations, Player 1 won with symbol {symbol}", "-"*50, sep="\n")
                else:
                    print("-"*50, f"Congratulations, Player 2 won with symbol {symbol}", "-"*50, sep="\n")
                New_game()

        # Check all collums if the symbol is the same 
        for j in range(3):
            if (board[0][j] == board[1][j] == board[2][j] == symbol):
                if move == 1:
                    print("-"*50, f"Congratulations, Player 1 won with symbol {symbol}", "-"*50, sep="\n")
                else:
                    print("-"*50, f"Congratulations, Player 2 won with symbol {symbol}", "-"*50, sep="\n")
                New_game()

        # Check diagonal lane if the symbol is same 
        if (board[0][0] == board[1][1] == board[2][2] == symbol):
            if move == 1:
                print("-"*50, f"Congratulations, Player 1 won with symbol {symbol}", "-"*50, sep="\n")
            else:
                print("-"*50, f"Congratulations, Player 2 won with symbol {symbol}", "-"*50, sep="\n")
            New_game()

        # Check diagonal lane if the symbol is same 
        elif (board[0][2] == board[1][1] == board[2][0] == symbol):
            if move == 1:
                print("-"*50, f"Congratulations, Player 1 won with symbol {symbol}", "-"*50, sep="\n")
            else:
                print("-"*50, f"Congratulations, Player 2 won with symbol  {symbol}", "-"*50, sep="\n")
            New_game()

        # If there are no available board_numbers that means fields are full without winner
        elif board_numbers == []:
            print("-"*50, "There are no empty fields left, we have a TIE !!!", "-"*50, sep="\n")
            New_game()

    # New game option 
    def New_game():
        global New_game_value
        # Input for user 
        game_again = input("Do you want to play again (Yes/No):")
        game_again = game_again.lower()
        # If yes changes the new_game_value so we run the code without the rules function 
        if game_again == "yes":
            New_game_value = True 
            Main_code()
        # If no or the input is something different quit the program 
        elif game_again == "no":
            print("Closing the GAME, BYE !")
            quit()
        else: 
            print("Dont understand!, Cloasing the GAME")
            quit()

    # Run the Main_loop            
    Main_loop()

# Run the main code 
Main_code()




