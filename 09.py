# Private(like) attributes & methods
# conceptual Implementation in python:
# Private attributes & methods are meant to be used only within the class and are not accessible from outside the class

# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         # conceptually become private
#         self.__acc_pass=acc_pass # __ double underscore is used to make it private

#     def reset_pass(self):
#         print(self.__acc_pass)

#     def __hellow():
#         print("hellow")    

# acc1=Account("12345","abcde")

# print(acc1.acc_no)
# print(acc1.reset_pass())

# acc1.__hellow() #AttributeError: 'Account' object has no attribute '__hellow'

class Person:
    __name="anonymous"

    def __hello(self):
        print("Hellow person")

    def welcome(self):
        self.__hello()    

p1=Person()

# print(p1.__hello())
print(p1.welcome())