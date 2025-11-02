"""# Check if a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
    """
"""# Check if a number is positive, negative, or zero
n = int(input("Enter a number: "))

if n > 0:
    print("Positive number")
elif n < 0:
    print("Negative number")
else:
    print("Number is Zero") """

"""# Check voting eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

if a >= b and a >= c:
    print(a, "is the largest")
elif b >= a and b >= c:
    print(b, "is the largest")
else:
    print(c, "is the largest")"""

"""    # Find the largest number among three
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)"""

# Calculate electricity bill based on units
units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = (100 * 1) + (units - 100) * 2
else:
    bill = (100 * 1) + (100 * 2) + (units - 200) * 3

print("Total Electricity Bill: ₹", bill)