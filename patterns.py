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
        print(j, end="")
    print()