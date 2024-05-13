class Player:
    def __init__(self, name, health=100, level=1):
        self.name = name
        self.health = health
        self.level = level
        self.score = 0
        self.weapon = "Sword"
        self.experience = 0

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name}!")
        enemy.take_damage(10)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage!")

    def defend(self):
        print(f"{self.name} defends against the enemy's attack!")

    def interact_with_enemy(self, enemy):
        action = input(f"What do you want to do, {self.name}? Attack or Defend? ").lower()
        if action == "attack":
            self.attack(enemy)
        elif action == "defend":
            self.defend()
        else:
            print("Invalid action!")

    def __repr__(self):
        return f"Player(name='{self.name}', health={self.health}, level={self.level})"


class Enemy:
    def __init__(self, name, health=100, damage=10):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, player):
        print(f"{self.name} attacks {player.name}!")
        player.take_damage(self.damage)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage!")

    def interact_with_player(self, player):
        self.attack(player)

    def __repr__(self):
        return f"Enemy(name='{self.name}', health={self.health}, damage={self.damage})"


# Test interaction
player1 = Player("Hero")
enemy1 = Enemy("Goblin")

while player1.health > 0 and enemy1.health > 0:
    player1.interact_with_enemy(enemy1)
    if enemy1.health > 0:
        enemy1.interact_with_player(player1)

print("Battle ends!")
