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