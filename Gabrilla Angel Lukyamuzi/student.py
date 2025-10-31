class Student:
    def __init__(self, name):
        self.name = name 
    
    def introduce(self):
        return(f"My name is {self.name}")
    
class Girl(Student):
    def greet(self):
        super().introduce
        return("Nice to meeet you!")

g1 = Student("Gina")
g1.introduce()




