def add(a, b, c=0):
    return a + b + c

print(add(2, 3))      # 5
print(add(2, 3, 4))   # 9

print(5 + 3)        # 8 (addition)
print("Hello " + "World")  # Hello World (string concat)

class Bird:
    def fly(self):
        print("Bird flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

def start(obj):
    obj.fly()

start(Bird())
start(Airplane())

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

Dog().sound()
Cat().sound()

class Math:
    def add(self, a, b, c=0):
        print(a + b + c)

m = Math()
m.add(2, 3)      # 5
m.add(2, 3, 4)   # 9

print(len("Hello"))     # 5
print(len([1, 2, 3]))  # 3

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number   # private variable
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount!")

    def get_balance(self):
        return self.__balance


# Usage
acc = BankAccount("12345", 1000)
acc.deposit(500)
acc.withdraw(300)
print("Balance:", acc.get_balance())

class Vehicle:
    def start(self):
        print("Vehicle is starting...")


class Car(Vehicle):
    def start(self):
        print("Car starts with key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with kick or button")


# Usage
v1 = Car()
v2 = Bike()

v1.start()
v2.start()

class Calculator:

    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        return a + b


# Usage
calc = Calculator()

print(calc.add(2, 3))        # 2 arguments
print(calc.add(2, 3, 4))     # 3 arguments
print(calc.add(2.5, 3.5))    # float

class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()   # composition

    def start_car(self):
        print("Starting car...")
        self.engine.start()


# Usage
car = Car()
car.start_car()

class Student:
    school_name = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    @staticmethod
    def info():
        print("Students are part of a school")

    def display(self):
        print(self.name, "-", Student.school_name)


# Usage
s1 = Student("Hemz")
s2 = Student("Rahul")

s1.display()
s2.display()

Student.change_school("XYZ School")

s1.display()
s2.display()

Student.info()