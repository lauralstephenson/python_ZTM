import random
#can also import one thing, like:
# the module
#from random import choice

#can also give an alias to the imported file
#to prevent name collisions
#import random as thenumbers

#this prints the help file as a readme
#for this module
#print(help(random))

#this prints the module's directory to
#see what tools are available
#print(dir(random))

#this runs the random file to give 
#a random number between zero and one
print(random.random())
#gives a random integer between two integers
print(random.randint(1,10))
#pivot between a choice
print(random.choice([1,2,3,4,5]))
#shuffle among numbers
my_list = [1,2,3,4,5]
(random.shuffle(my_list))
print(my_list)