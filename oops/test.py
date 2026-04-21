def set_age(self, age):
    if age > 0:
        self.__age = age

def deposit(self, amount):
    if amount > 0:
        self.__balance += amount

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)

s1 = Student("Ravi", 80)
s2 = Student("Ram", 60)

s1.display()
s2.display()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(self.name, self.salary)

e1 = Employee("John", 50000)
e1.show_details()

class Bank:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        self.__balance -= amt

    def show_balance(self):
        print(self.__balance)

b = Bank()
b.deposit(1000)
b.withdraw(200)
b.show_balance()

class Vehicle:
    def start(self):
        print("Start")

class Car(Vehicle):
    def drive(self):
        print("Drive")

c = Car()
c.start()
c.drive()

class Animal:
    def sound(self):
        print("Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

Dog().sound()
Cat().sound()