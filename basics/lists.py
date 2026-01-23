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
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.sort()
print (fruits)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.sort(reverse = True)
print (fruits)

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist) 

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist)
"""

# copy list
"""
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print (mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print (mylist)
"""
# add list
"""
List1 = ["apple", "banana", "cherry"]
List2 = [1, 2, 3]
print (List1 + List2)

List1 = ["add", "sub", "div"]
List2 = [1, 2, 3]
for x in List2:
    List1.append(x)
print(List1)

List1 = ["add", "sub", "div"]
List2 = [1, 2, 3]
List1.append(List2)
print(List2)
"""
# List methods
"""
numbers = [3, 1, 4, 1, 5]

numbers.append(9)
print (numbers)

numbers.clear()
print (numbers)

nums = [3, 1, 4, 1, 5]
x = nums.copy()
print (x)

words = ["hiii", "byeee", "hoiiieee", "oyeeee", 5]
x = words.count("oyeeee")
print (x)

words = ["hiii", "byeee", "hoiiieee", "oyeeee"]
mywords = ("byeee", "tataaa")
words.extend(mywords)
print (words)

words = ["hiii", "byeee", "hoiiieee", "oyeeee"]
nums = (5, 6)
words.extend(nums)
print (words)
"""
#index

"""
words = ['hiii', 'byeee','tataaa', 'hoiiieee', 'oyeeee', 'byeee', 'tataaa']
x = words.index('tataaa')
print (x)

nums = (8, 1, 3, 0, 6, 7, 4, 6, 3, 0, 1)
x = nums.index(3)
print (x)

words = ['hiii', 'byeee','tataaa', 'hoiiieee', 'oyeeee', 'byeee', 'tataaa']
x = words.index('tataaa', 3)
print (x)
"""
#insert

"""
words = ['hiii', 'byeee','tataaa', 'hoiiieee', 'oyeeee', 'byeee', 'tataaa']
words.insert(2, 'hoyyy')
print (words)
"""
#pop

"""
words = ['hiii', 'byeee','tataaa', 'hoiiieee', 'oyeeee', 'byeee', 'tataaa']
words.pop(3)
print (words)

words = ['hiii', 'byeee','tataaa', 'hoiiieee', 'oyeeee', 'byeee', 'tataaa']
x = words.pop(3)
print (x)
"""
#remove


words = ['hiii', 'byeee','tataaa', 'hoiiieee', 'oyeeee', 'byeee', 'tataaa']
words.remove('byeee')
print (words)