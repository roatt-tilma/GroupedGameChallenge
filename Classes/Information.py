import random

class PlayerInfo:
    def get_name(self):
        name = input("Name: ")
        return name
    def get_regno(self):
        regno = input("Registration no.: ")
        return regno

class Question:
    def __init__(self, question, options, right_answer, diff_lvl, base_point):
        self.question = question
        self.options = options
        self.right_answer = right_answer
        self.diff_lvl = diff_lvl
        self.base_point = base_point

    def get_answer(self):
        print(self.question, "\n")
        random.shuffle(self.options)
        key_options = {chr(ord("a")+i):self.options[i] for i in range(len(self.options))}
        [print(key + ")", value) for key,value in key_options.items()]
        answer = key_options[input().lower()]
        return answer
    
