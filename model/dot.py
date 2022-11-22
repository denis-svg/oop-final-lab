import model.block as b

class Dot(b.Block):
    def __init__(self, row, col):
        super().__init__(row, col)
        # when the dot is eaten it will display image2
        self.is_eaten = False

    def setEaten(self):
        self.is_eaten = True

    def isEaten(self):
        return self.is_eaten

    
    