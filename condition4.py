"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a >= b and a <= c) or (a <= b and a >= c):
    print("Second largest is:", a)
elif (b >= a and b <= c) or (b <= a and b >= c):
    print("Second largest is:", b)
else:
    print("Second largest is:", c)"""

cost = float(input("Enter Cost Price: "))
sell = float(input("Enter Selling Price: "))

if sell > cost:
    profit = sell - cost
    percent = (profit / cost) * 100
    print("Profit =", profit)
    print("Profit Percentage =", percent, "%")
elif sell < cost:
    loss = cost - sell
    percent = (loss / cost) * 100
    print("Loss =", loss)
    print("Loss Percentage =", percent, "%")
else:
    print("No Profit No Loss")
