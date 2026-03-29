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