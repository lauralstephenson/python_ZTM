#Exploring OOP
class PlayerCharacter:
def __init__(self, name, age):
    self.name = name
    self.age = age
    
def speak(self):
    print(f"My name is {self.name}, and I am {self.age} years old.")
            
player1 = PlayerCharacter("andrei", 100)
player1.speak()

#using a dictionary instead of an object
player2 = {"name": "andrei", "age": 100}
print(player2["name"])
print(player2["age"])