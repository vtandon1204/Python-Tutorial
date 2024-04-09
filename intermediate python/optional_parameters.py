def func(x=1): # deafault parameter = 1
    return x**2

call = func(5)
print(call)

def func1(word, add=5, freq=1): # freq is an optional paraemter
    print(word*(freq+add))

call1 = func1("vaibhav ")
print(call1)



class Car(object):
    def __init__(self, make, model, year, condition='New', kms=0):
        self.make= make
        self.model= model
        self.year= year
        self.condition= condition
        self.kms= kms
    
    def display(self, showAll=True):
        if showAll:
            print("this car is a %s %s from %s, it is %s and has %s kms"
                  %(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("this car is a %s %s from %s"
                  %(self.make, self.model, self.year))

audi = Car ('Audi', 'A7', 2022, 'New', 0)
audi.display(True)            
bmw = Car ('BMW', '24', 2023)
bmw.display()
bmw.display(False)
            
