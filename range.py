#Range

#prints the range
print(range(100))

#prints all the numbers in the range
#this tells your loop how many time to run
for number in range(0,100):
  print(number)

#sends an emai 10 times
for number in range(0,10):
  print("email email list")

#sends an emai 10 times with no variable using _
for _ in range(0,10):
  print(_)

#uses the third parameter to jump per the number
for _ in range(0, 10, 2):
  print(_)

#counts backwards from 10 by 2s
for _ in range(10, 0, -2):
  print(_)

for _ in range(2):
  print(list(range(10)))