# Python file handling

# writing to a file
with open("kobina.txt","a") as myfile:
    myfile.write("My name is kobina Akofi-holison")
myfile.close

# reading from a file
with open("kobina.txt","r") as myfile:
   content =  myfile.readlines()
   print(content)
myfile.close