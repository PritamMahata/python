# Write a Python program that finds the largest of three given
# numbers. Prompt the user to enter three numbers and then display
# the largest among them.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 > num2:
    if num1 > num3:
        print(num1, "is the largest number.")
    else:
        print(num3, "is the largest number.")
else:
    if num2 > num3:
        print(num2, "is the largest number.")
    else:
        print(num3, "is the largest number.")

# or

print(max(num1, num2, num3), "is the largest number.")
