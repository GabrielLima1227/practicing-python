class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name: str, age: int, enrollment: str) -> None:
        super().__init__(name, age)
        self.enrollment = enrollment

    def __str__(self) -> str:
        return f"Name: {self.name}, Age:{self.age}, Enroll: {self.enrollment}"

new_student = Student("Gabriel", 20, "2023001")
print(new_student)