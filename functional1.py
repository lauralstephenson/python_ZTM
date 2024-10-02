from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ["sisi", "bibi", "titi", "carla"]


# capitalizing my_pets
def capitalize(string):
    # printing the capitalized list
    return string.upper()


print(list(map(capitalize, my_pets)))

# 2 Zip the 2 lists into a list of tuples,
# but sort the numbers from lowest to highest.
my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5, 4, 3, 2, 1]

# zipping the list together and sorting
print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


# returning only scores over 50
def only_over_50(score):
    return score > 50


# printing the list using filter
print(list(filter(only_over_50, scores)))

# 4 Combine all of the numbers that are in a
# list on this file
# using reduce (my_numbers and scores).
# What is the total?


# create the combined list
def accumulator(acc, item):
    return acc + item


# print the combined list
print(reduce(accumulator, (my_numbers + scores)))
