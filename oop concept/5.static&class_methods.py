class Dog:
    dogs=[] # class variable

    def __init__(self, name):
        self.name=name
        self.dogs.append(self)

    @classmethod # decorators
    def num_dogs(cls):     
            return len(cls.dogs)
        
    @staticmethod 
    def bark(n):
            #barks n times

            for _ in range(n):
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

