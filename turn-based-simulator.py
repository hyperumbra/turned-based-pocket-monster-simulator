# Import Libraries and Methods
import abc
import time
from random import randint
from enum import Enum

DamageTypes = Enum("DamageTypes", "Damaging")
Types = Enum("Types", "ELECTRIC NORMAL FLYING")


# creates an abstract base class to be instantiated through the attacks
# base class defines the possible properties that can be set for the attacks
class attack(metaclass=abc.ABCMeta):
    # base property for the type of damage the attack implements
    @abc.abstractproperty
    def damage_type(self):
        return NotImplemented

    # base propert for the typing of the attack for damage calculations
    @abc.abstractproperty
    def move_type(self):
        return NotImplemented


# create class for the attack Slam
class Slam(attack):
    # returns value of a damaging attack
    @property
    def damage_type(self):
        return DamageTypes.Damaging

    # NORMAL type attack
    @property
    def move_type(self):
        return Types.NORMAL


# create class for the attack Electrobolt
class Electrobolt(attack):
    # returns value of a damaging attack
    @property
    def damage_type(self):
        return DamageTypes.Damaging

    # ELECTRIC type attack
    @property
    def move_type(self):
        return Types.ELECTRIC


# create class for the attack Galethrust
class Galethrust(attack):
    # returns value of a damaging attack
    @property
    def damage_type(self):
        return DamageTypes.Damaging

    # FLYING type attack
    @property
    def move_type(self):
        return Types.FLYING


# create the stats for the monsters
Voltic = []
Skyress = []

# apply stats to Voltic
health_1 = randint(180, 211)
attack_1 = randint(115, 146)
magic_1 = randint(90, 121)
defense_1 = randint(105, 136)
magic_defense_1 = randint(105, 136)
speed_1 = randint(185, 216)

# health that is modified
current_health_1 = health_1

# apply stats to Skyress
health_2 = randint(190, 221)
attack_2 = randint(125, 156)
magic_2 = randint(65, 96)
defense_2 = randint(67, 98)
magic_defense_2 = randint(67, 98)
speed_2 = randint(145, 176)

# health that is modified
current_health_2 = health_2

# initial global variable to determine the attack the wild monster chooses
wild_choice = 0


# creates the class for monster1:
class monster1:
    current_health_1 = health_1
    current_health_2 = health_2

    # Method for the stats for monster 1
    def __init__(self, health_1, current_health_1, attack_1, magic_1, defense_1, magic_defense_1, speed_1):
        self.health_1 = health_1
        self.current_health_1 = current_health_1
        self.attack_1 = attack_1
        self.magic_1 = magic_1
        self.defense_1 = defense_1
        self.magic_defense_1 = magic_defense_1
        self.speed_1 = speed_1

    # Method for the attack of monster 1
    def attack(self, monster2):

        # calls the function to draw the text based UI for the game
        battle_text(monster1, monster2)
        # Asks the user for a move then creates a global variable to be defined across all methods and functions
        global user_choice
        user_choice = str.lower(input("What attack would you like to choose? (Slam, Electrobolt, or Blazing Shot) "))

        # if the user chooses Slam
        if user_choice == "slam":
            # calculates the damage dealt by using Slam
            damage_calculator(monster1, monster2)
            print("You used Slam.")
            # locally changes the value of current_health_2, then changes the value on a global scope
            global current_health_2
            current_health_2 -= DamageDealt
            print("Slam did {} damage.".format(DamageDealt))

        # if the user chooses Electrobolt
        elif user_choice == "electrobolt":
            # calculates the damage dealt by Electrobolt
            damage_calculator(monster1, monster2)
            print("You used Electrobolt.")
            # locally changes the value of current_health_2, then changes the value on a global scope
            global current_health_2
            current_health_2 -= DamageDealt
            print("Electrobolt did {} damage.".format(DamageDealt))

        # if the user chooses heal
        elif user_choice == "blazing shot":
            # calculates the damage dealt by Electrobolt
            damage_calculator(monster1, monster2)
            print("You used Blazing Shot")
            # locally changes the value of current_health_1, then changes the variable on a global scope
            global current_health_2
            current_health_2 -= DamageDealt
            print("Blazing Shot did {} damage.".format(DamageDealt))

        # output for invalid input
        else:
            print("That is not a valid move! Please choose again.")
            print(" ")


# create the class for monster2:
class monster2:
    # initializes a local value for current_health_1
    current_health_1 = health_1

    # method for the stats for monster 2
    def __init__(self, health_2, current_health_2, attack_2, magic_2, defense_2, magic_defense_2, speed_2):
        self.health_2 = health_2
        self.current_health_2 = current_health_2
        self.attack_2 = attack_2
        self.magic_2 = magic_2
        self.defense_2 = defense_2
        self.magic_2 = magic_defense_2
        self.speed_2 = speed_2

    # Method for the attack of monster 2
    def attack(self, monster1):
        # defines the local scope of the variable current_health_2 by setting it equal to the global health_2
        current_health_2 = health_2
        # calculates the chance for the wild monster to heal when its HP becomes low
        if current_health_2 <= 50:
            enemy_heal_chance = randint(0, 3)
            if enemy_heal_chance == 0 or enemy_heal_chance == 1:
                current_health_2 += 50
        else:
            global wild_choice
            wild_choice = randint(1, 4)

            # random chance for the attack to be Galethruster
            if wild_choice == 1 or wild_choice == 3:
                # calculates the damage dealt by Galethruster
                damage_calculator(monster1, monster2)
                # locally changes the value of current_health_1, then changes the value on a global scope
                global current_health_1
                current_health_1 -= DamageDealt
                print("The wild monster used Galethruster. It dealt {} damage.".format(DamageDealt))
                print(" ")

            # random chance for the attack to be Slam
            if wild_choice == 2 or wild_choice == 4:
                # calculates the damage dealt by Slam
                damage_calculator(monster1, monster2)
                # locally changes the value of current_health_1, then changes the value on a global scope
                global current_health_1
                current_health_1 -= DamageDealt
                print("The wild monster used Slam. It dealt {} damage.".format(DamageDealt))
                print(" ")


# attaches the stats and classes to the lists for each respective monster
Voltic.append(monster1(health_1, current_health_1, attack_1, magic_1, defense_1, magic_defense_1, speed_1))
Skyress.append(monster2(health_2, current_health_2, attack_2, magic_2, defense_2, magic_defense_2, speed_2))


# function that's called to calculkate the damage of each attack
def damage_calculator(monster1, monster2):
    # sets an initial value for STAB
    STAB = 1

    # Critical Strike Chance Modifier
    Critical = 1
    Critical_Chance = randint(0, 9)
    if Critical_Chance == 0:
        Critical = 2

    # Modifier for Minimum Possible Damage Dealt
    DmgModifierLow = STAB * Critical * 0.85
    # Modifier for Maximum Possible Damage Dealt
    DmgModifierHigh = STAB * Critical

    # sets Base Damage, Damage Stat used, and opposing Defenseive Stat based upon user input
    # as well as which random move the wild monster uses

    # sets damage and defense variables based upon player using Electrobolt
    if user_choice == 'electrobolt':
        AttackDamage = magic_1
        DamageDefense = magic_defense_2
        # sets base damage value
        Base = 80
        # STAB (Same Type Attack Bonus) modifier
        STAB = 1.5
    # sets damage and defense variables based upon player using Slam
    elif user_choice == 'slam':
        AttackDamage = attack_1
        DamageDefense = defense_2
        # sets base damage value
        Base = 50
        # STAB (Same Type Attack Bonus) modifier
        STAB = 1
    # sets damage and defense variables based upon player using Blazing Shot
    elif user_choice == 'blazing shot':
        AttackDamage = magic_1
        DamageDefense = magic_defense_2
        # sets base damage value
        Base = 150
        # STAB (Same Type Attack Bonus) modifier
        STAB = 1.5
    # sets damage and defense variables based upon wild monster using Slam
    if wild_choice == 4 or wild_choice == 2:
        AttackDamage = attack_2
        DamageDefense = defense_1
        # sets base damage value
        Base = 50
        # STAB (Same Type Attack Bonus) modifier
        STAB = 1.5
    # sets damage and defense variables based upon wild monster using Galethruster
    elif wild_choice == 1 or wild_choice == 3:
        AttackDamage = magic_2
        DamageDefense = magic_defense_1
        # sets base damage value
        Base = 80
        # STAB (Same Type Attack Bonus) modifier
        STAB = 1.5

    # creates a maximum and minimum range of damage values
    DamageHigh = int(round(((210 / 250) * (AttackDamage / DamageDefense) * (Base) + 2) * DmgModifierHigh))
    DamageLow = int(round(((210 / 250) * (AttackDamage / DamageDefense) * (Base) + 2) * DmgModifierLow))

    # randomly selects an integer between the maximum and minimum damage values
    # and gives DamageDealt a global scope
    global DamageDealt
    DamageDealt = randint(DamageLow, DamageHigh)


def battle(monster1, monster2):
    # while both monster are above 0 HP, the battle continues
    while current_health_1 > 0 and current_health_2 > 0:
        # checks the speed to determine which monster moves first in a turn
        if speed_1 >= speed_2:
            monster1.attack(monster1, monster2)
            monster2.attack(monster1, monster2)
            time.sleep(5)
        elif speed_1 < speed_2:
            monster2.attack(monster1, monster2)
            monster1.attack(monster1, monster2)
            time.sleep(5)
        # ends battle if wild monster's HP is at 0
        if current_health_2 <= 0:
            print("The enemy Skyress has fainted...")
            # deems player the winner if their monster's HP is above 0
            if current_health_1 > 0:
                print("You have defeated the wild Skyress.")
            break
        # ends battle if user's monster's HP is at 0
        if current_health_1 <= 0:
            print("Your Voltic has fainted...")
            # deems wild monster the winner if its HP is above 0
            if current_health_2 > 0:
                print("You were defeated by the wild Skyress...")
                print("GAME OVER!")
            break


# creates a function for the intro text to clean up the main()
def intro_text():
    print(" ")
    print(" ")
    print(" ")
    name = str.lower(input("???: Hey there. What's your name? "))
    name = name.title()
    print("???: Nice to meet you, {}.".format(name))
    time.sleep(3)
    print("???: We are in danger. You're a monster tamer right? Please use your monster and save us.")
    time.sleep(3)
    print("{}: No problem.".format(name))


# function to create the text-based UI that's called every turn of the battle
def battle_text(monster1, monster2):
    print(" _____________________________")
    print("  Skyress      HP: {}/{}".format(current_health_2, health_2))
    print(" ")
    print(" ")
    print("  Voltic      HP: {}/{}".format(current_health_1, health_1))
    print(" ______________________________")


# gives the order of operations for functions and the methods that are passed as
# parameters of the functions and the subsequent methods that call functions for
# calculations and text to be run
def main():
    intro_text()
    battle(monster1, monster2)


# executes the main function
if __name__ == "__main__":
    main()
