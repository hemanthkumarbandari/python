from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def stop(self):
        pass


class C1(Car):
    def stop(self):
        print("Car stopped")


ob1 = C1()
ob1.stop()

from abc import ABC, abstractmethod


# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass   # no implementation here


# Child Class
class Car(Vehicle):

    def start(self):
        print("Car starts with key")

    def stop(self):
        print("Car stopped")


# Object Creation
car = Car()

# Method Calls
car.start()
car.stop()

from abc import ABC, abstractmethod
import math

# Abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Circle Class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


# Rectangle Class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Usage
c = Circle(5)
r = Rectangle(4, 3)

print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())

from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Credit Card Payment
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


# UPI Payment
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


# Net Banking Payment
class NetBankingPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Net Banking")


# Usage
p1 = CreditCardPayment()
p2 = UPIPayment()
p3 = NetBankingPayment()

p1.pay(1000)
p2.pay(500)
p3.pay(2000)

#all methods

from abc import ABC, abstractmethod


# Abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def show(self):
        pass


# Child Class
class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def show(self):
        print("This is a Square")


# Usage
s = Square(4)

print("Area:", s.area())
s.show()

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#plmsss

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

d = Dog()
d.sound()

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Area =", self.l * self.b)

r = Rectangle(5, 4)
r.area()
