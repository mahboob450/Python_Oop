# Pillors of OOP
# Abstraction -> Hinding the implementation details of a class and only showing the essentials features to the user

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("Car started...")  

car1=Car()
car1.start()         

# Encapsulation->Wrapping data and function into a single unit(object).

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("total balance = ",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was cradited")
        print("total balance = ",self.get_balance())
    
    def get_balance(self):
        return self.balance


acc1=Account(10000,12345667)
print(acc1.balance)
print(acc1.account_no)     

acc1.debit(100)
acc1.credit(100)