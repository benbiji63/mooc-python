# Write your solution here


def longest_series_of_neighbours(list):
    count = 1
    longest = 1
    while list != []:
        if len(list) <= 1:
            break
        if list[0] + 1 == list[1] or list[0] - 1 == list[1]:
            count += 1
        else:
            longest = max(longest, count)
            count = 1

        list = list[1:]
    longest = max(longest, count)
    return longest
