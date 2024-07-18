WIDTH = 20
HEIGHT = 20

class Map:
    def __init__(self, size: tuple):
        self.x = size[0]
        self.y = size[1]
        self.coordinates = {}
        for x in range(self.x):
            for y in range(self.y):
                self.coordinates.update({(x,y): Tile()})
    
    def printMap(self):
        for y in range(self.y):
            y_string = ""
            for x in range(self.x):
                y_string += str(self.coordinates[(x,y)].getType())
                y_string += " "
            print(y_string)

class Tile:
    def __init__(self):
        self.type = 0

    def getType(self):
        return self.type


testMap = Map((WIDTH,HEIGHT))
testMap.printMap()
