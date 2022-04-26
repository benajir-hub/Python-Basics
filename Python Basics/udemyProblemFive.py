#Factorial of a number

n = int(input("Entar the number for factorial: "))
count = 1
while(n != 0):
    count = count * n
    n = n-1

print("Factorial is ",count)