# LISTS: collection of same/different datatypes
item1 = ['apple', 'pear', 3]
print(item1)

# printing single element of list
print(item1[1])
for i in range(0,3):
    print(item1[i])

print(item1[0:2]) # 2 index is not included
print(item1[-1]) # 1st index but from the last

# change the existing element of the list
item1[1] = 'orange'
print(item1)

# add an element to the list
item1.append('banana') # append() will add the element to the end of the list
print(item1)

# inserting an element at a position
item1.insert(2,'peanuts')
print(item1)

# combining two or more lists
item2 = ['shoes','watch','toys']
print(item2)

items = item1+item2
print(items)
print(len(items)) 

print('shoes' in items)
print('soda' in items)
