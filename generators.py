#generators
def generator_function(num):
    for i in range(num):
        yield i*2

g = generator_function(100)
#call next to iterate
next(g)
next(g)
print(next(g))

#Use yield instead        
#def make_list(num):
    #result = []
    #for i in range(num):
     #   result.append(i*2)
    #return(result)
#don't do this...use yield
#my_list = make_list(100)

#print(my_list)