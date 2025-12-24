# class & instance attributes 
# Class attributes are variables that belong to the class itself and are shared among all its object
class Student:
    college = "ABC University"   # class attribute

    def __init__(self, name):
        self.name = name         # instance attribute

s1 = Student("Karan")
s2 = Student("Naman")
Student.college = "XYZ College" #Modifying Class Attribute
print(Student.college) #Accessing Class Attribute

print(s1.college)
print(s2.college)
print(s1.name)
print(s2.name)
# college is shared by both objects.

# Object attributes are variables that are defined using self and are unique for each object of a class.

# If class and instance variables have the same name, Python gives priority to the instance variable.
# Instance variable > Class variable