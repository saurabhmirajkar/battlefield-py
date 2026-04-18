"""
Battlefield

A simple battle video game in python

heroes : knight, wizard, healer

powers / attacks :
- a knight uses sword
- a wizard uses fireball
- a healer uses spell to heal a specific hero

villain: golem 
- a golem automatically uses its super-power "slam" after 3 turns

game conclusion:
- when either all heroes or golem healh becomes 0
"""

from random import randint


class Character:

    name: str
    _health: int

    def __init__(self, name, health):
        self.name = name
        self._health = health

    def get_health(self) -> int:
        return self._health

    # def heal(self, amount, target):
    #     target._health += amount
    #     print(
    #         f"{self.name} health increased by {amount}! Remaining health is {self._health}")

    def take_damage(self, amount: int):
        self._health -= amount
        if self._health < 0:
            self._health = 0

        if self._health == 0:
            print(f"{self.name} has taken down in the field!")
        else:
            print(
                f"{self.name} took damage of {amount} damage! Remaining health is {self._health}")

    def attack(self, target):
        pass


class Knight(Character):

    def attack(self, target: Character):
        damage = randint(10, 25)
        print(f"⚔️ {self.name} swings a heavy broadsword at {target.name}!")
        target.take_damage(damage)


class Wizard(Character):

    def attack(self, target: Character):
        damage = randint(10, 25)
        print(f"🔥 {self.name} casts a blazing fireball at {target.name}!")
        target.take_damage(damage)


# class Healer(Character):

#     def attack(self, target):
#         amount = randint(10,20)
#         target.heal(amount, target)


class Villain(Character):

    def attack(self, target1, target2):
        damage = randint(10, 50)
        print(f"🔥 {self.name} uses superpower slam at heroes!")
        target1.take_damage(damage)
        target2.take_damage(damage)


arthur = Knight(name="Arthur", health=100)
merlin = Wizard(name="Merlin", health=80)
golem = Villain(name="Golem", health=200)

print("--- Battle Start ---")

print("--- Round 1 ---")
arthur.attack(golem)
merlin.attack(golem)
golem.attack(arthur, merlin)

print("--- Round 2 ---")
arthur.attack(golem)
merlin.attack(golem)
golem.attack(arthur, merlin)

print("--- Round 3 ---")
arthur.attack(golem)
merlin.attack(golem)
golem.attack(arthur, merlin)
