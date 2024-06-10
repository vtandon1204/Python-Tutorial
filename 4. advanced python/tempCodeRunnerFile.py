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