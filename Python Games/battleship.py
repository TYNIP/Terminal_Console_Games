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
    def __init__(self, name, size=5):
        self.size = size
        self.player_field = self.create_field()
        self.hidden_field = self.create_field()
        self.ships = [(2, 'horizontal'), (3, 'vertical')]  # Length and orientation of ships
        self.place_ships()
        self.name = name

    def create_field(self):
        return [['O' for _ in range(self.size)] for _ in range(self.size)]

    def print_field(self, field):
        for row in field:
            print(" ".join(row))

    def place_ship(self, ship_length, direction):
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
        for ship_length, direction in self.ships:
            self.place_ship(ship_length, direction)

    def play(self):

        #Uncomment to see field with the ships

        """ print("Hidden Field (Ships):")
        self.print_field(self.hidden_field) """
        print("\nYour Field:")
        self.print_field(self.player_field)
        while not self.all_ships_sunk():
            try:
                x, y = map(int, input(f"{self.name}Select Your Coordinates to shoot (x y): ").split())
                if 0 <= x < self.size and 0 <= y < self.size:
                    if self.hidden_field[y][x] == 'X':
                        print()
                        print(f"{self.name} You hit a ship!")
                        self.player_field[y][x] = '*'
                    else:
                        print()
                        print(f"{self.name} You missed!")
                        self.player_field[y][x] = 'X'
                    print("Your Field:")
                    self.print_field(self.player_field)
                else:
                    print("Invalid coordinates. Please select coordinates within the field range.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")
        print()
        print(f"Congratulations {self.name}! You sank all the ships! You Won")
        print()

    def all_ships_sunk(self):
        total_parts = sum(length for length, _ in self.ships)
        hits = 0
        for row in self.player_field:
            for cell in row:
                if cell == '*':
                    hits += 1
        return hits == total_parts



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
        level = 9
    elif difficultyInput == 'easy':
        level = 5
    else:
        print('Invalid Difficulty Level')

print(f'Field Size {level}')
game = BattleshipGame(nameInput, level)
game.play()
