from Classes.player import Player
from Classes.Information import PlayerInfo, Question

info = PlayerInfo()

name = info.get_name()
regno = info.get_regno()
player1 = Player(name, regno)
question1 = Question("blah blah?", ["1","2","3","4"], "1", 2, 10)

print(question1.get_answer())




