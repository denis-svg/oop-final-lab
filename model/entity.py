import model.block as b

class Entity(b.Block):
    def __init__(self, row, col):
        super().__init__(row, col)
    
    def move(self, pos):
        self.location.setRow(self.location.getRow() + pos[0])
        self.location.setCol(self.location.getCol() + pos[1])
