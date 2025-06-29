class Dog:
    def __init__(self, name: str) -> None:
        self.name = name

    def bark(self) -> None:
        print(f"{self.name} is barking!")

    def eat(self) -> None:
        print(f"{self.name} is eating.")


my_dog = Dog("Spike")
my_dog.bark()
my_dog.eat()