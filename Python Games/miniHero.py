""" 
MiniHero
-----------------------------------------------------------------------------
Mini adventure game, you play as a hero on a mission to defeat a horde of goblins.
      
Rules:
    - Encounter and battle goblins until you defeat five of them.
    - Each goblin has a random amount of health between 30 and 60.
    - During battles, you can choose to attack or defend against the goblin's attacks.
    - If your health reaches 0, the game is over.
    - After defeating a goblin, you have the option to recover 10 health points or increase your attack power by 5.
    - The goblins can randomly choose to attack or defend during their turns.
To Exit: ctrl + c 
-----------------------------------------------------------------------------
TYNIP: ENJOY!
"""

import random
#Hero class
class Player:
    def __init__(self, name, health=100, level=1):
        self.name = name
        self.health = health
        self.level = level
        self.score = 0
        self.weapon = "Sword"
        self.experience = 0
        self.attack_power = 10

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name}!")
        enemy.take_damage(self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage!")

    def defend(self, enemy_damage):
        print(f"{self.name} defends against the enemy's attack!")
        self.take_damage(enemy_damage / 2)

    def recover(self):
        self.health += 10
        print(f"{self.name} recovers 5 health points. Current health: {self.health}")

    def increase_attack_power(self):
        self.attack_power += 5
        print(f"{self.name} increases attack power by 5. Current attack power: {self.attack_power}")

    def interact_with_enemy(self, enemy):
        print()
        action = input(f"What do you want to do, {self.name}? Attack or Defend? ").lower()
        if action == "attack":
            self.attack(enemy)
            print()
        elif action == "defend":
            self.defend(enemy.damage)
            print()
        else:
            print("Invalid action!")

    def __repr__(self):
        return f"Player(name='{self.name}', health={self.health}, level={self.level})"

#Enemy class
class Enemy:
    def __init__(self, name, health=None, damage=10):
        self.name = name
        self.damage = damage
        if health is None:
            self.health = random.randint(30, 60)
        else:
            self.health = health

    def attack(self, player):
        print(f"{self.name} attacks {player.name}!")
        player.take_damage(self.damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {damage} damage! Current health: {self.health}")

    def defend(self, player_damage):
        print(f"{self.name} defends against {player_damage} damage!")
        self.health += 5
        print(f"New {self.name} current health: {self.health}")

    def interact_with_player(self, player):
        action = random.choice(["attack", "defend"])
        if action == "attack":
            self.attack(player)
        else:
            self.defend(player.attack_power)

    def __repr__(self):
        return f"Enemy(name='{self.name}', health={self.health}, damage={self.damage})"

""" GAME """
print("""
-----------------------------------------------------------------------------
MiniHero
-----------------------------------------------------------------------------
Mini adventure game, you play as a hero on a mission to defeat a horde of goblins.
      
Rules:
    - Encounter and battle goblins until you defeat five of them.
    - Each goblin has a random amount of health between 30 and 60.
    - During battles, you can choose to attack or defend against the goblin's attacks.
    - If your health reaches 0, the game is over.
    - After defeating a goblin, you have the option to recover 10 health points or increase your attack power by 5.
    - The goblins can randomly choose to attack or defend during their turns.
To Exit: ctrl + c 
-----------------------------------------------------------------------------
TYNIP: ENJOY!
-----------------------------------------------------------------------------
""")
print('Welcome Hero!')

player1 = Player("Hero")
goblins_defeated = 0
end = True

while end:
    goblin = Enemy("Goblin")
    print(f"A new goblin appears with {goblin.health} health!")

    while goblin.health > 0 and player1.health > 0:
        player1.interact_with_enemy(goblin)
        if goblin.health > 0:
            goblin.interact_with_player(player1)

    if player1.health <= 0:
        print("Game over! You were defeated.")
        end = False
        break
    if goblins_defeated >= 5:
        print("You have defeated all the goblins! Hero Wins.")
        end = False
        break

    print("You defeated the goblin!")
    goblins_defeated += 1
    print(f"{player1.name}'s current health: {player1.health}")
    if goblins_defeated < 5:
        option = input("Do you want to recover 10 health points or increase your attack power by 5? recover/increase: ").lower()
        if option == "recover":
            player1.recover()
        elif option == "increase":
            player1.increase_attack_power()
