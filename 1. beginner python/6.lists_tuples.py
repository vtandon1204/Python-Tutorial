# LISTS: collection of same/different datatypes
fruits = ['apple', 'pear', 3]
print(fruits)

# printing single element of list
print(fruits[1])
for i in range(0,3):
    print(fruits[i])

print(fruits[0:2]) # 2 index is not included
print(fruits[-1]) # 1st index but from the last

# change the existing element of the list
fruits[1] = 'orange'
print(fruits)

# add an element to the list
fruits.append('banana') # append() will add the element to the end of the list
print(fruits)

# inserting an element at a position
fruits.insert(2,'peanuts')
print(fruits)

# TUPLES: used for coordinates
position = (2,3)
color = (255,255,255)
print(type(color))