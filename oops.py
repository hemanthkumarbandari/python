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

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def display(self):
        print("Name:", self.name)

s = Student("Hemz")
s.display()

class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

p = Penguin()
p.fly()

class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self, name, lang):
        super().__init__(name)
        self.lang = lang

    def show(self):
        print(self.name, "codes in", self.lang)

d = Developer("Hemz", "Python")
d.show()

class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(B):
    def showC(self):
        print("Class C")

obj = C()
obj.showA()
obj.showB()
obj.showC()