from tkinter import *
import random

# Creating of window

game = Tk()
game.title("Tic Tac Toe Game")
game.minsize(width=500, height=400)
game.resizable(True, True)
game.config(background="#00dbca")
icon = PhotoImage(file='icon.ico')
game.iconphoto(True, icon)

players = ["x","o"]
player = random.choice(players)
buttons = ([0,0,0],
           [0,0,0],
           [0,0,0])
label = Label(text=player + " turn", font=("Helvetica", 15))
label.pack(side="top", anchor="c", pady=10)



def rules_game():

    rules = Tk()
    rules.title("Rules for Tic Tac Toe Game")
    rules.minsize(width=500, height=400)
    rules.resizable(True, True)
    rules.config(background="#00dbca")  
    # Rules in window
    text_1 = (f"Welcome to TIC TAC TOE",
            f"="*42,
            f"GAME RULES:",
            f"Each player can place one mark (or stone)",
            f"per turn on the 3x3 grid. The WINNER is",
            f"who succeeds in placing three of their",
            f"Marks in a:",
            f"* Horizontal",
            f"* Vertical",
            f"* Diagonal",
            f"="*42,
            )

    for i in text_1:   
        welcome_msg = Label(rules, text=i, background="#00dbca", font=("Helvetica", 15, "italic"),
                                    fg="black")
        welcome_msg.pack(side="top", expand=True, anchor="c", pady=(0, 0), padx=0)
    rules.mainloop()

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False

def new_game():

    global player

    player = random.choice(players)

    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

def empty_spaces():
    spaces = 9 

    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -=1
    
    if spaces == 0:
        return False
    else:
        return True


rules_button = Button(game, text="Rules of the game", command=rules_game )
rules_button.pack(side="left", anchor="ne", pady=0, padx=10)

restar_button = Button(game, text="Restart the game", command=new_game )
restar_button.pack(side="right", anchor="ne", pady=0, padx=10)

frame = Frame(game)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',20), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)


# Main cyclus
game.mainloop()
