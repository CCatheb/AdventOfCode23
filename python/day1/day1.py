# CCatheb, Advent Of Code 2023
# Python Edition
# Python 3.10.12
# 01/12/2023

import os

def read_data_from_file(path: str) -> list :
    """ Read the file at the passed path and set a var containing the strings.
    One string per line in the file.
    """

    with open(path) as f:
        lines = f.readlines()

    return lines

def search_from_start(string: str) -> str :
    """This function search the first digit in the passed string,
    starting from the index 0.
    """

    for i in range(len(string)):
        try:
            int(string[i])
            return string[i]
        except ValueError:
            continue

def search_from_end(string: str) -> str :
    """This function search the first digit in the passed string,
    starting from the index -1.
    """

    for i in range((len(string)-1), -1, -1):
        try:
            int(string[i])
            return string[i]
        except ValueError:
            continue

if __name__ == "__main__":

    total = 0

    cur_dir = os.getcwd()
    data_file = cur_dir + "/data.txt"

    list_of_str = read_data_from_file(data_file)

    for string in list_of_str:
        first = search_from_start(string)
        last = search_from_end(string)
        print(f"STR {string} :\t{first}{last}")
        total = total + int(f"{first}{last}")

    print(f"TOTAL :\t{total}")
