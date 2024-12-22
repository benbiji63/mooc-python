# Write your solution here
def length_of_longest(stringList):
    sorted_list = sorted(stringList,key=len)  # Sorting the list based on length of string
    longest_string = sorted_list[len(sorted_list)-1]  # Getting the last element
    return len(longest_string) #Returning the length of longest string

