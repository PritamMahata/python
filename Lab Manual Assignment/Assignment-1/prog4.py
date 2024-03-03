# Write a Python program that classifies a person's age into different
# categories such as infant, child, teenager, adult, or senior citizen.
# Prompt the user to enter their age and then display the
# corresponding category.

age = int(input("Enter your age: "))
if (age >= 0) and (age <= 1):
    print("You are an infant.")
elif (age > 1) and (age <= 12):
    print("You are a child.")
elif (age > 12) and (age <= 19):
    print("You are a teenager.")
elif (age > 19) and (age <= 60):
    print("You are an adult.")
else:
    print("You are a senior citizen.")
