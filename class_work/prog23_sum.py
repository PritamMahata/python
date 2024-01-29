# WAP that input multiple numbers and print their sum.
count = sum = 0
ans = "y"
while ans == "y" or ans == "Y":
    num = int(input("Enter a number: "))
    if num < 0:
        break
    sum += num
    count += 1
    ans = input("Another number? (y/n): ")
else:
    print("You entered", count, "numbers so far.")
print("Sum =", sum)
