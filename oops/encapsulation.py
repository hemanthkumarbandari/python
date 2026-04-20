class Student:
    def __init__(self):
        self.__name = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


class Employee:
    def __init__(self):
        self.__salary = 0

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

    def get_salary(self):
        return self.__salary


class Rectangle:
    def __init__(self):
        self.__length = 0
        self.__width = 0

    def set_dimensions(self, l, w):
        self.__length = l
        self.__width = w

    def get_area(self):
        return self.__length * self.__width


class Car:
    def __init__(self):
        self.__brand = ""
        self.__speed = 0

    def set_brand(self, brand):
        self.__brand = brand

    def accelerate(self, value):
        self.__speed += value

    def get_speed(self):
        return self.__speed


class Book:
    def __init__(self):
        self.__title = ""
        self.__author = ""

    def set_details(self, t, a):
        self.__title = t
        self.__author = a

    def get_details(self):
        return self.__title + " by " + self.__author


class Circle:
    def __init__(self):
        self.__radius = 0

    def set_radius(self, r):
        self.__radius = r

    def get_area(self):
        return 3.14 * self.__radius * self.__radius


class Laptop:
    def __init__(self):
        self.__price = 0

    def set_price(self, price):
        if price > 0:
            self.__price = price

    def get_price(self):
        return self.__price


class Person:
    def __init__(self):
        self.__name = ""
        self.__city = ""

    def set_info(self, name, city):
        self.__name = name
        self.__city = city

    def get_info(self):
        return self.__name + " from " + self.__city


class Account:
    def __init__(self):
        self.__password = ""

    def set_password(self, password):
        self.__password = password

    def check_password(self, input):
        return self.__password == input


s = Student()
s.set_name("Hemz")
s.set_age(20)

b = BankAccount()
b.deposit(1000)
b.withdraw(200)

e = Employee()
e.set_salary(50000)

r = Rectangle()
r.set_dimensions(5, 4)

c = Car()
c.set_brand("Tesla")
c.accelerate(60)

bk = Book()
bk.set_details("Python", "Guido")

ci = Circle()
ci.set_radius(7)

l = Laptop()
l.set_price(80000)

p = Person()
p.set_info("Hemz", "Vizag")

a = Account()
a.set_password("1234")

print(s.get_name(), s.get_age())
print(b.get_balance())
print(e.get_salary())
print(r.get_area())
print(c.get_speed())
print(bk.get_details())
print(ci.get_area())
print(l.get_price())
print(p.get_info())
print(a.check_password("1234"))