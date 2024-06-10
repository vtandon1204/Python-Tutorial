# Metaclasses: defines the rules for a class 
# whereas a class defines the rules for an object and operations performed on it

def hello():
    class Hi:
        pass
    return Hi



class test:
    pass

print(test)
print(test())
print(type(test)) # defines about the type of the class

Test = type('Test',(),{"x":5}) # another way of creating a class
print(Test())
t = Test()
print(t.x)



class Foo:
    def show(self):
        print("hi")
   
def add_attribute(self):
    self.z=9     
Test = type('Test',(Foo,),{"x":5, "add_attribute":add_attribute})
t = Test()
t.add_attribute()
print(t.z)
