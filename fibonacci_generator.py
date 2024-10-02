#Creating a Fibonacci sequence
#Using generators
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        #storing it temporarily with temp
        #makes it run faster
        temp = a
        a = b
        b = temp + b

for x in fib(21):
    print(x)