# Write a Python program that checks whether a given year is a leap
# year or not. Prompt the user to enter a year and then display whether
# it is a leap year or not.

y = int(input("Enter a year: "))
if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
    print(f"{y} is a leap year.")
else:
    print(f"{y} is a leap year.")
