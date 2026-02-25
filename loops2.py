n = 10

for i in range(1, n + 1):
    print(i, end=" ")

n = 10

for i in range(2, n + 1, 2):
    print(i, end=" ")

n = 5
total = 0

for i in range(1, n + 1):
    total += i
print(total)

n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)

num = 1234
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print(rev)

n = 7
is_prime = True

for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break

if is_prime and n > 1:
    print("Prime")
else:
    print("Not Prime")

n = 6
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

n = 6
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

num = 12345
count = 0

while num > 0:
    count += 1
    num //= 10

print(count)
