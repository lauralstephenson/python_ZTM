# List Comprehensions
# list, set, dictionary

# The normal way to create a list
my_list = []

for char in "hello":
    my_list.append(char)

print(my_list)

# [param for param in iterable]
my_list1 = [char for char in "hello"]
my_list2 = [num for num in range(0, 100)]
# this one multiplies all numbers by 5
my_list3 = [num * 5 for num in range(0, 100)]
# this one returns only the even nubmers
my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]

print(my_list1)
print(my_list2)
print(my_list3)
print(my_list4)