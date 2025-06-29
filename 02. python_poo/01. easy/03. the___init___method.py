class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  

    def introduce(self):
        print(f"Hello, i'm {self.name} and i'm {self.age} years old.")

my_person01 = Person("Gabriel", 20)
my_person01.introduce()

my_person02 = Person("Alícia", 20)
my_person02.introduce()