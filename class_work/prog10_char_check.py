# write a program to check if the user has entered a charecter, digit, white space or a special charecter.
inp = input("Enter a charecter ")
if inp.isalpha():
    print("You enter alphabet")
elif inp.isdigit():
    print("You enter digit")
elif inp.isspace():
    print("You enter a white space")
else:
    print("You enter a special charecter")
