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


# create instance of the class
bird1 = bird()
chicken1 = chicken()
eagle1 = eagle

# call birds intro and flight methods
bird1.intro()
bird1.flight()

# call chicken's intro and flight methods
chicken1.intro()
chicken1.flight()

# call eagle1's intro and flight methods
eagle1.intro()
eagle1.flight()