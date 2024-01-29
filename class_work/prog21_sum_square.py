# WAP to find the sum of squares of first 5 numbers using while loop
sum = 0
i = 1
while i <= 5:
    sum += int(input("Enter a number: "))**2
    i += 1
print("Sum =", sum)
