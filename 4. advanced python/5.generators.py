# Generators : generates every outcome continously without holding it in a memory
# --> optimisation of memory consumption

def test_fib(n):
    a,b =0,1
    for i in range(n):
        yield a # 'yield' is keyword used to make generator function
        a,b=b,a+b
        
test_fib(10)
        
for i in test_fib(10):
    print(i)


def test_fib1():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
fib = test_fib1() # object for the function (used as an iterator)
for i in range (10):
    print(next(fib))
    
    