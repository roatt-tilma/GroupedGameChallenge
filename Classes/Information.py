import random
import time
import threading

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

    def __countTick(self):
        global timer
        timer = 0
        global up 
        up = False
        while timer < 61 and up == False:
            timer += 1
            time.sleep(1)
            print(timer)
        if timer == 60:
            timer = 'exceed'
        
    def start_stopwatch(self):
        countTick_thread = threading.Thread(target = self.__countTick)
        countTick_thread.start()
        return countTick_thread

    def get_answer(self):
        print(self.question, "\n")
        random.shuffle(self.options)
        key_options = {chr(ord("a")+i):self.options[i] for i in range(len(self.options))}
        [print(key + ") ", value) for key,value in key_options.items()]
        watch = self.start_stopwatch()
        answer = key_options[input().lower()]
        global up
        up = True
        watch.join()
        time = timer
        return answer, time
    
    def check_answer(self, answer):
        if answer == self.right_answer:
            return True
        return False
    
class Admin:    
    def add_questions(self, f):
            question = input("Enter the question.\n")
            options = input("Enter the options separated by '||' in single line\n")
            right_answer = input("Enter the right answer\n")
            f.write(question + "\n")
            f.write(options + "\n")
            f.write(right_answer + "\n")
    
    def __getAllQuestions(self, filename):
        file_location = ".\\Questions\\" + filename
        f = open(file_location, "r")
        li = [i for i in f.read().split("**||**") if i]
        li.pop()
        f.close()
        return li
    
    def __build_question_objects(self, li):
        return_list = []
        for el in li:
            question_att = [i for i in el.splitlines() if i]
            quest = question_att[0]
            options = question_att[1].split("||")
            right_answer = question_att[2]
            diff_lvl, base_points = tuple(map(int, question_att[3].split()))
            question = Question(quest, options, right_answer, diff_lvl, base_points)
            return_list.append(question)
        return return_list

    def load_questions(self):
        n = 5
        easy_questions = random.sample(self.__getAllQuestions("Question_easy.txt"), n)
        medium_questions = random.sample(self.__getAllQuestions("Question_medium.txt"), n - 1)    
        hard_questions = random.sample(self.__getAllQuestions("Question_hard.txt"), n - 2)
        HOT_questions = random.sample(self.__getAllQuestions("Question_HOT.txt"), n - 3)        
        easy_questions = self.__build_question_objects(easy_questions)
        medium_questions = self.__build_question_objects(medium_questions)
        hard_questions = self.__build_question_objects(hard_questions)
        HOT_questions = self.__build_question_objects(HOT_questions)

        questions = [easy_questions, medium_questions, hard_questions, HOT_questions]

        return questions


    