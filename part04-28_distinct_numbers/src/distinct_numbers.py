# Write your solution here


def distinct_numbers(list1):
    distinct_list = []
    for num in list1:
        if num not in distinct_list:
            distinct_list.append(num)
    return sorted(distinct_list)
