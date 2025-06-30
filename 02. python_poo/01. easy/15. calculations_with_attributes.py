class Rectangle:
    def __init__(self, height: float, width: float) -> None:
        self.height = height
        self.width = width

    def area(self) -> float:
        return self.height * self.width

    def perimeter(self) -> float:
        return (self.height + self.width) * 2

my_rectangle = Rectangle(10, 15)
print(my_rectangle.area())
print(my_rectangle.perimeter())