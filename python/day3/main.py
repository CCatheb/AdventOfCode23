import re

""" TECHNICAL EXPLANATION:

Imagine we have the following (simple) table:

╔═══╦═══╦═══╦═══╦═══╦═══╗
║   ║ 1 ║ 2 ║ 3 ║ 4 ║ 5 ║
╠═══╬═══╬═══╬═══╬═══╬═══╣
║ 1 ║   ║   ║   ║   ║   ║
║ 2 ║   ║ 3 ║ 1 ║ 5 ║   ║
║ 3 ║   ║   ║   ║   ║   ║
╚═══╩═══╩═══╩═══╩═══╩═══╝

The actions to perform are the following:
    => Find the first digit, and get its coordinates
        -> The coordinates of the 3 would be [2,2], written as [Col_Start, Line_Start]
    => Continue on the same line until:
        -> There is no more digit
        -> We reached the end of the line
    => Get the coordinates of the last digit written as [Col_End, Line_End] (here, it would be [4, 2])
        -> The number of digits between these 2 coordinates is:
            Col_End - Col_Start + 1 (in this example, 4-2+1 = 3 digits)
    => Once these data are found:
        -> Get a list of each coordinates that you should check:
            For the start digit:
                [Col_Start - 1, Line_Start -1] ; [Col_Start - 1, Line_Start] ; [Col_Start - 1, Line_Start +1]
                [Col_Start, Line_Start -1] ; [Col_Start, Line_Start +1]
            For the end digit:
                [Col_Start + 1, Line_Start -1] ; [Col_Start + 1, Line_Start] ; [Col_Start + 1, Line_Start +1]
                [Col_Start, Line_Start -1] ; [Col_Start, Line_Start +1]
            For any digit between the start and the end:
                -> Determine the digit position (in this case, the 1 is in position 1 as 3 is the 0)
                So, the coordinates to check would be:
                [Col_Start + Digit_Pos, Line_Start -1] ; [Col_Start + Digit_Pos, Line_Start +1]
        -> In any case, as soon as we find a symbol, we should consider the full digit as a part number.
        This means:
            -> Add the full number to the sum of all  part number
            -> Start searching for any other number, starting at [Col_End +2, Line_End]. If Col_End +2 is over the lenght
                of the line, go to the next line.

"""

def read_file(path: str) -> list :
    with open(path, 'r') as f:
        return f.readlines()


class char():

    x = 0
    y = 0
    value = ""

    def __init__(self, x, y, value) -> None:
        self.x = x
        self.y = y
        self.value = value

    def get_coordinates(self):
        return (self.x, self.y)

    def get_value(self):
        return self.value

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_value(self, value):
        self.value = str(value)

    def is_value_an_int(self):
        try:
            int(self.value)
            return True
        except ValueError:
            return False

if __name__ == "__main__":

    data = read_file("dataset.txt")

    # Clear the data, remove the \n
    for i in range(len(data)):
        data[i] = data[i].strip()
    
    char_data = []

    # This first loop goes through all the lines
    for i in range(len(data)):

        line = data[i]
        line_data = []

        # This second loop goes through the string itself, and
        # instanciates an item for each character encoutered.
        for j in range(len(line)):
            item = char(i,j,line[j])
            line_data.append(item)

        char_data.append(line_data)

    print(char_data[0][0].is_value_an_int())