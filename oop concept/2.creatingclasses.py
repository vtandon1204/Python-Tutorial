class Human(object):
# Methods: something we create using def in the class (functions of class)
# Attributes: like variables that belong to a certian object; a 'self' keyword is used to create it 
    def __init__(self, name,age):
        # 'self' represents the instance of class, you are calling to
        self.name=name
        self.age = age
        print('nice, you made a dog')

    def speak(self):
        print('hi i am', self.name,'and i am',self.age,'years old')
    
    def change_age(self,age):
        self.age = age
    
    def add_weight(self,weight):
        self.weight = weight

vt = Human('vt',20) # 'vt' is an instance of type Dog
# vt.__init__ # no need to call it here, it automatically does
rt = Human('rt',46)
vt.speak()
rt.speak()
vt.change_age(3)
vt.add_weight(65)
print(vt.age)
print(vt.weight)