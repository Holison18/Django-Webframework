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

# Example 2, using list comprehendsion to find the square of element is a list
myList2 = [3,2,4,5,1]

squared = [x**2 for x in myList2]
print(squared)

# creating a list of even numbers
even = [even_number for even_number in range(11) if even_number%2==0]
print(even)

# creatig a matrix using a list comprehension
matrix = [[array for array in range(4)] for array in range(3)]
print(matrix)

# appending character to a list
# using the traditional for loop expression
myList3 = []
for character in 'Kofi':
    myList3.append(character)
print(myList3)


# using list comprehendsion
myList3 = [character for character in "Kofi"]
print(myList3)