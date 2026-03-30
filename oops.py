class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

s1 = Student("Hemz")
s1.show()