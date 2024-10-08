"""
Projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jan Kašpárek
email: jan.kasparek96@gmail.com
discord: jankasparek0720
"""


def main_code():
    # List of lists for creation of board
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    # Board numbers for filling the board by symbols
    board_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def gameboard(rows: int = 3, colums: int = 3):
        """
        Creation of gameboard for tic tac toe
        """
        for i in range(rows):
            print("\n+---+---+---+")
            print("|", end="")
            for j in range(colums):
                print("", board[i][j], end=" |")
        print("\n+---+---+---+")

    def choose_symbol(index: bool = True):
        """
        Player chooses a game symbol X or O

        Returns:
            str: symbol_1, symbol_2 are player symbols
        """
        while index:
            print("-" * 42)
            # Pick a symbol
            player_symbol = input(str("Chose a player symbol [X, O]: "))
            print("-" * 42)
            # Compare input with available symbols
            if player_symbol.upper() == "X" or player_symbol.upper() == "O":
                symbol_1 = player_symbol.upper()
                if symbol_1 == "X":
                    symbol_2 = "O"
                else:
                    symbol_2 = "X"
                print(f"Player 1 choose symbol {symbol_1}, Player 2 has {symbol_2}")
                # Dont need to continue the loop index = False
                index = False
            else:
                print("This is not a valid input, try again:")
        return symbol_1, symbol_2

    def modify_board(number: int, symbol: str):
        """
        Board modifier
        Modulo % is used for distinction between rows of the board
        Each row is [0, 1, 2] but numbers inputs for second row are 3, 4, 5,
        After using modulo % 3 we get  3 == 0, 4 == 1, 5 == 2

        Args:
            number (int): board number for symbol field input
            symbol (str): symbol to add to field
        """
        # Number -1 coz board index starts from 0
        number -= 1
        # 1st row of the board
        if number in range(0, 3):
            board[0][number] = symbol
        # 2nd row
        elif number in range(3, 6):
            board[1][number % 3] = symbol
        # 3rd row
        elif number in range(6, 10):
            board[2][number % 6] = symbol
        gameboard()

    def check_winner(symbol):
        """
        Check for matching symbol of each row, column and diagonal.
        If there is a winner it goes to new_game()
        """
        # Check matching symbol for each rows and columns
        for rows, columns in zip(range(3), range(3)):
            #  Check rows
            if board[rows][0] == board[rows][1] == board[rows][2] == symbol:
                print(
                    "-" * 50,
                    f"Congratulations, Player with symbol {symbol} WON!!!!",
                    "-" * 50,
                    sep="\n",
                )
                new_game()

            #  Check columns
            if board[0][columns] == board[1][columns] == board[2][columns] == symbol:
                print(
                    "-" * 50,
                    f"Congratulations, Player with symbol {symbol} WON!!!!",
                    "-" * 50,
                    sep="\n",
                )
                new_game()

        #  Check symbols diagonaly
        if (
            board[0][0] == board[1][1] == board[2][2] == symbol
            or board[0][2] == board[1][1] == board[2][0] == symbol
        ):
            print(
                "-" * 50,
                "-" * 50,
                sep="\n",
            )
            new_game()

        elif board_numbers == []:  # No more blank space availeble
            print(
                "-" * 50,
                "There are no empty fields left, we have a TIE !!!",
                "-" * 50,
                sep="\n",
            )
            new_game()

        return False

    def player_move():
        """
        Switching between player moves
        """
        symbol_1, symbol_2 = choose_symbol()  # Import symbols from function
        move_counter = 0
        while True:
            # Switching between players
            current_symbol = symbol_1 if move_counter % 2 == 0 else symbol_2
            print("-" * 50)
            move_input = input(
                f"Player {current_symbol}. Please enter your move number (1-9):"
            )
            print("-" * 50)

            # If input is not a digit
            if not move_input.isdigit():
                print(f"This is not a digit")
            else:
                move_input = int(move_input)
                # If input is in range but not available
                if move_input in range(1, 10) and move_input not in board_numbers:
                    print("This playing field is already occupied")
                elif move_input not in board_numbers:  # Input not in range
                    print("This number is not in valid range")
                else:
                    board_numbers.remove(move_input)
                    modify_board(move_input, current_symbol)
                    check_winner(current_symbol)
                    # Add one for player changover in next iteration
                    move_counter += 1

    def new_game():
        """
        Play again
        """
        game_again = input("Do you want to play again (Yes/No):")
        game_again = game_again.lower()
        if game_again == "yes":  # If yes go again to main_code()
            main_code()
        elif game_again == "no":  # Otherwise quit()
            print("Closing the GAME, BYE !")
        else:
            print("Dont understand!, Cloasing the GAME")
        quit()

    print(
        "=" * 42,
        "Welcome to TIC TAC TOE",
        "=" * 42,
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
        "=" * 42,
        "{:^40}".format("Let's start the game"),
        "=" * 42,
        sep="\n",
    )

    gameboard()
    player_move()


if __name__ == "__main__":
    main_code()
