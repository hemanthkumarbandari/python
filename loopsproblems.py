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