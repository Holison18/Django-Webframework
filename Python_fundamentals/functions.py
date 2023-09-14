"""
    Functions allow us to perform specific tasks
    syntax:
    def function_name(parameter:dtype)->return_type:
        docstring
        # function body
        return statement
"""

# create a function to add two number
def addNumber(num1:int,num2:int)-> int:
    """This function takes two numbers as arguments and adds them"""
    results = num1 + num2
    return results

# call addNumber function with num1 and num2 as arguments
print("Results = {}".format(addNumber(num1=12,num2=23)))


# A function to determine if a number is a prime number
def is_prime(n:int)->int:
    if n in [2,3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r+=2
    return True
print(is_prime(76))
print(is_prime(19))

# create a function to check whether the number passed as an argument is even or odd
def evenOdd(x):
    if x % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

evenOdd(13)
evenOdd(10)

# in programming there are two types of function
# 1. Functions that perform a task and
# 2. Functions that return a value

# using Keyword argument
def increment(number,by):
    return number + by

print(increment(number=34,by=6))

# default arguments for functions
# All option parameters should come after the required parameters
def increment1(number:int,by=1)->int: # pass a default increment parameter to increment1
    return number + by

print(increment1(10))

# *args are used to define functions with multiple arguments
def multiply(*numbers:int)->int:
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(3,2,4,1,5))
