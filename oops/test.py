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

class Student:
    def __init__(self, marks):
        self.marks = marks

    def grade(self):
        if self.marks > 50:
            print("Pass")
        else:
            print("Fail")

s = Student(40)
s.grade()

class ATM:
    def __init__(self):
        self.__bal = 0

    def deposit(self, a):
        self.__bal += a

    def withdraw(self, a):
        self.__bal -= a

    def check(self):
        print(self.__bal)

a = ATM()
a.deposit(1000)
a.withdraw(200)
a.check()

class Employee:
    def work(self):
        print("Work")

class Developer(Employee):
    def work(self):
        print("Code")

class Manager(Employee):
    def work(self):
        print("Manage")

Developer().work()
Manager().work()

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Circle area")

class Rectangle(Shape):
    def area(self):
        print("Rectangle area")

Circle().area()
Rectangle().area()

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(self.name, self.price)

Product("Pen",10).display()
Product("Book",50).display()
Product("Bag",500).display()

#2
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(self.name, self.age, self.marks)

s1 = Student("Ram", 20, 85)
s2 = Student("Sam", 21, 90)
s3 = Student("Tom", 19, 78)

s1.display()
s2.display()
s3.display()

class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def show_details(self):
        print(self.name, self.department, self.salary)

e1 = Employee("John", "IT", 50000)
e2 = Employee("Sara", "HR", 45000)

e1.show_details()
e2.show_details()

class BankAccount:
    def __init__(self, b):
        self.__b = b

    def deposit(self, a):
        self.__b += a

    def withdraw(self, a):
        if a <= self.__b:
            self.__b -= a

    def check_balance(self):
        print(self.__b)

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
acc.check_balance()