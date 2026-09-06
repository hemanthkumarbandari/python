####"""
####x = 5
####y = 25
####print(x, "suare is", end=" - ")
####print(y)
####
####a = 5
####b = 10
####
####print(a)
####print(end='\n')
####print()
####print(b)
####
####name = input("Name-")
####age = int(input("Age-"))
####Salary = float(input("Amount-"))
####IsLead = bool(input())
####print (name)
####print (age)
####print (Salary)
####print(IsLead)
####print(type(name))
####print(type(age))
####print(type(Salary))
####print(type(IsLead))
####
####num = input().split()
####print(num)
####print(type(num))
####
####a,b,c = map(int,input().split())
####print(a)
####lst = list(map(int,input().split()))
####print(lst) 
####
####"""
####"""
####"""
####
#####DataTypes
####
####name = "Hemanth"
####age = 21
####gender = "Male"
####weight = 60.17
####isTeacher = True
####
#####set - unique values
####fruitsILiked = {"apple", "banana", "orange"}
####
##### List - ordered values
####earningFrom2022 = [22, 23, 22, 25, 23, 56]
####
##### Fixed, repeat
##### Tuple - fixed values
####earningBefore2022 = (22, 23, 24, 22, 29, 30)
####
##### Key value
##### Dictionary - key-value pairs
####prop = {
####    "orange": 5,
####    "onion": "7kg",
####    "mango": "1kg"
####}
####
##### None
####overHyped = None
####
####print(name, type(name))
####print(age, type(age))
####print(gender, type(gender))
####print(weight, type(weight))
####print(isTeacher, type(isTeacher))
####print(fruitsILiked, type(fruitsILiked))
####print(earningFrom2022, type(earningFrom2022))
####print(earningBefore2022, type(earningBefore2022))
####print(prop, type(prop))
####print(overHyped, type(overHyped))
####
##### String
####name = "Hemanth"
####
##### Integer
####age = 21
####
##### Float
####salary = 45000.50
####
##### Boolean
####isStudent = True
####
##### List
####skills = ["Python", "Java", "SQL"]
####
##### Tuple
####coordinates = (17.3850, 78.4867)
####
##### Set
####numbers = {10, 20, 30, 40}
####
##### Dictionary
####student = {
####    "name": "Hemanth",
####    "age": 21,
####    "course": "CSE"
####}
####
##### None
####result = None
####
##### Print values and their data types
####print(name, type(name))
####print(age, type(age))
####print(salary, type(salary))
####print(isStudent, type(isStudent))
####print(skills, type(skills))
####print(coordinates, type(coordinates))
####print(numbers, type(numbers))
####print(student, type(student))
####print(result, type(result))
####
##### Python Data Types Practice
####
####product_name = "Laptop"          # String
####price = 54999                    # Integer
####discount = 12.5                  # Float
####in_stock = True                  # Boolean
####
####colors = ["Black", "Silver", "White"]       # List
####dimensions = (15.6, 10.2, 0.7)              # Tuple
####available_sizes = {"S", "M", "L", "XL"}     # Set
####
####product = {
####    "name": product_name,
####    "price": price,
####    "discount": discount,
####    "in_stock": in_stock
####}                                          # Dictionary
####
####warranty = None                            # NoneType
####
####print(product_name, type(product_name))
####print(price, type(price))
####print(discount, type(discount))
####print(in_stock, type(in_stock))
####print(colors, type(colors))
####print(dimensions, type(dimensions))
####print(available_sizes, type(available_sizes))
####print(product, type(product))
####print(warranty, type(warranty)) 
####
#####string
####firstname = "Hemz"
####secondname = "Here"
####name = firstname + " " + secondname
####print(name)
####
#####list
####lst = [1,2,3,4]
####lst.append(5)
####print(lst)
####lst.pop(1)
####print(lst)
####print(lst[3])
####lst.insert(1,2)
####print(lst)
####lst[0]= 7
####print(lst)
####
#####tuple
####num = (1,2,3,4,5)
####print(num[1])
####
##### String
####firstname = "Hemz"
####secondname = "Here"
####
####name = firstname + " " + secondname
####
####print(name)
####
##### List
####lst = [1, 2, 3, 4]   # [] creates list
####
####lst.append(5)       # () calls append
####print(lst)
####
####lst.pop(1)           # () calls pop, 1 is the argument
####print(lst)
####
####print(lst[3])        # [] indexes the list
####
####lst.insert(1, 2)    # () calls insert
####print(lst)
####
####lst[0] = 7          # [] indexes and changes the item
####print(lst)
####
##### Tuple
####num = (1, 2, 3, 4, 5)  # () creates tuple
####
####print(num[1])           # [] indexes the tuple
####
###
####dictionary
###
###dic = {
###    "Name":"Hemz",
###    "Age": 20,
###    "Gender": "Male"
###    }
###
###dic["place"] = "Miyapur"
###del dic["Age"]
###print(dic)
###print(dic["Gender"])
###
###st = set()
###d = {}
###
###st = {1, 2, 3}
###d = {"name":12}
###
###name = ""
###age = 0
###lst = []
###tup = {}
###d = {}
###st = set() 
###
###st = {1, 2, 3, 4, 5}
###st.add(6)
###st.remove(3)
###print(st)
###
####immutable
###x = 5
###print(id(x))
###X= 12
###print(id(x)) #same id if same value, diff id if dif val.
###
###x = 5
###y = 5
###y = 7
###print(id(x))
###print(id(y))
###
###weight = 52.39
###print(id(weight))
###weight = 55.99
###print(id(weight))
###
###a = True
###b = True
###print(id(a))
###print(id(b))
###a = False
###b = False
###print(id(a))
###print(id(b))
###
###name = "Hemant"
###print(name[0])
###
####time and space
###arr = [10, 20, 30, 40, 50] #O(1)
###
###print(arr[2])
###
###arr = [1, 2, 3, 4, 5]
###
###for x in arr:
###    print(x)
##
##a = 4.5
##print(a,type(a))
##
##res = int(a)
##print(res,type(res))
##
##res1 = str(a)
##print(res1,type(res1))
##
##lst = [2,3,4,5]
##print(lst,type(lst))
##
##res2 = tuple(lst)
##print (res2,type(res2))
##
##res3 = set(lst)
##print(res3,type(res3))
##
##colur = ["a", "b", "c"]
##qty = [3,4,5]
#
#name = "Hemanth"
#print(name[0])
#print(name[1])
#print(name[2])
#
#print(name[0:3])
#print(name[0:5:3])
#
#name = "Hemz Here"
#print(name[0:])
#print(name[-1::-1])
#
#lst = [2,3,4,5,12]
#
#print(lst[0])
#print(lst[2])
#print(lst[0:2])
#print(lst[0::2])
#
#print(lst[-1::-1])
#print(lst[-1:0:-1])
##: - start : end before, :: start :: end step
#
#statement = "I will work heard and chase my DREAMS"
#lst = statement.split()
#print(lst)
#print(type(lst))
#
#fruits = ["orange", "mango", "grapes", "water melon"]
#res = " ".join(fruits)
#print(res)

mark = int(input("Enter your mark: "))

if mark >= 90:
    print("A")
elif mark >= 75:
    print("B")
elif mark >= 60:
    print("C")
elif mark >= 33:
    print("D")
else:
    print("FAIL")