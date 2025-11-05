# Input marks for 5 subjects
m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))

avg = (m1 + m2 + m3 + m4 + m5) / 5

print("Average Marks:", avg)

if avg >= 90:
    print("Grade: A+ (Outstanding)")
elif avg >= 75:
    print("Grade: A (Excellent)")
elif avg >= 60:
    print("Grade: B (Good)")
elif avg >= 40:
    print("Grade: C (Pass)")
else:
    print("Grade: F (Fail)")
