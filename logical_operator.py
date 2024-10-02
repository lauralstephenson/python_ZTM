#Logical Operator
is_magician = False
is_expert = True

#check of magician and expert are true
#if both are true, print "You are a master magician!"
if is_magician and is_expert:
  print("You are a master magician!")

#check if magician but not expert is true
#if both are true, print "At least you're getting there!"
elif is_magician and not is_expert:
  print("At least you're getting there!")

#check if not magician. 
#if not magician, print "You need magic powers!"
elif not is_magician:
  print("You need magic powers!")