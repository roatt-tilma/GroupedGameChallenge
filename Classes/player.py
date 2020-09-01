class Player:
    def __init__(self, name, regno):
        self.name = name
        self.regno = regno
        self.score = 0
    
    def add_score(self, points):
        self.score += points
    
    def get_points(self, base_point, diff_lvl, rem_time):
        return base_point + (diff_lvl * rem_time)/60
    
    def check_answer(self, answer, right_answer):
        if answer == right_answer:
            return True
        return False


    