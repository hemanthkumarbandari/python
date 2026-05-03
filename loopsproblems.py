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