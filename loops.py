"""for i in range(1, 11):
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)"""

"""sum = 0
for i in range(1, 11):
    sum += i
print("Sum =", sum)"""

"""
word = input("Enter word: ")
for ch in word:
    print(ch)
str1 = ("red")
str2 = ("orange")
print str1+str2
"""

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum:", sum)

n = 12345
count = 0

while n > 0:
    count += 1
    n //= 10

print("Digits =", count)

n = 1234
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print("Reversed =", rev)

text = "hemz is learning python"
vowels = "aeiou"

for ch in text:
    if ch in vowels:
        print(ch)

n = 6
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b