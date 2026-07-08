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

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

print(is_prime(17))

def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(8)

def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"

    for ch in text:
        if ch in vowels:
            count += 1

    return count

print(count_vowels("Programming"))