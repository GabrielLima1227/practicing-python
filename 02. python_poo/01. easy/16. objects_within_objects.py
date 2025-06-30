class Adress:
    def __init__(self, number, street, city) -> None:
        self.number = number
        self.street = street
        self.city = city

    def __str__(self) -> str:
        return f"Number: {self.number}, Street: {self.street}, City: {self.city}"

class Person:
    def __init__(self, name, age, adress: Adress) -> None:
        self.name = name
        self.age = age  
        self.address = adress

    def __str__(self) -> None:
        return f"Hello, i'm {self.name}, i'm {self.age} years old and my adress is {self.address}"

my_person01 = Person("Gabriel", 20, Adress(419, "Av.Chagas Rodrigues", "FS"))
print(my_person01)