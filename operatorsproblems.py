# Swap two numbers without using a third variable
a = 10
b = 5
a = a ^ b #bitwise xor
b = a ^ b
a = a ^ b
print("1. Swapped values:", a, b)

# Check if a number is a power of 2
n = 16
if n > 0 and (n & (n - 1)) == 0: #should give n-(n-1) = 0
    print("2.", n, "is a power of 2")
else:
    print("2.", n, "is not a power of 2")

# Find maximum of two numbers using operators
a = 25
b = 50
max_val = (a + b + abs(a - b)) // 2
print("3. Maximum =", max_val)

# Toggle case of a character using bitwise XOR
ch = 'a'
if 'a' <= ch <= 'z':
    ch = chr(ord(ch) ^ 32)
elif 'A' <= ch <= 'Z':
    ch = chr(ord(ch) ^ 32)
print("4. Toggled case:", ch)

# Check if a number is even or odd using bitwise
n = 13
if n & 1:
    print("5. Odd")
else:
    print("5. Even")

# Combined assignment operations
x = 5
x += 10
x *= 2
x //= 3
x **= 2
print("6. Result =", x)

# Logical operator chaining
a = 10
b = 20
c = 5
if a < b and not (b < c or c > a):
    print("7. Condition True")
else:
    print("7. Condition False")

# Use ternary operator to find the greatest number
x = 10
y = 20
print("8. Greater number is", x if x > y else y)

# Complex logical & bitwise expression
a, b, c = 5, 10, 0
c = a & b
if (c or a > b) and not (a == b):
    print("9. Complex condition True")
else:
    print("9. Complex condition False")

# Use walrus operator to check string length
if (length := len("Python")) > 5:
    print("10. Length =", length)
