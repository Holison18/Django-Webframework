# fizz_buzz 
# The fizz_buzz function takes an input
# If the input is divisible by 3 we print fizz
# if the input is divisible by 5 we print buzz
# if the input is divisible by both we print fizz_buzz else return the number itself

def fizz_buzz(number:int):
    if (number % 3 == 0) and (number % 5 == 0):
        return "Fizzbuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number

# pass the number 9 to fizz_buzz
print(fizz_buzz(9)) 

# pass the number 10 to fizz_buzz
print(fizz_buzz(10)) 

# pass the number 15 to fizz_buzz
print(fizz_buzz(15)) 

# pass the number 1 to fizz_buzz
print(fizz_buzz(1)) 