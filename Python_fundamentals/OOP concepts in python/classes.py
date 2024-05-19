# creating a dog class
class Dog(object):
    """ A simple attempt to model a dog"""

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    # create a sit function for the dog
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting")

    def rollover(self):
        """simulate dog rolling over in response to a command"""
        print(self.name.title() + " rolled over")

