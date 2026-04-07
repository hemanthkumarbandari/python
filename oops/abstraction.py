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