# This code takes an integer input from the user and prints all its divisors.
a = int(input("Enter a number: "))
i=1
while i<=a:
    if a % i == 0:
        print(i)
    i += 1
