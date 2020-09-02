class Player:
    def __init__(self, name, regno):
        self.name = name
        self.regno = regno
        self.score = 0
    
    def add_score(self, base_points, rem_time, diff_lvl):
        points = base_points + (rem_time*diff_lvl/60)
        self.score += points


    