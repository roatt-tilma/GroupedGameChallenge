from Classes.Information import Question

class Player:
    def __init__(self, name, regno):
        self.name = name
        self.regno = regno
        self.score = 0
    
    def add_score(self, base_points, rem_time, diff_lvl):
        points = base_points + (rem_time*diff_lvl/60)
        self.score += points

class Game:
    def start_game(self, stacks, q_no, diff_lvl, player, number_of_questions):
        if q_no > number_of_questions:
            print("Maximum questions limit is reached!!")
            return
        stack = stacks[diff_lvl-1]
        question = stack.pop()
        answer, time = question.get_answer()
        if time == "exceed":
            print("time exceeded!!")
        elif question.check_answer(answer.lower()):
            player.add_score(question.base_point, 61-time, diff_lvl)
            if diff_lvl < 4:
                diff_lvl += 1
        else:
            if diff_lvl > 1:
                diff_lvl -= 1
        
        self.start_game(stacks, q_no+1, diff_lvl, player, number_of_questions)


    