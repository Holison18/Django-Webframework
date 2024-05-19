# creating a dog class
class Dog(object):
    """A simple attempt to model a dog"""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    # create a sit function for the dog
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting")

    def rollover(self):
        """simulate dog rolling over in response to a command"""
        print(self.name.title() + " rolled over")


# creat an instance of the dog class
hope = Dog("Hope", 24)
hope.sit()
hope.rollover()

# Print the name and ageof the dog hope
print(f"My dog's name is {hope.name.title()}.")
print(f"My dog is {hope.age} years old.")
