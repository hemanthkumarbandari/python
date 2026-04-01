class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

s1 = Student("Hemz")
s1.show()

# parent
class Employee:
    def show_employee(self):
        print("I am an Employee")
#child
class Developer(Employee):
    def show_developer(self):
        print("I am a Developer")
#obj
dev = Developer()
#obj from child
dev.show_developer()
#obj from parent
dev.show_employee()

#inheritence

class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()

class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

c = Car()
c.start()
c.drive()