class Point():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.coords=(self.x,self.y)

    def move(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,p):
        return Point(self.x+p.x, self.y+p.y)
    
    def __sub__(self,p):
        return Point(self.x-p.x, self.y-p.y)
    
    def __mul__(self,p):
        return self.x*p.x + self.y*p.y
    
    def __str__(self): # To represent in a meaningful mehtod 
        return "("+str(self.x)+','+str(self.y)+")"

    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)
    
    def __len__(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)
    
    def __gt__(self,p):
        return self.length() > p.length()
    def __ge__(self,p):
        return self.length() >= p.length()
    def __lt__(self,p):
        return self.length() < p.length()
    def __le__(self,p):
        return self.length() <= p.length()
    def __eq__(self,p):
        return self.x==p.x and self.y==p.y
    
p1= Point(3,4)
p2= Point(4,6)
p3= Point(2,7)
p4= Point(5,4)

p5=p1+p2
p6=p4-p1
p7=p2*p3

# print('vt' + '1204')
# p1+p2 # ERROR 
print(p5)
print(p6)
print(p7)

print(p1==p2)
print(p1>=p2)
print(p1>p2)
print(p1<=p2)
print(p1<p2)

len(p3)