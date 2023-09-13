# Polymorphism means having different forms.

# define a parent bird class
class bird(object):

    def intro(self):
        print("There are many types of birds")
    
    def flight(self):
        print("Most of the birds can fly but some cannot")
    
class chicken(bird):
     
    def flight(self):
        print("Chicken cannot fly")


class eagle(bird):
    
    def flight(self):
        print("Eagles can fly very high")
