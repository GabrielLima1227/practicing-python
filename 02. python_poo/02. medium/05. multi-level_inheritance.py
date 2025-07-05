class Vehicle:
    def move(self) -> str:
        return "The vehicle is moving."

class Car(Vehicle):
    def drive(self) -> str:
        return "The car is driving."

class ElectricCar(Car):
    def charge_battery(self) -> str:
        return "The electric car's battery is charging."

my_electric_car = ElectricCar()

print(my_electric_car.charge_battery())
print(my_electric_car.drive())
print(my_electric_car.move())