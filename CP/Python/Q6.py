# Q6.py
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

min_num = a
if b < min_num:
    min_num = b
if c < min_num:
    min_num = c

print(f"The minimum number is: {min_num}")