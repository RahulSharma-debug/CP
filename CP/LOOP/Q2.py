#find the number of digits in a number
a=int(input("Enter a number: "))
count = 0
while a>0:
    count +=1
    a = a//10
print(count)