"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a >= b and a <= c) or (a <= b and a >= c):
    print("Second largest is:", a)
elif (b >= a and b <= c) or (b <= a and b >= c):
    print("Second largest is:", b)
else:
    print("Second largest is:", c)"""

"""cost = float(input("Enter Cost Price: "))
sell = float(input("Enter Selling Price: "))

if sell > cost:
    profit = sell - cost
    percent = (profit / cost) * 100
    print("Profit =", profit)
    print("Profit Percentage =", percent, "%")
elif sell < cost:
    loss = cost - sell
    percent = (loss / cost) * 100
    print("Loss =", loss)
    print("Loss Percentage =", percent, "%")
else:
    print("No Profit No Loss")"""
# Check type of triangle
"""
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle")
"""
"""
num = abs(int(input("Enter a number: ")))

if num < 10:
    print("Single-digit")
elif num < 100:
    print("Double-digit")
else:
    print("More than two digits")
ch = input("Enter a character: ")

if 'A' <= ch <= 'Z':
    print("Uppercase letter")
elif 'a' <= ch <= 'z':
    print("Lowercase letter")
elif '0' <= ch <= '9':
    print("Digit")
else:
    print("Special character")
"""
"""
num = int(input("Enter a number: "))

if num % 5 == 0 or num % 7 == 0:
    print("Multiple of 5 or 7")
else:
    print("Not a multiple of 5 or 7")
"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b != 0:
        print(a / b)
    else:
        print("Division by zero not allowed")
else:
    print("Invalid operator")