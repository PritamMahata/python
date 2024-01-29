# WAP to print the grade of a student based on the marks entered by the user.
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A grade")
elif marks >= 80:
    print("B grade")
elif marks >= 60:
    print("C grade")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
