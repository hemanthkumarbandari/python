"""
# Reverse a Number
# "Write a program to reverse a given integer using loops."

n = 1234
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print(rev)

# Palindrome Number
# "Check whether a number is a palindrome using a loop."

n = 121
temp = n
rev = 0

while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10

print("Palindrome" if temp == rev else "Not Palindrome")

# Count Digits
# "Count the number of digits in a given integer."

n = 12345
count = 0

while n > 0:
    count += 1
    n //= 10

print(count)

# Fibonacci Series
# "Print the first N Fibonacci numbers using a loop."

n = 6
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Prime Number Check
# "Check if a number is prime using a loop."

n = 29
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

print("Prime" if is_prime else "Not Prime")

# Multiplication Table
# "Print multiplication table of a given number up to 10."

n = 5

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

# Factorial Calculation
# "Calculate factorial of a number using a loop."

n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)

# Armstrong Number
# "Check whether a number is an Armstrong number."

n = 153
temp = n
power = len(str(n))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

print("Armstrong" if total == n else "Not Armstrong")

# Star Pattern - Right Triangle
# "Print a right triangle star pattern using loops."

n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Largest Digit in a Number
# "Find the largest digit present in a given number using loops."

n = 73952
max_digit = 0

while n > 0:
    digit = n % 10
    if digit > max_digit:
        max_digit = digit
    n //= 10

print(max_digit)

# Reverse a String
# "Reverse a given string using a loop without slicing."

s = "hello"
rev = ""

for ch in s:
    rev = ch + rev

print(rev)

# Sum of Even and Odd Numbers
# "Find the sum of even and odd numbers from 1 to N using loops."

n = 10
even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Even Sum:", even_sum)
print("Odd Sum:", odd_sum)

# Factors of a Number
# "Print all factors of a given number using a loop."

n = 12

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")

# Count Vowels
# "Count the number of vowels in a string using loops."

s = "programming"
count = 0

for ch in s:
    if ch.lower() in "aeiou":
        count += 1

print(count)

# Count Vowels
# "Count the number of vowels in a string using loops."

s = "programming"
count = 0

for ch in s:
    if ch.lower() in "aeiou":
        count += 1

print(count)

# Reverse a String
# "Reverse a given string using a loop without slicing."

s = "hello"
rev = ""

for ch in s:
    rev = ch + rev

print(rev)
"""

# practice
# practice

n = int(input("enter no."))
for i in range (1, n+1):
    print(i)

n = int(input("Enter No."))

total = 0

for i in range(1, n+1):
    total = n + i

    print("sum= ", total)


num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Reverse a Number

num = int(input("Enter number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed Number =", reverse)

# Count Digits in a Number

num = int(input("Enter number: "))

count = 0

while num > 0:
    count += 1
    num = num // 10

print("Total Digits =", count)

# Palindrome Number Check

num = int(input("Enter number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# Fibonacci Series

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    
    c = a + b
    a = b
    b = c
    
# Star Pyramid Pattern

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    
    print()