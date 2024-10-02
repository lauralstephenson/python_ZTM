#Dictionary Methods
user = {
  "basket": [1,2,3],
  "greet":"hello",
  "age":20
  }

user2 = dict(name="JohnJohn")
user3 = user.copy()
print(user3)
print(user.get("basket"))
print(user.get("age", 55))
print(user2)
print(user.update({"age":55}))
print(user.items())