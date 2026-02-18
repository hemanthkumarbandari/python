def can_enter_club():
    age = int(input("Enter your age: "))
    if age >= 21:
        print(True)
    else:
        print(False)

for i in range(1, 6):
    print(i, "-", i * i)

x = 20
y = 6

result = x // y
print(result)

sentence = "Coding on CodeChef"

words = sentence.split()

for word in words:
    print(word, "-", len(word))

print(sentence, "-", len(sentence))

num = int(input())
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

x = int(input())
y = int(input())
z = int(input())

if x > y > z:
    print("Increasing")
elif x < y < z:
    print("Decreasing")
else:
    print("Neither")

student_grades = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 68
}

name = input()

if name in student_grades:
    print(student_grades[name])
else:
    print("Not Found")

nums = list(map(int, input().split()))
print(nums[0] * nums[2])

def isEven(num):
    return num % 2 == 0

t = int(input())

for _ in range(t):
    num = int(input())
    if isEven(num):
        print("Even")
    else:
        print("Odd")

def calculatePower(base, exponent):
    return base ** exponent

base, exponent = map(int, input().split())
print(calculatePower(base, exponent))




