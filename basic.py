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