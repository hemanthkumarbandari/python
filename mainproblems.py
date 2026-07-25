7"""#Reverse a String
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
    print("Not Anagram")"""

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