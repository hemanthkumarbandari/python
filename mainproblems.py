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
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in s1 + s1:
    print("Rotation")
else:
    print("Not Rotation")

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

<<<<<<< HEAD
print ("Reversed String:", reverse)
=======
print("Reversed String:", reverse)

s = input("Enter a string: ")

if len(s) > 1:
    result = s[-1] + s[1:-1] + s[0]
else:
    result = s

print("Result:", result)

s = input("Enter a string: ")

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

max_char = ""
max_count = 0

for ch in freq:
    if freq[ch] > max_count:
        max_count = freq[ch]
        max_char = ch

print("Most frequent character:", max_char)
print("Count:", max_count)

s = input("Enter a string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

first = second = 0
first_char = second_char = ""

for ch in freq:
    if freq[ch] > first:
        second = first
        second_char = first_char
        first = freq[ch]
        first_char = ch
    elif freq[ch] > second and freq[ch] != first:
        second = freq[ch]
        second_char = ch

print("Second most frequent character:", second_char)
print("Count:", second)

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print("Result:", result)

s = input("Enter a sentence: ")

words = s.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

s = input("Enter a string: ")

seen = ""

for ch in s:
    if ch in seen:
        print("First repeated character:", ch)
        break
    seen += ch
else:
    print("No repeated character")

s = input("Enter a string: ")

vowels = ""
consonants = ""

for ch in s:
    if ch.lower() in "aeiou":
        vowels += ch
    else:
        consonants += ch

print("Result:", vowels + consonants)

s = input("Enter a string: ")

flag = True

for ch in s:
    if not ('a' <= ch <= 'z' or 'A' <= ch <= 'Z'):
        flag = False
        break

if flag:
    print("Only alphabets")
else:
    print("Contains other characters")

numbers = list(map(int, input("Enter numbers: ").split()))

largest = second = float('-inf')

for n in numbers:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("Second largest:", second)

n = int(input("Enter N: "))
numbers = list(map(int, input("Enter numbers: ").split()))

expected = n * (n + 1) // 2

actual = 0
for num in numbers:
    actual += num

missing = expected - actual

print("Missing number:", missing)
>>>>>>> 4c2149e4e20840aad4d205552ff5f6cf50ae269c
