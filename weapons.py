class Weapon:
    def __init__(self, name: str, weapon_type: str, atk: int, value: int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.atk = atk
        self.value = value


punch = Weapon(name='Punch', weapon_type='Blunder', atk=2, value=0)
sword = Weapon(name='Sword', weapon_type='Sharp', atk=5, value=10)
knife = Weapon(name='Knife', weapon_type='Sharp', atk=3, value=5)
short_bow = Weapon(name='Short Bow', weapon_type='Ranged', atk=4, value=9)
fire_ball = Weapon(name='Fire Ball', weapon_type='Magic', atk=7, value=15)