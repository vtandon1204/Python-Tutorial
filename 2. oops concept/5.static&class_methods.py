class Dog:
    dogs=[] # class variable

    def __init__(self, name):
        self.name=name
        self.dogs.append(self)

    @classmethod # decorators
    def num_dogs(cls): # cls means the name of the class
            return len(cls.dogs)
        
    @staticmethod # dont need the class to call them
    # we pass only the parameters we use
    def bark(n):
            #barks n times
            for i in range(n):
                print('Bark!')
    
class Math:
      @staticmethod
      def add(x, x2):
            return x+x2
      
tomy = Dog("Tomy")
bruno = Dog("Bruno")

print(Dog.dogs)
print(tomy.dogs)

print(Dog.num_dogs())

Dog.bark(6)

