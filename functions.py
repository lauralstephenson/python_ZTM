#Functions

#define function
#default parameters
def say_hello(name = "Robot", emoji = "\U0001F916"):
  print(f"Hello there, {name} {emoji}!")

#call function
#arguments
say_hello("Laura", "\U0001f600")
say_hello("Dan", "\U0001F606")
say_hello("Emily", "\U0001F923")
say_hello()
#keyword arguments
#this is terrible practice
#don't do it
#say_hello(emoji = "\U0001f600", name = "Bibi")