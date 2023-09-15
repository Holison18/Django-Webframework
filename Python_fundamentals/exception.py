# Python Exception handling is an important concept in python

# using the try except for a division by zero exception

number = 8
try:
    number/0
except ZeroDivisionError:
    print("Cannot Divide an number by zero")
    