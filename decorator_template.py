#A nested decorator template
def decorator_demo(func):
    def inner_function(*args, **kwargs):
        #write code
    return inner_function

@decorator_demo
def f(x):
    #some code