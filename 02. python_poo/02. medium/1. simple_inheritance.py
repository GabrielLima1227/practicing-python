class Animal:
    def make_sound(self):
        print("Some generic animal sound.")

class Dog(Animal):
    def make_sound(self):
        print("Woof woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")


generic_animal = Animal()
dog = Dog()
cat = Cat()

generic_animal.make_sound()  
dog.make_sound()             
cat.make_sound()             