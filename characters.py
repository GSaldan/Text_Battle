from health_bar import HealthBar


class Character:
    def __init__(self, name: str, health: int, defense: int, atk: int, max_health: int):
        self.weapon = None
        self.name = name
        self.health = health
        self.defense = defense
        self.atk = atk
        self.max_health = max_health

    def attack(self, target) -> None:
        target.health = target.health + target.defense - self.atk - self.weapon.atk
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f'{self.name} attacked {target.name}\n{target.name} took {self.atk + self.weapon.atk - target.defense} '
              f'damage')


# ----- CHARACTER SUBCLASSES ----- #
class Warrior(Character):
    def __init__(self, name: str, health: int, defense: int, atk: int, max_health: int, weapon):
        super().__init__(name=name, health=health, defense=defense, atk=atk, max_health=max_health)
        self.weapon = weapon
        # Change the color parameter to change health bar color and length to make it bigger or smaller
        self.health_bar = HealthBar(self, color='blue', length=30)

    # Weapon equip
    def equip_weapon(self, weapon) -> None:
        self.weapon = weapon
        print(f'{self.name} equipped {weapon.name}.')


class Orc(Character):
    def __init__(self, name: str, health: int, defense: int, atk: int, max_health: int, weapon):
        super().__init__(name=name, health=health, defense=defense, atk=atk, max_health=max_health)
        self.weapon = weapon
        # Change the color parameter to change health bar color and length to make it bigger or smaller
        self.health_bar = HealthBar(self, color='red', length=30)

    # Weapon equip
    def equip_weapon(self, weapon) -> None:
        self.weapon = weapon
        print(f'{self.name} equipped {weapon.name}.')
