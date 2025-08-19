#reverse of an number
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reverse of the number:", reverse)