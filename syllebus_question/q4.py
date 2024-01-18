# Armstrong and palindrome number
def armstrong(n):
    arm_num = 0
    for i in n:
        arm_num = arm_num + int(i) ** len(n)
    if str(arm_num) == n:
        print(n, " is a armstrong number")
    else:
        print(n, " is not a armstrong number")


def palindrome(n):
    rev = n[::-1]
    if rev == n:
        print(n, "is a palindrom number")
    else:
        print(n, "is not a palindrom number")


num = str(int(input("Enter a number: ")))
armstrong(num)
palindrome(num)
