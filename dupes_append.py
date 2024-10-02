#Exercise: Check for duplicates in list creating new and dupe lists using append:
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
#empty list to hold unique elements from list
new_list = []
#empty list to hold dupes
dupe_list = []
#iterate over list
for item in some_list:
  #if item is not in new_list, add it to new_list
  if item not in new_list:
    new_list.append(item)
  #if item is in new_list, add it to dupe_list
  else:
    dupe_list.append(item)
#print new_list
print(new_list)
#print dupe_list
print(dupe_list)