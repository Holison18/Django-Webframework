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

class Restaurant(object):
    "This a restaurant class"

    def __init__(self, name:str, cuisine_type:str):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes the restaurant"""
        print(f"The name of the restaurant is {self.name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} restaurant is opened now!")


# creat an instance of the dog class
hope = Dog("Hope", 24)
hope.sit()
hope.rollover()

# Print the name and ageof the dog hope
print(f"My dog's name is {hope.name.title()}.")
print(f"My dog is {hope.age} years old.")


print()
print()

# create an instance of the restaurant class
Edziban = Restaurant("Edziban Delight","French Cuisine")
Edziban.describe_restaurant()
Edziban.open_restaurant()

# Print the attributes of the restaurant class
print("Name of Restaurant: {}".format(Edziban.name.title()))
print("Cuisine: {}".format(Edziban.cuisine_type))


