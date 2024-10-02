#dictionary comprehensions
#dictionaries are key:value pairs

simple_dict = {
    "a" : 1,
    "b" : 2
}
#This multiplies the values by the 
#power of two 
my_dict = {key:value**2 for key, value in simple_dict.items()}
#This runs the power of two on the value
#then only returns the even ones
my_dict1 = {k:v**2 for k, v in simple_dict.items() 
    if v % 2 ==0}
#this makes the item is the key
#and the item *2 is the vauie
my_dict2 = {num:num*2 for num in [1,2,3]}

print(my_dict)
print(my_dict1)
print(my_dict2)