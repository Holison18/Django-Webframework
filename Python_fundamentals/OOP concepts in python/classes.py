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

    # add a speak function
    def speak(self):
        print("My name is {}".format(self.name))

# object instantiation
hope = Dog("Hope")
risky = Dog("Risky")

# Assessing class attributes
print("Hope is a {}".format(hope.__class__.str1))
print("Risky is a {}".format(risky.__class__.str1))
print()

# Printing the name of the dog using the speak method
hope.speak()
risky.speak()
