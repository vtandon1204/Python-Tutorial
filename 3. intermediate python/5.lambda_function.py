# normal function
def func(x):
    return x+5
print(func(2))

# lambda function
func2 = lambda x: x+5
print(func2(9))

# lambda function in a normal function
def func3(x):
    func4 = lambda x: x+5
    return func4(x) + 30
print(func3(10))

# lambda function with multiple parameters & optional parameters
func5 = lambda x,y=4: x+y
print(func5(30))
print(func5(2,2))


# lambda function with map & filter function
a = [1,2,3,4,5,6,7,8,9,10]
newList = list(map(lambda x: x+5,a)) # this creates a list with every element increased by 5
list2 = list(filter(lambda x: x%2==0,a))
print(newList)
print(list2)