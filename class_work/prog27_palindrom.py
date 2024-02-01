# WAP to check if a number is a palindrome or not.
num = int(input("Enter a number: "))
temp = num
rev = 0
while num > 0: 
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10
if temp == rev:
    print(temp,"is Palindrome number")
else:
    print(temp,"is not a Palindrome number")