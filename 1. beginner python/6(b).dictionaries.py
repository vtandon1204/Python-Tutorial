# Dictionary
# values are retreived using the keys (strings, number etc.) 
# whereas in lists, it is done by using the indices
# the order of values does not matter

d = {'vt':1212121212,
     'sd':3434343434,}

print(d['vt'])
print(d['sd'])

d['rt'] = 5656565656

print(d)

del d['vt']
print(d)

for key in d:
    print("key:",key)
    print('value:',d[key])
    
print('vt' in d)
print('rt' in d)

d.clear()
print(d)
