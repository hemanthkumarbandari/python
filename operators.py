sum1 = 100 + 50
sum2 = sum1 + 250
sum3 = sum2 + sum2

print(sum1)
print(sum2)
print(sum3)

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

x = 12
y = 5

print(x / y)

x = 10
print("x =", x)

x += 5
print("x += 5 →", x)

x -= 3
print("x -= 3 →", x)

x *= 2
print("x *= 2 →", x)

x /= 4
print("x /= 4 →", x)

x //= 2
print("x //= 2 →", x)

x %= 2
print("x %= 2 →", x)

x **= 3
print("x **= 3 →", x)

x = 10
x &= 5
print("x &= 5 →", x)

x = 10
x |= 5
print("x |= 5 →", x)

x = 10
x ^= 5
print("x ^= 5 →", x)

x = 10
x >>= 2
print("x >>= 2 →", x)

x = 10
x <<= 2
print("x <<= 2 →", x)


x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = 10
y = 4

print("x =", x, "→", bin(x))
print("y =", y, "→", bin(y))

print("x & y =", x & y)
print("x | y =", x | y)
print("x ^ y =", x ^ y)
print("~x =", ~x)
print("x << 2 =", x << 2)
print("x >> 2 =", x >> 2)

x = 10 + 2 * 3
y = (10 + 2) * 3
z = 2 ** 3 ** 2
a = not (10 > 5 and 3 < 4)
b = 10 | 2 & 8

print("x =", x)
print("y =", y)
print("z =", z)
print("a =", a)
print("b =", b)
