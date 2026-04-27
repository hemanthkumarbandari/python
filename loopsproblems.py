# Reverse a Number
# "Write a program to reverse a given integer using loops."

n = 1234
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print(rev)