# Try/Except 
t=(1,2,3,4)
# t[0]=4 #TypeError: 'tuple' object does not support item assignment

try:
    print("Hi") # no error
    t[0]=3 # definitely throw an error
    print("Hello")

except:
    print("caught the error")    

# user input
# result=input("Hey , give me a number: ") # code will get stuck here ,  display this message on the terminal waiting for the user to respond.
# print(f"the result is {result}")


# List comprehension: to make quickly
# List comprehension is a compact and efficient way to create lists using a single line of code.
li=[i for i in range(6)]
for i in li:
    print(i,end=' ')

print()

l=[i*i for i in range(1,5) if i%2==0]  
for i in l:
    print(i,end=" ")

a=[x if (x%2==0) else 5 for x in range(5)]
print(a)

# point to remember:
# if-else then write it before for loop
# if only we use if condition then write it after for loop
print()
b=[0 for i in range(5)]
print(b)
print()
# [1,2]+[3,5,4]  list concatination

for a , b in zip(range(3),range(4,7)): # a and b simultaneously loop through their respective range
    print(a,b)
c=[(a,b) for a,b in zip(range(3),range(4,7))]    
print(c)
d={a:b for a,b in zip(range(3),range(4,7))}
print(d)

# python script: “A Python script is a .py file containing Python code that is executed by the Python interpreter to perform a task.”