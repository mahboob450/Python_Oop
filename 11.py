# class method:
# A class method is bound to the class and receive the class as an implicit first argument.
# Note- static method can not access or modify class state and generally for utility

class Person:
    name="anonymous"

    # def changeName(self,name):
    #     # self.name=name
    #     # Person.name="Rahul"
    #     self.__class__.name="Mukesh"

    @classmethod      #cls class ka reference hota hai -> class ko refer kerta hai.ye @classmethod ke sath use hota hai (jaise self instance ke liye hota hai).                  
    def changeName(cls, name):
        cls.name=name

p1=Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)        