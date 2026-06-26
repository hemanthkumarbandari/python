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

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog bark")

d = Dog()
d.sound()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Usage
s = Student("Hemz", 20)
s.display()

class Car:
    def __init__(self):
        print("Car object created")


# Usage
c1 = Car()
c2 = Car()

class Calculator:
    def multiply(self, a, b):
        return a * b


# Usage
calc = Calculator()
print("Result:", calc.multiply(3, 4))

# Class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Object creation
s1 = Student("Hemz", 20)

# Calling method
s1.display()

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print(f"Balance: {self.balance}")


acc = BankAccount("Hemz", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.display_balance()

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_grade(self):
        if self.marks >= 90:
            grade = "A"
        elif self.marks >= 75:
            grade = "B"
        elif self.marks >= 50:
            grade = "C"
        else:
            grade = "Fail"

        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", grade)

# Object Creation
s1 = Student("Hemz", 85)
s1.show_grade()

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)

# Object Creation
acc = BankAccount("Hemz", 5000)

acc.deposit(1000)
acc.withdraw(2000)
acc.display()

class Book:
    def __init__(self, title):
        self.title = title
        self.is_issued = False

    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            print(f"{self.title} has been issued.")
        else:
            print(f"{self.title} is already issued.")

    def return_book(self):
        if self.is_issued:
            self.is_issued = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is already available.")

# Object Creation
book1 = Book("Python Basics")

book1.issue_book()
book1.return_book()

class Mobile:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        print("Battery Charged")

    def use(self, percent):
        if self.battery >= percent:
            self.battery -= percent
            print("Phone Used")
        else:
            print("Low Battery")

    def display(self):
        print("Brand:", self.brand)
        print("Battery:", self.battery, "%")

# Object Creation
m1 = Mobile("Samsung", 50)

m1.charge(30)
m1.use(20)
m1.display()

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough money!")

    def show(self):
        print(self.name, "has", self.balance, "rupees")

# Example
acc = BankAccount("Hemanth", 100)   # Start with 100
acc.deposit(50)                     # Add 50 → total 150
acc.withdraw(30)                    # Take 30 → total 120
acc.show()                          # Show balance

class Car:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Car Brand:", self.brand)

# Object Creation
c1 = Car("Toyota")
c1.display()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

# Object Creation
e1 = Employee("Rahul", 30000)
e1.display()