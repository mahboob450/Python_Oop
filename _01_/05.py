# Q-> create student class that takes name and marks of three subjects as arguments in constructor.Then create a method to print the average.

class Student:
    def __init__(self,name,s1,s2,s3):
        self.name=name
        self.s1=s1
        self.s2=s2
        self.s3=s3

    def avg(self):
        print(f" average marks of {self.name} is {(self.s1+self.s1+self.s1)/3}")    

s1=Student("Mahboob",98,97,100)
s1.avg()      
        