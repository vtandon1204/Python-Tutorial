# Map Function
li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

# Ques. Apply this function to every element of the list and store the result in a new list
# Method_1 (using basics)
newList = []
for x in li:
    newList.append(func(x))

print(newList)

# Method_2 (using map function)
# Map function takes 2 parameters: Function & List
# it applies the function to every element of the list
print(list(map(func,li))) # here, list is the keyword (in green color) & 'li' is the list we are using (in blue color).

# Method_3
print([func(x) for x in li if x%2==0])