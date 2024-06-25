# Object: specific instances of a class with common properties
# Class: abstraction of sum entity having set of properties and methods
import turtle
x = 4 # here 'x' is an instance of 'int' class
y = 'hello' # here 'y' is an instance of 'str' class
print(type(x))
print(type(y))
y.strip(print(y)) # remove leading and trailing whitespace (spaces, tabs, newlines) from a string. 

vt = turtle.Turtle()
# here we are creating a new instance of turtle object stored in 'vt' (Turtle is the class name)
print(y.upper()) #here, 'upper' is not a function but a method which is applied to class 'str' only
print(y.replace('l','t'))
def func(x):
    return x+1

print(func(4))