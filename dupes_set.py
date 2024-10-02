#Exercise: Check for duplicates in list using set:
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
#find the length of the list
print(len(some_list))
#create a new set (no dupes in sets) from the list
my_set = set(some_list)
#check for duplicates between lists
print(len(my_set))
#compare lengths and print if list contains dupes
if len(some_list) != len(my_set):
  print("Duplicates found  in list!")

else:
  print("No duplicates found in list!")