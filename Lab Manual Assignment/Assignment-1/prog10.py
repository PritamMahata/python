# Write a Python program that checks whether a given character is a
# vowel or a consonant. Prompt the user to enter a character and then
# display whether it is a vowel or a consonant.
c = input("Enter a character: ")
if c.lower() in ["a", "e", "i", "o", "u"]:
    print(f"{c} is a vowel")
else:
    print(f"{c} is a consonant")
