number = int(input("Enter a number: "))

if number % 5 == 0 and number % 11 == 0:
    print(f"{number} is divisible by both 5 and 11")
else:
    print(f"{number} is not divisible by both 5 and 11")