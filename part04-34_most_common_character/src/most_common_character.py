# Write your solution here


def most_common_character(string):
    char_dict = {}

    while string != "":
        beginning_length = len(string)
        first_char = string[0]
        string = string.replace(first_char, "")
        ending_length = len(string)
        count = beginning_length - ending_length
        char_dict.update({f"{first_char}": count})
    return max(char_dict, key=lambda k: char_dict[k])
