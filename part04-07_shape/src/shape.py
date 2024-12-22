def line(length, string):
    if string == "":
        string = "*"
    print(string[0] * length)


def shape(width, char1, height, char2):
    for i in range(width + 1):
        line(i, char1)
    for i in range(height):
        line(width, char2)


if __name__ == "__main__":
    shape(5, "x", 2, "o")
