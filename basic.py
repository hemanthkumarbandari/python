print ("hey world")
print("Python")
print ("Hi")
num = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0:
    print("The number is a multiple of both 2 and 3")
elif num % 2 == 0:
    print("The number is a multiple of 2")
elif num % 3 == 0:
    print("The number is a multiple of 3")
else:
    print("The number is not a multiple of 2 or 3")
balance = 10000
amount = int(input("Enter withdrawal amount: "))

if amount > balance:
    print("Insufficient balance")
elif amount % 100 != 0:
    print("Enter amount in multiples of 100")
else:
    balance -= amount
    print("Withdraw successful")
    print("Remaining Balance:", balance)
amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0

final_price = amount - discount

print("Discount:", discount)
print("Final Price:", final_price)
temp = float(input("Enter Temperature: "))

if temp > 30:
    print("Hot")
elif temp >= 20:
    print("Warm")
else:
    print("Cold")
year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if a >= b and a >= c:
    print(a, "is largest")
elif b >= a and b >= c:
    print(b, "is largest")
else:
    print(c, "is largest")