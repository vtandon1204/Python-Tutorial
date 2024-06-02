import inspect

# print(inspect.getsource(list))
x = [1,2, 3]
y = [4,5]
# print(x()3)
print(x+y)
print(x[1]) 
print(type(x)) 


class Person:
    
    def __init__ (self,name):
        self.name= name
    def __repr__(self):
        return f"{self.name}"
    def __mul__(self,x):
        if(type(x) is not int):
            raise Exception("innvalid argument, must be int")
        self.name = self.name*x
p =Person('vt')
# p*4
# print(p) # it shows it's memory address location of the object 
print(p)


# print(dir(int)) # it lists all the dunder functions of integer

a= 100
a.__add__(5)
print(a)


class vt:
    # def __new__(cls): # helps in term of creating a new instance
    #     print("this is new")
        
    def __init__(self):
        print("this is init")
        self.phone=788
    
    def __str__(self):
        return "this is magic call of str"
    
v = vt()
print(v)
print(v.phone)