import os
from characters import Warrior, Orc
from weapons import sword, punch, short_bow, knife, fire_ball

# Instructions: Choose the attributes of the fighters and type the commands to create an epic text battle!

# ----- COMMANDS ----- #
# .attack(target) - .health_bar.draw() - .equip_weapon(weapon) - .health_bar.update()

# ----- WEAPONS ----- #
# sword, punch, short_bow, knife, fire_ball

# Warrior and orc attributes
warrior = Warrior(name='Warrior', health=120, defense=5, atk=10, max_health=150, weapon=punch)
orc = Orc(name='Orc', health=130, defense=2, atk=12, max_health=150, weapon=punch)

# ----- MAIN GAME LOOP ----- #
while warrior.health and orc.health > 0:
    # Clean the console after every loop to keep it clean
    os.system('cls')

    # Attack command and health bar
    warrior.attack(orc)
    orc.health_bar.draw()

    orc.attack(warrior)
    warrior.health_bar.draw()

    input()

else:
    print(f'The {warrior.name} have {warrior.health} Health left!\n'
          f'and the {orc.name} have {orc.health} health left!')
    print('GAME OVER!')
