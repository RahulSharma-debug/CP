x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

if x < y and x < z:
    print("Minimum is", x)
elif y < z:
    print("Minimum is", y)
else:
    print("Minimum is", z)