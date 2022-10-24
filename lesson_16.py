import random


class TestUnit:
    def get_test(self):
        return f"TEST"

    def __str__(self):
        return f"TEST__TEST"


class Unit:
    def __init__(self):
        self.health = 100

    def get_damage(self):
        self.health = random.randint(1, self.health)

    def health_me(self):
        self.health += 10
        self.health = 100 if self.health > 100 else self.health

    def __str__(self):
        return f"{self.health}"


class Warrior(TestUnit, Unit, ):
    def __init__(self):
        super().__init__()
        self.strength = 10

    def __str__(self):
        unit_str = super().__str__()
        return f"{unit_str} \nstrength: {self.strength}"


class Mage(Unit):
    def __init__(self):
        self.health = 10
        self.intelligence = 10

    def __str__(self):
        return f"{self.health} intelligence: {self.intelligence}"


gendalf = Mage()

gendalf.get_damage()
print(gendalf)
gendalf.health_me()
print(gendalf)
print(gendalf.get_test())

boromir = Warrior()
boromir.get_damage()
print(boromir)
boromir.health_me()
print(boromir)
