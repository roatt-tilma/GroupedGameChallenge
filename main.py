from Classes.player import Player, Game
from Classes.Information import Question, Admin
from tkinter import *
from PIL import ImageTk, Image

def submit(name, regno, info):
    global player
    player = Player(name, regno)
    info.destroy()
    start_game()

def back(any_frame):
    any_frame.destroy()
    create_homepage()

def add_again(the_frame):
    the_frame.destroy()
    add_questions()

def get_info():
    frame.destroy()
    info = LabelFrame(root, text = "Player Information", padx = 250, pady = 250)
    info.place(x = 700, y = 250)
    n = Label(info, text = "Name", width = 15, anchor = W).grid(row = 0, column = 0, columnspan = 1)
    r = Label(info, text = "Registration No.", width = 15, anchor = W).grid(row = 1, column = 0)
    name = Entry(info)
    regno = Entry(info)
    name.grid(row = 0, column = 1, pady = 10)
    regno.grid(row = 1, column = 1, pady = 20)
    back_button = Button(info, text = "Back", width = 10, height = 2,  activebackground = "red", command = lambda: back(info)).grid(row = 2, column = 0, sticky = "nsew")
    s = Button(info, text = "SUBMIT", width = 10, height = 2,  activebackground = "blue", command = lambda: submit(name.get(), regno.get(), info)).grid(row = 2, column = 1, sticky = "nsew")

def start_game():
    question_stacks = admin_handle.load_questions()
    game_handle.launch_game(question_stacks, 1, 1, player, 5)
    resultFrame = LabelFrame(root, text = "Result", padx = 250, pady = 250)
    result = Label(resultFrame, text = player.name + ", your score is: " + str(player.score), fg = "green", font = 80, pady = 20)
    resultFrame.place(x = 700, y = 250)
    result.pack()
    back_button = Button(resultFrame, text = "Back", width = 10, height = 2,  activebackground = "blue", command = lambda: back(resultFrame)).pack()

def check_passcode(passcode, info):
    if passcode == "Admin":
        info.destroy()
        add_questions()
    else:
        try:
            error_label.pack_forget()
        except:
            pass
        error_label.grid(row = 2, column = 0)

def get_passcode():
    frame.destroy()
    info = LabelFrame(root, text = "Passcode Prompt", padx = 250, pady = 250)
    info.place(x = 700, y = 250)
    global error_label
    error_label = Label(info, text = "Wrong Passcode!!", fg = "red")
    p = Label(info, text = "Passcode", width = 15, anchor = W).grid(row = 0, column = 0)
    passcode = Entry(info, show = "*")
    passcode.grid(row = 0, column = 1, pady = 10)
    back_button = Button(info, text = "Back", width = 10, height = 2,  activebackground = "red", command = lambda: back(info)).grid(row = 1, column = 0, sticky = "nsew")
    s = Button(info, text = "SUBMIT", width = 10, height = 2, activebackground = "blue", command = lambda: check_passcode(passcode.get(), info)).grid(row = 1, column = 1, sticky = "nsew")
    
def create_homepage():
    global frame
    frame = LabelFrame(root, text = "Who's the Boss? - GGC", padx = 250, pady = 250)
    frame.place(x = 700, y = 250)

    start_G = Button(frame, text = "Start Game", width = 20, height = 3, activebackground = "blue", command = get_info).grid(pady = 10)
    add_Q = Button(frame, text = "Add Questions", width = 20, activebackground = "blue", command = get_passcode).grid(pady = 10)
    button_exit = Button(frame, text = 'Exit', width = 20, activebackground = "red", command = root.quit).grid()

def easy(ADQ):
    for widget in ADQ.winfo_children():
        widget.destroy()
    f = open(r".\Questions\Question_easy.txt", "a")
    admin_handle.add_question(f, ADQ)
    f.write("1 3\n")
    f.write("**||**\n")
    f.close()
    label1 = Label(ADQ, text = "You added an easy question!", fg = "blue", font = "100")
    back_button = Button(ADQ, text = "Done", width = 10, height = 2, activebackground = "blue", command = lambda: back(ADQ))
    add_button = Button(ADQ, text = "Add Again", width = 10,  height = 2, activebackground = "blue", command = lambda: add_again(ADQ))
    label1.grid(row = 0, column = 0, columnspan = 2, pady = 10)
    back_button.grid(row = 1, column = 0, pady = 10, padx = 3)
    add_button.grid(row = 1, column = 1, pady = 10, padx = 3)

def medium(ADQ):
    for widget in ADQ.winfo_children():
        widget.destroy()
    f = open(r".\Questions\Question_medium.txt", "a")
    admin_handle.add_question(f, ADQ)
    f.write("2 5\n")
    f.write("**||**\n")
    f.close()
    label1 = Label(ADQ, text = "You added a medium question!", fg = "blue", font = "100")
    back_button = Button(ADQ, text = "Back", width = 10, height = 2, activebackground = "blue", command = lambda: back(ADQ))
    add_button = Button(ADQ, text = "Add Again", width = 10,  height = 2, activebackground = "blue", command = lambda: add_again(ADQ))
    label1.grid(row = 0, column = 0, columnspan = 2, pady = 10)
    back_button.grid(row = 1, column = 0, pady = 10, padx = 3)
    add_button.grid(row = 1, column = 1, pady = 10, padx = 3)

def hard(ADQ):
    for widget in ADQ.winfo_children():
        widget.destroy()
    f = open(r".\Questions\Question_hard.txt", "a")
    admin_handle.add_question(f, ADQ)
    f.write("3 7\n")
    f.write("**||**\n")
    f.close()
    label1 = Label(ADQ, text = "You added a hard question!", fg = "blue", font = "100")
    back_button = Button(ADQ, text = "Back", width = 10, height = 2, activebackground = "blue", command = lambda: back(ADQ))
    add_button = Button(ADQ, text = "Add Again", width = 10,  height = 2, activebackground = "blue", command = lambda: add_again(ADQ))
    label1.grid(row = 0, column = 0, columnspan = 2, pady = 10)
    back_button.grid(row = 1, column = 0, pady = 10, padx = 3)
    add_button.grid(row = 1, column = 1, pady = 10, padx = 3)

def hot(ADQ):
    for widget in ADQ.winfo_children():
        widget.destroy()
    f = open(r".\Questions\Question_HOT.txt", "a")
    admin_handle.add_question(f, ADQ)
    f.write("4 10\n")
    f.write("**||**\n")
    f.close()
    label1 = Label(ADQ, text = "You added a HOT question!", fg = "blue", font = "100")
    back_button = Button(ADQ, text = "Back", width = 10, height = 2, activebackground = "blue", command = lambda: back(ADQ))
    add_button = Button(ADQ, text = "Add Again", width = 10,  height = 2, activebackground = "blue", command = lambda: add_again(ADQ))
    label1.grid(row = 0, column = 0, columnspan = 2, pady = 10)
    back_button.grid(row = 1, column = 0, pady = 10, padx = 3)
    add_button.grid(row = 1, column = 1, pady = 10, padx = 3)

def add_questions():
    ADQ = LabelFrame(root, text = "Add Questions", padx = 250, pady = 250)
    ADQ.place(x = 600, y = 150)
    label1 = Label(ADQ, text = "Choose difficulty level:", font = "100").grid(row = 0, column = 0, columnspan = 4)
    Easy = Button(ADQ, text = "Easy", width = 10, height  = 2, command = lambda: easy(ADQ))
    Medium = Button(ADQ, text = "Medium", width = 10, height  = 2, command = lambda: medium(ADQ))
    Hard = Button(ADQ, text = "Hard", width = 10, height  = 2, command = lambda: hard(ADQ))
    HOT = Button(ADQ, text = "HOT", width = 10, height  = 2, command = lambda: hot(ADQ))
    back_button = Button(ADQ, text = "Back", width = 10, height = 2, activebackground = "blue", command = lambda: back(ADQ))
    Easy.grid(row = 1, column = 0, padx = 5, pady = 20)
    Medium.grid(row = 1, column = 1, padx = 5, pady = 20)
    Hard.grid(row = 1, column = 2, padx = 5, pady = 20)
    HOT.grid(row = 1, column = 3, padx = 5, pady = 20)
    back_button.grid(row = 2, padx = 20, pady = 50, columnspan = 4)
    
if __name__ == "__main__":
    global root
    root = Tk()
    root.attributes('-fullscreen', True)
    root.title("Who's the Boss? - Grouped Game Challenge")
    root.iconbitmap('icon.ico')
    global game_handle
    game_handle = Game(root)
    global admin_handle
    admin_handle = Admin(root)
    create_homepage()
    root.mainloop()













