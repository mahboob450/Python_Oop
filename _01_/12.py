# Property decorator -> we use @property decorator an any method in the class to use the method as a property

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        # self.percentage=str((self.phy + self.chem + self.math )/3) + "%"



    @property
    def calPerc(self):
        return str((self.phy + self.chem + self.math )/3) + "%"


s1=Student(98,97,90)
# print(s1.percentage)

s1.phy=90
# print(s1.percentage) # percentage is still same even phy=90 
# s1.calPerc()
# print(s1.percentage)

print(s1.calPerc)

# as a homework, study-> @getter @setter

