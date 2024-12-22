# Write your solution here


def everything_reversed(str_list):
    new_list = []
    for item in str_list:
        new_list.append(item[::-1])
    return new_list[::-1]
