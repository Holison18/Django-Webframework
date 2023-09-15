# python regular expression

import re 

# verify an email to make sure it meets the standard of an email
pattern = "[a-zA-Z0-9]+@[a-zA-z]+\.(com|edu|net)" 

# ask user for input
userInput = input("Email: ")

if re.search(pattern,userInput):
    print("Valid email")
else:
    print("Invalid email")


# check if the contact a user enters in 10 digits
contact_pattern = r'\+233\d{9}$'

# get users contact
contact = input("Contact: ")
if re.match(contact_pattern,contact):
    print("Valid contact")
else:
    print("Invalid contact")