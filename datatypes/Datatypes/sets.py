myset = {"orange", "banana", "papaya"}
print (myset)

myset = {"orange", "banana", "papaya", "orange"}
print (myset)

myset = {"orange", "banana", True, 1, 2, 3, "papa"}
print (myset)

myset = {"orange", "banana", 1, 2, 3, True, "papa"}
print (myset)

s = {"car", "bike", "auto", False, 0, 1}
print (s)

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1) # values changes everytime
print(set2)
print(set3) 

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset = {'car', 'bus', 'bike'}
newset = {'hero', 'honda', 'susuki'}
thisset.update(newset)
print (thisset)

newset = {'hi', 'hey', 'hola'}
x = newset.pop()
print (x)
print (newset)

sett = {"red", "red" , "red"}
print (sett)

#remove

newset = {'hi', 'hey', 'hola'}
newset.remove("hi")
print (newset)

newset = {'hi', 'hey', 'hola'}
newset.discard("hi")
print (newset)

newset = {'hi', 'hey', 'hola'}
x = newset.pop()
print (x)
print(newset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#loops

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

#join

set1 = {'big', 'bug', 'mug', 'jeg'}
set2 = {'cat', 'hat', 'jet', 'kit'}
set3 = {1, 2, 3, 4}
myset = set1.union(set2, set3)
print (myset)

set1 = {'big', 'bug', 'mug', 'jeg'}
set2 = {'cat', 'hat', 'jet', 'kit'}
set3 = {1, 2, 3, 4}
myset = set1 | set2 | set3
print (myset)

set1 = {'big', 'bug', 'mug', 'jeg'}
set2 = {'jeg', 'hat', 'jet', 'bug'}
set3 = set1.intersection(set2)
print (set3)

set1 = {'big', 'bug', 'mug', 'jeg'}
set2 = {'jeg', 'hat', 'jet', 'bug'}
set1 & set2
print (set3)

set1 = {'big', 'bug', 'mug', 'jeg'}
set2 = {'jeg', 'hat', 'jet', 'bug'}
set3 = set1.difference(set2)
print (set3)

set1 = {'big', 'bug', 'mug', 'jeg'}
set2 = {'jeg', 'hat', 'jet', 'bug'}
set1 - set2
print (set3)

set1 = {'big', 'bug', 'mug', 'jeg'}
set2 = {'jeg', 'hat', 'jet', 'bug'}
set3 = set1.difference_update(set2)
print (set3)

set1 = {'big', 'bug', 'mug', 'jeg'}
set2 = {'jeg', 'hat', 'jet', 'bug'}
set3 = set1.symmetric_difference(set2)
print (set3)

set1 = {'big', 'bug', 'mug', 'jeg'}
set2 = {'jeg', 'hat', 'jet', 'bug'}
set3 = set1.symmetric_difference_update(set2)
print (set3)

set1 = {'big', 'bug', 'mug', 'jeg'}
set2 = {'jeg', 'hat', 'jet', 'bug'}
set3 = set1 ^ set2
print (set3)

x = frozenset({'set', 'bet', 'wet'})
print (x)
print (type(x))

set1 = {'bug', 'bug', 'mug', 'jeg'}
set2 = {'jeg', 'hat', 'jet', 'bug'}
set3 = set1.symmetric_difference_update(set2)
print (set3)
