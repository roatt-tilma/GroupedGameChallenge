from Classes.player import Player
from Classes.Information import PlayerInfo, Question, Admin

admin_handle = Admin()
player_handle = PlayerInfo()

print("*******************MAIN MENU*****************")
print("1. Start Quiz")
print("2. Add questions")

choice = int(input("Enter choice: "))

if choice == 1:
    name = player_handle.get_name()
    regno = player_handle.get_regno()
    player1 = Player(name, regno)  
    
    questions = admin_handle.load_questions()

    print(name + ", your score is:", player1.score) 
elif choice == 2:
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















