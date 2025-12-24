class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod # decorator->Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it
    def hello():
        print("hellow")

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val

        print("hi",self.name,"your avg score is:",sum/3)


s1=Student("Tony stark",[99,98,100])

s1.get_avg()
s1.hello()