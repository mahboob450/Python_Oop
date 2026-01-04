class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7)*self.radius**2

    def perimeter(self):
        return 2*(22/7)*self.radius

c1=Circle(21)
print(c1.area())
print(c1.perimeter())     

#  Q. Define a Employee class with attributes role, department and salary. This class also a showDetails() method.
# Create an Engineer class that inherits properties from employee and has additional attributes : name and age

class Employee:

    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("salary =",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75,000")

engg1=Engineer("Mahboob",23)        
engg1.showDetails()

# Q. create a class called order which stores item and its price.
#    Use Dunder function __gt__() to convey that order1>order2 if price of order1> price of order2

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,ord2):
        return self.price> ord2.price

ord1=Order("Chips",20)            
ord2=Order("tea",15)  

print(ord1>ord2)
