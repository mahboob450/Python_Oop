# ASCII value
print(chr(97)) # convert int to character
print(ord('a'))  # convert char to int
result={a:chr(a) for a in range(97,123)}
print(result)

# ** module
# from copy import deepcopy : #copy->module,
# deepcopy → original object aur copy bilkul alag memory me hote hain
# ek me change karo → doosre par koi effect nahi
from copy import deepcopy

a = [[1, 2], [3, 4]]
b = deepcopy(a)

b[0][0] = 99

print(a)  # [[1, 2], [3, 4]]
print(b)  # [[99, 2], [3, 4]]
# yaha a change nahi hua, kyunki deepcopy use kiya

from copy import copy

a = [[1, 2], [3, 4]]
b = copy(a)

b[0][0] = 99

print(a)  # [[99, 2], [3, 4]]  #changed

import copy as cp #:- cp is alias of copy . cp is used everywhere to access the library
a=[1,2,3]
b=cp.deepcopy(a)
print(a is b) # False

# import numpy as nu
# print(nu)

"""
Python me libraries / modules ke examples 👇
(5 popular & important)

1️⃣ math:Mathematical operations ke liye
import math
math.sqrt(16)   # 4.0

2️⃣ sys : System-specific parameters aur functions
import sys
print(sys.version)

3️⃣ os:Operating system ke sath kaam karne ke liye
import os
os.getcwd()   # current directory

4️⃣ random:Random numbers generate karne ke liye
import random
random.randint(1, 10)

5️⃣ copy:Object copying ke liye (copy, deepcopy)
from copy import deepcopy

✅ 5 Python Libraries

(Libraries = modules ka collection)

1️⃣ NumPy – numerical & array operations
2️⃣ Pandas – data analysis & dataframes
3️⃣ Matplotlib – data visualization / graphs
4️⃣ TensorFlow – machine learning & deep learning
5️⃣ Requests – HTTP requests / API calling

✅ 5 Python Modules

(Modules = single .py file)

1️⃣ math – mathematical functions
2️⃣ os – operating system interaction
3️⃣ sys – system-specific parameters
4️⃣ random – random number generation
5️⃣ copy – object copying (copy, deepcopy)

👉 Note:
Module → single file (e.g. math, sys) :-A single Python file containing functions and variables
Library → modules ka collection (e.g. numpy, pandas)
"""

# ** PIP:-pip is Python’s package manager.It is used to install, update, and remove Python libraries/packages.

"""
🔹 Common pip commands
1️⃣ Package install karna
pip install numpy

2️⃣ Package uninstall karna
pip uninstall numpy

3️⃣ Installed packages dekhna
pip list
"""

# ** LAMBDA FUNCTION:- it is one line anonymous function
# It can accept any number of parameters
add=lambda a , b : a+b

print(add(2,4))
#  maps , filters, sort
# 1.maps:map function takes some list or iterable object and apply the function to every single element inside the list

my_num=[1,2,3,4,5]

def square(x): # defining a function to calculate the square of num
    return x**2
# squares=list(map(square,my_num)) # use a list , map each item to square function
squares=list(map(lambda x:x**2,my_num))  # using lambda function . we can pass lambda function as an argument to another function
print(squares)   

# 2.Filters:- apply the function to every single item inside the list or iterable object 
# and if the function returns true then we keep the item else we reject that item

even=list(filter(lambda x:x%2==0,my_num))
print(even)

# 3.Sort: it sorts the items of a list.we define lambda function to define key
values=[(1,'b',"hellow"),(2,'a',"world"),(3,'c',"okay")]
# sorted_values=sorted(values,key=lambda x:x[2])
sorted_values=sorted(values,key=lambda x:x[1]+ x[2])
print(sorted_values)

# Reduce:it is going to take list or an iterable object and reduce it to a single value
# accumulated(accu) -> by default it is always num[0]
# x by default it is always num[0]
# accu=1 x=2-> accu+x=3
# accu=3 x=3 -> accu+x=6 ...continuee
num=[1,2,3,4,5]
from functools import reduce
sumofnumber=reduce(lambda accu,x:accu+x , num)
print(sumofnumber)

maxvalue=reduce(lambda acc,x:acc if acc>x else x,num)
print(maxvalue)