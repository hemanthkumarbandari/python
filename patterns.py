n = 5

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

n = 5

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()

n = 5

for i in range(n):
    for j in range(1, i+2):
        print(i+1, end="")
    print()

n = 5

for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()

n = 5

for i in range(n):
    for j in range(1,n-i+1):
        print(j, end="")
    print()

n = 5

for i in range(n):
    for j in range(n-i):
        print(j+1, end="")
    print()