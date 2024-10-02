# Using our wizard game to explore OOP
# Users can be Wizards or Archers  or Ogres
# How do we make sure they are signed in first?
class User:
    # make sure we have a user email
    def __init__(self, email):
        self.email = email

    # make sure the user is signed in
    def sign_in(self):
        print("Logged in!")


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    # show polymorphism: same class, different outcomes
    def attack(self):
        print(f"Attacking with arrows! Arrows left- {self.num_arrows}")


wizard1 = Wizard("Merlin", 60, "merlin@gmail.com")
archer1 = Archer("Robin", 30, "robin@yahoo.com")


def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)
print(wizard1.email)
#object introspection using dir()
print(dir(wizard1))
