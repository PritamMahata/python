# Write a Python program that determines the number of days in a
# given month of a year. Prompt the user to enter the month and year,
# and then display the number of days.

m = int(input("Enter the month: "))
y = int(input("Enter the year: "))
if m == 2:
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        print("29 days")
    else:
        print("28 days")
elif m in [4, 6, 9, 11]:
    print("30 days")
else:
    print("31 days")
