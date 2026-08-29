"""
x = 5
y = 25
print(x, "suare is", end=" - ")
print(y)

a = 5
b = 10

print(a)
print(end='\n')
print()
print(b)

name = input("Name-")
age = int(input("Age-"))
Salary = float(input("Amount-"))
IsLead = bool(input())
print (name)
print (age)
print (Salary)
print(IsLead)
print(type(name))
print(type(age))
print(type(Salary))
print(type(IsLead))

num = input().split()
print(num)
print(type(num))

a,b,c = map(int,input().split())
print(a)
lst = list(map(int,input().split()))
print(lst) 

"""
"""

name = "Hemanth"
age = 21
gender = "Male"
weight = 60.17
isTeacher = True

#set - unique values
fruitsILiked = {"apple", "banana", "orange"}

# List - ordered values
earningFrom2022 = [22, 23, 22, 25, 23, 56]

# Fixed, repeat
# Tuple - fixed values
earningBefore2022 = (22, 23, 24, 22, 29, 30)

# Key value
# Dictionary - key-value pairs
prop = {
    "orange": 5,
    "onion": "7kg",
    "mango": "1kg"
}

# None
overHyped = None

print(name, type(name))
print(age, type(age))
print(gender, type(gender))
print(weight, type(weight))
print(isTeacher, type(isTeacher))
print(fruitsILiked, type(fruitsILiked))
print(earningFrom2022, type(earningFrom2022))
print(earningBefore2022, type(earningBefore2022))
print(prop, type(prop))
print(overHyped, type(overHyped))

# String
name = "Hemanth"

# Integer
age = 21

# Float
salary = 45000.50

# Boolean
isStudent = True

# List
skills = ["Python", "Java", "SQL"]

# Tuple
coordinates = (17.3850, 78.4867)

# Set
numbers = {10, 20, 30, 40}

# Dictionary
student = {
    "name": "Hemanth",
    "age": 21,
    "course": "CSE"
}

# None
result = None

# Print values and their data types
print(name, type(name))
print(age, type(age))
print(salary, type(salary))
print(isStudent, type(isStudent))
print(skills, type(skills))
print(coordinates, type(coordinates))
print(numbers, type(numbers))
print(student, type(student))
print(result, type(result))

# Python Data Types Practice

product_name = "Laptop"          # String
price = 54999                    # Integer
discount = 12.5                  # Float
in_stock = True                  # Boolean

colors = ["Black", "Silver", "White"]       # List
dimensions = (15.6, 10.2, 0.7)              # Tuple
available_sizes = {"S", "M", "L", "XL"}     # Set

product = {
    "name": product_name,
    "price": price,
    "discount": discount,
    "in_stock": in_stock
}                                          # Dictionary

warranty = None                            # NoneType

print(product_name, type(product_name))
print(price, type(price))
print(discount, type(discount))
print(in_stock, type(in_stock))
print(colors, type(colors))
print(dimensions, type(dimensions))
print(available_sizes, type(available_sizes))
print(product, type(product))
print(warranty, type(warranty)) 

# String
name = input("Enter your name: ")

# Integer
age = int(input("Enter your age: "))

# Float
salary = float(input("Enter your salary: "))

# Boolean
isWorking = input("Are you working? (yes/no): ") == "yes"

# List
subjects = ["Python", "Java", "SQL"]

# Tuple
marks = (85, 90, 78)

# Set
languages = {"Python", "Java", "Python"}

# Dictionary
person = {
    "name": name,
    "age": age,
    "salary": salary
}

# None
extra = None

print("\n--- Details ---")
print("Name:", name)
print("Age:", age)
print("Salary:", salary)
print("Working:", isWorking)
print("Subjects:", subjects)
print("Marks:", marks)
print("Languages:", languages)
print("Person:", person)
print("Extra:", extra)

print("\n--- Data Types ---")
print(type(name))
print(type(age))
print(type(salary))
print(type(isWorking))
print(type(subjects))
print(type(marks))
print(type(languages))
print(type(person))
print(type(extra))

"""
# Student Result Program

name = "Hemanth"
marks = [85, 72, 90, 68, 88]

total = sum(marks)
average = total / len(marks)

passed = average >= 40

student = {
    "name": name,
    "total": total,
    "average": average,
    "passed": passed
}

print("Student:", student["name"])
print("Total:", student["total"])
print("Average:", student["average"])
print("Passed:", student["passed"])

print("\nData Types:")
print(type(name))
print(type(marks))
print(type(total))
print(type(average))
print(type(passed))
print(type(student))