"""
#Reverse a String
s = input("Enter a string: ")

reverse = s[::-1]

print("Reversed String:", reverse)

#Check Palindrome
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Count Vowels
s = input("Enter a string: ")

count = 0

for ch in s.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)

#Find Length of String (Without len())
s = input("Enter a string: ")

count = 0

for ch in s:
    count += 1

print("Length:", count)

#Count Frequency of Characters
s = input("Enter a string: ")

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

print(palindrome("madam"))

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print("After removing duplicates:", result)

s = input("Enter a sentence: ")

words = s.split()

reverse = words[::-1]

print(" ".join(reverse))

s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

print(reverse)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1 == s2:
    print("Strings are Equal")
else:
    print("Strings are Not Equal")

s = input("Enter a string: ")
ch = input("Enter the character to search: ")

count = 0

for i in s:
    if i == ch:
        count += 1

print("Occurrences:", count)

s = input("Enter a string: ")

print("Uppercase:", s.upper())

s = input("Enter a string: ")

letters = digits = special = 0

for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special Characters:", special)

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch != " ":
        result += ch

print("After removing spaces:", result)

s = input("Enter a sentence: ")

words = s.split()

largest = words[0]

for word in words:
    if len(word) > len(largest):
        largest = word

print("Largest Word:", largest)

s = input("Enter a string: ")

flag = True

for ch in s:
    if ch < '0' or ch > '9':
        flag = False
        break

if flag:
    print("String contains only digits")
else:
    print("String does not contain only digits")

s = input("Enter a string: ")
ch = input("Enter the character to search: ")

count = 0

for i in s:
    if i == ch:
        count += 1

print("Occurrences:", count)
"""

s = input("Enter a string: ")

reverse = ""

for char in s:
    reverse = char + reverse

print("Reversed String:", reverse)