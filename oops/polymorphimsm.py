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