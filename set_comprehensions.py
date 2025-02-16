# Set Comprehensions
# Sets do NOT allow duplicates
# [param for param in iterable]
my_set1 = {char for char in "hello"}
my_set2 = {num for num in range(0, 100)}
# this one multiplies all numbers by 5
my_set3 = {num * 5 for num in range(0, 100)}
# this one returns only the even nubmers
my_set4 = {num**2 for num in range(0, 100) if num % 2 == 0}

print(my_set1)
print(my_set2)
print(my_set3)
print(my_set4)