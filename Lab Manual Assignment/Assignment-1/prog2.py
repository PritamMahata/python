# Write a Python program that checks whether a given number is even 
# or odd. Prompt the user to enter a number and then display whether 
# it is even or odd. 
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")