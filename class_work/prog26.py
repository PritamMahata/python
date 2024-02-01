# WAP to find sum of the series s = 1 + X + X^2 + X^3 + ... + X^n

x = int(input("Enter value of x: "))
n = int(input("Enter value of n: "))
s = 0
for a in range(n+1):
    s += x**a
print("Sum of first", x,"terms:", s)
