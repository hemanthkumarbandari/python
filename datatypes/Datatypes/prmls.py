age = 20
print(type(age))

height = 5.9
print(type(height))

name = "hemz"
print(type(name))

male = True
print(type(male))

dreams = ["bike", "car", "house"]
print(type(dreams))

nums = (10, 20, 30)
print(type(nums))

student = {
    "Name" : "hemz",
    "Roll" : 10
}

print(student)
print(type(student))

### counting datatypes
data = [10, "hemz", 6.1, "shahi", 21]

ints = 0
strings = 0
floats = 0

for item in data:
    if type(item) == int:
        ints += 1 #ints = ints + 1
    if type(item) == str:
        strings += 1
    if type(item) == float:
        floats += 1

print("int count;", ints)
print("string count;", strings)
print("flaot count;", floats)

age = 20
print(type(age))

height = 5.9
print(type(height))

name = "hemz"
print(type(name))

male = True
print(type(male))

dreams = ["bike", "car", "house"]
print(type(dreams))

nums = (10, 20, 30)
print(type(nums))

student = {
    "Name" : "hemz",
    "Roll" : 10
}

print(student)
print(type(student))

### counting datatypes
data = [10, "hemz", 6.1, "shahi", 21]

ints = 0
strings = 0
floats = 0

for item in data:
    if type(item) == int:
        ints += 1 #ints = ints + 1
    if type(item) == str:
        strings += 1
    if type(item) == float:
        floats += 1

print("int count;", ints)
print("string count;", strings)
print("flaot count;", floats)

a = 10
b = 5.5

result = a + b

print(result)
print(type(result))