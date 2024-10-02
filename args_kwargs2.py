#*args and **kwargs 2
#*args first, arguments
def add_items(*args):
    print(args)
    result = sum(args)
    print(result)
    
add_items(1,2,3)
add_items(3,4,5,6)
add_items()
add_items(2,3)
add_items(-2,-4,-5,-6,7.8)

#now **kwargs, keyword arguments
def add_items(*args, **kwargs):
    print(args, kwargs)
    result = sum(args)
    print(result)
k = 1
a = 3    
add_items(1,2,3, k*2, a*3)