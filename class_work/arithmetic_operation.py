# WAP to perform arithmetic operations on two numbers.
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
add = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
idiv = n1 // n2
mod = n1 % n2
print(n1, "+", n2, "=", add)
print(n1, "-", n2, "=", sub)
print(n1, "*", n2, "=", mul)
print(n1, "/", n2, "=", div)
print(n1, "//", n2, "=", idiv)
print(n1, "%", n2, "=", mod)
