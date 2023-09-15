# python regular expression
# this program verifies an email to make sure it meets the standard of an email
import re 

pattern = "[a-zA-Z0-9]+@[a-zA-z]+\.(com|edu|net)" 

# ask user for input
userInput = input()

if re.search(pattern,userInput):
    print("Valid email")
else:
    print("Invalid email")