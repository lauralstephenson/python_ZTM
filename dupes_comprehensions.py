#Exercise: Check for duplicates in list creating new and dupe lists using count and append
#Exercise Append: Use Comprehensions
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
#making a blank list
duplicates = []
duplicates1 = []
#making a list that appends anything that is repeated in the list, so this is WITHOUT dupes
[duplicates.append(item) for item in some_list if item not in duplicates] 
#an alternate way of doing this using count--same # of items, no dupes
#sets don't have duplicates! So this is a list OF THE DUPES
duplicates1 = list(set([item for item in some_list if some_list.count(item) > 1]))
#print as a string
print(str(duplicates))
print(str(duplicates1))