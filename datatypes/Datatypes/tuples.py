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
"""
tuple = ("red", "mud", "food")
(pink, blue, black) = tuple
print (pink)
print (blue)
print (black)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
"""
"""
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

fruits = ("apple", "banana", "cherry", "hi", "strawberry", "raspberry")

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)
"""
#loops
"""
thistuple = ("red", "blue", "pink", "orange")
for i in range(len(thistuple)):
    print (thistuple[i])

thistuple = ("red", "blue", "pink", "orange")
i = 0 
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
"""
#join tuples
"""
t1 = ("red", "blue", "orange")
t2 = (1, 2, 3)
print (t1 + t2)

t1 = ("red", "blue", "orange")
t2 = (1, 2, 3)
print (t1 + t2*2)

t1 = ("red", "blue", "orange")
t2 = (1, 2, 3)
print ((t1 + t2)*2)
"""
#count

thistuple = (1,2,2,3,5,5,5,6)
newtuple = thistuple.count(5)
print (newtuple)

#index

thistuple = (1,2,2,3,5,5,5,6)
x = thistuple.index(3)
print (x)
