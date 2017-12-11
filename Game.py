
class Game:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.keys = {
                        "esc" : 27, "enter" : 13, "left" : 75,
                        "up": 72, "right": 77, "down": 80,
                    }
        self.directions = {
                    "s" : (0, -1),
                    "j" : (0,  1),
                    "z" : (1, 0),
                    "v" : (-1,  0),
                }
        self.direction = "z"
        self.body = [(0, 0), (1, 0), (2, 0)]
        self.food = [(0,2)]
        self.moves = 0
        self.fRefresh = 30
        self.fAmount = 1
        self.fLimit = 9000
        self.fTicks = 0
