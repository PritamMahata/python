# Write a Python program that checks whether a given number is 
# positive, negative, or zero. Prompt the user to enter a number and 
# then display whether it is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
