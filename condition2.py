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

# Check voting eligibility
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
    print(c, "is the largest")