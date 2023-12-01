# CCatheb, Advent Of Code 2023
# Python Edition
# Python 3.10.12
# 01/12/2023

import os
import json

def read_data_from_file(path: str) -> list :
    """ Read the file at the passed path and set a var containing the strings.
    One string per line in the file.
    """
    with open(path) as f:
        lines = f.readlines()
    return lines

def read_data_from_json(path: str) -> dict:
    """ Read the passed JSON file and return the dict """
    with open(path) as f:
        data = json.load(f)
    return data

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
    return "0"

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
    return "0"

def replace_digits(digits: dict, string: str) -> str:
    """This function replaces a written digit such as 'nine' by the integer one, 9
    """

    for key, value in digits.items():
        if key in string:
            string = string.replace(key, str(value))
    return string

if __name__ == "__main__":

    total = 0

    cur_dir = os.getcwd()
    data_file = cur_dir + "/data.txt"
    digits_file = cur_dir + "/digits.json"

    list_of_digits = read_data_from_json(digits_file)
    list_of_str = read_data_from_file(data_file)


    for string in list_of_str:

        string = replace_digits(list_of_digits, string)
        first = search_from_start(string)
        last = search_from_end(string)
        
        total = total + int(f"{first}{last}")

    print(f"TOTAL :\t{total}")