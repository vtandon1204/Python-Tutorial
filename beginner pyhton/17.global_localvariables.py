#  Globo & Loco variable
var = 9 # global varibale
loop = True
newVar = 23
def func(x):
    newVar = 7 # local variable to the function 'func'
    print(newVar)
    if x == 5:
        return newVar
    
def func1():
    newVar = 5
    print(var) # var is a global variable
    print(newVar)

def func2():
    # newVar = 5
    loop = False
    print(loop)
    print(newVar)
# Note: --> if a local variable is not defined in the function then code will consider the global variable.
#       --> local varibales are generally defined inside the function

func(3)
func(var)
func(5)
func1()
func2()
# print(newVar) # it will throw an error as newVar is declared int he scope of 'func' function only

# If we want to change the value of global variable from inside a function, we need to use the global keyword
def func3(x):
    global loop

    loop = 434

    if x == 5:
        return newVar

func3(2)
print(loop)