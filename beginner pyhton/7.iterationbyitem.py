fruits = ['apple', 'pears', 'strawberries',3,64,2]
for fruit in fruits:
#    print(fruit) # iterating by item and not by indices
    if fruit == 'pears':
        print(fruit)
    else:
        print('not pears')
    
# for i in range (0,6):
for i in range(len(fruits)):
    if fruits[i] == 'pears': # iterating by indices
        print(fruits[i])
    else:
        print('not pears')