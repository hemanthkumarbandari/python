"""
#valid triangle 
a = int(input("Enter side a:"))
b = int(input("Enter side b:"))
c = int(input("Enter side c:"))
if a+b>c and b+c > a and a+c>b:
    print ("Triangle is valid")
else:
    print("invalid")
"""
# divisible by 3 and 5
num = int(input("Enter a Number;"))
if num % 3 == 0 and num % 5 == 0:
    print("divisible1")