# Write a Python program that implements a simple calculator with 
# operations such as addition, subtraction, multiplication, and division. 
# Prompt the user to enter two numbers and the desired operation, and 
# then perform the calculation.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    print(f"The result of {num1} + {num2} is {num1 + num2}.")
elif operation == "-":
    print(f"The result of {num1} - {num2} is {num1 - num2}.")
elif operation == "*":
    print(f"The result of {num1} * {num2} is {num1 * num2}.")
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print(f"The result of {num1} / {num2} is {num1 / num2}.")
else:
    print("Invalid operation.")
    
# or
op =  eval(input("Write your eqution: "))
print("Ans: ",op)