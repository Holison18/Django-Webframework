# Python Exception handling is an important concept in python

# using the try except for a division by zero exception

number = 8
try:
    number/0
except ZeroDivisionError:
    print("Cannot Divide an number by zero")


myList = [1,2,3]
try:
    print(myList[1])

    # this will raise an errow since the index exceeds the actual number of elements
    print(myList[3])
except:
    print("An Error occurred")


#try with an else statement
def abys(a,b):
    try:
        c = ((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b gives a zero divison error")
    else:
        print(c)

abys(2.0,3.0)
abys(3.0,3.0)