
class Entity:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.type = t


class Game:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.keys = {
            "esc" : 27, 
            "enter" : 13, 
            "left" : 75,
            "up": 72, 
            "right": 77, 
            "down": 80,
        }
        self.directions = {
            "s" : (0, -1), "j" : (0, 1),
            "z" : (1, 0), "v" : (-1, 0),
        }
        self.direction = "z"
        self.fields = []
        self.entities = {
            "snake" : [
                Entity(0, 0, "snake"),
                Entity(1, 0, "snake"),
                Entity(2, 0, "snake"),
            ],
            "food" : [
                Entity(0, 2, "food"),
            ],
        }
        self.moves = 0
        self.refresh = 30
        self.amount = 1
        self.limit = 9000
        self.ticks = 0

        for i in range(self.height):
            row = [None] * self.width
            self.fields.append(row)

        for row in entities:
            for entity in row:
                self.fields[entity.y][entity.x] = entity

    def addEntity(self, entity, listName):
        self.entities[listName].append(entity)
        self.positions[entity.y][entity.x] = entity
        
    def getEntity(self, x, y):
        entity = self.positions[y][x]
        return entity

    def remEntity(self, entity, listName):
        i = li.index(entity)
        self.entities[listName].pop(i)
        self.positions[entity.y][entity.x] = None

    def move(self):
        offset = self.directions[self.direction]
        last = self.entities["snake"][count -1]

        newEntity = Entity(last[0] + offset[0], last[1] + offset[1])
        occupied = getEntity(entity.x, entity.y)

        if not occupied:
            self.addEntity(newEntity, "snake")
            self remEntity(self.entities["snake"][0])
        elif occupied.type == "food"
            self.addEntity(newEntity, "snake")
            self remEntity(occupied)
        elif occupied.type == "snake":
            print("Game over")


