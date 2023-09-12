# creating a class
'''
    to create a class we use the class keyword followed by the name of the class
    All attributes in the class by default are public
'''

# create a dog class
class Dog:
    # class attribute
    str1 = "Mammal"

    def __init__(self,name):
        self.name = name

# object instantiation
hope = Dog("Hope")
risky = Dog("Risky")

# Assessing class attributes
print("A Dog is a {}".format(hope.__class__.str1))
print("A Dog is a {}".format(risky.__class__.str1))

# Accessing instance attributes
print("The name of my dog is {}".format(hope.name))
print("The name of my dog is {}".format(risky.name))