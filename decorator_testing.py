#Decorator Testing Module
from time import time
def performance(func):
    def wrapper(*args, **kwargs):
        #testing how long it takes to
        #run a function
        #tests performance
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        #prints the time in milliseconds
        print(f"took {t2-t1} ms")
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000):
        i*5

long_time()