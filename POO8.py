class Forma:

    def __init__(self):
        return 'Construtor da forma.'

    def area(self):
        return 'Área da forma: '

    def perimetro(self):
        print('Perimetro da forma: ')
    pass

class Quadrado(Forma):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return f'{Forma.area(self)}{self.lado ** 2}'

q = Quadrado(2)
print(q.area())
