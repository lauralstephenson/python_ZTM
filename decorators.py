# Decorator Pattern
# this one has an argument
#def my_decorator(func):
    
    #def wrap_func(x):
     #   print("*********")
      #  func(x)
       # print("*********")

    
    #return wrap_func

#now using *args and **kwargs
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("*********")
        func(*args, **kwargs)
        print("*********")

    return wrap_func
# the argument is in the def and pring
@my_decorator
def hello(greeting, emoji =':)'):
    print(greeting, emoji)


@my_decorator
def bye(greeting):
    print(greeting)


hello("Hi!")
bye("See ya later!")
