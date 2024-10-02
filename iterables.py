#Looping over dictionaries

user = {
  "name": "Golllum", 
  "age": 5006, 
  "can_swim": False
}

#Prints the key value pairs
for item in user.items():
  print(item)

#or do it this way
#for item in user.items():
  #key, value = item;
  #print(key, value)

#even better to do it this way
for key, value in user.items():
  print(key, value)

#Prints the values
for item in user.values():
  print(item)

#Prints the keys
for item in user.keys():
  print(item)