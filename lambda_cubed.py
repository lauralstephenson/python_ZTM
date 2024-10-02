#Cube a Lambda
my_list = [5,4,3]

print(list(map(lambda item: item*item*item, my_list)))
print(my_list)

newList = sorted(a, key = lambda x: x[1], reverse = True)

#Sort a tupled list using lambda using ONLY THE SECOND TUPLE ELEMENT
a = [(0,2), (4.3), (10, -1), (9,9)]
a.sort(key=lambda x: x[1])
print(a)