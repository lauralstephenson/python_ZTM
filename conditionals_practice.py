#Conditionals
is_old = False
is_licensed = True

#Change the True and False for different results
if is_old and is_licensed:
  print("You are old enough to drive, and you have a license!")

elif is_licensed:
  print("You are licensed to drive!")
else:
  print("You're not old enough to drive!")