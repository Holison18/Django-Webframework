# find the factorial of a number
def fact(n):
    if n<=1:
        return 1
    return n * fact(n-1)

print(f"The factorial of 5 is: {fact(5)}")