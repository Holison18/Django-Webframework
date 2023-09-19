# list comprehendsion
# normal list
myList = [1,2,3,4,5]

for i in myList: # This is the traditional way of looping through a list using a for loop
    print(i)

# python list comprehension syntax:
# newList = [expression(element) for element in oldlist if condition]

# for example incrementing every element in our list by 1
newList = [(x+1) for x in myList]
# print newlist
print(newList)