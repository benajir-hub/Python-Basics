
def factorial(n):
    if n < 1:
        return False
    else:
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)



n = int(input("Enter a number for factorizing: "))
result = factorial(n)
print("Factorized result: ", result)