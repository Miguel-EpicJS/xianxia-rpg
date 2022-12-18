from enum import Enum

class World:
    def __init__(self, world = []):
        self.world = world
        self.current = (0,0)
        self.size = 0
        self.tilesType = Enum('Tiles', ["Player", "Forest", "City"])
        self.tilesDefault = { "type": self.tilesType.Forest.value, "qi": 100 }


    def create(self, size = 8):
        self.size = size
        
        self.world = [[ dict(self.tilesDefault) for _ in range(size)] for _ in range(size)]
        self.current = (size//2, size//2)
        
        self.world[size//2][size//2] = { "type": self.tilesType.Player.value, "qi": 100}

    def show(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.world[i][j]["type"] == self.tilesType.Player.value:
                    print( f'\033[93m{self.world[i][j]["type"]}\033[0m', end=' ' )
                else:
                    print( self.world[i][j]["type"], end=' ' )
            print("")

    def get_world(self):
        return self.world

    def move(self, pos):
        self.world[self.current[0]][self.current[1]]["type"] = self.tilesType.Forest.value
        self.current = tuple(map(lambda i, j: i+j, self.current, pos))
        self.world[self.current[0]][self.current[1]]["type"] = self.tilesType.Player.value

    def absorb(self, amount):
        self.world[self.current[0]][self.current[1]]["qi"] -= amount
        return amount

