##
class Student:
    def __init__(self, name):
        self.name = name             ##public
        self._gpa = 3.5              ##protected
        self.__password = "8890."        ##private

s1 = Student('Gabriella')
print(f"My name is {s1.name}. I have a GPA of {s1._gpa}.")   ##cannot print password because it was made private

##changing student name and gpa and password
s1.name = 'Jennifer'
s1._gpa = 2.9
s1.__password = "345£"

print(s1.name)
print(s1._gpa)

