# Swap two numbers without using a third variable
a = 10
b = 5
a = a ^ b #bitwise xor
b = a ^ b
a = a ^ b
print("1. Swapped values:", a, b)
