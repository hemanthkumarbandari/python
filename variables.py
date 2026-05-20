"""
x = 5
y = "jhon"
print (x)
print (y)

s = "10"
n = int(s)
cnt = 5
f = float(cnt)
age = 25
s2 = str(age)

print(n)  
print(f)  
print(s2)

word = "Python"
length = len(word)
print("Length of the word:", length)

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

x = y = z = "Orange"

print(x)
print(y)
print(z)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

name = "hemz"
age = 21

print (name)
print (age)

x = "shashi"
y = 19

print(x)
print(y)

a = "hi"
b = 18
c = 12.56
d = True
e = ("hi, hlo, hey")
f = 5 + 6j
g = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

x = 10
print (x == 15)

a, b, c = 10, 20 ,30
print(a, b, c)

a, b = 10, 20

a, b = b, a

print(a)
print(b)

x = 100
def test():
  print(x)

test()
"""
x = 100
def test1():
  y = 200
  print(y)
def test2():
  print(x)

test1()
test2()
print(x)

x = 10
def change():
  global x
  x = 20

change()

x = 5

def fun():
  x = 10
  print(x)
  
fun()
print(x)