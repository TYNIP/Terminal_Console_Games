""" 
BATTLESHIP
-----------------------------------------------------------------------------
Rules:
    - Type exact location by using the x y format. Example: 1, 2 = x:1 y:2
    - x : missed
    - * : hit ship
To Exit: ctrl + c 
-----------------------------------------------------------------------------
TYNIP: ENJOY!
"""

import random

class BattleshipGame:
    def __init__(self, name, size):
        self.size = size
        self.name = name
        self.player_field = self.create_field()
        self.hidden_field = self.create_field()
        self.place_ships()

    def create_field(self):
        return [['O' for _ in range(self.size)] for _ in range(self.size)]

    def print_field(self, field):
        for row in field:
            print(" ".join(row))

    def place_ship(self, ship_length):
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - ship_length)
            for i in range(ship_length):
                self.hidden_field[y][x + i] = 'X'
        else:
            x = random.randint(0, self.size - ship_length)
            y = random.randint(0, self.size - 1)
            for i in range(ship_length):
                self.hidden_field[y + i][x] = 'X'

    def place_ships(self):
        self.place_ship(2)  # Place 2-length ship
        self.place_ship(3)  # Place 3-length ship

    def play(self):
        print("Hidden Field (Ships):")
        self.print_field(self.hidden_field)
        print("\nYour Field:")
        self.print_field(self.player_field)
        while not self.all_ships_sunk():
            try:
                x, y = map(int, input(f"{self.name} Select Your Coordinates to shoot (x y): ").split())
                if 0 <= x < self.size and 0 <= y < self.size:
                    if self.hidden_field[y][x] == 'X':
                        print("You hit a ship!")
                        self.player_field[y][x] = '*'
                    else:
                        print("You missed!")
                        self.player_field[y][x] = 'X'
                    print("Your Field:")
                    self.print_field(self.player_field)
                else:
                    print("Invalid coordinates. Please select coordinates within the field range.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")

        print(f"Congratulations {self.name}! You sank all the ships! You Won!")

    def all_ships_sunk(self):
        for row in self.hidden_field:
            for cell in row:
                if cell == 'X':
                    return False
        return True


""" GAME """
print("""
-----------------------------------------------------------------------------
BATTLESHIP
-----------------------------------------------------------------------------
Rules:
    - Type exact location by using the x y format. Example: 1, 2 = x:1 y:2
    - x : missed
    - * : hit ship
To Exit: ctrl + c 
-----------------------------------------------------------------------------
TYNIP: ENJOY!
-----------------------------------------------------------------------------
""")
print('Welcome Gamer!')
nameInput = input('Type Your Name Stranger: ')
level = 0
while level == 0:
    difficultyInput = input(f"{nameInput} Select Difficulty: easy, normal, hard: ")
    if difficultyInput == 'hard':
        level = 11
    elif difficultyInput == 'normal':
        level = 8
    elif difficultyInput == 'easy':
        level = 3
    else:
        print('Invalid Difficulty Level')

game = BattleshipGame(nameInput, level)
game.play()
