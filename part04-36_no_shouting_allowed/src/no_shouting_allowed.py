# Write your solution here


def no_shouting(string_list):
    new_list = []
    for string in string_list:
        if not string.isupper():
            new_list.append(string)
    return new_list
