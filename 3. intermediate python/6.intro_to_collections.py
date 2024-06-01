import collections 
# data types/object which can store multiple objects 
from collections import Counter

# Containers
# list 
# set
# dict
# tuple - inmutable

#Types
# 1. counter 
# 2. deque
# 3. namedTuple()
# 4. orderedDict
# 5. defaultdict

a = Counter('gallad') #string as argument
print(a)
b = Counter(['a','b','c','c']) #list as argument
print(b)
c = Counter({'a':1, 'b':2}) #dict as argument
print(c)
d = Counter(cats=4, dogs=7)
print(d)
print(d['cats'])
print(d['pets'])

print(list(a.elements()))
print(list(b.elements()))
print(list(c.elements()))
print(list(d.elements()))


print(a.most_common(2))
print(b.most_common(2))
print(c.most_common(2))
print(d.most_common(2))


e = Counter(a=4,b=2,c=0,d=-2)
f = ['a','b','b','c']
e.subtract(f)
print(e)

e.update(f)
print(e)
e.update(f)
print(e)

e.clear()
print(e) 

g = Counter(a=4,b=2,c=0,d=-2)
h = Counter(['a','b','b','c'])
print(g+h)
print(g-h) # if element count <=0 , it will not be shown
print(g & h) # min element count
print(g | h) # max element count
