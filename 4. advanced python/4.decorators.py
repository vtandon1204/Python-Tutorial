# Decorators: modify the behaviour of a function 

def test():
    print("start of function")
    print("this is my function to test")
    print(3+4)
    print("end of function")

test()
#*************************************************
def decorate(func):
    def inner_dec():
       print("start of function")
       func()
       print("end of function")
    return inner_dec

@decorate
def test1():
    print(3+5)

test1()

#****************************************************
import time

def timer_test(func):
    def inner_test_timer():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return inner_test_timer

@timer_test
def test2():
    print(4+21)

test2()

@timer_test
def test3():
    for i in range(2318924):
        pass

test3()