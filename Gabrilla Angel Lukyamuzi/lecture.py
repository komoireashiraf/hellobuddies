##
class Student:
    def __init__(self, name, age, gpa):
        self.name = name 
        self._age = age 
        self.__gpa = gpa 

def get_gpa(self):
    return self.__gpa

def set_gpa(self,value):
    if 0.0 <= value <= 5:
        self.__gpa = value
    else:
        print("The GPA must be between 0 and 5!")

s1 = Student('Gabby', 21, 10)
print(s1.set_gpa())
s1.set_gpa(12)


@property
def gpa (self,value)