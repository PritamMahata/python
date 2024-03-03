# Write a Python program that calculates the grade of a student based 
# on their marks in a subject. Prompt the user to enter the marks 
# scored by the student and then display the corresponding grade 
# according to a predefined grading system.
sub1 = float(input("Enter the marks of the first subject: "))
sub2 = float(input("Enter the marks of the second subject: "))
sub3 = float(input("Enter the marks of the third subject: "))
sub4 = float(input("Enter the marks of the fourth subject: "))
sub5 = float(input("Enter the marks of the fifth subject: "))
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5
if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: F")
    