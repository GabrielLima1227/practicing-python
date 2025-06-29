class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year

    def specs(self) -> None:
        print(f"The model is {self.model}, the make is {self.make} and the year is {self.year}")

    def accelerate(self) -> None:
        print(f"The {self.model} is accelerating!")

my_car = Car("Toyota", "Corolla", "2018")
my_car.specs()
my_car.accelerate()