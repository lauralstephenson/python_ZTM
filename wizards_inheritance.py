#Showing multiple inheritance
# Using our wizard game to explore OOP
# Users can be Wizards or Archers  or Ogres
# How do we make sure they are signed in first?
class User:
    # make sure the user is signed in
    def sign_in(self):
        print("Logged in!")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    # show polymorphism: same class, different outcomes
    def attack(self):
        print(f"Attacking with arrows! Arrows left- {self.num_arrows}")

    def run(self):
        print("Runs really fast!")
    
class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

wizard1 = Wizard("Merlin", 60)
archer1 = Archer("Robin", 30)

def player_attack(char):
    char.attack()

#multiple inheritance
hybrid1 = Hybrid("Borgie", 50, 22)
print(hybrid1.run())