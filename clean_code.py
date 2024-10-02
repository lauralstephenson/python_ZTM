#Wordy Code example
def is_even1(num):
  if num % 2 == 0:
    return True
  elif num % 2 != 0:
    return False

print(is_even1(50))
print(is_even1(5))

#Clean Code example
def is_even(num):
  return num % 2 == 0

print(is_even(50))
print(is_even(5))
