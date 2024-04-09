# Static & Class Methods
class person(object):
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def getPopulation(cls): # class method: it can be called in any instance of the class.
        # you dont need to have an object related to that class
        return cls.population
    
    @staticmethod
    def isAdult(age): # static method: it can be called without creating any object of that class.
        # it is used when you dont need 'self' or actual object for that class
        # it cannot access the class variables as it doesn't have acess to the class name
        # it can only access the varibales that you pass in the parameter list
        return age>=18
    
    def display(self):
        print(self.name, 'is', self.age, 'years old')
    
person1 = person('vaibhav', 20)

print(person.getPopulation()) # no object needed