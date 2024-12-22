# Write your solution here


def list_sum(list1, list2):
    list_of_sums = []
    for i in range(len(list1)):
        sum = list1[i] + list2[i]
        list_of_sums.append(sum)
    return list_of_sums


# if __name__ == "__main__":
