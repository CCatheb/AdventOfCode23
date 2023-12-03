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
    """ This class defines a game and the basics elements needed to do the job. 
    """
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
        """ This function returns the first digital value found in the passed string """
        return int(re.findall('[0-9]+', string)[0])

    def set_game_id(self) -> int:
        """ This function sets the game identifier """
        self.id = self.find_number(self.data.split(':')[0])

    def find_rolls(self) -> list:
        """ This function set the list of rolls made in the current game using the ; separator """
        self.rolls = self.data.split(':')[1].split(';')

    def find_color_in_roll(self, color: str, rolls: list) -> int:
        """ This function is used to fin the specified color in the specified roll, and returns the number of cubes
        that have this color.
        """
        rolls = rolls.split(',')
        for j in range(len(rolls)):
            roll = rolls[j]
            if color in roll:
                return self.find_number(roll)
        return 0

if __name__ ==  "__main__":

    # Setup all the needed vars
    list_of_games = []
    list_of_valid_games = []
    colors = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    
    # Read the input file
    file_data = read_file("dataset.txt")

    total_id = 0
    total_power = 0

    # Parse the data and set all the games
    for data in file_data:
        my_game = game()
        list_of_games.append(my_game)
        my_game.data = data
        my_game.set_game_id()
        my_game.find_rolls()

        # Start of real "logic" part here
        # Iterate through all the rolls
        for roll in my_game.rolls:
            # For each color, get the value of dices in the current roll
            for color, max_val in colors.items():
                value = my_game.find_color_in_roll(color, roll)

                # If we are over the max value set the color as unvalid
                if value > max_val:
                    my_game.colors[color]["status"] = False
                # This next part is about finding the max amout of dices needed
                if value > my_game.colors[color]["count"]:
                    my_game.colors[color]["count"] = value

        # Calculate the power of the game
        for color in my_game.colors.values():
            print(f"Game {my_game.id} got power of {my_game.power}")
            my_game.power *= color["count"]

        list_of_valid_games.append(my_game)

    # Parse all the valid games, and add their total ID
    for my_game in list_of_valid_games:
        if all(color["status"] for color in my_game.colors.values()):
            total_id = total_id + my_game.id

    # For all the games, add their total power
    for my_game in list_of_games:
        total_power = total_power + my_game.power

    # Print the result
    print(total_id)
    print(total_power)