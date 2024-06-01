# Filter Function
def add7(x):
    return x+7

def isOdd(x):
    return x%2!=0

a = [1,2,3,4,5,6,7,8,9,10]
b = list(filter(isOdd,a))
c = list(map(add7,b)) # using map function along with filter function
# this 'c' list will take out the odd numbers (given by filter function in b)
# and add 7 to them (given by map function)
print(b)
print(c)
