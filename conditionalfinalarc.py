"""# Input marks for 5 subjects
m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))

avg = (m1 + m2 + m3 + m4 + m5) / 5

print("Average Marks:", avg)

if avg >= 90:
    print("Grade: A+ (Outstanding)")
elif avg >= 75:
    print("Grade: A (Excellent)")
elif avg >= 60:
    print("Grade: B (Good)")
elif avg >= 40:
    print("Grade: C (Pass)")
else:
    print("Grade: F (Fail)")"""

"""a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /, %): ")

if op == '+':
    print("Result =", a + b)
elif op == '-':
    print("Result =", a - b)
elif op == '*':
    print("Result =", a * b)
elif op == '/':
    if b != 0:
        print("Result =", a / b)
    else:
        print("Error: Division by zero not allowed")
elif op == '%':
    if b != 0:
        print("Result =", a % b)
    else:
        print("Error: Division by zero not allowed")
else:
    print("Invalid Operator")"""

age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen? (yes/no): ").lower()
has_license = input("Do you have a valid driving license? (yes/no): ").lower()

if age >= 18:
    if citizen == "yes":
        if has_license == "yes":
            print("✅ You are eligible to drive in India.")
        else:
            print("❌ You need a valid driving license to drive.")
    else:
        print("❌ Only Indian citizens are eligible for this check.")
else:
    print("❌ You are underage and cannot drive.")
