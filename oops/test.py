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