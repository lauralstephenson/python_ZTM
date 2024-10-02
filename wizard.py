# OOP
# silly Harry Potter type game
class PlayerCharacter:  # Class
    # code
    #class object attribute
    membership = True
    def __init__(self, name="anonymous", age=0):  # name is a parameter
        if (age > 18):
            self.name = name  # this is a method
            self.age = age

def run(self):
    print("run")

#now we're adding a @classmethod
@classmethod
def adding_things(cls, num1, num2):
    return cls("Teddy", num1 + num2)

#now we're using the @staticmethod
def adding_things2(num1, num2):
    return num1 + num2

#now we're instantiating the @classmethod
player3 = PlayerCharacter.adding_things(2,3)
print(player3)
# now we're instantiating self as
# our first player
player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tom", 21)

print(player1.name)
print(player1.age)
print(player2.name)
print(player2.age)