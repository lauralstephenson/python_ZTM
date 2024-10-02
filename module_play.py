from collections import Counter, defaultdict, OrderedDict

# this keeps a dictionary of how many times
# a thing in a dictionary occurred the most
li = [1, 2, 3, 4, 5, 6, 7]
print(Counter(li))

# turning a list into a counter is a very
# useful thing to do in coding
# helps with optimization problems
# example, counting duplicate emails
sentence = "blah blah blah thinking aboaut Python"
print(Counter(li))
print(Counter(sentence))

# allows us to access a key and gives it a
# default value
# the lambda lets us tell the user the
# item they are looking for does not exist
dictionary = defaultdict(lambda: "Does not exist!", {"a": 1, "b": 2})
print(dictionary["c"])

# no longer need to use OrderedDict
# as of Python 3.7
d = OrderedDict()
d["a"] = 1
d["b"] = 2

d2 = OrderedDict()
d2["a"] = 1
d2["b"] = 2

print(d2 == d)
