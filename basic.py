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