# Method->Methods are functions that belong to objects.
class Student:
    college = "ABC University"   # class attribute

    def __init__(self, name):
        self.name = name         # instance attribute

    def welcome(self):
        print("welcome student!",self.name)    

s1 = Student("Karan")
s2 = Student("Naman")
print(s1.name)
s1.welcome()