# Write your solution here
def same_chars(string, index1, index2):
    if len(string) <= index2 or len(string) <= index1:
        return False
    return string[index1] == string[index2]


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
