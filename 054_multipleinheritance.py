"""
multiple inheritance = inherit from more than one parent class
                        C(A, B)

multilevel inheritance = inherit from a parent which inherits from another parent
"""
class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This {self.name} is eating")
    def sleep(self):
        print(f"This {self.name} is sleeping")



class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("bugs")
hawk = Hawk("tony")
fish = Fish("nemo")

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()

rabbit.sleep()
hawk.eat()
fish.sleep()

print(fish.name)


