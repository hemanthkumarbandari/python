"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)

mylist = ["m","n","o","p","q"]
mylist[2:]=["x","y","z"]
print(mylist)

mylist = ['1','2','3','4']
mylist.append('5')
print(mylist)

mylist = ['1','2','3','4']
morenums = ['6','7','8','9']
mylist.append('5')
mylist.insert(1, "0")
print(mylist)

mylist = ['1','2','3','4']
morenums = ['6','7','8','9']
mylist.append('5')
mylist.insert(1, "0")
mylist.extend(morenums)
print(mylist)

"""
"""
list = ["hi", "hlo", "hey"]
for x in list:
    print(x)

list = ["hi", "hlo", "hey"]
for i in range(len(list)):
    print(i)

list = ["hi", "hlo", "hey"]
i = 0
while i < len(list):
   print(list[i])
   i = i+1

list = ['orange', 'blue', 'black', 'red', 'pink']
newlist = []
for x in list:
    if "a" in x:
        newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ["fruit: " + x for x in fruits if "a" in x]
print(newlist)

list = ['orange', 'blue', 'black', 'red', 'pink']
for x in list

"""
# list sort
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.sort()
print (fruits)

