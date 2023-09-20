# In this program we are given two different list and are required to combine each of the elements
names = ["Kobina","Ama"]
occupations = ["Banker","Programmer"]

# using list comprehension and the zip method
result = [(f"Name: {i} | occupation{j}") for i,j in zip(names,occupations)]
print(result)

# let's try another example where we have the marks of students and bonus marks allocated to them.
# We want to add the original marks and the bonus marks

students = ['Afua','Kwamina','Adwoa','Araba','James','Ewura Ama']
marks = [67,89,80,77,65,75]
bonus = [10,7,5,2,20,10]
totalMarks = [(f"{name} : {i+j}") for name,i,j in zip(students,marks,bonus)]

for i in totalMarks:
    print(i)

# With my last example, let try finding matches within two list
list1 = ["Akosua",45.6,323,22,1,"Eminsah"]
list2 = ["Akosua",323,323,3553,323]
common = ["True" if i==j else "False" for i,j in zip(list1,list2)]

# print common
print(common)

# using map, lambda and zip method
# using the marks and bonuses example
marks = [67,89,80,77,65,75]
bonus = [10,7,5,2,20,10]
totalMarks2 = list(map(lambda x, y: x + y, zip(marks, bonus)))
for total in totalMarks2:
    print(total)