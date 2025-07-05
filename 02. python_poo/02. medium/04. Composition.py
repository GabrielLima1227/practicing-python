class Engine:
    def __init__(self) -> None:
        self._is_on = False 

    @property
    def is_on(self) -> bool:
        return self._is_on

    def turn_on(self) -> None:
        if not self._is_on: 
            self._is_on = True
            print("The engine is working (ON).")
        else:
            print("The engine is already ON.")

    def turn_off(self) -> None:
        if self._is_on:
            self._is_on = False
            print("The engine is not working (OFF).")
        else:
            print("The engine is already OFF.")

class Vehicle:
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model
        self.engine = Engine()

    def turn_on_vehicle(self) -> None:
        """Liga o veículo, chamando o método turn_on do seu motor."""
        print(f"\nAttempting to turn on the {self.brand} {self.model}...")
        self.engine.turn_on()

    def turn_off_vehicle(self) -> None:
        """Desliga o veículo, chamando o método turn_off do seu motor."""
        print(f"\nAttempting to turn off the {self.brand} {self.model}...")
        self.engine.turn_off()

    def get_status(self) -> str:
        status = "ON" if self.engine.is_on else "OFF"
        return f"The {self.brand} {self.model} is currently {status}."

my_car = Vehicle("Toyota", "Corolla")
print(my_car.get_status())

my_car.turn_on_vehicle()
print(my_car.get_status())

my_car.turn_on_vehicle()

my_car.turn_off_vehicle()
print(my_car.get_status())

my_car.turn_off_vehicle()

my_motorcycle = Vehicle("Honda", "CBR500R")
print(my_motorcycle.get_status())
my_motorcycle.turn_on_vehicle()
print(my_motorcycle.get_status())