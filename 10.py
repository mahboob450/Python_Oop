# Inheritance->when one class(child/derived) derives the properties and methods of another class(parent/base)

# Types of inhertance

# single inhertance:-One parent, one child
class Car:
    color="Black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod  # ->> koe v method static hone ka matlb ye hota hai ki har new instance k liye bo method bar bar create nhi hoga..puri class k liye common rhega..> kyo ki static methods instance attribute ko change kerta he nhi hai..-> it is used when na to class k attribute and nahi instance k attribute use ho rhe hai
    # @staticmethod class ke andar aisa method hota hai jo self ya cls use nahi karta aur class/object dono se call ho sakta hai.
        print("car stopped.")    

class ToyotaCar(Car):
    def __init__(self , name):
        self.name=name

car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")   

print(car1.start())
print(car1.color)

# Multi-level inheritance:-Chain of inheritance

class Car:
    color="Black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")    

class ToyotaCar(Car):
    def __init__(self , brand):
        self.name=brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type


car3=Fortuner("disel")
print(car3.start())

# Multiple inheritance:- Many parents, one child

class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class C(A,B):
    varC="welcome to class C"

c1=C()

print(c1.varC)
print(c1.varB)
print(c1.varA)

# super method-> super() method is used to access methods of the parent class
# super() ka use parent class ke constructor ya methods ko child class se call karne ke liye hota hai.

class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped.")    

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()


car1=ToyotaCar("prius","electric")

print(car1.type)