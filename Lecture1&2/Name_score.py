import string
"""Name Scores
names.txt - text file containing over five-thousand first 
names, begin by sorting it into alphabetical order. Then working 
out the alphabetical value for each name, multiply this value 
by its alphabetical position in the list to 
obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, 
COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

Hint: By "alphabetical value" they mean the sum of the 
characters in the name, if each character is converted into 
its position in the alphabet, so A=1, B=2, etc."""

def read_file(file: str) -> list:
    """
    A function that appends lines to a list.
    Input: a string value of a file.
    Output: a list object of all the names in the file.
    """
    name_dict = {}
    line_count = 1
    with open(file, "r") as f:
        name_list = []
        for line in f.lower():
            name_list.append(line)
        name_sort = name_list.sort()
        for name in name_sort:
            name_value = calc_name_value(name)
            name_dict[name] = list(line_count, name_value)

    return name_dict

def calc_name_value(name: str) -> int:
    name_count_value = 0
    for c in name.lower():
        name_count += ALPHABET.find(c) + 1
    return name_count
    
def main():
    print(read_file("names.txt"))

main()