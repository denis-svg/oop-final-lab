import json
import model.wall as w
import model.dot as d


class Maze:
    def __init__(self) -> None:
        self.walls = {}
        self.dots = {}
        self.resetMaze()
    
    def resetMaze(self):
        dots_loc = {}
        walls_loc = {}
        self.walls = {}
        self.dots = {}

        f = open('model/dots.json')
        dots_loc = json.load(f)
        f.close()

        f = open('model/walls.json')
        walls_loc = json.load(f)
        f.close()
        i = 0
        for key in dots_loc.keys():
            if key not in self.dots:
                row, col = key.split(";")
                i += 1
                self.dots[key] = d.Dot(int(row), int(col))
        
        for key in walls_loc.keys():
            if key not in self.walls:
                row, col = key.split(";")
                i += 1
                self.walls[key] = w.Wall(int(row), int(col))

    def isWall(self, row, col):
        key = str(row) + ';' + str(col)
        if key in self.walls:
            return True
        return False

    def isDot(self, row, col):
        key = str(row) + ';' + str(col)
        if key in self.dots:
            return True
        return False
    
    def getDotsEaten(self):
        i = 0
        for key in self.dots.keys():
            if self.dots[key].isEaten():
                i += 1
        return i



        