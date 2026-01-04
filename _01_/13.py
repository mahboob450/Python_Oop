# polymorphism: operator overloading
# when the same operator is allowed to have different meaning according to the context

#  operators and dunder functions

# a+b addition -> a.__add__(b)
# a-b substraction -> a.__sub__(b)
# a*b multipliction -> a__mul___(b)
# a/b division ->  a.__truediv___(b)
# a%b modulous -> a.__mod___(b)


class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newReal=self.real + num2.real
        newImg=self.img + num2.img  
        return Complex(newReal,newImg)  

    def __sub__(self,num2):
        newReal=self.real - num2.real
        newImg=self.img - num2.img  
        return Complex(newReal,newImg)  

num1=Complex(1,3)
num1.showNumber()

num2=Complex(4,6)
num2.showNumber()

num3=num1+num2
num3.showNumber()
