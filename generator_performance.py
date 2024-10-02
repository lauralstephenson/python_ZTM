#Generator Performance
from time import time

def performance(fn):
    
@performance
def long_time:
    print("1")
#using a generator like range means
#it is only holding one number
#at a time in memory for 
#better performance
    for i in range(1000000):
        i*5
        
@performance
def long_time2():
    print("2")
    for i in list(range(100000)):
        i*5
        
long_time()
long_time2()