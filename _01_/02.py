# _ _init_ _ Function
# constructor -> All classes have a function called __init__ , which is always executed when the object is being initiated.

class Student:
    # Default constructor
    # def __init__(self):
    #     print("default constructor is called!") #Python automatically ek default constructor provide karta hai, lekin jaise hi programmer __init__() define karta hai, default constructor override ho jata hai.

    # Parametrized constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print(self)  

s1=Student("karan",98) 
print(s1) #<__main__.Student object at 0x00000239431D6F90>
 

print(s1.name,s1.marks)

s2=Student("Naman",89)
print(s2.name,s2.marks)

# s3=Student()
# data , variable -> attributes
# The self parameter is a reference to the current instance of the class,and is used to access variables that belongs to the class.

