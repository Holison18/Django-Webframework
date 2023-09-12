# create a person class (oarent class)
class person(object):

    # the init constructor
    def __init__(self,idnumber,name):
        self.idnumber = idnumber
        self.name = name

    def printDetails(self):
        print("Name: {}".format(self.name))
        print("ID: {}".format(self.idnumber))

# create a base class for employee
class employee(person):

    # the init constructor
    def __init__(self, idnumber, name,department,salary,role):
        super().__init__(idnumber, name)
        self.department = department
        self.salary = salary
        self.role = role
    

    def printDetails(self):
        super().printDetails()
        print("Department: {}".format(self.department))
        print("Salary: {}".format(self.salary))
        print("Role: {}".format(self.role))


holison = employee(20765490,"Kobina Akofi-Holison","Software Engineering",5000,"Project Manager")
holison.printDetails()

    