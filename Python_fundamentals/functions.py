"""
    Functions allow us to perform specific tasks
    syntax:
    def function_name(parameter:dtype)->return_type:
        docstring
        # function body
        return statement
"""

# create a function to add two number
def addNumber(num1:int,num2:int)-> int:
    """This function takes two numbers as arguments and adds them"""
    results = num1 + num2
    return results

num1 = int(input("Num1: "))
num2 = int(input("Num2: ")) 

# call addNumber function with num1 and num2 as arguments
print("Results = {}".format(addNumber(num1,num2)))