"""
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#access
x = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print (x[2:6])
#updating 

x = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
y = list(x)
y[1] = "graph"
x = tuple(y)
print (x)

x = ("red", "mud", "fud", "bed")
y = list(x)
y[1] = "ted"
x = tuple(y)
print(x) 
"""
#unpack

tuple = ("red", "mud", "food")
(pink, blue, black) = tuple
print (pink)
print (blue)
print (black)


