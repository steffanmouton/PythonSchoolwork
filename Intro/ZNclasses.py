# Create two classes
## Zombie and Ninja
### THese two clases will be instantiated with health, power, name

# main loop will contain 5v5 combat involving a party of 5 Ninjas and a party of 5 Zombies
# loop will exit when a party has no "alive" members
# two classes should have the same method to call in the loop
## example: z = Zombie() n=Ninja() n.fight(z) z.fight(n)

class Zombie:
    def __init__(self, name, hp, pwr):
        self._name = name
        self._health = hp
        self._power = pwr
    
    def fight(self, target):
        target.take_damage(self._power)

    def take_damage(self, dmg):
        self._health -= dmg

class Ninja:
    def __init__(self, name, hp, pwr):
        self._name = name
        self._health = hp
        self._power = pwr
    
    def fight(self, target):
        target.take_damage(self._power)

    def take_damage(self, dmg):
        self._health -= dmg


