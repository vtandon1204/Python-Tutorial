# Compiler: higher level of code to lower level (byte) code conversion
# Interpreter: takes some code (byte) and interpret it to run on the machine

class Dog:
    def __init__(self):
        self.bark()
        # here self.bark() is not defined and only called

# but in python, the compiler will only convert this code into byte code
# and not check whether it's valid or not
# this is because most of the code is run at the run-time and not at compile-time

def make_class(x):
    class Dog:
        def __init__(self, name):
            self.name = name
        
        def print_value(self):
            print(x)
    return Dog

cls = make_class(10)
d = cls("vt")
print(d.name)
d.print_value()
# print(cls) 

for i in range(10):
    def show():
        print(i*2)
        
show()


import inspect
from queue import Queue
def func(x):
    if x == 1:
        def rv():
            print("x is equal to 1")
    else:
        def rv():
            print("x is not equal to 1")
    
    return rv

new_func = func(1)
new_func()

print(id(new_func))
print(inspect.getsource(new_func))
print(inspect.getsource(Queue))