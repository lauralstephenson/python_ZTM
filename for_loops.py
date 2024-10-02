#For loops

#Prints each letter in a string
for item in "Zero to Mastery":
  print(item)

#Prints each item in a list
for items in [1,2,3,4,5]:
  print(items)

#Prints each item in a set
for set_items in {1,2,3,4,5}:
  print(set_items)

#Prints each item in a tuple
for tuple_items in [1,2,3,4,5]:
  print(tuple_items)

#Prints iems from a tuple and an item from a list together
for itemx in (1,2,3,4,5):
  for x in [
           "a", 
           "b", 
           "c"]:
    print(itemx, x)