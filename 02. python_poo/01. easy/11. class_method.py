class GeometricShape:
    @classmethod
    def create_square(cls, side):
        return Square(side)

class Square:
    def __init__(self, side) -> None:
        self.side = side

    def area(self) -> float:
        return self.side * self.side

my_square = GeometricShape.create_square(5)
print(my_square.area())