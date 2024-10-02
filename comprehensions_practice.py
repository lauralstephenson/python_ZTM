#Practicing comprehensions
nums = [1,2,3,4,5,6,7,8,9,10]

# want "n" for each "n" in nums
my_list = []
for n in nums:
  my_list.append(n)
print(my_list)
#copy using the list comprehension method
my_list = [n for n in nums]
print(my_list)

# want "n*n" for each "n" in nums
my_list1 = []
for n in nums:
  my_list1.append(n*n)
print(my_list1)
#exponents using the list comprehension method
my_list2 = [n*n for n in nums]
print(my_list2)

#want "n" for each "n" in nums if "n" is even
my_list3 = []
for n in nums:
  if n % 2 == 0:
    my_list3.append(n)
print(my_list3)
#even numbers using the list comprehension method
my_list4 = [n for n in nums if n % 2 == 0]
print(my_list4)

#want "n" for each "n" in nums if "n" is odd
my_list5 = []
for n in nums:
  if n % 2 == 1:
    my_list5.append(n)
print(my_list5)
#odd numbers using the list comprehension method
my_list6 = [n for n in nums if n % 2 == 1]
print(my_list6)

#using a map + lambda
my_list7 = list(map(lambda n: n*n, nums))
print(my_list7)

#using a filter + lambda
my_list8 = list(filter(lambda n: n%2 ==0, nums))
print(my_list8)

#I want a letter, number pair for each letter in "abcd" and each number in "0123"
my_list9 = []
for letter in "abcd":
  for number in "0123":
    my_list9.append((letter, number))
print(my_list9)

#nested for loops in list comprehension
my_list10 = [(letter, num) for letter in "abcd" for num in range(4)]
print(my_list10)


#Dictionary Comprehensions
names= ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heroes = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]

#Dict for names and heroes for each name, hero in zip(names, heroes)
my_dict = {}
for name, hero in zip(names, heroes):
  my_dict[name] = hero
print(my_dict)
#using data comprehensions and zip while leaving off Peter's name
my_dict1 = {name: hero for name, hero in zip (names, heroes) if name != "Peter"}
print(my_dict1)