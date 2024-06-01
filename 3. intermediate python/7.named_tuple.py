import collections
from collections import namedtuple

Point = namedtuple('Point','x y z')
# Point is the name of object which is a namedtuple and 'x y z' are it's fields

newP = Point(3,4,5) # consider Point as a Class
print(newP)

Point1 = namedtuple('Point_1', {'x':0, 'y':0, 'z':0})
p1 = Point1(1,2,3)
print(p1)
print(p1.x,p1.y,p1.z)
print(p1[0])
print(newP._asdict())
print(newP._fields)

p2 = newP._replace(y=9)
print(p2)

p3 = Point._make(['a','b','c'])
print(p3)