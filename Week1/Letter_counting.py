import random
import math

def count_chars(string: str) -> dict:
    """
    A function that takes a string as input.
    It counts the number of instances and puts the character as the key 
    and the corresponding count as the value in a dictionary.
    It returns the dictionary.
    """
    dict_char = {}
    list_char = []
    for letter in string:
        for char in letter:
            list_char.append(char.lower())

    for char in list_char:
        if char in dict_char:
            dict_char[char] += 1
        else:
            dict_char[char] = 1

    return dict_char

def print_counted_dict(dict_char: dict):
    """
    A function that takes a dictionary as input and 
    prints out a f-string with the keys and values of the dictionary.
    """
    for keys, values in dict_char.items():
        print(f"Char - {keys} <--> count in string - {values} \n")

def main():
    string = "ABABAB KKS ok sakd"
    dict_char_count = count_chars(string)
    print_counted_dict(dict_char_count)

main()