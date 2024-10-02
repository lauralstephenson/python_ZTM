#lambda function lambda param: func(param) 
# OR lambda param: action(param)
from functools import reduce

my_list = [1,2,3]

#lambda to multiply by 2
print(list(map(lambda item: item*2, my_list)))
print(my_list)
#lamda to filter
print(list(filter(lambda item: item % 2 !=0, my_list)))
#lambda to reduce
#notice we don't use list because this 
#returns only one number, not a list
print(reduce(lambda acc, item: acc + item, my_list))