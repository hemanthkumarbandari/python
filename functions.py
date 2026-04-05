#Armstrong
def armstrong(n):
    s = 0
    for i in str(n):
        s += int(i) ** len(str(n))
    if s == n:
        print("Armstrong")
    else:
        print("Not Armstrong")

armstrong(153)

#Palindrome Strings
def find_palindrome(lst):
    for i in lst:
        if i == i[::-1]:
            print(i)

words = ["madam","apple","level","python","radar"]
find_palindrome(words)

#basics

def function():
    print("hi")
function()
function()

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

