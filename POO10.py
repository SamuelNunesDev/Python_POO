

class Teste:

    def __init__(self, x=1, y=0):
        self.__x = x
        self.y = x

    def getX(self):
        return self.__x
    pass

p = Teste(5, 10)
print(p.getX())
