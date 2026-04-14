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