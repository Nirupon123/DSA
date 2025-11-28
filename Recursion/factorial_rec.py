def factorial_rec(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_rec(n - 1)

num = int(input("Enter a number: "))
print("The factorial of", num, "is:", factorial_rec(num))
