import re

""" TECHNICAL EXPLANATION:

Imagine we have the following (simple) table:

╔═══╦═══╦═══╦═══╦═══╦═══╗
║   ║ 1 ║ 2 ║ 3 ║ 4 ║ 5 ║
╠═══╬═══╬═══╬═══╬═══╬═══╣
║ 1 ║   ║   ║   ║   ║   ║       Number 5 is determined by its coordinates [x, y] = [2, 4]
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

    def __init__(self, x, y, value) -> None:
        self.x = x
        self.y = y
        self.value = value

    @property
    def coordinates(self):
        return (self.x, self.y)

    @property
    def is_int(self):
        try:
            int(self.value)
            return True
        except ValueError:
            return False

    def set_x(self, x):
        # Represents the line
        self.x = x

    def set_y(self, y):
        # Represents the column
        self.y = y

    def set_value(self, value):
        self.value = str(value)

    

class number():
    """ This class defines a number, e.g. the full '315' given in the example.
    It is defined using:

        -> The start char (meaning the object 'char')
            => 3 in the example
        -> The end char (meaning the object 'char')
            => 5 in the example
    
    """


    def __init__(self, start: char, end: char) -> None:
        self.start = start
        self.end = end
        self.length = (self.end.y - self.start.y + 1) 
        self.coordinates_to_check = self._calculate_elements_to_check()

    def _calculate_elements_to_check(self):
        """ This method is used to calculate all the coordinates to check 
        to find a special character.

        The method uses the number defined start and end to perform operations.

        Returns:
            - coordinates_to_check (list): List of all the coordinates to check, given as a tuple, such as (x, y)

        Reminder from the top comment:
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
        """
        coordinates_to_check = []

        # i will represents the position of the char in the number
        for i in range(self.length):
            
            if i == 0:
                # Special case, we are at the first char
                for j in range(-1, 2, 1):
                    coordinates_to_check.append((self.start.x + j, self.start.y -1))
                coordinates_to_check.append((self.start.x -1, self.start.y))
                coordinates_to_check.append((self.start.x +1, self.start.y))
            elif i == self.length - 1:
                #Another special case, we are at the end
                for j in range(-1, 2, 1):
                    coordinates_to_check.append((self.start.x + j, self.start.y +1))
                coordinates_to_check.append((self.start.x -1, self.start.y))
                coordinates_to_check.append((self.start.x +1, self.start.y))
            else:
                # We are in the 'normal' case
                coordinates_to_check.append(self.start.x + 1, self.start.y + i )
                coordinates_to_check.append(self.start.x - 1, self.start.y + i )
        
        return coordinates_to_check
    

def check_coordinates(coordinates: list, data: list) -> bool :
    """This method check the given list of coordinates.
    If any of these coordinates contains a special character, then it returns True.
    Else, it returns False

    Args:
        coordinates (list): List of all the coordinates to check. Must be a list of char objects.
               data (list): The FULL data input.
    """

    for coordinate in coordinates:
        pass



if __name__ == "__main__":

    data = read_file("dataset.txt")
    #data = ["...........828...559.................181...%..........613.......10...928...*...993.+.........758.*.........471...#../...............573....."]

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

    number_of_columns = len(line_data)
    number_of_lines = len(char_data)

    number_list = []

    # This first loop goes through all the lines
    for i in range(number_of_lines):
        start_found = False
        # This one goes through all the columns
        for j in range(number_of_columns):
            element = char_data[i][j]

            if element.is_int:
                if not start_found:
                    # If the item found is an int and we did not found the start, that means that this item is
                    # the start of a number
                    start = element
                    start_found = True

            elif not element.is_int:
                if start_found:
                    # If we already found the start and this item is not a int, that means that the item
                    # before this one was the end of the started int
                    end = char_data[i][j-1]
                    my_number = number(start, end)
                    number_list.append(my_number)
                    start_found = False

            elif j == len(number_of_columns-1):
                # In this case, we reached the end of the line, so we can say that the actual digit is the end
                end = element
                my_number = number(start, end)
                number_list.append(my_number)


