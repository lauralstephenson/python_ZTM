#Tuple An Immutable List
my_tuple = (1,2,3,4,5)
x = my_tuple[0]
y = my_tuple[1]
user = {
  "basket": [1,2,3],
  "greet": "Hello!",
  "age": 20
}
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])
print(5 in my_tuple)
print(user.items())
#Two Tuple Methods
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))