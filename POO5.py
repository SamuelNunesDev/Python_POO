class Square:

    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return self.side * 4

    def area(self):
        return self.side ** 2
    pass


class Rectangle:

    def __init__(self, width, height):
        self.width, self.height = width, height

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def area(self):
        return self.width * self.height

q = Square(5)
print(q.perimeter())
print(q.area())
r = Rectangle(5, 10)
print(r.perimeter(), r.area())
