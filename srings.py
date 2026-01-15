"""
s = "Hemanth Kumar"
print("Original String:", s)

print("Reverse:", s[::-1])

s2 = "madam"
print("Is Palindrome:", s2 == s2[::-1])

vowels = "aeiouAEIOU"
print("Vowel Count:", sum(1 for ch in s if ch in vowels))

print("Consonant Count:", sum(1 for ch in s if ch.isalpha() and ch not in vowels))

print("Uppercase:", s.upper())
print("Lowercase:", s.lower())

print("Word Count:", len(s.split()))

print("Remove Spaces:", s.replace(" ", ""))

print("Length:", len(s))

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print("Character Frequency:", freq)

a = "listen"
b = "silent"
print("Are Anagrams:", sorted(a) == sorted(b))

s3 = "swiss"
for ch in s3:
    if s3.count(ch) == 1:
        print("First Non-Repeating Character:", ch)
        break

print("Replace Vowels:", "".join("*" if ch in vowels else ch for ch in s))

num = "12345"
print("Only Digits:", num.isdigit())

mixed = "abc1234xyz"
print("Digit Count:", sum(ch.isdigit() for ch in mixed))

unique = ""
for ch in s:
    if ch not in unique:
        unique += ch
print("Remove Duplicates:", unique)

sentence = "Python is very easy"
print("Reverse Words:", " ".join(sentence.split()[::-1]))
"""
print("Title Case:", sentence.title())

print("Contains 'Kumar':", "Kumar" in s)

words = sentence.split()
print("Longest Word:", max(words, key=len))
