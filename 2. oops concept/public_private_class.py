class _Private: # can only be used inside the same file / same scope
    def __init__ (self, name):
        self.name= name
    
class NotPrivate: # can be accessed anywhere
    def __init__ (self, name):
        self.name = name 
        self.priv = _Private(name)

    def _display(self): # private because of the starting '_'
        print("Hello")

    def display(self):
        print("Hi")

# Note: In Python, there is no such terms like Public and Private Classes
#       It is only the convention that are used to declare pseudo, private or public class
