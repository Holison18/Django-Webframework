# the assert keyword is very helpful when debugging
# using assertion without an error message
def average(marks):
    assert len(marks)!=0
    return sum(marks)/len(marks)

myList = [34,45,43,23]
print(average(myList))

# when an assertion evaluates to false it raises an error message
# myList = []
# print(average(myList))

# using assertion with and error message
def average2(marks):
    assert len(marks) != 0,"list is empty"
    return sum(marks)/len(marks)

myList = [34,45,43,23]
print(average(myList))

#when an assertion evaluates to false it raises an error message
myList = []
print(average(myList))