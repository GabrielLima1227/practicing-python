class Person:
    name = ""
    def introduce(self) -> None:
        print(f"Hello, i'm {self.name}")

my_person01 = Person()
my_person01.name = "Gabriel"
my_person01.introduce()

my_person02 = Person()
my_person02.name = "Maria"
my_person02.introduce()