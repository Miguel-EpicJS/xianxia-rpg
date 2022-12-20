from enum import Enum

from colors import Colors

class World:
    def __init__(self, world = []):
    
        self.colorManager = Colors()

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
                    print( f'{self.colorManager.Yellow(self.world[i][j]["type"])}', end=' ' )
                elif self.world[i][j]["qi"] == 0:
                    print( f'{self.colorManager.Red(self.world[i][j]["type"])}', end=' ')
                elif self.world[i][j]["type"] == self.tilesType.Forest.value:
                    print( f'{self.colorManager.Green(self.world[i][j]["type"])}', end=' ')
                else:
                    print( self.world[i][j]["type"], end=' ' )
            print("")

    def get_world(self):
        return self.world

    def move(self, pos):
        if pos[0] + self.current[0] < 0 or pos[1] + self.current[1] < 0 or pos[0] + self.current[0] == self.size or pos[1] + self.current[1] == self.size:
            return
        self.world[self.current[0]][self.current[1]]["type"] = self.tilesType.Forest.value
        self.current = tuple(map(lambda i, j: i+j, self.current, pos))
        self.world[self.current[0]][self.current[1]]["type"] = self.tilesType.Player.value

    def absorb(self, amount):
        if self.world[self.current[0]][self.current[1]]["qi"] >= amount:
            self.world[self.current[0]][self.current[1]]["qi"] -= amount
            return True
        return False

