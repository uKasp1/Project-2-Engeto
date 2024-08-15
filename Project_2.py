"""
Projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jan Kašpárek
email: jan.kasparek96@gmail.com
discord: jankasparek0720
"""


def main_code():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
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
        """
        while index:
            print("-" * 42)
            player_symbol = input(
                str("Chose a player symbol [X, O]: ")
            )  # Pick a symbol
            print("-" * 42)
            if (
                player_symbol.upper() == "X" or player_symbol.upper() == "O"
            ):  # Compare input with available symbols
                symbol_1 = player_symbol.upper()
                if symbol_1 == "X":
                    symbol_2 = "O"
                else:
                    symbol_2 = "X"
                print(f"Player 1 choose symbol {symbol_1}, Player 2 has {symbol_2}")
                index = False
            else:
                print("This is not a valid input, try again:")
        return symbol_1, symbol_2

    def modify_board(number, symbol):
        """
        Board modifier
        Modulo % is used for distinction between rows of the board
        """
        number -= 1
        if number in range(0, 3):  # 1st row of the board
            board[0][number] = symbol
        elif number in range(3, 6):  # 2nd row
            board[1][number % 3] = symbol
        elif number in range(6, 10):  # 3rd row
            board[2][number % 6] = symbol
        gameboard()

    def check_winner(symbol):
        """
        Check for matching symbol of each row, column and diagonal.
        If there is a winner it goes to new_game()
        """
        # Check matching symbol for each rows and columns
        for rows, columns in zip(range(2), range(2)):
            #  Check
            if board[rows][0] == board[rows][1] == board[rows][2] == symbol:
                print(
                    "-" * 50,
                    f"Congratulations, Player with symbol {symbol} WON!!!!",
                    "-" * 50,
                    sep="\n",
                )
                new_game()
            if board[0][columns] == board[1][columns] == board[2][columns] == symbol:
                print(
                    "-" * 50,
                    f"Congratulations, Player with symbol {symbol} WON!!!!",
                    "-" * 50,
                    sep="\n",
                )
                new_game()

        if (
            board[0][0] == board[1][1] == board[2][2] == symbol
            or board[0][2] == board[1][1] == board[2][0] == symbol
        ):  # Check symbols diagonaly
            print(
                "-" * 50,
                f"Congratulations, Player with symbol {symbol} WON!!!!",
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
            current_symbol = (
                symbol_1 if move_counter % 2 == 0 else symbol_2
            )  # Switching between players
            print("-" * 50)
            move_input = input(
                f"Player {current_symbol}. Please enter your move number (1-9):"
            )
            print("-" * 50)

            if not move_input.isdigit():  # If input is not a digit
                print(f"This is not a digit")
            else:
                move_input = int(move_input)
                if (
                    move_input in range(1, 10) and move_input not in board_numbers
                ):  # If input is in range but not available
                    print("This playing field is already occupied")
                elif move_input not in board_numbers:  # Input not in range
                    print("This number is not in valid range")
                else:
                    board_numbers.remove(move_input)
                    modify_board(move_input, current_symbol)
                    check_winner(current_symbol)
                    move_counter += 1  # Add one for player changover in next iteration

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
