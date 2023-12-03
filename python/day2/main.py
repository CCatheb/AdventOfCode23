import re


"""
         ________Roll_________  ______Roll_____  ________Roll_________
        /_____________________\/_______ Game __\/_____________________\
        /                                                              \
Game 11: 9 blue, 1 red, 6 green; 6 red, 1 green; 10 blue, 3 green, 6 red

"""


def read_file(path: str) -> list :
    with open(path, 'r') as f:
        return f.readlines()

class game() :
    
    def __init__(self) -> None:
        self.id = 0
        self.data = ""
        self.rolls = []
        self.power = 1
        self.colors = {
            "red": {
                "status": True,
                "count": 0,
            },
            "green": {
                "status": True,
                "count": 0,
            },
            "blue": {
                "status": True,
                "count": 0,
            },
        }

    @staticmethod
    def find_number(string: str) -> int:
        return int(re.findall('[0-9]+', string)[0])

    def set_game_id(self) -> int:
        self.id = self.find_number(self.data.split(':')[0])

    def find_rolls(self) -> list:
        self.rolls = self.data.split(':')[1].split(';')

    def find_color_in_roll(self, color: str, rolls: list) -> int:
        rolls = rolls.split(',')
        for j in range(len(rolls)):
            roll = rolls[j]
            if color in roll:
                #print(f"Found {color} in '{roll[i]}'\n\tVALUE = {self.find_number(roll[i])}")
                return self.find_number(roll)
        return 0

if __name__ ==  "__main__":

    list_of_games = []
    list_of_valid_games = []
    colors = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    file_data = read_file("dataset.txt")

    total_id = 0
    total_power = 0

    for data in file_data:
        my_game = game()
        list_of_games.append(my_game)
        my_game.data = data
        my_game.set_game_id()
        my_game.find_rolls()
        for roll in my_game.rolls:
            #print(roll)
            for color, max_val in colors.items():
                #print(f"{color}\t{max_val}")
                value = my_game.find_color_in_roll(color, roll)
                #print(f"GAME {my_game.id}\n\tROLL\t{roll}\n\tCOLOR\t{color}\n\t\tFOUND {value} MAX IS {max_val}")
                if value > max_val:
                    my_game.colors[color]["status"] = False
                if value > my_game.colors[color]["count"]:
                    my_game.colors[color]["count"] = value
        for color in my_game.colors.values():
            print(f"Game {my_game.id} got power of {my_game.power}")
            my_game.power *= color["count"]

        list_of_valid_games.append(my_game)

    for my_game in list_of_valid_games:
        if all(color["status"] for color in my_game.colors.values()):
            print(f"Game {my_game.id} is valid.")
            total_id = total_id + my_game.id

    for my_game in list_of_games:
        total_power = total_power + my_game.power

        

    print(total_id)
    print(total_power)