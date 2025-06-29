class Point:
    def __init__(self, x_value: int, y_value: int) -> None:
        self.x_value = x_value
        self.y_value = y_value

    def __eq__(self, other: object) -> bool:
        if self.x_value == other.x_value and self.y_value == other.y_value:
            return True
        return False

my_point01 = Point(10, 20)
my_point02 = Point(10,20)
my_point03 = Point(15,30)

print(my_point01 == my_point02)
print(my_point02 == my_point03)
print(my_point01 == my_point03)