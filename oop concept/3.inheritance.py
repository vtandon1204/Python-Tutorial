# class Dog(object):
#     def __init__(self, name, age):
        
#         self.name=name
#         self.age = age
#         # print('nice, you made a dog')

#     def speak(self):
#         print('hi i am', self.name,'and i am',self.age,'years old')
    
#     def talk(self):
#         print('Bark!')


# class Cat(Dog): # here Dog is the parent class of Cat class (child) 
#     # Cat class is inherited/derived from Dog class
#     # all the attributes and methos are inherited
#     def __init__(self, name, age, colour):
#         super().__init__(name,age) # name and age got added to Cat object from Dog class
#         self.colour= colour

#         # self.name='tech' #overwriting the name of Cat object as 'tech'

#     def talk(self): # overwriting the 'talk' method
#         print('Meow!')



# rt = Dog('rt',3)
# rt.speak()
# rt.talk()

# vt = Cat('vt',8,'black')
# vt.speak()
# vt.talk()


class Vehicle():
    def __init__(self, price, gas, colour):
        self.price=price
        self.gas=gas
        self.colour=colour

    def fillupTank(self):
        self.gas=100

    def emptyTank(self):
        self.gas=0

    def leftGas(self):
        return self.gas
    
class Car(Vehicle):
    def __init__(self, price, gas, colour, speed):
        super().__init__(price,gas,colour)
        self.speed=speed
    
    def beep(self):
        print('Beep!')

class Truck(Vehicle):
    def __init__(self, price, gas, colour, tires):
        super().__init__(price,gas,colour)
        self.tires=tires
    
    def beep(self):
        print('Honk!')