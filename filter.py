#filter(function_name, data)

def multiply_by2(item):
  return item*2

def only_odd(item):
  return item % 2 != 0

print(list(filter(only_odd, [1,2,3])))