import collections
from collections import deque

d = deque("hello", maxlen=4)
# d.maxlen = 7
# attribute 'maxlen' of 'collections.deque' objects 
# is not writable
print(d)

d.append(5)
d.appendleft(10)
print(d)

d.pop()
d.popleft()
d.popleft()
print(d)

d.reverse()
print(d)

d.extend('2121')
print(d)

d.rotate(2)
print(d)
d.rotate(-3)
print(d)


d.clear()
print(d) 
