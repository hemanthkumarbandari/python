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
"""

a,b,c = map(int,input().split())
print(a)
lst = list(map(int,input().split()))
print(lst)