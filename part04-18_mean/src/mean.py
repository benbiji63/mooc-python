# Write your solution here
# You can test your function by calling it within the following block


def mean(list1):
    return sum(list1) / len(list1)


if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)
