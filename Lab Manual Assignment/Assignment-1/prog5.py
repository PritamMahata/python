# Write a Python program that checks whether a given set of three
# numbers can form a valid triangle and if so, whether it is an
# equilateral, isosceles, or scalene triangle. Prompt the user to enter
# three numbers and then display the type of triangle.
s1 = int(input("Enter the length of the first side: "))
s2 = int(input("Enter the length of the second side: "))
s3 = int(input("Enter the length of the third side: "))
if (s1 + s2) > s3 and (s2 + s3) > s1 and (s3 + s1) > s2:
    if s1 == s2 == s3:
        print("The given set of numbers form an equilateral triangle.")
    elif s1 == s2 or s2 == s3 or s3 == s1:
        print("The given set of numbers form an isosceles triangle.")
    else:
        print("The given set of numbers form a scalene triangle.")
else:
    print("The given set of numbers cannot form a valid triangle.")
