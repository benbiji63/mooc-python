# Write your solution here

def shortest(stringList):
    sorted_list = sorted(stringList,key=len)  # Sorting the list based on length of string
    shortest_string = sorted_list[0] # Getting the first element
    return shortest_string # Returning the shortest string