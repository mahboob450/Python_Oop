# del keyword-> used to delete object properties or object itself
# del s1.name , del s1

class Student:
    def __init__(self,name):
        self.name=name

s1=Student("mahboob") 
print(s1)
# del s1
del s1.name
print(s1.name) #AttributeError: 'Student' object has no attribute 'name'
print(s1)       