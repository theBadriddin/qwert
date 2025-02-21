
from abc import ABC, abstractmethod
from uuid import uuid4 as id



class School:
    def __init__(self , name , number):
        self.name = name 
        self.number = number
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def show_all_people(self):
        return [p.get_info() for p in self.people]


class Classroom(School):
    def __init__(self , number , subject ):
       super().__init__(number)
       self.subject = subject
       self.student = []

    def add_student(self, student):
       self.student.append(student)

    def class_info(self):
        return f"Room_number: {self.number}, Subject is: {self.subject} room, Students: {[s.name for s in self.student]}"

################# Maktab va sinf xona klasslari tayyor

class Person(ABC):
    def __init__(self , name , sourname , age, id):
        self.name = name
        self.sourname = sourname
        self.age = age
        self._id = id()


    @abstractmethod
    def get_role(self):
       pass


    def get_info(self):
        return f"Name: {self.name}, Sourname: {self.sourname}, Age: {self.age}, Role: {self.get_role()}"

class Student(Person):
    def __init__(self, name, sourname, age, grade):
        super().__init__(name,sourname,age)
        self.grade = grade

    def study(self):
        return f"{self.name} is studying."

    def get_role(self):
        return "Student"



class Teacher(Person):
    def __init__(self, name, sourname,  age, subject):
        super().__init__(name, sourname, age)
        self.subject = subject

    def teach(self):
        return f"{self.name} is teaching {self.subject}."

    def get_role(self):
        return "Teacher"



class Direktor(Person):
    def __init__(self, name , sourname, age , years_worked):
        super().__init__(name , sourname , age)
        self.years_worked = years_worked

    def manages(self):
        return f"{self.name} is managing the school"

    def get_role(self):
        return "Direktor(Manager)"

class Cafeteria:
    def __init__(self, name, chef, capacity):
        self.name = name
        self.chef = chef
        self.capacity = capacity
        self.menu = []

    def add_food(self, food):
        self.menu.append(food)
        return f"{food} has been added to the menu."

    def show_menu(self):
        return f"Menu in {self.name}: {', '.join(self.menu) if self.menu else 'No food available'}"

    def serve_food(self):
        return f"{self.chef} is serving food to students."

    def get_info(self):
        return f"{self.name} is managed by {self.chef} and can accommodate {self.capacity} people."

school = School("PDP school")
classroom1 = Classroom(27, "English")
student1 = Student("Badriddin",  "Baxtiyorov", 17 , 5)
teacher1 = Teacher("SHaxlo", "Askarova" , 30, "English")
school.add_person(teacher1)
school.add_person(student1)
cafeteria1 = Cafeteria("Sunrise Cafeteria", "Chef Umar", 100)
director1 = Direktor("Asliddin", "Ismoilov", 25)
print(director1.get_info())
print()
print(cafeteria1.get_info())
print(cafeteria1.add_food("Pizza"))
print(cafeteria1.add_food("Soup"))