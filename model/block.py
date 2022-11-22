import model.point as p


class Block:
    def __init__(self, row, col):
        self.location = p.Point(row, col)
    
    def setPosition(self, row, col):
        self.location.setRow(row)
        self.location.setCol(col)
