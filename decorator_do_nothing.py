from functools import wraps

def do_nothing(f):
    @wraps(f)
    def inner(*args, **kwargs):
        return f(*args, **kwargs)
    return inner

@do_nothing
def alpha(*args, **kwargs):
    #a function for viewing arguments
    print(f"args = {args}")
