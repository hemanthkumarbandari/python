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