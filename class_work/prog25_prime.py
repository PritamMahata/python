# WAP to search for prime numbers from 15 to 25.

for num in range(15, 26):
    for i in range(2, num):
        if num % i == 0:
            print("Found a factor:(", i, ") for", num)
            break
    else:
        print(num, "is a prime number.")