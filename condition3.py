"""# Check type of triangle
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
    print("Not a valid triangle")"""

"""# Calculate grade based on marks
marks = int(input("Enter marks (0-100): "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")"""

"""# Simple calculator using conditionals
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /, %): ")

if op == '+':
    print("Result =", a + b)
elif op == '-':
    print("Result =", a - b)
elif op == '*':
    print("Result =", a * b)
elif op == '/':
    print("Result =", a / b)
elif op == '%':
    print("Result =", a % b)
else:
    print("Invalid operator")"""

"""# Calculate electricity bill
units = int(input("Enter total units used: "))

if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = 100 * 1 + (units - 100) * 2
elif units <= 300:
    bill = 100 * 1 + 100 * 2 + (units - 200) * 3
else:
    bill = 100 * 1 + 100 * 2 + 100 * 3 + (units - 300) * 5

print("Total bill = ₹", bill)"""

# Print day name based on number
num = int(input("Enter a number (1-7): "))

if num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
elif num == 7:
    print("Sunday")
else:
    print("Invalid number")
