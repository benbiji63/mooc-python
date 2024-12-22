# Write your solution here

def all_the_longest(stringList):
    sorted_list = sorted(stringList,key=len)  # Sorting the list based on length of string
    length_of_longest_string = len(sorted_list[len(sorted_list)-1])  # Getting the last element
    return list(filter(lambda x:len(x) == length_of_longest_string,sorted_list))  # Returning all the elements with max length 