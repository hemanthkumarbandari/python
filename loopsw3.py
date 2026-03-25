i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

is_logged_in = True

if is_logged_in:
  print("Welcome back!")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 
