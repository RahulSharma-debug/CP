percentage = float(input("Enter percentage: "))

if percentage > 85:
    grade = "A+"
elif percentage > 65:
    grade = "A"
elif percentage > 45:
    grade = "B"
elif percentage >= 25:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)