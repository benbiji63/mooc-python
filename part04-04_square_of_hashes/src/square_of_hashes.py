# Copy here code of line function from previous exercise


def line(length, string):
    if string == "":
        string = "*"
    print(string[0] * length)


def square_of_hashes(size):
    for i in range(size):
        line(size, "#")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
