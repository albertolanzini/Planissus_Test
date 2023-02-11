import sys

#Carviz is our carnivore class.
#They are defined by Energy, Age, Lifetime and Social Attitude.

class Carviz:

    def __init__(self, energy, age, lifetime, socialattitude):
        self.energy = energy
        self.age = age
        self.lifetime = lifetime
        self.socialattitude = socialattitude

#Erbast is our herbivore class.
#They are defined by Energy, Age, Lifetime and Social Attitude.

class Erbast:

    def __init__(self, energy, age, lifetime, socialattitude):
        self.energy = energy
        self.age = age
        self.lifetime = lifetime
        self.socialattitude = socialattitude

with open(sys.argv[1], 'r') as my_file:
    Map = my_file.read()
    C = Map.splitlines()
    grid = []
