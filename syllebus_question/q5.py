# Fibonacci series
num = int(input("Enter a number: "))
a = 0
b = 1
c = 1
for i in range(num):
    print(a,end=" ")
    a = b
    b = c
    c = a + c