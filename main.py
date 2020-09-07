from Classes.player import Player, Game
from Classes.Information import PlayerInfo, Question, Admin
from tkinter import *


# creating window
root = Tk()
width, height = root.winfo_width(), root.winfo_height()
root.geometry("%dx%d+0+0" %(800, 800))
root.title("Who's the Boss? - Grouped Game Challenge")

admin_handle = Admin()
player_handle = PlayerInfo()
game_handle = Game()

def start_game():
    name = player_handle.get_name()
    regno = player_handle.get_regno()
    player1 = Player(name, regno)  
    
    question_stacks = admin_handle.load_questions()
    game_handle.start_game(question_stacks, 1, 1, player1, 5)
    print(player1.name, ", your score is: ", player1.score)

# creating label
#label = Label(root, text = "First Label", bg = "black", fg = "blue")
#label.grid(row = 0, column = 0)

# creating button
myButton = Button(root, text = "Start Game", command = start_game, bg = 'red', fg = 'green')
myButton.pack()

# running mainloops
root.mainloop()

def add_questions():
    print("Choose difficulty level")
    print("1. Easy\n2. Medium\n3. Hard\n4. HOT")
    diff_lvl = int(input())
    if diff_lvl == 1:
        n = int(input("Enter the number of questions to be added"))
        f = open(r".\Questions\Question_easy.txt", "a")
        for _ in range(n):
            admin_handle.add_questions(f)
            f.write("1 3\n")
            f.write("**||**\n")
    elif diff_lvl == 2:
        n = int(input("Enter the number of questions to be added"))
        f = open(r".\Questions\Question_medium.txt", "a")
        for _ in range(n):
            admin_handle.add_questions(f)
            f.write("2 5\n")
            f.write("**||**\n")
    elif diff_lvl == 3:
        n = int(input("Enter the number of questions to be added"))
        f = open(r".\Questions\Question_hard.txt", "a")
        for _ in range(n):
            admin_handle.add_questions(f)
            f.write("3 7\n")
            f.write("**||**\n")
    elif diff_lvl == 4:
        n = int(input("Enter the number of questions to be added"))
        f = open(r".\Questions\Question_HOT.txt", "a")
        for _ in range(n):
            admin_handle.add_questions(f)
            f.write("4 10\n")
            f.write("**||**\n")
    else:
        print("Invalid Input")















