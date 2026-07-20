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