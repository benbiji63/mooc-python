# Write your solution here


def even_numbers(my_list):
    return list(filter(lambda x: x % 2 == 0, my_list))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
