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

name = "Hemanth"
age = 21
gender = "Male"
weight = 60.17
isTeacher = True
fruitsILiked = {"apple", "banana", "orange"}

# List
earningFrom2022 = [22, 23, 22, 25, 23, 56]

# Fixed, repeat
# Tuple
earningBefore2022 = (22, 23, 24, 22, 29, 30)

# Key value
# Dictionary
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