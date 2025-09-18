# A CLASS
#A CLASS IS A BLUEPRINT FOR OBJECTS
#DEFINES ATTRIBUTES(DATA)+ METHODS(BEHAVIOUR)A
#OBJECT
#INSTANCE OF A CLASS
#MULTIPLE OBJECTS FRON ONE CLASS
#example one
class Car:
    def __init__(self,Model,year):
        self.Model = 'hilux'
        self.year = 2020
    
    def description(self):
        print(f"the model of the car is {self.Model}")
        print(f"the year of the car is {self.year}")

    
 


#example two