import random
import math

def count_chars(chars: str) -> dict:
    dict = {}
    for char in chars:
        if chars[char] in chars:
            chars[char] += 1
        else:
            chars[char] = 0
    return dict

def main():
    string = "ABABAB"
    dict = count_chars(string)
    print(dict)

main()