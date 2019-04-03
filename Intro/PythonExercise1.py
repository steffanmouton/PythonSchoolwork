# Create two classes
## Zombie and Ninja
### THese two clases will be instantiated with health, power, name

# main loop will contain 5v5 combat involving a party of 5 Ninjas and a party of 5 Zombies
# loop will exit when a party has no "alive" members
# two classes should have the same method to call in the loop
## example: z = Zombie() n=Ninja() n.fight(z) z.fight(n)

import ZNclasses as ZN
import random

z1 = ZN.Zombie("Smoker", random.randint(50, 75), random.randint(10, 25))
z2 = ZN.Zombie("Witch", random.randint(50, 75), random.randint(10, 25))
z3 = ZN.Zombie("Jockey", random.randint(50, 75), random.randint(10, 25))
z4 = ZN.Zombie("Tank", random.randint(50, 75), random.randint(10, 25))
z5 = ZN.Zombie("Boomer", random.randint(50, 75), random.randint(10, 25))
zombies = [z1, z2, z3, z4, z5]

n1 = ZN.Ninja("Naruto", random.randint(50, 75), random.randint(10, 25))
n2 = ZN.Ninja("Hayabusa", random.randint(50, 75), random.randint(10, 25))
n3 = ZN.Ninja("Wolf", random.randint(50, 75), random.randint(10, 25))
n4 = ZN.Ninja("Raiden", random.randint(50, 75), random.randint(10, 25))
n5 = ZN.Ninja("Genji", random.randint(50, 75), random.randint(10, 25))
ninjas = [n1, n2, n3, n4, n5]

def check_deaths(zlist, nlist):
    for z in zlist:
        if z._health <= 0:
            zlist.remove(z)
    for n in nlist:
        if n._health <= 0:
            nlist.remove(n)


def battle(zlist, nlist):
    while zlist and nlist:
        for z, n in zip(zlist, nlist):
            z.fight(n)
            n.fight(z)
            check_deaths(zlist, nlist)

def show_victors(zlist, nlist):
    if zlist:
        print "========\nZombies Win!\n========"
        for z in zlist:
            print z._name, z._health
        return
        
    if nlist:
        print "========\nNinjas Win!\n========"
        for n in nlist:
            print n._name, n._health
        return

    print "========\nEveryone is dead!!\n========"

battle(zombies, ninjas)
show_victors(zombies, ninjas)