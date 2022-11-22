import model.block as b

class Wall(b.Block):
    def __init__(self, row, col):
        super().__init__(row, col)