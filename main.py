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
    def __init__(self, name: str, health: int):
        self.name = name
        self._health = health

    def is_alive(self) -> bool:
        return self._health > 0

    def heal(self, amount: int):
        self._health += amount
        print(
            f"✨ {self.name}'s health increased by {amount}! Remaining health: {self._health}")

    def take_damage(self, amount: int):
        # prevent health from going into negative numbers
        self._health = max(0, self._health - amount)

        if self._health == 0:
            print(f"💀 {self.name} has been taken down on the battlefield!")
        else:
            print(
                f"💥 {self.name} took {amount} damage! Remaining health: {self._health}")

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


class Healer(Character):
    def attack(self, target: list[Character]):
        amount = randint(10, 20)
        for hero in target:
            if hero.is_alive():
                print(f"🌿 {self.name} casts a healing spell on {hero.name}!")
                hero.heal(amount)


class Villain(Character):
    def __init__(self, name: str, health: int):
        super().__init__(name, health)
        self.rounds = 0

    def attack(self, heroes: list[Character]):
        damage = randint(10, 30)
        self.rounds += 1

        if self.rounds % 3 == 0:
            print(f"🌋 {self.name} uses SUPERPOWER SLAM on all heroes!")
            damage += 20
        else:
            print(f"🪨 {self.name} attacks the heroes!")

        for hero in heroes:
            if hero.is_alive():
                hero.take_damage(damage)


# --- Game Execution ---
if __name__ == "__main__":
    arthur = Knight(name="Arthur", health=100)
    merlin = Wizard(name="Merlin", health=80)
    elena = Healer(name="Elena", health=60)
    golem = Villain(name="Golem", health=200)

    heroes_team = [arthur, merlin, elena]
    print("--- Battle Start ---")

    rounds = 0

    # Pythonic condition: Loop while Golem is alive AND at least one hero is alive
    while golem.is_alive() and any(hero.is_alive() for hero in heroes_team):
        print(f"\n--- Round {rounds + 1} ---")

        # 1. Heroes' Turn
        if arthur.is_alive():
            arthur.attack(golem)

        if merlin.is_alive():
            merlin.attack(golem)

        if elena.is_alive():
            if rounds % 2 == 0:
                elena.attack(heroes_team)
            else:
                print(f"⏳ {elena.name} is charging her spell this round.")

        # 2. Check if the Golem died from the heroes' attacks
        if not golem.is_alive():
            print("\n🏆 Heroes win! The golem has been defeated!")
            break

        # 3. Villain's Turn (Only happens if Golem survived step 2)
        golem.attack(heroes_team)

        # 4. Check if all heroes died from the Golem's attack
        if not any(hero.is_alive() for hero in heroes_team):
            print("\n☠️ Golem wins! All heroes have been defeated!")
            break

        rounds += 1

    print("--- Battle End ---")
