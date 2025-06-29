class Animal:
    def __init__(self, name: str, species: str = "Unknow") -> None:
        self.name = name
        self.species = species

    def __str__(self) -> str:
        return f"Name: {self.name}, Species: {self.species}"

my_animal01 = Animal("Marujo", "Cat")
my_animal02 = Animal("Spike")

print(my_animal01)
print(my_animal02)