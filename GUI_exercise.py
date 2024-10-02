#Our First GUI Exercise
picture = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]

#iterate over picture
for row in picture:
  #change all the 1's to *
  for pixel in row:
    if (pixel == 1):
      print("*", end=" ")
#change all the 0's to ""
    else:
      print(" ", end=" ")
  print(" ")

#Cleaner code
#iterate over picture
for row in picture:
  #change all the 1's to *
  fill = "*"
  empty = " "
  for pixel in row:
    if pixel:
      print(fill, end=" ")
#change all the 0's to ""
    else:
      print(empty, end=" ")
  print(" ")
