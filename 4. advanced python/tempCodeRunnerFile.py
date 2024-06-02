
class vt:
    def __new__(cls): # helps in term of creating a new instance
        print("this is new")
        
    def __init__(self):
        print("this is init")
        self.phone=788
    
    def __str__(self):
        return "this is magic call of str"
    
v = vt()
print(v)